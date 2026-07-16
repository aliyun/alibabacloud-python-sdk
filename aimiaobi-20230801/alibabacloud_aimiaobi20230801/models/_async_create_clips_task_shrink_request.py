# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncCreateClipsTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        adapt_mode: str = None,
        alignment: str = None,
        close_music: bool = None,
        close_subtitle: bool = None,
        close_voice: bool = None,
        closing_credits_url: str = None,
        color_words_shrink: str = None,
        cosy_voice_app_key: str = None,
        cosy_voice_token: str = None,
        custom_voice_style: str = None,
        custom_voice_url: str = None,
        custom_voice_volume: int = None,
        height: int = None,
        high_def_source_videos_shrink: str = None,
        music_style: str = None,
        music_url: str = None,
        music_volume: int = None,
        opening_credits_url: str = None,
        stickers_shrink: str = None,
        subtitle_font_size: int = None,
        task_id: str = None,
        text_width: str = None,
        voice_style: str = None,
        voice_volume: int = None,
        width: int = None,
        workspace_id: str = None,
    ):
        self.adapt_mode = adapt_mode
        self.alignment = alignment
        # Specifies whether to disable the background music.
        self.close_music = close_music
        # Specifies whether to disable the subtitles.
        self.close_subtitle = close_subtitle
        # Specifies whether to disable the narration voice.
        self.close_voice = close_voice
        # The URL of the closing credits video.
        self.closing_credits_url = closing_credits_url
        # The array of animated text elements.
        self.color_words_shrink = color_words_shrink
        # The AppKey of CosyVoice.
        self.cosy_voice_app_key = cosy_voice_app_key
        # The token of CosyVoice.
        self.cosy_voice_token = cosy_voice_token
        # The voice tone of CosyVoice.
        self.custom_voice_style = custom_voice_style
        # The URL of the custom audio track.
        self.custom_voice_url = custom_voice_url
        # The volume of the custom audio track.
        self.custom_voice_volume = custom_voice_volume
        # The height of the video.
        self.height = height
        # The list of high-definition video structures.
        self.high_def_source_videos_shrink = high_def_source_videos_shrink
        # The type of recommended music.
        self.music_style = music_style
        # The URL of the background music.
        self.music_url = music_url
        # The volume of the background music.
        self.music_volume = music_volume
        # The URL of the opening credits video.
        self.opening_credits_url = opening_credits_url
        # The array of sticker structures.
        self.stickers_shrink = stickers_shrink
        # The font size of the subtitles.
        self.subtitle_font_size = subtitle_font_size
        # The unique ID of the task.
        # 
        # This parameter is required.
        self.task_id = task_id
        self.text_width = text_width
        # The type of narration voice.
        self.voice_style = voice_style
        # The volume of the narration voice.
        self.voice_volume = voice_volume
        # The width of the video.
        self.width = width
        # The [Bailian workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adapt_mode is not None:
            result['AdaptMode'] = self.adapt_mode

        if self.alignment is not None:
            result['Alignment'] = self.alignment

        if self.close_music is not None:
            result['CloseMusic'] = self.close_music

        if self.close_subtitle is not None:
            result['CloseSubtitle'] = self.close_subtitle

        if self.close_voice is not None:
            result['CloseVoice'] = self.close_voice

        if self.closing_credits_url is not None:
            result['ClosingCreditsUrl'] = self.closing_credits_url

        if self.color_words_shrink is not None:
            result['ColorWords'] = self.color_words_shrink

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

        if self.high_def_source_videos_shrink is not None:
            result['HighDefSourceVideos'] = self.high_def_source_videos_shrink

        if self.music_style is not None:
            result['MusicStyle'] = self.music_style

        if self.music_url is not None:
            result['MusicUrl'] = self.music_url

        if self.music_volume is not None:
            result['MusicVolume'] = self.music_volume

        if self.opening_credits_url is not None:
            result['OpeningCreditsUrl'] = self.opening_credits_url

        if self.stickers_shrink is not None:
            result['Stickers'] = self.stickers_shrink

        if self.subtitle_font_size is not None:
            result['SubtitleFontSize'] = self.subtitle_font_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.text_width is not None:
            result['TextWidth'] = self.text_width

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
        if m.get('AdaptMode') is not None:
            self.adapt_mode = m.get('AdaptMode')

        if m.get('Alignment') is not None:
            self.alignment = m.get('Alignment')

        if m.get('CloseMusic') is not None:
            self.close_music = m.get('CloseMusic')

        if m.get('CloseSubtitle') is not None:
            self.close_subtitle = m.get('CloseSubtitle')

        if m.get('CloseVoice') is not None:
            self.close_voice = m.get('CloseVoice')

        if m.get('ClosingCreditsUrl') is not None:
            self.closing_credits_url = m.get('ClosingCreditsUrl')

        if m.get('ColorWords') is not None:
            self.color_words_shrink = m.get('ColorWords')

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

        if m.get('HighDefSourceVideos') is not None:
            self.high_def_source_videos_shrink = m.get('HighDefSourceVideos')

        if m.get('MusicStyle') is not None:
            self.music_style = m.get('MusicStyle')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        if m.get('MusicVolume') is not None:
            self.music_volume = m.get('MusicVolume')

        if m.get('OpeningCreditsUrl') is not None:
            self.opening_credits_url = m.get('OpeningCreditsUrl')

        if m.get('Stickers') is not None:
            self.stickers_shrink = m.get('Stickers')

        if m.get('SubtitleFontSize') is not None:
            self.subtitle_font_size = m.get('SubtitleFontSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TextWidth') is not None:
            self.text_width = m.get('TextWidth')

        if m.get('VoiceStyle') is not None:
            self.voice_style = m.get('VoiceStyle')

        if m.get('VoiceVolume') is not None:
            self.voice_volume = m.get('VoiceVolume')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

