from setuptools import setup


setup(
    name='cldfbench_honkola_et_al2013',
    py_modules=['cldfbench_honkola_et_al2013'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'honkola_et_al2013=cldfbench_honkola_et_al2013:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
