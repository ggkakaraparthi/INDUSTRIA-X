import os


def inspect_dataset():

    print("=" * 60)
    print("        INDUSTRIA-X - VISUAL INSPECTION")
    print("=" * 60)

    inspection_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "inspection"
    )

    if not os.path.exists(inspection_path):

        print("\nINSPECTION DATASET STATUS")
        print("-" * 40)
        print("Status : NOT AVAILABLE")

        print("\nDefect Classification : Not evaluated")
        print("Defect Localization   : Not evaluated")
        print("Robustness Testing    : Not evaluated")
        print("False Accept/Reject   : Not evaluated")

        print("\nReason:")
        print(
            "No organizer-provided inspection image/defect "
            "dataset is available in the supplied files."
        )

        print("\nThe inspection pipeline is ready for future data.")

        return

    print("\nInspection dataset found.")
    print("Inspection module ready for analysis.")


if __name__ == "__main__":
    inspect_dataset()