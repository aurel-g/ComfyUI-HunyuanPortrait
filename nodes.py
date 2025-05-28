from omegaconf import OmegaConf


class LoadHunyuanPortraitImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_path": ("STRING", {"default": "assets/source_image.png"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "input_image"
    CATEGORY = "HunyuanPortrait"

    def input_image(self, image_path):
        image = image_path
        return (image,)
        

class LoadHunyuanPortraitVideo:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_path": ("STRING", {"default": "assets/driving_video.mp4"}),
            }
        }

    RETURN_TYPES = ("VIDEO",)
    RETURN_NAMES = ("video",)
    FUNCTION = "input_video"
    CATEGORY = "HunyuanPortrait"

    def input_video(self, video_path):
        video = image_path
        return (video,)

