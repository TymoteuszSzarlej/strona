from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SystemLog, EmailQueue, EmailTemplate
from .serializers import SystemLogSerializer, EmailQueueSerializer, EmailTemplateSerializer
from django.utils.timezone import now
from django.core.mail import send_mail

class SystemLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SystemLog.objects.all().order_by('-timestamp')
    serializer_class = SystemLogSerializer

    @action(detail=False, methods=['get'])
    def recent_errors(self, request):
        logs = SystemLog.objects.filter(level='ERROR').order_by('-timestamp')[:20]
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data)


class EmailQueueViewSet(viewsets.ModelViewSet):
    queryset = EmailQueue.objects.all().order_by('-created_at')
    serializer_class = EmailQueueSerializer

    @action(detail=True, methods=['post'])
    def send(self, request, pk=None):
        email = self.get_object()
        if email.status == 'SENT':
            return Response({'detail': 'Email already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(
                subject=email.subject,
                message=email.body,
                from_email='noreply@example.com',
                recipient_list=[email.to],
                fail_silently=False,
            )
            email.status = 'SENT'
            email.sent_at = now()
            email.save()
            return Response({'detail': 'Email sent successfully.'})
        except Exception as e:
            email.status = 'FAILED'
            email.error_message = str(e)
            email.retries += 1
            email.save()
            return Response({'detail': 'Sending failed.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all().order_by('name')
    serializer_class = EmailTemplateSerializer
