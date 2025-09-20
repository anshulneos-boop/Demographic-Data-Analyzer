import pandas as pd

# Load dataset
df = pd.read_csv("adult.data.csv")

def calculate_demographics():
    # Race count
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage with Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]

    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # Rich percentage among min hour workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # Country with highest percentage of rich
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (country_rich_counts / country_counts * 100).idxmax()
    highest_earning_country_percentage = round((country_rich_counts / country_counts * 100).max(), 1)

    # Top occupation for rich in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax() if not india_rich.empty else None

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
