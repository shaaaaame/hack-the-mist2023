
class Disease:
        def __init__(self, name, diagnosis, treatment, group):
            self.name = name
            self.diagnosis = diagnosis
            self.treatment = treatment
            self.group = group


    # List of disease objects
disease_list = [
        Disease("Acne and Rosacea",
                "Acne: Inflammation of the sebaceous glands in the skin, Rosacea: Chronic inflammatory skin condition that affects the face",
                "Acne: Topical and oral medication, Rosacea: Medication and lifestyle changes", "Skin conditions"),
        Disease("Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions",
                "Pre-cancerous skin lesion caused by sun damage, Basal Cell Carcinoma: Most common type of skin cancer, Malignant Lesions: Various forms of skin cancer",
                "Surgical removal, radiation therapy, chemotherapy", "Skin cancers"),
        Disease("Atopic Dermatitis", "Chronic inflammatory skin condition characterized by dry and itchy skin",
                "Moisturizers, topical corticosteroids, and antihistamines", "Allergic skin conditions"),
        Disease("Bullous Disease",
                "Autoimmune disorders that affect the skin and mucous membranes, characterized by fluid-filled blisters",
                "Oral and topical medication, steroids, and immune-suppressants", "Autoimmune skin conditions"),
        Disease("Cellulitis Impetigo and other Bacterial Infections",
                "Cellulitis: Infection of the skin and subcutaneous tissue, Impetigo: Contagious skin infection caused by bacteria, Other Bacterial Infections: Various bacterial infections that affect the skin",
                "Antibiotics, drainage of abscesses, and wound care", "Bacterial skin infections"),
        Disease("Eczema", "Chronic inflammatory skin condition characterized by dry, itchy, and red skin",
                "Moisturizers, topical corticosteroids, and antihistamines", "Allergic skin conditions"),
        Disease("Exanthems and Drug Eruptions",
                "Rash caused by viral or bacterial infections, Drug Eruptions: Skin reaction caused by medication",
                "Treatment aims to ease symptoms of the skin rash and other virus symptoms. For example, your healthcare provider might recommend lotions or creams to reduce itchiness, and acetaminophen or nonsteroidal anti-inflammatory drugs (NSAIDs) can lower fever and relieve body aches.",
"Skin rashes"),
        Disease("Hair Loss Photos Alopecia and other Hair Diseases",
                "Alopecia: Hair loss, Other Hair Diseases: Various conditions that affect hair growth",
                "Topical or oral medication, hair transplant, or hairpiece", "Hair conditions"),
        Disease("Herpes HPV and other STDs Photos",
                "Herpes: Viral infection that causes painful blisters, HPV: Sexually transmitted virus that causes warts, Other STDs: Various sexually transmitted infections",
                "Antiviral medication, removal of warts, and antibiotics", "Sexually transmitted infections"),
        Disease("Light Diseases and Disorders of Pigmentation",
                "Disorders that affect the skin's pigmentation, caused by exposure to light or genetics",
                "Topical or oral medication, laser treatment, or phototherapy", "Skin pigmentation disorders"),
        Disease("Lupus and other Connective Tissue diseases",
                "Lupus: Autoimmune disorder that affects various organs including skin, Connective Tissue Diseases: Various disorders that affect the connective tissues in the body",
                "Oral and topical medication, steroids, and immune-suppressants", "Connective tissue disorders"),
        Disease("Melanoma Skin Cancer Nevi and Moles",
                "Melanoma: Deadly form of skin cancer, Nevi and Moles: Pigmented skin growths that can be benign or malignant",
                "Surgical removal, radiation therapy, chemotherapy", "Skin Cancer"),
        Disease("Nail Fungus and other Nail Disease", "Fungal infection that affects the nails, causing them to become discolored, thickened, and brittle", "Topical or oral antifungal medication, laser treatment, removal of the nail", "Fungal infections"),
        Disease("Poison Ivy Photos and other Contact Dermatitis", "Allergic reaction to contact with a substance, such as poison ivy, that causes redness, itching, and blistering of the skin", "Topical or oral medication, avoidance of the offending substance", "Skin conditions"),
        Disease("Scabies Lyme Disease and other Infestations and Bites", "Infestation of the skin by the Sarcoptes scabiei mite, Lyme disease: Bacterial infection transmitted by ticks, causing fever, headache, and rash", "Topical or oral medication for scabies, antibiotics for Lyme disease", "Infestations and bites"),
        Disease("Seborrheic Keratoses and other Benign Tumors", "Benign skin growths that can appear anywhere on the body, but are most commonly found on the face, chest, and back", "Surgical removal, cryotherapy, electrosurgery", "Skin conditions"),
        Disease("Systemic Disease", "Various skin conditions that are related to underlying systemic diseases, such as lupus or diabetes", "Treatment of underlying disease, topical or oral medication for skin symptoms", "Systemic diseases"),
        Disease("Tinea Ringworm Candidiasis and other Fungal Infections", "Fungal infections of the skin, nails, and hair, causing itching, scaling, and redness", "Topical or oral antifungal medication, avoidance of moisture and tight clothing", "Fungal infections"),
        Disease("Urticaria Hives", "Allergic reaction to various triggers, causing red, itchy, raised welts on the skin", "Antihistamines, avoidance of the triggering substance", "Skin conditions"),
        Disease("Vascular Tumors", "Abnormal growths of blood vessels in the skin, such as hemangiomas and port-wine stains", "Surgical removal, laser treatment, medication for symptoms", "Skin conditions"),
        Disease("Warts Molluscum and other Viral Infections", "Viral infections that cause small, raised bumps on the skin, such as warts and molluscum contagiosum", "Topical medication, cryotherapy, surgical removal", "Viral infections")]
def nametopara(lst, str):
    for dis in lst:
        if dis.name == str:
                return [dis.diagnosis, dis.treatment, dis.group]
                break
def namethedisease(lst, num):
        naming = input("Enter a disease name")
        print((nametopara(lst, naming))[num])
namethedisease(disease_list, 1)




