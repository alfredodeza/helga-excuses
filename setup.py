from setuptools import setup

setup(
	name='helga-excuses',
	use_hg_version=True,
	author="Alfredo Deza",
	author_email="contact@deza.pe",
	url="https://github.com/alfredodeza/helga-excuses",
	packages=setuptools.find_packages(),
	include_package_data=True,
	zip_safe=True,
    install_requires=[
        'BeautifulSoup',
        'requests',
    entry_points = dict(
        helga_handlers = [
            'excuses = helga_excuses.excuses:ExcusesExtension',
        ],
    ),
)
