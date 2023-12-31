import unreal

ik_controller = unreal.IKRigController().get_controller()

# 定义资产的名称和保存路径
asset_name = "MyIKRigDefinition"
asset_path = "/Game/MetaHumans/Dhruv"

# 获取资产工具和资产目录服务
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

# 检查资产是否已存在
existing_assets = asset_registry.get_assets_by_path(unreal.Paths.normalize_directory_name(asset_path))
for asset in existing_assets:
    if asset.asset_name == asset_name:
        print(f"Asset already exists: {asset.asset_path}")
        ik_rig_definition = unreal.load_asset(asset.asset_path)
        break
else:
    # 创建一个新的IKRigDefinition资产
    ik_rig_definition_factory = unreal.IKRigDefinitionFactory()
    ik_rig_definition = asset_tools.create_asset(asset_name, asset_path, None, ik_rig_definition_factory)
    if ik_rig_definition:
        print(f"Created new IKRigDefinition asset: {asset_path}/{asset_name}")
    else:
        print("Failed to create IKRigDefinition asset.")

# 现在你有了ik_rig_definition对象，你可以根据需要对其进行操作
