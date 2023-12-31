import unreal

"""
unreal.IKRetargetBatchOperation 是 Unreal Engine 插件 IKRig 提供的一个类，
用于批量复制和重定向一组动画资产。这个功能特别有用于需要将一系列动画从一个角色骨架转移到另一个角色骨架的情况，
例如，已有一套动画(针对特定的角色, 例如Mixamo下载的一列动画)，希望将这些动画应用到另一个外形或比例不同的角色上。
"""

# 资产路径
source_mesh_path = "/Game/Path/To/SourceSkeletalMesh"
target_mesh_path = "/Game/Path/To/TargetSkeletalMesh"
ik_retargeter_path = "/Game/Path/To/YourIKRetargeter"

# 加载资产
source_mesh = unreal.load_asset(source_mesh_path)
target_mesh = unreal.load_asset(target_mesh_path)
ik_retargeter_asset = unreal.load_asset(ik_retargeter_path)

# 定义要重定向的动画资产列表
# animations_to_retarget = unreal.EditorUtilityLibrary.get_selected_assets()
animations_to_retarget = [
    unreal.load_asset("/Game/Path/To/Animation1"),
    unreal.load_asset("/Game/Path/To/Animation2")
]

# 准备参数
assets_to_retarget = [unreal.AssetData(anim) for anim in animations_to_retarget]
search_string = "OldCharacter"  # 假设原文件名中包含"OldCharacter"
replace_string = "NewCharacter"  # 新文件名将包含"NewCharacter"
prefix = "New_"  # 新文件名前缀
suffix = "_Retargeted"  # 新文件名后缀

# 执行批量重定向操作
new_assets = unreal.IKRetargetBatchOperation.duplicate_and_retarget(
    assets_to_retarget=assets_to_retarget,
    source_mesh=source_mesh,
    target_mesh=target_mesh,
    ik_retarget_asset=ik_retargeter_asset,
    search=search_string,
    replace=replace_string,
    prefix=prefix,
    suffix=suffix,
    remap_referenced_assets=True
)

# 打印新创建的动画资产路径
for asset_data in new_assets:
    print(asset_data.object_path)
