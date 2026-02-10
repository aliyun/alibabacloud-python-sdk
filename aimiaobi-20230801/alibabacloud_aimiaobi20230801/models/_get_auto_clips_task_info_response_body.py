# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetAutoClipsTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAutoClipsTaskInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAutoClipsTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAutoClipsTaskInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis_results: List[main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResults] = None,
        close_music: bool = None,
        close_subtitle: bool = None,
        close_voice: bool = None,
        closing_credits_url: str = None,
        color_words: List[main_models.GetAutoClipsTaskInfoResponseBodyDataColorWords] = None,
        content: str = None,
        custom_voice_style: str = None,
        custom_voice_url: str = None,
        custom_voice_volume: int = None,
        error_message: str = None,
        media_cloud_timeline: str = None,
        music_style: str = None,
        music_url: str = None,
        music_volume: int = None,
        opening_credits_url: str = None,
        output_video_file_key: str = None,
        output_video_url: str = None,
        reference_video: main_models.GetAutoClipsTaskInfoResponseBodyDataReferenceVideo = None,
        source_videos: List[main_models.GetAutoClipsTaskInfoResponseBodyDataSourceVideos] = None,
        status: int = None,
        step: str = None,
        stickers: List[main_models.GetAutoClipsTaskInfoResponseBodyDataStickers] = None,
        subtitle_font_size: int = None,
        task_id: str = None,
        timelines: List[main_models.GetAutoClipsTaskInfoResponseBodyDataTimelines] = None,
        voice_style: str = None,
        voice_volume: int = None,
    ):
        self.analysis_results = analysis_results
        self.close_music = close_music
        self.close_subtitle = close_subtitle
        self.close_voice = close_voice
        self.closing_credits_url = closing_credits_url
        self.color_words = color_words
        self.content = content
        self.custom_voice_style = custom_voice_style
        self.custom_voice_url = custom_voice_url
        self.custom_voice_volume = custom_voice_volume
        self.error_message = error_message
        self.media_cloud_timeline = media_cloud_timeline
        self.music_style = music_style
        self.music_url = music_url
        self.music_volume = music_volume
        self.opening_credits_url = opening_credits_url
        self.output_video_file_key = output_video_file_key
        self.output_video_url = output_video_url
        self.reference_video = reference_video
        self.source_videos = source_videos
        self.status = status
        self.step = step
        self.stickers = stickers
        self.subtitle_font_size = subtitle_font_size
        self.task_id = task_id
        self.timelines = timelines
        self.voice_style = voice_style
        self.voice_volume = voice_volume

    def validate(self):
        if self.analysis_results:
            for v1 in self.analysis_results:
                 if v1:
                    v1.validate()
        if self.color_words:
            for v1 in self.color_words:
                 if v1:
                    v1.validate()
        if self.reference_video:
            self.reference_video.validate()
        if self.source_videos:
            for v1 in self.source_videos:
                 if v1:
                    v1.validate()
        if self.stickers:
            for v1 in self.stickers:
                 if v1:
                    v1.validate()
        if self.timelines:
            for v1 in self.timelines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnalysisResults'] = []
        if self.analysis_results is not None:
            for k1 in self.analysis_results:
                result['AnalysisResults'].append(k1.to_map() if k1 else None)

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

        if self.content is not None:
            result['Content'] = self.content

        if self.custom_voice_style is not None:
            result['CustomVoiceStyle'] = self.custom_voice_style

        if self.custom_voice_url is not None:
            result['CustomVoiceUrl'] = self.custom_voice_url

        if self.custom_voice_volume is not None:
            result['CustomVoiceVolume'] = self.custom_voice_volume

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.media_cloud_timeline is not None:
            result['MediaCloudTimeline'] = self.media_cloud_timeline

        if self.music_style is not None:
            result['MusicStyle'] = self.music_style

        if self.music_url is not None:
            result['MusicUrl'] = self.music_url

        if self.music_volume is not None:
            result['MusicVolume'] = self.music_volume

        if self.opening_credits_url is not None:
            result['OpeningCreditsUrl'] = self.opening_credits_url

        if self.output_video_file_key is not None:
            result['OutputVideoFileKey'] = self.output_video_file_key

        if self.output_video_url is not None:
            result['OutputVideoUrl'] = self.output_video_url

        if self.reference_video is not None:
            result['ReferenceVideo'] = self.reference_video.to_map()

        result['SourceVideos'] = []
        if self.source_videos is not None:
            for k1 in self.source_videos:
                result['SourceVideos'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.step is not None:
            result['Step'] = self.step

        result['Stickers'] = []
        if self.stickers is not None:
            for k1 in self.stickers:
                result['Stickers'].append(k1.to_map() if k1 else None)

        if self.subtitle_font_size is not None:
            result['SubtitleFontSize'] = self.subtitle_font_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['Timelines'] = []
        if self.timelines is not None:
            for k1 in self.timelines:
                result['Timelines'].append(k1.to_map() if k1 else None)

        if self.voice_style is not None:
            result['VoiceStyle'] = self.voice_style

        if self.voice_volume is not None:
            result['VoiceVolume'] = self.voice_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis_results = []
        if m.get('AnalysisResults') is not None:
            for k1 in m.get('AnalysisResults'):
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResults()
                self.analysis_results.append(temp_model.from_map(k1))

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
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataColorWords()
                self.color_words.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CustomVoiceStyle') is not None:
            self.custom_voice_style = m.get('CustomVoiceStyle')

        if m.get('CustomVoiceUrl') is not None:
            self.custom_voice_url = m.get('CustomVoiceUrl')

        if m.get('CustomVoiceVolume') is not None:
            self.custom_voice_volume = m.get('CustomVoiceVolume')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MediaCloudTimeline') is not None:
            self.media_cloud_timeline = m.get('MediaCloudTimeline')

        if m.get('MusicStyle') is not None:
            self.music_style = m.get('MusicStyle')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        if m.get('MusicVolume') is not None:
            self.music_volume = m.get('MusicVolume')

        if m.get('OpeningCreditsUrl') is not None:
            self.opening_credits_url = m.get('OpeningCreditsUrl')

        if m.get('OutputVideoFileKey') is not None:
            self.output_video_file_key = m.get('OutputVideoFileKey')

        if m.get('OutputVideoUrl') is not None:
            self.output_video_url = m.get('OutputVideoUrl')

        if m.get('ReferenceVideo') is not None:
            temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataReferenceVideo()
            self.reference_video = temp_model.from_map(m.get('ReferenceVideo'))

        self.source_videos = []
        if m.get('SourceVideos') is not None:
            for k1 in m.get('SourceVideos'):
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataSourceVideos()
                self.source_videos.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        self.stickers = []
        if m.get('Stickers') is not None:
            for k1 in m.get('Stickers'):
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataStickers()
                self.stickers.append(temp_model.from_map(k1))

        if m.get('SubtitleFontSize') is not None:
            self.subtitle_font_size = m.get('SubtitleFontSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.timelines = []
        if m.get('Timelines') is not None:
            for k1 in m.get('Timelines'):
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataTimelines()
                self.timelines.append(temp_model.from_map(k1))

        if m.get('VoiceStyle') is not None:
            self.voice_style = m.get('VoiceStyle')

        if m.get('VoiceVolume') is not None:
            self.voice_volume = m.get('VoiceVolume')

        return self

class GetAutoClipsTaskInfoResponseBodyDataTimelines(DaraModel):
    def __init__(
        self,
        clips: List[main_models.GetAutoClipsTaskInfoResponseBodyDataTimelinesClips] = None,
        content: str = None,
        timeline_id: str = None,
    ):
        self.clips = clips
        self.content = content
        self.timeline_id = timeline_id

    def validate(self):
        if self.clips:
            for v1 in self.clips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clips'] = []
        if self.clips is not None:
            for k1 in self.clips:
                result['Clips'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['Content'] = self.content

        if self.timeline_id is not None:
            result['TimelineId'] = self.timeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clips = []
        if m.get('Clips') is not None:
            for k1 in m.get('Clips'):
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataTimelinesClips()
                self.clips.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('TimelineId') is not None:
            self.timeline_id = m.get('TimelineId')

        return self

class GetAutoClipsTaskInfoResponseBodyDataTimelinesClips(DaraModel):
    def __init__(
        self,
        clip_id: str = None,
        content_inner: str = None,
        in_: int = None,
        in_ex: float = None,
        out: int = None,
        out_ex: float = None,
        video_id: str = None,
        video_name: str = None,
    ):
        self.clip_id = clip_id
        self.content_inner = content_inner
        self.in_ = in_
        self.in_ex = in_ex
        self.out = out
        self.out_ex = out_ex
        self.video_id = video_id
        self.video_name = video_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clip_id is not None:
            result['ClipId'] = self.clip_id

        if self.content_inner is not None:
            result['ContentInner'] = self.content_inner

        if self.in_ is not None:
            result['In'] = self.in_

        if self.in_ex is not None:
            result['InEx'] = self.in_ex

        if self.out is not None:
            result['Out'] = self.out

        if self.out_ex is not None:
            result['OutEx'] = self.out_ex

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.video_name is not None:
            result['VideoName'] = self.video_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipId') is not None:
            self.clip_id = m.get('ClipId')

        if m.get('ContentInner') is not None:
            self.content_inner = m.get('ContentInner')

        if m.get('In') is not None:
            self.in_ = m.get('In')

        if m.get('InEx') is not None:
            self.in_ex = m.get('InEx')

        if m.get('Out') is not None:
            self.out = m.get('Out')

        if m.get('OutEx') is not None:
            self.out_ex = m.get('OutEx')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')

        return self

class GetAutoClipsTaskInfoResponseBodyDataStickers(DaraModel):
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

class GetAutoClipsTaskInfoResponseBodyDataSourceVideos(DaraModel):
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

class GetAutoClipsTaskInfoResponseBodyDataReferenceVideo(DaraModel):
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

class GetAutoClipsTaskInfoResponseBodyDataColorWords(DaraModel):
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

class GetAutoClipsTaskInfoResponseBodyDataAnalysisResults(DaraModel):
    def __init__(
        self,
        lens_infos: List[main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfos] = None,
        media_id: str = None,
        media_name: str = None,
        media_url: str = None,
    ):
        self.lens_infos = lens_infos
        self.media_id = media_id
        self.media_name = media_name
        self.media_url = media_url

    def validate(self):
        if self.lens_infos:
            for v1 in self.lens_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LensInfos'] = []
        if self.lens_infos is not None:
            for k1 in self.lens_infos:
                result['LensInfos'].append(k1.to_map() if k1 else None)

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_name is not None:
            result['MediaName'] = self.media_name

        if self.media_url is not None:
            result['MediaUrl'] = self.media_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lens_infos = []
        if m.get('LensInfos') is not None:
            for k1 in m.get('LensInfos'):
                temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfos()
                self.lens_infos.append(temp_model.from_map(k1))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaName') is not None:
            self.media_name = m.get('MediaName')

        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')

        return self

class GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfos(DaraModel):
    def __init__(
        self,
        analysis_content: str = None,
        end_time: main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfosEndTime = None,
        start_time: main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfosStartTime = None,
    ):
        self.analysis_content = analysis_content
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.end_time:
            self.end_time.validate()
        if self.start_time:
            self.start_time.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_content is not None:
            result['AnalysisContent'] = self.analysis_content

        if self.end_time is not None:
            result['EndTime'] = self.end_time.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisContent') is not None:
            self.analysis_content = m.get('AnalysisContent')

        if m.get('EndTime') is not None:
            temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfosEndTime()
            self.end_time = temp_model.from_map(m.get('EndTime'))

        if m.get('StartTime') is not None:
            temp_model = main_models.GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfosStartTime()
            self.start_time = temp_model.from_map(m.get('StartTime'))

        return self

class GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfosStartTime(DaraModel):
    def __init__(
        self,
        hour: int = None,
        mill_second: int = None,
        minute: int = None,
        second: int = None,
    ):
        self.hour = hour
        self.mill_second = mill_second
        self.minute = minute
        self.second = second

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hour is not None:
            result['Hour'] = self.hour

        if self.mill_second is not None:
            result['MillSecond'] = self.mill_second

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.second is not None:
            result['Second'] = self.second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('MillSecond') is not None:
            self.mill_second = m.get('MillSecond')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Second') is not None:
            self.second = m.get('Second')

        return self

class GetAutoClipsTaskInfoResponseBodyDataAnalysisResultsLensInfosEndTime(DaraModel):
    def __init__(
        self,
        hour: int = None,
        mill_second: int = None,
        minute: int = None,
        second: int = None,
    ):
        self.hour = hour
        self.mill_second = mill_second
        self.minute = minute
        self.second = second

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hour is not None:
            result['Hour'] = self.hour

        if self.mill_second is not None:
            result['MillSecond'] = self.mill_second

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.second is not None:
            result['Second'] = self.second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('MillSecond') is not None:
            self.mill_second = m.get('MillSecond')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Second') is not None:
            self.second = m.get('Second')

        return self

