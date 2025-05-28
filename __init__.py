from .nodes import LoadHunyuanPortraitImage, LoadHunyuanPortraitVideo, LoadHunyuanPortraitConfig, HunyuanPortrait

NODE_CLASS_MAPPINGS = {
    "LoadHunyuanPortraitImage": LoadHunyuanPortraitImage,
    "LoadHunyuanPortraitVideo": LoadHunyuanPortraitVideo,
    "LoadHunyuanPortraitConfig": LoadHunyuanPortraitConfig,
    "HunyuanPortrait": HunyuanPortrait,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadHunyuanPortraitImage": "Load HunyuanPortrait Image",
    "LoadHunyuanPortraitVideo": "Load HunyuanPortrait Video",
    "LoadHunyuanPortraitConfig": "Load HunyuanPortrait Config",
    "HunyuanPortrait": "HunyuanPortrait",
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
