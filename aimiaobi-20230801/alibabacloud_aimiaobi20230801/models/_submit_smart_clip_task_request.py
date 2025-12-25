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
        self.editing_config = editing_config
        self.extend_param = extend_param
        # This parameter is required.
        self.input_config = input_config
        self.output_config = output_config
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
        self.count = count
        self.file_name = file_name
        self.height = height
        self.max_duration = max_duration
        self.save_to_generated_content = save_to_generated_content
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
        self.background_musics = background_musics
        self.speech_texts = speech_texts
        self.stickers = stickers
        self.titles = titles
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
        # This parameter is required.
        self.id = id
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
        # This parameter is required.
        self.height = height
        # This parameter is required.
        self.sticker_id = sticker_id
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
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
        # This parameter is required.
        self.id = id
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
        # This parameter is required.
        self.id = id
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
        self.background_music_config = background_music_config
        self.media_config = media_config
        self.speech_config = speech_config
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
        self.alignment = alignment
        self.timeline_in = timeline_in
        self.timeline_out = timeline_out
        self.x = x
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
        self.asr_config = asr_config
        self.speech_rate = speech_rate
        self.style = style
        self.voice = voice
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
        self.alignment = alignment
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.spacing = spacing
        self.x = x
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
        self.style = style
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

