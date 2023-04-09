# Django Client Whitelist

Django Client Whitelist is a middleware that restricts access to certain endpoints in a Django app to a predefined list of client hosts. It is a simple and effective solution to improve the security of your application.

## Problem
In a production environment, it is crucial to restrict access to API endpoints to only those hosts that are authorized to access them. Unauthorized access can lead to malicious attacks and compromise the security of your Django application.

## Solution
Django Client Whitelist provides a solution to this problem by allowing you to create a predefined list of client hosts that are allowed to access the API. With this middleware in place, you can be sure that only authorized hosts can request your API endpoints, making your application more secure.

## Installation
Install Django Client Whitelist using pip:

```bash
pip install django-client-whitelist
```
add `client_whitelist` to your `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'client_whitelist',
    # ...
]
```
Add ClientWhitelistMiddleware to your middleware stack:

```python
# settings.py
MIDDLEWARE = [
    # ...
    'client_whitelist.middleware.ClientWhitelistMiddleware',
    # ...
]
```

## Usage

Define the `PROTECTED_ENDPOINTS` and `ALLOWED_CLIENT_HOSTS` settings in your settings file:

```python
# settings.py
PROTECTED_ENDPOINTS = [
    '/admin/',
    '/api/',
]

ALLOWED_CLIENT_HOSTS = [
    'example.com',
    '192.168.1.1',
]
```

Note: In a development environment, it may be convenient to allows requests from any client host.

```python
ALLOWED_CLIENT_HOSTS = ['*']
```

However, it is important to note that this should not be used in a production environment as it undermines the security measures provided by Django Client Whitelist. It is recommended to use a predefined list of client hosts that are authorized to access the API in a production environment.

Once you have installed and configured Django Client Whitelist, it will start protecting your endpoints immediately. Any requests to a protected endpoint from a client host that is not in the allowed list will result in a 403 Forbidden response.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
