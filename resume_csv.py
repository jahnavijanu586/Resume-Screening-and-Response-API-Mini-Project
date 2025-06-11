import pandas as pd

sample_data = {
    'blurb': [
        "Experienced Python developer with 5+ years in machine learning.",
        "MBA holder with 3 years in project management.",
        "No experience, looking for internship.",
        "Java engineer with 10+ years experience.",
        "Experienced data scientist proficient in Python and SQL.",
        "Project manager with expertise in Agile methodologies.",
        "Seeking a software engineering internship in Java.",
        "Machine learning specialist with experience in TensorFlow."
    ],
    'label': ['Shortlist', 'Shortlist', 'Reject', 'Shortlist', 'Shortlist', 'Shortlist', 'Reject', 'Shortlist']
}
df = pd.DataFrame(sample_data)
df.to_csv('resumes_dataset.csv', index=False)
