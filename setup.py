import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weighted-delaunay", # Replace with your own username
    version="0.0.1",
    author="Mark Klose, Bansi Chhatrala, Alex Nahapetyan",
    author_email="mwklose@ncsu.edu, bschhatr@ncsu.edu, anahape@ncsu.edu",
    description="A packaged used to calculate the weighted delaunay triangulation in N-dimensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ale0x78/weighted-delaunay",
    project_urls={
        "Bug Tracker": "https://github.com/Ale0x78/weighted-delaunay/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=['scipy', 'numpy'],
)