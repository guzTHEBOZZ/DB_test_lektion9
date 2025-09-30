import barcode
from barcode.writer import ImageWriter
import uuid

# Generér en unik ID (kan også være dit eget nummer)
unik_id = '123456789012'  # EAN13 kræver præcis 12 cifre (13. ciffer er kontrolciffer)

# Vælg stregkode-format (f.eks. Code128, EAN13, EAN8)
stregkode_type = barcode.get_barcode_class('EAN13')

# Lav stregkoden
stregkode = stregkode_type(unik_id, writer=ImageWriter())

# Gem den som PNG
filnavn = stregkode.save("min_stregkode")

print(f"Stregkode gemt som {filnavn}.png med ID: {unik_id}")
