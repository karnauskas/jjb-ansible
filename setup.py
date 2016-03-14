#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='jenkins-job-builder-ansible',
    version='0.1.1',
    description='Ansible build step for Jenkins Job Builder',
    author='Marius Karnauskas',
    author_email='marius.karnauskas@gmail.com',
    license='MIT',
    url='https://github.com/nkts/jjb-ansible',
    keywords='jenkins ansible job builder yaml',
    entry_points={
        'jenkins_jobs.builders': [
            'ansibleplaybook=jenkins_job_builder_ansible.modules.builders.ansible:ansibleplaybook'
        ]
    },
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
