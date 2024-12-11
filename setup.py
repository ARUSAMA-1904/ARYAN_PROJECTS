from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

# Read the dependencies from requirements.txt
requirements = parse_requirements("requirements.txt")

# Define the setup
setup(
    name="ARYAN_PROJECTS",  # Replace with your project name
    version="0.1.0",  # Update your project version
    description="Your project description here",
    author="ARYAN NAIR",
    author_email="nairaryan1904@gmail.com",
    packages=find_packages(),
    install_requires=requirements,  # Dependencies loaded from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify minimum Python version
)
