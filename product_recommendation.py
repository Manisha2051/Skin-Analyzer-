# # product_recommendation.py

# def recommend_products(skin_type, issues):
#     """
#     Returns morning & night skincare routines with products
#     based on skin type and detected issues.
#     """

#     # ---------- BASE ROUTINE BY SKIN TYPE ----------
#     base_routines = {
#         "dry-skin": {
#             "morning": [
#                 ("Cleanser", "CeraVe Hydrating Cleanser", "Gently cleanses without drying"),
#                 ("Moisturizer", "Nivea Soft Cream", "Provides deep hydration"),
#                 ("Sunscreen", "La Shield SPF 40", "Hydrating sun protection")
#             ],
#             "night": [
#                 ("Cleanser", "Simple Refreshing Face Wash", "Removes dirt gently"),
#                 ("Serum", "Minimalist Hyaluronic Acid 2%", "Hydrates and plumps dry skin"),
#                 ("Moisturizer", "Cetaphil Moisturizing Cream", "Restores skin barrier overnight")
#             ]
#         },

#         "oily-skin": {
#             "morning": [
#                 ("Cleanser", "CeraVe Foaming Cleanser", "Removes oil and impurities"),
#                 ("Serum", "Minimalist Niacinamide 10%", "Controls oil and acne"),
#                 ("Moisturizer", "Neutrogena Hydro Boost Gel", "Oil-free hydration"),
#                 ("Sunscreen", "La Shield SPF 40", "Matte finish sunscreen")
#             ],
#             "night": [
#                 ("Cleanser", "The Derma Co Salicylic Cleanser", "Unclogs pores"),
#                 ("Serum", "The Ordinary Niacinamide", "Reduces acne marks"),
#                 ("Moisturizer", "Cetaphil Oil Control Moisturizer", "Non-comedogenic hydration")
#             ]
#         },

#         "normal-skin": {
#             "morning": [
#                 ("Cleanser", "Simple Refreshing Cleanser", "Balances oil and moisture"),
#                 ("Serum", "Minimalist Vitamin C 10%", "Brightens complexion"),
#                 ("Moisturizer", "Pond’s Super Light Gel", "Light hydration"),
#                 ("Sunscreen", "Neutrogena Ultra Sheer SPF 50", "Daily UV protection")
#             ],
#             "night": [
#                 ("Cleanser", "CeraVe Hydrating Cleanser", "Removes dirt gently"),
#                 ("Serum", "The Ordinary Retinol 0.2%", "Improves texture and tone"),
#                 ("Moisturizer", "Nivea Soft Cream", "Locks in overnight moisture")
#             ]
#         },

#         "combination-skin": {
#             "morning": [
#                 ("Cleanser", "Simple Refreshing Face Wash", "Cleans without over-drying"),
#                 ("Serum", "Minimalist Niacinamide 5%", "Balances oily T-zone"),
#                 ("Moisturizer", "Neutrogena Hydro Boost", "Hydrates dry areas"),
#                 ("Sunscreen", "Re’equil Ultra Matte SPF 50", "Matte finish sun protection")
#             ],
#             "night": [
#                 ("Cleanser", "CeraVe Foaming Cleanser", "Removes dirt & oil"),
#                 ("Serum", "The Ordinary Hyaluronic Acid", "Hydrates dry zones"),
#                 ("Moisturizer", "Simple Light Moisturizer", "Non-greasy hydration")
#             ]
#         }
#     }

