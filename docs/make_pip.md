**Make PIP your self**

1. `git clone https://github.com/humblesami/sam-djtools.git`
2. `cd sam-djtools`

3. Find and replace `sam-djtools` with your own `your_module_name`

**Build and test using sample_usage locally**

rm -r dist/*

rm -r build/*

pip install -r requirements.txt

python setup.py sdist bdist_wheel -v=1.0

**Test the built package**

`pip uninstall -y your_module_name`

`pip install dist/your_module_name-1.0-py3-none-any.whl`

**Upload your pip**

Install twine

`sudo apt-get update`

`sudo apt-get install twine`

https://twine.readthedocs.io/en/stable/

`pip install twine`

**Sample config files for twine**

1. .pypirc_test (add this to root directory where setup.py exists)

    [distutils]
    index-servers = pypi

    [pypi]
    repository: https://test.pypi.org/legacy/
    username: __token__
    password: token1


2. .pypirc_prod (add this to root directory where setup.py exists)

    [distutils]
    index-servers = pypi

    [pypi]
    repository: https://pypi.org/legacy/
    username: __token__
    password: token2

**Final Step**

`twine upload --repository testpypi dist/*`

`twine upload dist/* --config-file .pypirc_test`


*After upload Install the uploaded package*

pip install -i https://test.pypi.org/simple/ your_module_name


`twine upload dist/* --config-file .pypirc_prod`

*After upload Install the uploaded package*

pip install your_module_name