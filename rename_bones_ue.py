
"""
首先安装
使用示例：
import pyfile as PYF
# 假设PYF中用def定义了各种function, 假设有一个是get_all_level_actors()
from importlib import reload
reload(PYF)
PYF.get_all_level_actors()

"""
import unreal
from deal_excel_names import excel_to_dicts

def rename_bones_in_selected_skeleton(excel_file_path='', source=''):
    """
    Renames the bones in the selected skeleton asset in UE's Content Browser using the provided dictionary.
    
    Args:
    - rename_dict (dict): A dictionary where the keys are the original bone names and the values are the new bone names.
    
    Note: This function must be run within Unreal Engine's Python environment.
    """
    # Check if the Excel file path was provided
    if not excel_file_path:
        raise ValueError("No Excel file path provided.")
    # Check if the source column name was provided
    if not source:
        raise ValueError("No source column name provided.")
    # Generate the rename dictionary from the Excel file
    rename_dict = excel_to_dicts(excel_file_path)[source]

    # Get the selected assets in the content browser
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    
    # Loop through the selected assets to find the Skeleton assets
    for asset in selected_assets:
        # Check if the asset is a Skeleton
        if isinstance(asset, unreal.Skeleton):
            # Get the current bone names
            bone_names = asset.get_editor_property('bone_names')
            
            # Loop through each bone name and rename it if it's in the rename dictionary
            for bone_name in bone_names:
                if bone_name in rename_dict:
                    new_bone_name = rename_dict[bone_name]
                    if new_bone_name:  # Check if new name is not None or empty
                        # Rename the bone
                        asset.rename_bone(bone_name, new_bone_name)
            
            # Save the changes to the asset
            unreal.EditorAssetLibrary.save_asset(asset.get_path_name(), True)
            print(f'Bones have been renamed in the skeleton asset: {asset.get_path_name()}')

    print('Completed renaming bones in selected skeleton assets.')

# The rename_dict should be the dictionary obtained from the excel_to_dictionaries function,
# where the keys are the names in the metahuman and the values are the third-party names.
# Example usage:
# rename_dict = excel_to_dictionaries('/path/to/your/excel/file.xlsx')['third_party_bone_names_column']
# rename_bones_in_selected_skeleton(rename_dict)



if __name__ == '__main__':
    # 先在内容浏览器中选中需要修改的.uasset文件
    excel_file_path = r'./ik_bones_rename.xlsx'
    source = 'mixamo_xiaobairen'
    rename_bones_in_selected_skeleton(excel_file_path=excel_file_path, source=source)
