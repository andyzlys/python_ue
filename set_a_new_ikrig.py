import unreal


# 定义IK Rig和骨骼网格的名称和路径
ik_rig_asset_name = "MyIKRigDefinition"
skeletal_mesh_asset_path = "/Game/Path/To/YourSkeletalMesh.YourSkeletalMesh"  # 替换为骨骼网格路径
asset_path = "/Game/MetaHumans/Dhruv"

# 加载骨骼网格资产
asset_to_check = unreal.EditorAssetLibrary.load_asset(skeletal_mesh_asset_path)

# 确保骨骼网格资产已正确加载
if not asset_to_check:
    print("Asset is none.")
elif not isinstance(asset_to_check, unreal.SkeletalMesh):
    print("The class of this Asset is not expected.")
else:
    # 获取资产工具
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # 创建IKRigDefinition资产
    ik_rig_definition_factory = unreal.IKRigDefinitionFactory()
    ik_rig_definition_factory.set_editor_property('edit_after_new', True)
    ik_rig_definition = asset_tools.create_asset_with_dialog(ik_rig_asset_name, asset_path, unreal.IKRigDefinition, ik_rig_definition_factory)

    # 保存对IKRigDefinition资产的更改
    asset_full_path = f"{asset_path}/{ik_rig_asset_name}.{ik_rig_asset_name}"  # 构建资产的完整路径
    saved = unreal.EditorAssetLibrary.save_asset(asset_full_path, only_if_is_dirty=True)
    if saved:
        print(f"Asset saved successfully: {asset_full_path}")
    else:
        print(f"Failed to save asset: {asset_full_path}")


    if ik_rig_definition:
        print(f"Created new IKRigDefinition asset: {asset_path}/{ik_rig_asset_name}")

        ik_rig_definition.set_editor_property('preview_skeletal_mesh', asset_to_check)

        # asset_full_path = f"{asset_path}/{ik_rig_asset_name}.{ik_rig_asset_name}"  # 构建资产的完整路径
        # saved = unreal.EditorAssetLibrary.save_asset(asset_full_path, only_if_is_dirty=True)
        # if saved:
        #     print(f"Asset saved successfully: {asset_full_path}")
        # else:
        #     print(f"Failed to save asset: {asset_full_path}")

        ik_rig_definition.set_editor_property('draw_goals', True)
        ik_rig_controller = unreal.IKRigController.get_controller(ik_rig_definition)
        ik_rig_controller.add_retarget_chain('spine', 'spine_01', 'spine_02', 'None')


    else:
        print("Failed to create IKRigDefinition asset.")


        