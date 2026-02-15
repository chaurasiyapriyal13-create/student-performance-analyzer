import os
import pandas as pd

def main():
    # If your CSV is in root, use: "student_data.csv"
    # If your CSV is inside data folder, use: "data/student_data.csv"
    df = pd.read_csv("data/student_data (3).csv")

    # Create average grade from G1, G2, G3
    df["avg_grade"] = df[["G1", "G2", "G3"]].mean(axis=1).round(2)

    # Flag system based on avg grade
    def flag(x):
        if x < 10:
            return "RED"
        elif x >= 14:
            return "GREEN"
        else:
            return "WHITE"

    df["performance_flag"] = df["avg_grade"].apply(flag)

    # Save outputs
    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/cleaned_student_data (3).csv", index=False)

    # Report
    with open("outputs/report.txt", "w", encoding="utf-8") as f:
        f.write("Student Performance Report\n")
        f.write(f"Total students: {len(df)}\n")
        f.write(f"Average grade: {df['avg_grade'].mean():.2f}\n\n")
        f.write("Flag counts:\n")
        f.write(df["performance_flag"].value_counts().to_string())

    print("Done  Check outputs folder")

if __name__ == "__main__":
    main()
