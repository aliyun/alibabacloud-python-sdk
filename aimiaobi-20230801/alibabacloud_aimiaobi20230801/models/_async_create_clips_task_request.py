# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class AsyncCreateClipsTaskRequest(DaraModel):
    def __init__(
        self,
        close_music: bool = None,
        close_subtitle: bool = None,
        close_voice: bool = None,
        closing_credits_url: str = None,
        color_words: List[main_models.AsyncCreateClipsTaskRequestColorWords] = None,
        cosy_voice_app_key: str = None,
        cosy_voice_token: str = None,
        custom_voice_style: str = None,
        custom_voice_url: str = None,
        custom_voice_volume: int = None,
        height: int = None,
        high_def_source_videos: List[main_models.AsyncCreateClipsTaskRequestHighDefSourceVideos] = None,
        music_style: str = None,
        music_url: str = None,
        music_volume: int = None,
        opening_credits_url: str = None,
        stickers: List[main_models.AsyncCreateClipsTaskRequestStickers] = None,
        subtitle_font_size: int = None,
        task_id: str = None,
        voice_style: str = None,
        voice_volume: int = None,
        width: int = None,
        workspace_id: str = None,
    ):
        self.close_music = close_music
        self.close_subtitle = close_subtitle
        self.close_voice = close_voice
        self.closing_credits_url = closing_credits_url
        self.color_words = color_words
        self.cosy_voice_app_key = cosy_voice_app_key
        self.cosy_voice_token = cosy_voice_token
        self.custom_voice_style = custom_voice_style
        self.custom_voice_url = custom_voice_url
        self.custom_voice_volume = custom_voice_volume
        self.height = height
        self.high_def_source_videos = high_def_source_videos
        self.music_style = music_style
        self.music_url = music_url
        self.music_volume = music_volume
        self.opening_credits_url = opening_credits_url
        self.stickers = stickers
        self.subtitle_font_size = subtitle_font_size
        # This parameter is required.
        self.task_id = task_id
        self.voice_style = voice_style
        self.voice_volume = voice_volume
        self.width = width
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.color_words:
            for v1 in self.color_words:
                 if v1:
                    v1.validate()
        if self.high_def_source_videos:
            for v1 in self.high_def_source_videos:
                 if v1:
                    v1.validate()
        if self.stickers:
            for v1 in self.stickers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.close_music is not None:
            result['CloseMusic'] = self.close_music

        if self.close_subtitle is not None:
            result['CloseSubtitle'] = self.close_subtitle

        if self.close_voice is not None:
            result['CloseVoice'] = self.close_voice

        if self.closing_credits_url is not None:
            result['ClosingCreditsUrl'] = self.closing_credits_url

        result['ColorWords'] = []
        if self.color_words is not None:
            for k1 in self.color_words:
                result['ColorWords'].append(k1.to_map() if k1 else None)

        if self.cosy_voice_app_key is not None:
            result['CosyVoiceAppKey'] = self.cosy_voice_app_key

        if self.cosy_voice_token is not None:
            result['CosyVoiceToken'] = self.cosy_voice_token

        if self.custom_voice_style is not None:
            result['CustomVoiceStyle'] = self.custom_voice_style

        if self.custom_voice_url is not None:
            result['CustomVoiceUrl'] = self.custom_voice_url

        if self.custom_voice_volume is not None:
            result['CustomVoiceVolume'] = self.custom_voice_volume

        if self.height is not None:
            result['Height'] = self.height

        result['HighDefSourceVideos'] = []
        if self.high_def_source_videos is not None:
            for k1 in self.high_def_source_videos:
                result['HighDefSourceVideos'].append(k1.to_map() if k1 else None)

        if self.music_style is not None:
            result['MusicStyle'] = self.music_style

        if self.music_url is not None:
            result['MusicUrl'] = self.music_url

        if self.music_volume is not None:
            result['MusicVolume'] = self.music_volume

        if self.opening_credits_url is not None:
            result['OpeningCreditsUrl'] = self.opening_credits_url

        result['Stickers'] = []
        if self.stickers is not None:
            for k1 in self.stickers:
                result['Stickers'].append(k1.to_map() if k1 else None)

        if self.subtitle_font_size is not None:
            result['SubtitleFontSize'] = self.subtitle_font_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.voice_style is not None:
            result['VoiceStyle'] = self.voice_style

        if self.voice_volume is not None:
            result['VoiceVolume'] = self.voice_volume

        if self.width is not None:
            result['Width'] = self.width

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseMusic') is not None:
            self.close_music = m.get('CloseMusic')

        if m.get('CloseSubtitle') is not None:
            self.close_subtitle = m.get('CloseSubtitle')

        if m.get('CloseVoice') is not None:
            self.close_voice = m.get('CloseVoice')

        if m.get('ClosingCreditsUrl') is not None:
            self.closing_credits_url = m.get('ClosingCreditsUrl')

        self.color_words = []
        if m.get('ColorWords') is not None:
            for k1 in m.get('ColorWords'):
                temp_model = main_models.AsyncCreateClipsTaskRequestColorWords()
                self.color_words.append(temp_model.from_map(k1))

        if m.get('CosyVoiceAppKey') is not None:
            self.cosy_voice_app_key = m.get('CosyVoiceAppKey')

        if m.get('CosyVoiceToken') is not None:
            self.cosy_voice_token = m.get('CosyVoiceToken')

        if m.get('CustomVoiceStyle') is not None:
            self.custom_voice_style = m.get('CustomVoiceStyle')

        if m.get('CustomVoiceUrl') is not None:
            self.custom_voice_url = m.get('CustomVoiceUrl')

        if m.get('CustomVoiceVolume') is not None:
            self.custom_voice_volume = m.get('CustomVoiceVolume')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        self.high_def_source_videos = []
        if m.get('HighDefSourceVideos') is not None:
            for k1 in m.get('HighDefSourceVideos'):
                temp_model = main_models.AsyncCreateClipsTaskRequestHighDefSourceVideos()
                self.high_def_source_videos.append(temp_model.from_map(k1))

        if m.get('MusicStyle') is not None:
            self.music_style = m.get('MusicStyle')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        if m.get('MusicVolume') is not None:
            self.music_volume = m.get('MusicVolume')

        if m.get('OpeningCreditsUrl') is not None:
            self.opening_credits_url = m.get('OpeningCreditsUrl')

        self.stickers = []
        if m.get('Stickers') is not None:
            for k1 in m.get('Stickers'):
                temp_model = main_models.AsyncCreateClipsTaskRequestStickers()
                self.stickers.append(temp_model.from_map(k1))

        if m.get('SubtitleFontSize') is not None:
            self.subtitle_font_size = m.get('SubtitleFontSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VoiceStyle') is not None:
            self.voice_style = m.get('VoiceStyle')

        if m.get('VoiceVolume') is not None:
            self.voice_volume = m.get('VoiceVolume')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AsyncCreateClipsTaskRequestStickers(DaraModel):
    def __init__(
        self,
        duration: int = None,
        dync_frames: int = None,
        height: int = None,
        timeline_in: int = None,
        url: str = None,
        width: int = None,
        x: float = None,
        y: float = None,
    ):
        self.duration = duration
        self.dync_frames = dync_frames
        self.height = height
        self.timeline_in = timeline_in
        self.url = url
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.dync_frames is not None:
            result['DyncFrames'] = self.dync_frames

        if self.height is not None:
            result['Height'] = self.height

        if self.timeline_in is not None:
            result['TimelineIn'] = self.timeline_in

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('DyncFrames') is not None:
            self.dync_frames = m.get('DyncFrames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('TimelineIn') is not None:
            self.timeline_in = m.get('TimelineIn')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class AsyncCreateClipsTaskRequestHighDefSourceVideos(DaraModel):
    def __init__(
        self,
        video_id: str = None,
        video_name: str = None,
        video_url: str = None,
    ):
        self.video_id = video_id
        self.video_name = video_name
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.video_name is not None:
            result['VideoName'] = self.video_name

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

class AsyncCreateClipsTaskRequestColorWords(DaraModel):
    def __init__(
        self,
        content: str = None,
        effect_color_style: str = None,
        font_size: int = None,
        timeline_in: int = None,
        timeline_out: int = None,
        x: float = None,
        y: float = None,
    ):
        self.content = content
        self.effect_color_style = effect_color_style
        self.font_size = font_size
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
        if self.content is not None:
            result['Content'] = self.content

        if self.effect_color_style is not None:
            result['EffectColorStyle'] = self.effect_color_style

        if self.font_size is not None:
            result['FontSize'] = self.font_size

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
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EffectColorStyle') is not None:
            self.effect_color_style = m.get('EffectColorStyle')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('TimelineIn') is not None:
            self.timeline_in = m.get('TimelineIn')

        if m.get('TimelineOut') is not None:
            self.timeline_out = m.get('TimelineOut')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

