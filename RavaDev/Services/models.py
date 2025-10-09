from django.db import models

class Service(models.Model):
    # Podstawowe informacje
    nr = models.IntegerField(unique=True, verbose_name="Numer usługi")
    title = models.CharField(max_length=200, verbose_name="Nazwa usługi")
    description = models.TextField(verbose_name="Opis usługi")
    long_description = models.TextField(verbose_name="Długi opis usługi", null=True, blank=True)

    # Cechy i ich zakresy
    feature_1_name = models.CharField(max_length=100, verbose_name="Nazwa cechy 1")
    feature_1_ranges = models.CharField(max_length=200, verbose_name="Zakresy cechy 1")
    feature_2_name = models.CharField(max_length=100, verbose_name="Nazwa cechy 2")
    feature_2_ranges = models.CharField(max_length=200, verbose_name="Zakresy cechy 2")
    

    DEMAND_LEVELS = [
        ('very_low', 'Bardzo niski'),
        ('low', 'Niski'),
        ('medium', 'Średni'),
        ('medium_high', 'Średni-wysoki'),
        ('high', 'Wysoki'),
        ('very_high', 'Bardzo wysoki'),
    ]
    
    demand_level = models.CharField(
        max_length=20, 
        choices=DEMAND_LEVELS, 
        verbose_name="Poziom popytu"
    )
    demand_coefficient = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name="Współczynnik popytu"
    )
    
    SUPPLY_LEVELS = [
        ('none', 'Brak'),
        ('very_low', 'Bardzo niska'),
        ('low', 'Niska'),
        ('medium', 'Średnia'),
        ('high', 'Wysoka'),
    ]
    
    local_supply = models.CharField(
        max_length=20, 
        choices=SUPPLY_LEVELS, 
        verbose_name="Podaż lokalna"
    )
    supply_coefficient = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name="Współczynnik podaży"
    )
    
    # Ceny rynkowe
    market_price_range = models.CharField(
        max_length=100, 
        verbose_name="Zakres cen rynkowych"
    )
    price_coefficient = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name="Współczynnik ceny"
    )
    
    # Limity cenowe
    price_min = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Cena minimalna rynkowa"
    )
    price_max = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Cena maksymalna rynkowa"
    )
    local_price_min = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Lokalna cena minimalna"
    )
    local_price_max = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Lokalna cena maksymalna"
    )
    
    # Relacja rynkowa
    market_relation = models.TextField(verbose_name="Relacja rynkowa")
    
    # Numery zakresów dla cech
    range_number_1 = models.IntegerField(verbose_name="Numer zakresu 1")
    range_number_2 = models.IntegerField(verbose_name="Numer zakresu 2")
    
    # Współczynniki wyceny
    valuation_coefficient = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name="Współczynnik wyceny"
    )
    valuation = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Wycena"
    )
    
    # Obrazy
    image1 = models.ImageField(upload_to='Services/', null=True, blank=True)
    image2 = models.ImageField(upload_to='Services/', null=True, blank=True)
    image3 = models.ImageField(upload_to='Services/', null=True, blank=True)
    
    field = models.ForeignKey('Field', on_delete=models.CASCADE, verbose_name="Dziedzina", null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.id}. {self.title}"
    
    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"
        ordering = ['id']

    

class Field(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa dziedziny")
    description = models.CharField(max_length=200, verbose_name="Opis dziedziny")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Dziedzina"
        verbose_name_plural = "Dziedziny"
        ordering = ['id']