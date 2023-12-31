import unreal

# # ik_controller = unreal.get_controller()

# # 定义资产的名称和保存路径
# asset_name = "MyIKRigDefinition"
# asset_path = "/Game/MetaHumans/Dhruv"

# # 获取资产工具和资产目录服务
# asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
# asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

# # 检查资产是否已存在
# existing_assets = asset_registry.get_assets_by_path(unreal.Paths.normalize_directory_name(asset_path))
# for asset in existing_assets:
#     if asset.asset_name == asset_name:
#         print(f"Asset already exists: {asset.asset_path}")
#         ik_rig_definition = unreal.load_asset(asset.asset_path)
#         break
# else:
#     # 创建一个新的IKRigDefinition资产
#     ik_rig_definition_factory = unreal.IKRigDefinitionFactory()
#     ik_rig_definition = asset_tools.create_asset(asset_name, asset_path, None, ik_rig_definition_factory)
#     if ik_rig_definition:
#         print(f"Created new IKRigDefinition asset: {asset_path}/{asset_name}")
#     else:
#         print("Failed to create IKRigDefinition asset.")




# 定义IK Rig和骨骼网格的名称和路径
ik_rig_asset_name = "MyIKRigDefinition"
skeletal_mesh_asset_path = "/Game/Path/To/YourSkeletalMesh.YourSkeletalMesh"  # 替换为你的骨骼网格路径
asset_path = "/Game/MetaHumans/Dhruv"

# 加载骨骼网格资产
skeletal_mesh = unreal.load_asset(skeletal_mesh_asset_path)

# 确保骨骼网格资产已正确加载
if not skeletal_mesh or not isinstance(skeletal_mesh, unreal.SkeletalMesh):
    print("Failed to load the Skeletal Mesh asset.")
else:
    # 获取资产工具
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # 创建IKRigDefinition资产
    ik_rig_definition_factory = unreal.IKRigDefinitionFactory()
    ik_rig_definition_factory.set_editor_property('TargetSkeleton', skeletal_mesh.skeleton)  # 指定骨骼网格
    ik_rig_definition = asset_tools.create_asset(ik_rig_asset_name, asset_path, None, ik_rig_definition_factory)

    if ik_rig_definition:
        print(f"Created new IKRigDefinition asset: {asset_path}/{ik_rig_asset_name}")
    else:
        print("Failed to create IKRigDefinition asset.")
