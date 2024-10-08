from setuptools import setup, find_packages

setup(
    name="mon_projet_youtube",                # Nom du projet
    version="0.1",                    # Version du projet
    packages=find_packages(),         # Inclut automatiquement tous les modules
    install_requires=[                # Dépendances du projet
        'requests',                   # Par exemple, requests
    ],
    entry_points={                    # Pour exécuter ton script en ligne de commande
        'console_scripts': [
            'mon_projet=mon_projet_youtube.mon_script:main',
        ],
    },
)
