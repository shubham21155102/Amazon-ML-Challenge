import re
import pandas as pd

# Define the unit abbreviations dictionary
unit_abbreviations = {
    'item_weight': {
        'gram': ['g', 'gm', 'G', 'GM', 'gram'],
        'milligram': ['mg', 'mG', 'Milligram', 'milligram'],
        'kilogram': ['kg', 'KG', 'Kilogram', 'kilogram'],
        'ounce': ['oz', 'OZ', 'Ounce', 'ounce'],
        'pound': ['lb', 'LB', 'Pound', 'pound'],
        'ton': ['t', 'T', 'Ton', 'ton'],
        'microgram': ['µg', 'mcg', 'Microgram', 'microgram']
    }
}

# Create a reverse dictionary to map abbreviations to full units
unit_map = {}
for category, units in unit_abbreviations.items():
    for full_unit, abbreviations in units.items():
        for abbr in abbreviations:
            unit_map[abbr.lower()] = full_unit

# Regex pattern to find numbers followed by units
pattern = re.compile(r'(\d+\.?\d*)\s*([a-zA-Zµ]+)', re.IGNORECASE)

def extract_units(text):
    matches = pattern.findall(text)
    results = []
    for match in matches:
        number, unit = match
        unit = unit.lower()
        if unit in unit_map:
            full_unit = unit_map[unit]
            results.append(f"{number} {full_unit}")
    return ' '.join(results)

# Sample DataFrame
data = {
    'image_link': [
        'https://m.media-amazon.com/images/I/61I9XdN6OFL.jpg',
        'https://m.media-amazon.com/images/I/71gSRbyXmoL.jpg',
        'https://m.media-amazon.com/images/I/61BZ4zrjZXL.jpg',
        'https://m.media-amazon.com/images/I/612mrlqiI4L.jpg',
        'https://m.media-amazon.com/images/I/617Tl40LOXL.jpg',
        'https://m.media-amazon.com/images/I/61QsBSE7jgL.jpg',
        'https://m.media-amazon.com/images/I/81xsq6vf2qL.jpg',
        'https://m.media-amazon.com/images/I/71DiLRHeZdL.jpg',
        'https://m.media-amazon.com/images/I/91Cma3RzseL.jpg',
        'https://m.media-amazon.com/images/I/71jBLhmTNlL.jpg'
    ],
    'group_id': [748919, 916768, 459516, 459516, 731432, 731432, 731432, 731432, 731432, 731432],
    'entity_name': ['item_weight', 'item_volume', 'item_weight', 'item_weight', 'item_weight', 'item_weight', 'item_weight', 'item_weight', 'item_weight', 'item_weight'],
    'entity_value': ['500.0 gram', '1.0 cup', '0.709 gram', '0.709 gram', '1400 milligram', '1400 milligram', '1400 milligram', '1400 milligram', '1400 milligram', '1400 milligram'],
    'ocr_text': [
        "PROPOS' NATURE INGREDIENT MENAGER MULTI-USAGE TERRE dE SOMMIERES 4100% NATUREL Argile 10036 pure et   naturelle Lerre Sommierespreserte desproprietes absorbantes qui permettent nelloyage sec des laches recalcitrantes...",
        "TLaeE=_ 7672 Xe RRIFIC LEBENSMITTELECHT Cwe DAV GEPRAGTES DESIGN As YQULIKE BEST Designed in V cnre Y [Bextin ] LIZENZIERTE UND GESCHITZTE DESIGNS TEA WITH cccteics",
        "COMPOSITION Serving Size: Tablet (0.709 g) Each serving contains (Approx Values): Ingredient Oty / Serving % RDA\"\" #PHOSPHOcomplex@ Silybin (Sillybum marianum) 200 mg Dandelion (Taraxacum officinale) leaf extract...",
        "3 3 1 1 F IW! 1 5833 1 3 1 1 1 1 H 0 L 1 W # I 1 1 Hu I M 1 H H 1 V 1 Ji Hl U 0 H IH H Hhh 1 jj 1 Ilu 1 # 1 1 1 1 HH 1 1 1 1",
        "Horbaach' HIGH StRENGTH PSYLLIUM HUSK PLANTAGO OVATA 1400mG PLANT SEEDS FOOD VEGAN SUPPLEMENT 365 CAPSULES",
        "Naturally-Sourced Psyllium High strength 140Omg per serving Suitable for Vegans & Vegetarians HOrbaach\"\" Horbaach' hiGA StREnGTh PSYLLIUM HUSK 1400mG PLANTAGO ' OVATA PLANT SEEDS FOOD SUPPLEMENT 365 VEGAN CAPSULES",
        "",
        "VEGAN WHEAT FREE soy FREE OVATA DAIRY FREE FREE FROM PRESERVATIVES HOrBaaCh Horbaach' StRE NGTh AIGH PSYLLIUM HUSK PLANTAGO = SEEDS PLANT = 140OmG VEGAN 365 CAPSULES FOOD SUPPLEMENT",
        "",
        "NEW LOOK SAME TRUSTEDQUALITY OLD Horbaach NEW Horbaach' HIGh STRENGTH PSYLLIUM HIGH StRENGTh HUSK PSYLLIUM I4OOMG perving HUSK PLANTAGO OVATA 1400mG PLANT SEEDS FOOD VEGAN SUPPLEMENT 365 CAPSULES FOoD VEGAN SUPPLEMENT 365 CAPSULES PACKAGING MAY VARY HOrbaach"
    ]
}

df = pd.DataFrame(data)

# Apply the function to create a new column 'extracted_units'
df['extracted_units'] = df['ocr_text'].apply(extract_units)

print(df[['image_link', 'entity_name', 'entity_value', 'ocr_text', 'extracted_units']])
print(df[['image_link', 'entity_name', 'entity_value', 'extracted_units']])