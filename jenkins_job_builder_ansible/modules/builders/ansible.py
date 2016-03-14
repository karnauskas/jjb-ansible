import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base
from jenkins_jobs.errors import JenkinsJobsException
import logging

def ansibleplaybook(parser, xml_parent, data):
    """yaml: ansibleplaybook
    """
    logger = logging.getLogger("%s:ansibleplaybook" % __name__)
    apb = XML.SubElement(xml_parent, 'org.jenkinsci.plugins.ansible.AnsiblePlaybookBuilder')
    inventoryPath = XML.SubElement(apb, 'inventory', {'class':'org.jenkinsci.plugins.ansible.InventoryPath'})

    XML.SubElement(apb, 'playbook').text = data.get('playbook', 'deploy.yml')
    XML.SubElement(inventoryPath, 'path').text = data.get('inventory_path', '/etc/ansible/ec2.py')
    XML.SubElement(apb, 'limit').text = data.get('limit', '')

    XML.SubElement(apb, 'tags').text = data.get('tags', '')
    XML.SubElement(apb, 'skippedTags').text = data.get('skippedTags', '')
    XML.SubElement(apb, 'startAtTask').text = data.get('startAtTask', '')
    XML.SubElement(apb, 'credentialsId').text = data.get('credentialsId')
    XML.SubElement(apb, 'forks').text = str(data.get('forks', 5))
    XML.SubElement(apb, 'sudo').text = str(data.get('sudo', False)).lower()
    XML.SubElement(apb, 'sudoUser').text = data.get('sudoUser', 'root')
    XML.SubElement(apb, 'unbufferedOutput').text = str(data.get('unbufferedOutput', True)).lower()
    XML.SubElement(apb, 'colorizedOutput').text = str(data.get('colorizedOutput', False)).lower()
    XML.SubElement(apb, 'hostKeyChecking').text = str(data.get('hostKeyChecking', False)).lower()
    XML.SubElement(apb, 'additionalParameters').text = data.get('additionalParameters', '')
    XML.SubElement(apb, 'copyCredentialsInWorkspace').text = str(data.get('copyCredentialsInWorkspace', False)).lower()
