# About Problem

At first, we work at a company and we have some employee who work with together.But some of them are not happy in our company and they might think of leaving in our company.So we need to predict people who want to leave or churn in our company.People who want to churn is 1.People who dont want to churn is 0.We want to identity between 0 and 1.If people is likely to churn, we will send some bonus like money, air ticket, etc.., to stop from churning.We need to be accurate because we dont want to lose money for people who arent going to churn and we dont want to accidentally miss people who are going to churn.Our problem is binary classification.So we want to use binary classification models like logistic, decision tree, etc.., to identity them.

## About Dataset

In this project, we will use employee dataset from [kaggle](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset).

**_Context:_**

This dataset contains information about employees in a company, including their educational backgrounds, work history, demographics, and employment-related factors. It has been anonymized to protect privacy while still providing valuable insights into the workforce.

**_Columns:_**

_Education:_ The educational qualifications of employees, including degree, institution, and field of study.

_Joining Year:_ The year each employee joined the company, indicating their length of service.

_City:_ The location or city where each employee is based or works.

_Payment Tier:_ Categorization of employees into different salary tiers.

_Age:_ The age of each employee, providing demographic insights.

_Gender:_ Gender identity of employees, promoting diversity analysis.

_Ever Benched:_ Indicates if an employee has ever been temporarily without assigned work.

_Experience in Current Domain:_ The number of years of experience employees have in their current field.

_Leave or Not:_ a target column

**_Usage:_**

This dataset can be used for various HR and workforce-related analyses, including employee retention, salary structure assessments, diversity and inclusion studies, and leave pattern analyses. Researchers, data analysts, and HR professionals can gain valuable insights from this dataset.

## Instructions

Clone the project

```bash
  git clone https://github.com/anonyblank/mid-term.git
```

Go to the project directory

```bash
  cd mid-term
```

Install dependencies

```bash
  pipenv install
```

Activate environment

```bash
  pipenv shell
```

Create Directory

```bash
  mkdir model
```

Start the server

```bash
  pipenv run
```
