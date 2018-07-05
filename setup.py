from setuptools import setup, find_packages

setup(
    name='jenkins-job-builder-ansible',
    version='0.2.0',
    description='Ansible build step for Jenkins Job Builder',
    author='Marius Karnauskas',
    author_email='marius.karnauskas@gmail.com',
    license='MIT',
    url='https://github.com/karnauskas/jjb-ansible',
    keywords='jenkins ansible job builder yaml',
    entry_points={
        'jenkins_jobs.builders': [
            'ansibleplaybook=jenkins_job_builder_ansible.modules.builders.ansible:ansibleplaybook',
            'jobdsl=jenkins_job_builder_ansible.modules.builders.jobdsl:jobdsl'
        ]
    },
    install_requires = [
        'jenkins-job-builder'
    ],
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