#     # ---------- ADD-ON PRODUCTS BY SKIN ISSUE ----------
#     issue_addons = {
#         "facial redness": [
#             ("Serum", "Dr. Sheth’s Centella Calming Serum", "Soothes redness and irritation"),
#             ("Cream", "Avene Antirougeurs Fort", "Reduces facial redness and sensitivity")
#         ],
#         "skin pigmentation": [
#             ("Serum", "Minimalist Vitamin C 10%", "Reduces pigmentation and dark spots"),
#             ("Cream", "Melano-TX Cream", "Evens out skin tone and reduces patches")
#         ],
#         "clear healthy skin": [
#             ("Toner", "Dot & Key AHA Toner", "Removes dead skin for natural glow"),
#             ("Serum", "Minimalist Alpha Arbutin 2%", "Brightens dull skin tone")
#         ],
#         "wrinkles on face": [
#             ("Serum", "The Ordinary Retinol 1%", "Reduces wrinkles and fine lines"),
#             ("Cream", "Olay Regenerist Night Cream", "Improves firmness and elasticity")
#         ],
#         "acne on face": [
#             ("Spot Treatment", "Benzac AC Gel 2.5%", "Treats active acne and pimples"),
#             ("Serum", "Minimalist Niacinamide 10%", "Controls acne and oil")
#         ],
#         "dark circle under eyes": [
#             ("Eye Cream", "The Ordinary Caffeine Solution 5%", "Reduces puffiness and dark circles"),
#             ("Eye Gel", "Mamaearth Under Eye Cream", "Brightens under-eye area")
#         ],
#         "dark spot on face": [
#             ("Serum", "The Derma Co Kojic Acid Serum", "Lightens dark spots"),
#             ("Cream", "Olay Luminous Tone Perfecting Cream", "Fades discoloration gradually")
#         ]
#     }

#     # ---------- BUILD ROUTINE ----------
#     routines = base_routines.get(skin_type.lower(), {})
#     morning = routines.get("morning", []).copy()
#     night = routines.get("night", []).copy()

#     for issue in issues:
#         add_products = issue_addons.get(issue.lower(), [])
#         for product in add_products:
#             # add issue-specific treatments to night routine
#             night.append(product)

#     return morning, night


# # ---------- TEST ----------
# if __name__ == "__main__":
#     m, n = recommend_products("oily-skin", [
#         "acne on face", "dark spot on face", "wrinkles on face"
#     ])
#     print("🌞 Morning Routine:")
#     for step, name, use in m:
#         print(f"- {step}: {name} — {use}")
#     print("\n🌙 Night Routine:")
#     for step, name, use in n:
#         print(f"- {step}: {name} — {use}")


# product_recommendation.py

