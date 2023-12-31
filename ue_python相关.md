如何在ue的python中安装库
1. 找到项目文件，在办公室PC中，path是
    D:\UE5.3(x86)\UE_5.0\Engine\Binaries\ThirdParty\Python3\Win64
2. 在cmd中执行:
    "D:\UE5.3(x86)\UE_5.0\Engine\Binaries\ThirdParty\Python3\Win64\python.exe" -m pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple


**在使用UE中的python相关的功能和开发时，要注意**:
## 尽管Unreal Engine的Python API非常强大，但它主要用于资产管理、场景构建和简单的编辑器任务。对于复杂的动画操作，如骨骼重定向和动画数据的精细调整，可能更适合在UE编辑器中手动进行，或者使用UE的C++ API进行更深入的开发。


**UE常用命令(部分摘录)**
## unreal.EditorUtilityLibrary
    # classmethod get_actor_reference(path_to_actor) → Actor, 获取引用actor
    # * classmethod get_selected_assets() → Array[Object]
    # classmethod get_selected_assets_of_class(asset_class) → Array[Object]
    # classmethod get_selected_blueprint_classes() → Array[type(Class)]
## unreal.EditorAssetLibrary
    # classmethod checkout_asset(asset_to_checkout) → bool
    # classmethod checkout_loaded_asset(asset_to_checkout) → bool
    # classmethod consolidate_assets(asset_to_consolidate_to, assets_to_consolidate) → bool
    # classmethod delete_asset(asset_path_to_delete) → bool
    # classmethod duplicate_asset(source_asset_path, destination_asset_path)
    # classmethod find_asset_data(asset_path) → AssetData
    # classmethod find_package_referencers_for_asset(asset_path, load_assets_to_confirm=False) → Array[str]
    # classmethod get_path_name_for_loaded_asset(loaded_asset) → str
    # classmethod list_assets(directory_path, recursive=True, include_folder=False) → Array[str]
    # * classmethod load_asset(asset_path) → Object
    # classmethod load_blueprint_class(asset_path)
    # classmethod make_directory(directory_path) → bool
    # classmethod save_asset(asset_to_save, only_if_is_dirty=True) → bool
    # classmethod save_directory(directory_path, only_if_is_dirty=True, recursive=True) → bool
## unreal.AssetToolsHelpers
    # * classmethod get_asset_tools() → AssetTools
    ## unreal.AssetTools
        # create_asset(asset_name, package_path, asset_class, factory, calling_context='None') → Object
            Parameters:
                asset_name (str) – the name of the new asset
                package_path (str) – the package that will contain the new asset
                asset_class (type(Class)) – the class of the new asset
                factory (Factory) – the factory that will build the new asset
                calling_context (Name) – optional name of the module or method calling CreateAsset() - this is passed to the factory
                Returns:
                the new asset or NULL if it fails
                Return type:
                Object
        # create_asset_with_dialog(asset_name, package_path, asset_class, factory, calling_context='None', call_configure_properties=True) → Object
            Opens an asset picker dialog and creates an asset with the specified name and path
            Parameters:
                asset_name (str) –
                package_path (str) –
                asset_class (type(Class)) –
                factory (Factory) –
                calling_context (Name) –
                call_configure_properties (bool) –
                Return type:
                Object
        # duplicate_asset(asset_name, package_path, original_object) → Object
        # import_asset_tasks(import_tasks) → None
            Imports assets using tasks specified.
            Parameters:
                import_tasks (Array[AssetImportTask]) – Tasks that specify how to import each file
