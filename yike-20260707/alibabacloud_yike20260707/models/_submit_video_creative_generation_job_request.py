# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoCreativeGenerationJobRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        avatar_data: str = None,
        job_params: str = None,
        output_languages: str = None,
        resolution: str = None,
        scene_type: str = None,
        user_data: str = None,
        user_materials: str = None,
        with_subtitles: bool = None,
    ):
        # The aspect ratio. Valid values: 16:9 (default), 9:16, 4:3, and 3:4.
        # 
        # This parameter is required.
        self.aspect_ratio = aspect_ratio
        # The digital human information. The value is a JSON string. This parameter is required for the `creator-talk`, `creator-sales`, and `avatar-broadcast` scenes. It includes the following fields:
        # - AvatarPortrait: The digital human portrait. This field is required. The value is a string that represents the media asset ID of the portrait image or the image URL.
        # - AvatarVoice: The digital human voice. This field is optional. The value is a string that represents the voice audio ID or the audio URL.
        self.avatar_data = avatar_data
        # The job parameters. The value is a JSON string. This parameter includes the following fields:
        # - TextType: The text type. This field is required. The value is an integer. Valid values: 1 (original draft, such as product or news information, which the system automatically converts into a voiceover script) and 2 (voiceover script).
        # - TextContent: The text content. This field is required. The value is a string. The maximum length is 10,000 characters.
        # - VoiceDuration: The expected voiceover duration. This field is optional. The value is an integer. This field is configured when TextType is set to 1. Unit: seconds. Default value: 60. The final video duration will be slightly shorter than the expected duration.
        # - NarrationVoiceId: The narration voice ID. This field is valid only for the `briefing-voiceover` scene.
        # - SceneImage: The scene image. This field is optional. This field takes effect only for the three creator marketing scenes (creator-sales, creator-talk, and product-showcase). If you specify valid fields for other scenes, an InvalidParameter error is returned. If both fields are empty (including not specified or an empty object {}), it is equivalent to not providing this parameter, and the behavior is consistent with the existing process without rejecting the job. The Prompt and BackgroundMediaId or BackgroundMediaUrl fields are both optional, can coexist, and are not mutually exclusive. If only Prompt is specified, the text mode is used to generate the scene image. If only the background image is specified, the background image mode is used to fuse based on the background image. If both are specified, the background image takes precedence. If both BackgroundMediaId and BackgroundMediaUrl are specified, BackgroundMediaUrl takes precedence. This field includes the following sub-fields:
        #   - Prompt: The text description of the scene image. This field is optional. The value is a string. The maximum length is 2,000 characters. If the length exceeds the limit, an InvalidParameter error is returned. An empty string is considered as not provided.
        #   - BackgroundMediaId: The media asset ID of the background image. This field is optional. The value is a string. During submission, it is parsed into a URL by ice-media. If the parsing fails, the job is immediately rejected.
        #   - BackgroundMediaUrl: The direct URL of the background image. This field is optional. The value is a string. The URL must use the HTTP or HTTPS protocol. In this case, media asset parsing is not performed.
        # 
        # This parameter is required.
        self.job_params = job_params
        # The output languages. The value is a JSON array string. Valid values: CN, EN, and YUE. The `avatar-broadcast` and `creator-sales` scenes only support Chinese.
        self.output_languages = output_languages
        # The resolution. Valid values:
        # - 1080P
        # - 720P (default)
        # 
        # This parameter is required.
        self.resolution = resolution
        # The scene type. Valid values:
        # - briefing-voiceover: News broadcast (supplements video footage based on the voiceover or uses no digital human).
        # - creator-talk: Creator explanation (multiple shots for news, science, or finance).
        # - creator-sales: Creator product promotion (three-part structure for product promotion, reviews, or store visits).
        # - avatar-broadcast: Digital human broadcast (fixed single shot for broadcasts, announcements, or templates).
        # 
        # This parameter is required.
        self.scene_type = scene_type
        # The custom parameters. The value is a JSON string. The value is returned as-is in query or callback results. The maximum length is 8,192 characters. System reserved words:
        # * NotifyAddress: The callback URL. The URL must use the HTTP or HTTPS protocol. The maximum length is 2,048 characters. The callback is triggered after the node reaches the desired state.
        # * UserId: The UID of the actual resource ownership. If this field is missing, the system falls back to CallerUid.
        self.user_data = user_data
        # The list of user materials. The value is a JSON array string. This parameter includes the following fields:
        # - MediaId: The media asset ID. This is the ID of the image or video uploaded to the platform.
        # - Type: The media type.
        # - Action: The method of using the material. Valid values: `match` (matches suitable clips from the video material based on the voiceover) and `insert` (inserts the video material before the CTA shot. This is intelligently analyzed after shots are generated based on the voiceover. This value is valid only for videos). Default value: `match`.
        self.user_materials = user_materials
        # Specifies whether to include subtitles. Default value: true.
        self.with_subtitles = with_subtitles

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.avatar_data is not None:
            result['AvatarData'] = self.avatar_data

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.output_languages is not None:
            result['OutputLanguages'] = self.output_languages

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.scene_type is not None:
            result['SceneType'] = self.scene_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_materials is not None:
            result['UserMaterials'] = self.user_materials

        if self.with_subtitles is not None:
            result['WithSubtitles'] = self.with_subtitles

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('AvatarData') is not None:
            self.avatar_data = m.get('AvatarData')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('OutputLanguages') is not None:
            self.output_languages = m.get('OutputLanguages')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserMaterials') is not None:
            self.user_materials = m.get('UserMaterials')

        if m.get('WithSubtitles') is not None:
            self.with_subtitles = m.get('WithSubtitles')

        return self

