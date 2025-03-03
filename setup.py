from setuptools import setup, find_packages

setup(
    name='vector_db_exercise',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'openai',
        'faiss-cpu',
        'python-dotenv',
        'flask',
    ],
)
