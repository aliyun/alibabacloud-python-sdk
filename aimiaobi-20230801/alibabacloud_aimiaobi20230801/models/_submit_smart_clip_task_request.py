# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SubmitSmartClipTaskRequest(DaraModel):
    def __init__(
        self,
        editing_config: main_models.SubmitSmartClipTaskRequestEditingConfig = None,
        extend_param: str = None,
        input_config: main_models.SubmitSmartClipTaskRequestInputConfig = None,
        output_config: main_models.SubmitSmartClipTaskRequestOutputConfig = None,
        workspace_id: str = None,
    ):
        # Video editing configuration.
        self.editing_config = editing_config
        # Additional extended parameters. These parameters merge with InputConfig, OutputConfig, and EditingConfig.
        self.extend_param = extend_param
        # Input configuration.
        # 
        # This parameter is required.
        self.input_config = input_config
        # Output configuration.
        self.output_config = output_config
        # Alibaba Cloud Model Studio workspace ID. For more information, see [workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.editing_config:
            self.editing_config.validate()
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config.to_map()

        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param

        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestEditingConfig()
            self.editing_config = temp_model.from_map(m.get('EditingConfig'))

        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')

        if m.get('InputConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestInputConfig()
            self.input_config = temp_model.from_map(m.get('InputConfig'))

        if m.get('OutputConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestOutputConfig()
            self.output_config = temp_model.from_map(m.get('OutputConfig'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class SubmitSmartClipTaskRequestOutputConfig(DaraModel):
    def __init__(
        self,
        count: int = None,
        file_name: str = None,
        height: int = None,
        max_duration: int = None,
        save_to_generated_content: bool = None,
        width: int = None,
    ):
        # Number of output videos.
        self.count = count
        # Output file name. Must include {index}.
        self.file_name = file_name
        # Output video height.
        self.height = height
        # Maximum duration of the output video, in seconds.
        self.max_duration = max_duration
        # Save to Content Management.
        self.save_to_generated_content = save_to_generated_content
        # Output video width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.height is not None:
            result['Height'] = self.height

        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration

        if self.save_to_generated_content is not None:
            result['SaveToGeneratedContent'] = self.save_to_generated_content

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')

        if m.get('SaveToGeneratedContent') is not None:
            self.save_to_generated_content = m.get('SaveToGeneratedContent')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitSmartClipTaskRequestInputConfig(DaraModel):
    def __init__(
        self,
        background_musics: List[main_models.SubmitSmartClipTaskRequestInputConfigBackgroundMusics] = None,
        speech_texts: List[str] = None,
        stickers: List[main_models.SubmitSmartClipTaskRequestInputConfigStickers] = None,
        titles: List[str] = None,
        video_ids: List[main_models.SubmitSmartClipTaskRequestInputConfigVideoIds] = None,
    ):
        # List of background music IDs.
        self.background_musics = background_musics
        # List of voiceover script texts.
        self.speech_texts = speech_texts
        # List of stickers.
        self.stickers = stickers
        # List of titles.
        self.titles = titles
        # List of video material ID objects.
        # 
        # This parameter is required.
        self.video_ids = video_ids

    def validate(self):
        if self.background_musics:
            for v1 in self.background_musics:
                 if v1:
                    v1.validate()
        if self.stickers:
            for v1 in self.stickers:
                 if v1:
                    v1.validate()
        if self.video_ids:
            for v1 in self.video_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackgroundMusics'] = []
        if self.background_musics is not None:
            for k1 in self.background_musics:
                result['BackgroundMusics'].append(k1.to_map() if k1 else None)

        if self.speech_texts is not None:
            result['SpeechTexts'] = self.speech_texts

        result['Stickers'] = []
        if self.stickers is not None:
            for k1 in self.stickers:
                result['Stickers'].append(k1.to_map() if k1 else None)

        if self.titles is not None:
            result['Titles'] = self.titles

        result['VideoIds'] = []
        if self.video_ids is not None:
            for k1 in self.video_ids:
                result['VideoIds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.background_musics = []
        if m.get('BackgroundMusics') is not None:
            for k1 in m.get('BackgroundMusics'):
                temp_model = main_models.SubmitSmartClipTaskRequestInputConfigBackgroundMusics()
                self.background_musics.append(temp_model.from_map(k1))

        if m.get('SpeechTexts') is not None:
            self.speech_texts = m.get('SpeechTexts')

        self.stickers = []
        if m.get('Stickers') is not None:
            for k1 in m.get('Stickers'):
                temp_model = main_models.SubmitSmartClipTaskRequestInputConfigStickers()
                self.stickers.append(temp_model.from_map(k1))

        if m.get('Titles') is not None:
            self.titles = m.get('Titles')

        self.video_ids = []
        if m.get('VideoIds') is not None:
            for k1 in m.get('VideoIds'):
                temp_model = main_models.SubmitSmartClipTaskRequestInputConfigVideoIds()
                self.video_ids.append(temp_model.from_map(k1))

        return self

class SubmitSmartClipTaskRequestInputConfigVideoIds(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # Material ID.
        # 
        # This parameter is required.
        self.id = id
        # ID type:
        # materialId: Material Library reference ID
        # fileKey: FileKey in Alibaba Cloud Model Studio
        # url: Publicly accessible URL
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitSmartClipTaskRequestInputConfigStickers(DaraModel):
    def __init__(
        self,
        height: float = None,
        sticker_id: main_models.SubmitSmartClipTaskRequestInputConfigStickersStickerId = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # Height of the sticker.
        # 
        # This parameter is required.
        self.height = height
        # Sticker ID.
        # 
        # This parameter is required.
        self.sticker_id = sticker_id
        # Width of the sticker.
        # 
        # This parameter is required.
        self.width = width
        # X coordinate of the top-left corner of the sticker.
        # 
        # This parameter is required.
        self.x = x
        # Y coordinate of the top-left corner of the sticker.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        if self.sticker_id:
            self.sticker_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.sticker_id is not None:
            result['StickerId'] = self.sticker_id.to_map()

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('StickerId') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestInputConfigStickersStickerId()
            self.sticker_id = temp_model.from_map(m.get('StickerId'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class SubmitSmartClipTaskRequestInputConfigStickersStickerId(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # Sticker ID.
        # 
        # This parameter is required.
        self.id = id
        # ID type:
        # materialId: Material Library reference ID
        # fileKey: FileKey in Alibaba Cloud Model Studio
        # url: Publicly accessible URL
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitSmartClipTaskRequestInputConfigBackgroundMusics(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # Background music ID.
        # 
        # This parameter is required.
        self.id = id
        # ID type:
        # materialId: Material Library reference ID
        # fileKey: FileKey in Alibaba Cloud Model Studio
        # url: Publicly accessible URL
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitSmartClipTaskRequestEditingConfig(DaraModel):
    def __init__(
        self,
        background_music_config: main_models.SubmitSmartClipTaskRequestEditingConfigBackgroundMusicConfig = None,
        media_config: main_models.SubmitSmartClipTaskRequestEditingConfigMediaConfig = None,
        speech_config: main_models.SubmitSmartClipTaskRequestEditingConfigSpeechConfig = None,
        title_config: main_models.SubmitSmartClipTaskRequestEditingConfigTitleConfig = None,
    ):
        # Background music configuration.
        self.background_music_config = background_music_config
        # Media configuration.
        self.media_config = media_config
        # Voiceover configuration.
        self.speech_config = speech_config
        # Title configuration.
        self.title_config = title_config

    def validate(self):
        if self.background_music_config:
            self.background_music_config.validate()
        if self.media_config:
            self.media_config.validate()
        if self.speech_config:
            self.speech_config.validate()
        if self.title_config:
            self.title_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_music_config is not None:
            result['BackgroundMusicConfig'] = self.background_music_config.to_map()

        if self.media_config is not None:
            result['MediaConfig'] = self.media_config.to_map()

        if self.speech_config is not None:
            result['SpeechConfig'] = self.speech_config.to_map()

        if self.title_config is not None:
            result['TitleConfig'] = self.title_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundMusicConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestEditingConfigBackgroundMusicConfig()
            self.background_music_config = temp_model.from_map(m.get('BackgroundMusicConfig'))

        if m.get('MediaConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestEditingConfigMediaConfig()
            self.media_config = temp_model.from_map(m.get('MediaConfig'))

        if m.get('SpeechConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestEditingConfigSpeechConfig()
            self.speech_config = temp_model.from_map(m.get('SpeechConfig'))

        if m.get('TitleConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestEditingConfigTitleConfig()
            self.title_config = temp_model.from_map(m.get('TitleConfig'))

        return self

class SubmitSmartClipTaskRequestEditingConfigTitleConfig(DaraModel):
    def __init__(
        self,
        alignment: str = None,
        timeline_in: float = None,
        timeline_out: float = None,
        x: float = None,
        y: float = None,
    ):
        # TopLeft: Top-left corner of the video.
        # TopCenter: Top center of the vertical axis of the video.
        # TopRight: Top-right corner of the video.
        # CenterLeft: Left side of the horizontal center line of the video.
        # CenterCenter: Center of the video.
        # CenterRight: Right side of the horizontal center line of the video.
        # BottomLeft: Bottom-left corner of the video.
        # BottomCenter: Bottom center of the vertical axis of the video.
        # BottomRight: Bottom-right corner of the video.
        self.alignment = alignment
        # Time when the title appears.
        self.timeline_in = timeline_in
        # Time when the title disappears.
        self.timeline_out = timeline_out
        # Horizontal distance from the top-left corner of the banner text to the top-left corner of the output video. You can specify this value as a percentage or in pixels. If the value is between 0 and 0.9999, it represents a percentage of the output video width. If the value is an integer greater than or equal to 2, it represents an absolute pixel value. Default value: 0. This coordinate scales based on the source material size and the final output size.
        self.x = x
        # Vertical distance from the top-left corner of the banner text to the top-left corner of the output video. You can specify this value as a percentage or in pixels. If the value is between 0 and 0.9999, it represents a percentage of the output video height. If the value is an integer greater than or equal to 2, it represents an absolute pixel value. Default value: 0. This coordinate scales based on the source material size and the final output size.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alignment is not None:
            result['Alignment'] = self.alignment

        if self.timeline_in is not None:
            result['TimelineIn'] = self.timeline_in

        if self.timeline_out is not None:
            result['TimelineOut'] = self.timeline_out

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alignment') is not None:
            self.alignment = m.get('Alignment')

        if m.get('TimelineIn') is not None:
            self.timeline_in = m.get('TimelineIn')

        if m.get('TimelineOut') is not None:
            self.timeline_out = m.get('TimelineOut')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class SubmitSmartClipTaskRequestEditingConfigSpeechConfig(DaraModel):
    def __init__(
        self,
        asr_config: main_models.SubmitSmartClipTaskRequestEditingConfigSpeechConfigAsrConfig = None,
        speech_rate: float = None,
        style: str = None,
        voice: str = None,
        volume: float = None,
    ):
        # Caption parameter configuration.
        self.asr_config = asr_config
        # Speech rate of the voiceover script.
        # Valid values: -500 to 500. Default value: 0.
        # The corresponding playback speed multipliers for [-500, 0, 500] are [0.5, 1.0, 2.0].
        # Calculation method:
        # For 0.8× speed: (1 - 1/0.8) / 0.002 = -125
        # For 1.2× speed: (1 - 1/1.2) / 0.001 = 166
        # Use coefficient 0.002 for speeds less than 1×.
        # Use coefficient 0.001 for speeds greater than 1×.
        # Round the result to the nearest integer.
        # 
        # The calculation method is as follows:<br>
        # 0.8× speed: (1 − 1/0.8)/0.002 = −125<br>
        # 1.2× speed: (1 − 1/1.2)/0.001 = 166<br>
        # When the speed is less than 1×, use a coefficient of 0.002.<br>
        # When the speed is greater than 1×, use a coefficient of 0.001.<br>
        # The actual algorithm result is approximated.<br><br><br><br><br>
        self.speech_rate = speech_rate
        # Voiceover style. Default value: empty. If both Voice and Style are specified, Voice takes precedence.
        # Gentle: Gentle
        # Serious: Serious
        # Entertainment: Entertainment
        self.style = style
        # Specify one or more voice styles for the voiceover, separated by commas. When multiple voices are specified, one is randomly selected for synthesis. For available voice styles, see [Smart Voice Effect Examples](https://help.aliyun.com/zh/ims/developer-reference/smart-voice-effect-example?spm=a2c4g.11186623.0.0.13091ee6Pw4Jqz). Example: "zhimiao_emo,zhilun".
        self.voice = voice
        # Volume of the voiceover audio. Default value: 1. Valid values: 0 to 10.0. Decimal values are supported. Example: 0.5.
        self.volume = volume

    def validate(self):
        if self.asr_config:
            self.asr_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_config is not None:
            result['AsrConfig'] = self.asr_config.to_map()

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.style is not None:
            result['Style'] = self.style

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrConfig') is not None:
            temp_model = main_models.SubmitSmartClipTaskRequestEditingConfigSpeechConfigAsrConfig()
            self.asr_config = temp_model.from_map(m.get('AsrConfig'))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class SubmitSmartClipTaskRequestEditingConfigSpeechConfigAsrConfig(DaraModel):
    def __init__(
        self,
        alignment: str = None,
        font: str = None,
        font_color: str = None,
        font_size: str = None,
        spacing: str = None,
        x: float = None,
        y: float = None,
    ):
        # Caption alignment.
        # TopLeft: Top-left corner of the video.
        # TopCenter: Top center of the vertical axis of the video.
        # TopRight: Top-right corner of the video.
        # CenterLeft: Left side of the horizontal center line of the video.
        # CenterCenter: Center of the video.
        # CenterRight: Right side of the horizontal center line of the video.
        # BottomLeft: Bottom-left corner of the video.
        # BottomCenter: Bottom center of the vertical axis of the video.
        # BottomRight: Bottom-right corner of the video.
        self.alignment = alignment
        # Font of the caption text. For supported fonts, see the font list. Default font: SimSun.
        self.font = font
        # Color of the caption text. Format: # followed by a hexadecimal value. Example: #ffffff.
        self.font_color = font_color
        # Font size of the caption text. This size scales based on the source material size and the final output size. Default value: 0. Maximum value: 5000.
        self.font_size = font_size
        # Letter spacing of the caption text, in pixels.
        self.spacing = spacing
        # Horizontal distance from the top-left corner of the caption text to the top-left corner of the output video. You can specify this value as a percentage or in pixels. If the value is between 0 and 0.9999, it represents a percentage of the output video width. If the value is an integer greater than or equal to 2, it represents an absolute pixel value. Default value: 0. This coordinate scales based on the source material size and the final output size.
        self.x = x
        # Vertical distance from the top-left corner of the caption text to the top-left corner of the output video. You can specify this value as a percentage or in pixels. If the value is between 0 and 0.9999, it represents a percentage of the output video height. If the value is an integer greater than or equal to 2, it represents an absolute pixel value. Default value: 0. This coordinate scales based on the source material size and the final output size.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alignment is not None:
            result['Alignment'] = self.alignment

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.spacing is not None:
            result['Spacing'] = self.spacing

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alignment') is not None:
            self.alignment = m.get('Alignment')

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class SubmitSmartClipTaskRequestEditingConfigMediaConfig(DaraModel):
    def __init__(
        self,
        volume: float = None,
    ):
        # Volume of the video material. 0 means mute.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class SubmitSmartClipTaskRequestEditingConfigBackgroundMusicConfig(DaraModel):
    def __init__(
        self,
        style: str = None,
        volume: float = None,
    ):
        # Background music style. Default value: empty. If background music is already configured in InputConfig, this field does not take effect.
        # Valid values:
        # bgm-beauty: Fashion
        # bgm-chinese-style: Chinese style
        # bgm-cuisine: Food
        # bgm-dynamic: Dynamic
        # bgm-quirky: Quirky
        # bgm-relaxing: Relaxing
        # bgm-romantic: Romantic
        # bgm-upbeat: Upbeat
        self.style = style
        # Volume of the background music. Valid values: 0 to 10.0.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.style is not None:
            result['Style'] = self.style

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

