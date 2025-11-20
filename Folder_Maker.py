import os


def create_study_folders():
    """Create all 64 study folders from the learning plan"""

    # Define the folder structure
    folder_structure = {
        "01-learn-the-basic": [
            "basic-syntax",
            "variables-and-data-types",
            "conditionals",
            "loops",
            "type-casting",
            "exceptions",
            "functions",
            "lists",
            "tuples",
            "sets",
            "dictionaries"
        ],
        "02-data-structures-and-algorithms": [
            "arrays-and-linked-lists",
            "hash-tables",
            "heaps-stacks-and-queues",
            "binary-search-tree",
            "recursion",
            "sorting-algorithms"
        ],
        "03-modules": [
            "builtin",
            "custom"
        ],
        "04-lambdas": [],
        "05-decorators": [],
        "06-iterators": [],
        "07-regular-expressions": [],
        "08-object-oriented-programming": [
            "classes",
            "inheritance",
            "methods-and-dunder-methods"
        ],
        "09-package-managers": [],
        "10-common-packages": [],
        "11-list-comprehensions": [],
        "12-generator-expressions": [],
        "13-paradigms": [],
        "14-context-manager": [],
        "15-learn-a-framework": [
            "tornado",
            "sanic",
            "fastapi",
            "django",
            "flask"
        ],
        "16-concurrency": [
            "multiprocessing",
            "asynchrony",
            "gil",
            "threading"
        ],
        "17-environments": [
            "pipenv",
            "virtualenv",
            "pyenv"
        ],
        "18-static-typing": [
            "pydantic",
            "pyre",
            "pyright",
            "mypy",
            "typing-module"
        ],
        "19-code-formatting": [
            "yapf",
            "black",
            "ruff"
        ],
        "20-sphinx": [],
        "21-file-handling": [],
        "22-testing": [
            "tox",
            "nose",
            "unittest",
            "doctest",
            "pytest"
        ]
    }

    total_folders = 0
    created_folders = []

    # Create all folders
    for main_folder, sub_folders in folder_structure.items():
        # Create main folder
        os.makedirs(main_folder, exist_ok=True)
        created_folders.append(main_folder)
        total_folders += 1

        # Create sub-folders
        for sub_folder in sub_folders:
            sub_folder_path = os.path.join(main_folder, sub_folder)
            os.makedirs(sub_folder_path, exist_ok=True)
            created_folders.append(f"  └── {sub_folder}")
            total_folders += 1

    return total_folders, created_folders


def main():
    print("Creating study folder structure...")
    print("=" * 50)

    total_folders, created_folders = create_study_folders()

    print(f"Successfully created {total_folders} folders!")
    print("\nFolder structure created:")
    print("-" * 30)

    for folder in created_folders:
        print(folder)

    print(f"\nTotal: {total_folders} folders created successfully!")


if __name__ == "__main__":
    main()