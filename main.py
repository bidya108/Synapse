import argparse
from datetime import datetime
from synapse.pipelines.supervisor import run_pipeline


def main():
    parser = argparse.ArgumentParser(
        description="Synapse Daily - AI & ML News Digest"
    )

    parser.add_argument(
        "--demo",
        action="store_true",
        help="Generate a PDF using demo news without calling external APIs"
    )

    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")

    print(f"Starting Synapse Daily for {today}...")

    success = run_pipeline(
        date=today,
        demo=args.demo
    )

    if success:
        print("Synapse Daily completed successfully.")
    else:
        print("Synapse Daily could not generate the report.")


if __name__ == "__main__":
    main()