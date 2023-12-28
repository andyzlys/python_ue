import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for asset in selected_assets:
    for prop in unreal.SystemLibrary.get_class_properties(asset.get_class()):
            print(f"Property: {prop.get_name()} - Type: {prop.get_property_class().get_name()}")