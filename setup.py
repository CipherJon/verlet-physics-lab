from setuptools import find_packages, setup

setup(
    name="verlet-physics-lab",
    version="0.1.0",
    description="A Verlet physics simulation lab for softbody and ragdoll simulations",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pygame>=2.6.1",
    ],
    python_requires=">=3.10",
)
