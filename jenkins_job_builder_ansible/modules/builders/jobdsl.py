import xml.etree.ElementTree as ET

# from pprint import  pprint

def lower_bool(p):
    return str(p).lower()

def jobdsl(parser, parent, data):
    # pprint(data)

    plugin = ET.SubElement(parent, "javaposse.jobdsl.plugin.ExecuteDslScripts")

    inline_script = data.get("using-script-text", False)

    ET.SubElement(plugin, "usingScriptText").text = lower_bool(inline_script)

    if not inline_script:
        ET.SubElement(plugin, "targets").text = data.get("targets", "")
    if inline_script:
        ET.SubElement(plugin, "scriptText").text = data.get("script", "")

    ET.SubElement(plugin, "sandbox").text = lower_bool(data.get("sandbox", False))
    ET.SubElement(plugin, "ignoreExisting").text = lower_bool(data.get("ignore-existing", False))
    ET.SubElement(plugin, "ignoreMissingFiles").text = lower_bool(data.get("ignore-missing-files", False))
    ET.SubElement(plugin, "failOnMissingPlugin").text = lower_bool(data.get("fail-on-missing-plugin", False))
    ET.SubElement(plugin, "unstableOnDeprecation").text = lower_bool(data.get("unstable-on-deprecation", False))
    ET.SubElement(plugin, "removedJobAction").text = data.get("removed-job-action", "IGNORE").upper()
    ET.SubElement(plugin, "removedViewAction").text = data.get("removed-view-action", "IGNORE").upper()
    ET.SubElement(plugin, "removedConfigFilesAction").text = data.get("removed-config-files-action", "IGNORE").upper()
    ET.SubElement(plugin, "lookupStrategy").text = data.get("lookup-strategy", "JENKINS_ROOT")
    ET.SubElement(plugin, "additionalClasspath").text = "\n".join(data.get("classpath", []))

    # ET.dump(plugin)
