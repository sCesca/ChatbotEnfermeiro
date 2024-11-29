from setuptools import setup, find_packages

setup(
    name="chatbot-enfermeiro",
    version="0.1.0",
    description="Um chatbot enfermeiro simples.",
    author="Seu Nome",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    extras_require={
        "dev": ["flake8", "mypy", "pytest"],
    },
)
