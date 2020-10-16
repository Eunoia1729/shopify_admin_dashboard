# shopify_admin_dashboard

### How to Run ?

We use [pipenv](https://github.com/pypa/pipenv) to get running faster. With the
`.env` already created in the root directory, run the app:

1. Install Pipenv :
    - Just use pip:
        ```
        $ pip install pipenv
        ```
    - Or, if you’re using Ubuntu 17.10:
        ```
        $ sudo apt install software-properties-common python-software-properties
        $ sudo add-apt-repository ppa:pypa/ppa
        $ sudo apt update
        $ sudo apt install pipenv
        ```
    - Otherwise, if you’re on MacOS, you can install Pipenv easily with Homebrew:
        ```
        $ brew install pipenv
        ```
2. To run the project:
    ```
    $ pipenv install
    $ pipenv run python manage.py runserver
    ```

    You may get warnings about migrations, but they should not stop you.

3. Open <http://localhost:8000> in your browser to view the dashboard.
