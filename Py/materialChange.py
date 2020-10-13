import unreal


def replaceMaterial(original, replacement) :

    print "hello"
    original_asset = unreal.EditorAssetLibrary.load_asset(original)
    replacement_asset = unreal.EditorAssetLibrary.load_asset(replacement)
    unreal.EditorAssetLibrary.consolidate_assets(replacement_asset,[original_asset])

# Game: Content folder
replaceMaterial('/Game/Technical_school/Materials/Glass','/Game/Materials/M_Glass_Inst')