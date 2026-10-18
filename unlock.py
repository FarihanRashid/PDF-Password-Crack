import pikepdf

# Replace with your actual file name
input_filename = "929837541-Mentors-Private-University-Admission-Guide-2024.pdf"
output_filename = "Mentor2024Guide.pdf"

# Opens the restricted PDF and saves a copy without permissions flags
with pikepdf.open(input_filename) as pdf:
    pdf.save(output_filename)

print("PDF restrictions successfully removed!")