def recommend_products(skin_type, issues):
    """
    Returns morning & night skincare routines with products + prices
    based on skin type and detected issues.
    Prices are kept medium-budget (no costly products).
    """

    # ---------- BASE ROUTINE BY SKIN TYPE ----------
    base_routines = {
        "dry-skin": {
            "morning": [
                ("Cleanser", "CeraVe Hydrating Cleanser", "Gently cleanses without drying", 350),
                ("Moisturizer", "Nivea Soft Cream", "Provides deep hydration", 180),
                ("Sunscreen", "La Shield SPF 40", "Hydrating sun protection", 380)
            ],
            "night": [
                ("Cleanser", "Simple Refreshing Face Wash", "Removes dirt gently", 260),
                ("Serum", "Minimalist Hyaluronic Acid 2%", "Hydrates and plumps dry skin", 599),
                ("Moisturizer", "Cetaphil Moisturizing Cream", "Restores skin barrier overnight", 420)
            ]
        },

        "oily-skin": {
            "morning": [
                ("Cleanser", "CeraVe Foaming Cleanser", "Removes oil & impurities", 350),
                ("Serum", "Minimalist Niacinamide 10%", "Controls oil and acne", 599),
                ("Moisturizer", "Neutrogena Hydro Boost Gel", "Oil-free hydration", 350),
                ("Sunscreen", "La Shield SPF 40", "Matte finish sunscreen", 380)
            ],
            "night": [
                ("Cleanser", "The Derma Co Salicylic Cleanser", "Unclogs pores", 299),
                ("Serum", "The Ordinary Niacinamide 10%", "Reduces acne marks", 650),
                ("Moisturizer", "Cetaphil Oil Control Moisturizer", "Non-comedogenic hydration", 350)
            ]
        },

        "normal-skin": {
            "morning": [
                ("Cleanser", "Simple Refreshing Cleanser", "Balances oil & moisture", 260),
                ("Serum", "Minimalist Vitamin C 10%", "Brightens complexion", 599),
                ("Moisturizer", "Pond’s Super Light Gel", "Light hydration", 250),
                ("Sunscreen", "Neutrogena Ultra Sheer SPF 50", "Daily UV protection", 300)
            ],
            "night": [
                ("Cleanser", "CeraVe Hydrating Cleanser", "Removes dirt gently", 350),
                ("Serum", "The Ordinary Retinol 0.2%", "Improves texture & tone", 650),
                ("Moisturizer", "Nivea Soft Cream", "Locks in moisture", 180)
            ]
        },

        "combination-skin": {
            "morning": [
                ("Cleanser", "Simple Refreshing Face Wash", "Cleans without over-drying", 260),
                ("Serum", "Minimalist Niacinamide 5%", "Balances oily T-zone", 549),
                ("Moisturizer", "Neutrogena Hydro Boost", "Hydrates dry areas", 350),
                ("Sunscreen", "Re’equil Ultra Matte SPF 50", "Matte sun protection", 380)
            ],
            "night": [
                ("Cleanser", "CeraVe Foaming Cleanser", "Removes dirt & oil", 350),
                ("Serum", "The Ordinary Hyaluronic Acid", "Hydrates dry zones", 650),
                ("Moisturizer", "Simple Light Moisturizer", "Non-greasy hydration", 240)
            ]
        }
    }

    # ---------- ADD-ON PRODUCTS BY SKIN ISSUE ----------
    issue_addons = {
        "facial redness": [
            ("Serum", "Dr. Sheth’s Centella Calming Serum", "Soothes redness", 499),
            ("Cream", "Avene Antirougeurs Fort", "Reduces redness & sensitivity", 350)
        ],
        "skin pigmentation": [
            ("Serum", "Minimalist Vitamin C 10%", "Reduces pigmentation", 599),
            ("Cream", "Melano-TX Cream", "Evens out skin tone", 320)
        ],
        "clear healthy skin": [
            ("Toner", "Dot & Key AHA Toner", "Removes dead skin", 350),
            ("Serum", "Minimalist Alpha Arbutin 2%", "Brightens dull skin", 599)
        ],
        "wrinkles on face": [
            ("Serum", "The Ordinary Retinol 1%", "Reduces wrinkles", 650),
            ("Cream", "Olay Regenerist Night Cream", "Improves elasticity", 399)
        ],
        "acne on face": [
            ("Spot Treatment", "Benzac AC Gel 2.5%", "Treats active acne", 180),
            ("Serum", "Minimalist Niacinamide 10%", "Controls acne", 599)
        ],
        "dark circle under eyes": [
            ("Eye Cream", "The Ordinary Caffeine Solution 5%", "Reduces puffiness", 650),
            ("Eye Gel", "Mamaearth Under Eye Cream", "Brightens under-eyes", 350)
        ],
        "dark spot on face": [
            ("Serum", "The Derma Co Kojic Acid Serum", "Lightens dark spots", 499),
            ("Cream", "Olay Luminous Tone Perfecting Cream", "Fades discoloration", 399)
        ]
    }

    # ---------- BUILD ROUTINE ----------
    routines = base_routines.get(skin_type.lower(), {})
    morning = routines.get("morning", []).copy()
    night = routines.get("night", []).copy()

    for issue in issues:
        add_products = issue_addons.get(issue.lower(), [])
        for product in add_products:
            night.append(product)   # Issue treatments added to night routine

    return morning, night


# ---------- TEST ----------
if __name__ == "__main__":
    m, n = recommend_products("oily-skin", [
        "acne on face", "dark spot on face", "wrinkles on face"
    ])

    print("🌞 Morning Routine:")
    for step, name, use, price in m:
        print(f"- {step}: {name} — {use} — ₹{price}")

    print("\n🌙 Night Routine:")
    for step, name, use, price in n:
        print(f"- {step}: {name} — {use} — ₹{price}")
