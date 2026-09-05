import hou
import datetime

# Example: Rename current file to include timestamp if it's untitled
if hou.hipFile.name().endswith("untitled.hip"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Note: This requires saving to a new path, not just renaming the in-memory name
    hou.hipFile.save(f"{timestamp}.hip")
    
hou.appendSessionModuleSource('hou.hscript("autosave on")')