# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class StartRtcCloudRecordingRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        max_idle_time: int = None,
        mix_layout_params: main_models.StartRtcCloudRecordingRequestMixLayoutParams = None,
        mix_transcode_params: main_models.StartRtcCloudRecordingRequestMixTranscodeParams = None,
        notify_auth_key: str = None,
        notify_file_uploaded_format: List[str] = None,
        notify_url: str = None,
        record_params: main_models.StartRtcCloudRecordingRequestRecordParams = None,
        storage_params: main_models.StartRtcCloudRecordingRequestStorageParams = None,
        subscribe_params: main_models.StartRtcCloudRecordingRequestSubscribeParams = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        self.max_idle_time = max_idle_time
        self.mix_layout_params = mix_layout_params
        self.mix_transcode_params = mix_transcode_params
        self.notify_auth_key = notify_auth_key
        self.notify_file_uploaded_format = notify_file_uploaded_format
        self.notify_url = notify_url
        # This parameter is required.
        self.record_params = record_params
        # This parameter is required.
        self.storage_params = storage_params
        # This parameter is required.
        self.subscribe_params = subscribe_params

    def validate(self):
        if self.mix_layout_params:
            self.mix_layout_params.validate()
        if self.mix_transcode_params:
            self.mix_transcode_params.validate()
        if self.record_params:
            self.record_params.validate()
        if self.storage_params:
            self.storage_params.validate()
        if self.subscribe_params:
            self.subscribe_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.mix_layout_params is not None:
            result['MixLayoutParams'] = self.mix_layout_params.to_map()

        if self.mix_transcode_params is not None:
            result['MixTranscodeParams'] = self.mix_transcode_params.to_map()

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_file_uploaded_format is not None:
            result['NotifyFileUploadedFormat'] = self.notify_file_uploaded_format

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.record_params is not None:
            result['RecordParams'] = self.record_params.to_map()

        if self.storage_params is not None:
            result['StorageParams'] = self.storage_params.to_map()

        if self.subscribe_params is not None:
            result['SubscribeParams'] = self.subscribe_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('MixLayoutParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestMixLayoutParams()
            self.mix_layout_params = temp_model.from_map(m.get('MixLayoutParams'))

        if m.get('MixTranscodeParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestMixTranscodeParams()
            self.mix_transcode_params = temp_model.from_map(m.get('MixTranscodeParams'))

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyFileUploadedFormat') is not None:
            self.notify_file_uploaded_format = m.get('NotifyFileUploadedFormat')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('RecordParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestRecordParams()
            self.record_params = temp_model.from_map(m.get('RecordParams'))

        if m.get('StorageParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestStorageParams()
            self.storage_params = temp_model.from_map(m.get('StorageParams'))

        if m.get('SubscribeParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestSubscribeParams()
            self.subscribe_params = temp_model.from_map(m.get('SubscribeParams'))

        return self

class StartRtcCloudRecordingRequestSubscribeParams(DaraModel):
    def __init__(
        self,
        subscribe_user_id_list: List[main_models.StartRtcCloudRecordingRequestSubscribeParamsSubscribeUserIdList] = None,
    ):
        # This parameter is required.
        self.subscribe_user_id_list = subscribe_user_id_list

    def validate(self):
        if self.subscribe_user_id_list:
            for v1 in self.subscribe_user_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubscribeUserIdList'] = []
        if self.subscribe_user_id_list is not None:
            for k1 in self.subscribe_user_id_list:
                result['SubscribeUserIdList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscribe_user_id_list = []
        if m.get('SubscribeUserIdList') is not None:
            for k1 in m.get('SubscribeUserIdList'):
                temp_model = main_models.StartRtcCloudRecordingRequestSubscribeParamsSubscribeUserIdList()
                self.subscribe_user_id_list.append(temp_model.from_map(k1))

        return self

class StartRtcCloudRecordingRequestSubscribeParamsSubscribeUserIdList(DaraModel):
    def __init__(
        self,
        source_type: int = None,
        stream_type: int = None,
        user_id: str = None,
    ):
        self.source_type = source_type
        self.stream_type = stream_type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class StartRtcCloudRecordingRequestStorageParams(DaraModel):
    def __init__(
        self,
        file_info: List[main_models.StartRtcCloudRecordingRequestStorageParamsFileInfo] = None,
        ossparams: main_models.StartRtcCloudRecordingRequestStorageParamsOSSParams = None,
        storage_type: int = None,
        vod_params: main_models.StartRtcCloudRecordingRequestStorageParamsVodParams = None,
    ):
        self.file_info = file_info
        self.ossparams = ossparams
        # This parameter is required.
        self.storage_type = storage_type
        self.vod_params = vod_params

    def validate(self):
        if self.file_info:
            for v1 in self.file_info:
                 if v1:
                    v1.validate()
        if self.ossparams:
            self.ossparams.validate()
        if self.vod_params:
            self.vod_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileInfo'] = []
        if self.file_info is not None:
            for k1 in self.file_info:
                result['FileInfo'].append(k1.to_map() if k1 else None)

        if self.ossparams is not None:
            result['OSSParams'] = self.ossparams.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.vod_params is not None:
            result['VodParams'] = self.vod_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_info = []
        if m.get('FileInfo') is not None:
            for k1 in m.get('FileInfo'):
                temp_model = main_models.StartRtcCloudRecordingRequestStorageParamsFileInfo()
                self.file_info.append(temp_model.from_map(k1))

        if m.get('OSSParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestStorageParamsOSSParams()
            self.ossparams = temp_model.from_map(m.get('OSSParams'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VodParams') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestStorageParamsVodParams()
            self.vod_params = temp_model.from_map(m.get('VodParams'))

        return self

class StartRtcCloudRecordingRequestStorageParamsVodParams(DaraModel):
    def __init__(
        self,
        auto_compose: int = None,
        compose_vod_transcode_group_id: str = None,
        storage_location: str = None,
        vod_transcode_group_id: str = None,
    ):
        self.auto_compose = auto_compose
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id
        self.storage_location = storage_location
        self.vod_transcode_group_id = vod_transcode_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_compose is not None:
            result['AutoCompose'] = self.auto_compose

        if self.compose_vod_transcode_group_id is not None:
            result['ComposeVodTranscodeGroupId'] = self.compose_vod_transcode_group_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.vod_transcode_group_id is not None:
            result['VodTranscodeGroupId'] = self.vod_transcode_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCompose') is not None:
            self.auto_compose = m.get('AutoCompose')

        if m.get('ComposeVodTranscodeGroupId') is not None:
            self.compose_vod_transcode_group_id = m.get('ComposeVodTranscodeGroupId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('VodTranscodeGroupId') is not None:
            self.vod_transcode_group_id = m.get('VodTranscodeGroupId')

        return self

class StartRtcCloudRecordingRequestStorageParamsOSSParams(DaraModel):
    def __init__(
        self,
        ossbucket: str = None,
        ossendpoint: str = None,
    ):
        # This parameter is required.
        self.ossbucket = ossbucket
        # This parameter is required.
        self.ossendpoint = ossendpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossendpoint is not None:
            result['OSSEndpoint'] = self.ossendpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSEndpoint') is not None:
            self.ossendpoint = m.get('OSSEndpoint')

        return self

class StartRtcCloudRecordingRequestStorageParamsFileInfo(DaraModel):
    def __init__(
        self,
        file_name_pattern: str = None,
        file_path_prefix: List[str] = None,
        format: str = None,
        slice_duration: int = None,
        slice_name_pattern: str = None,
    ):
        self.file_name_pattern = file_name_pattern
        self.file_path_prefix = file_path_prefix
        # This parameter is required.
        self.format = format
        self.slice_duration = slice_duration
        self.slice_name_pattern = slice_name_pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name_pattern is not None:
            result['FileNamePattern'] = self.file_name_pattern

        if self.file_path_prefix is not None:
            result['FilePathPrefix'] = self.file_path_prefix

        if self.format is not None:
            result['Format'] = self.format

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        if self.slice_name_pattern is not None:
            result['SliceNamePattern'] = self.slice_name_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileNamePattern') is not None:
            self.file_name_pattern = m.get('FileNamePattern')

        if m.get('FilePathPrefix') is not None:
            self.file_path_prefix = m.get('FilePathPrefix')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        if m.get('SliceNamePattern') is not None:
            self.slice_name_pattern = m.get('SliceNamePattern')

        return self

class StartRtcCloudRecordingRequestRecordParams(DaraModel):
    def __init__(
        self,
        max_file_duration: int = None,
        record_mode: int = None,
        stream_type: int = None,
    ):
        self.max_file_duration = max_file_duration
        # This parameter is required.
        self.record_mode = record_mode
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_file_duration is not None:
            result['MaxFileDuration'] = self.max_file_duration

        if self.record_mode is not None:
            result['RecordMode'] = self.record_mode

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxFileDuration') is not None:
            self.max_file_duration = m.get('MaxFileDuration')

        if m.get('RecordMode') is not None:
            self.record_mode = m.get('RecordMode')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

class StartRtcCloudRecordingRequestMixTranscodeParams(DaraModel):
    def __init__(
        self,
        audio_bitrate: int = None,
        audio_channels: int = None,
        audio_sample_rate: int = None,
        frame_fill_type: int = None,
        video_bitrate: int = None,
        video_codec: str = None,
        video_framerate: int = None,
        video_gop: int = None,
        video_height: int = None,
        video_width: int = None,
    ):
        # This parameter is required.
        self.audio_bitrate = audio_bitrate
        # This parameter is required.
        self.audio_channels = audio_channels
        # This parameter is required.
        self.audio_sample_rate = audio_sample_rate
        self.frame_fill_type = frame_fill_type
        self.video_bitrate = video_bitrate
        self.video_codec = video_codec
        self.video_framerate = video_framerate
        self.video_gop = video_gop
        self.video_height = video_height
        self.video_width = video_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_bitrate is not None:
            result['AudioBitrate'] = self.audio_bitrate

        if self.audio_channels is not None:
            result['AudioChannels'] = self.audio_channels

        if self.audio_sample_rate is not None:
            result['AudioSampleRate'] = self.audio_sample_rate

        if self.frame_fill_type is not None:
            result['FrameFillType'] = self.frame_fill_type

        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate

        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec

        if self.video_framerate is not None:
            result['VideoFramerate'] = self.video_framerate

        if self.video_gop is not None:
            result['VideoGop'] = self.video_gop

        if self.video_height is not None:
            result['VideoHeight'] = self.video_height

        if self.video_width is not None:
            result['VideoWidth'] = self.video_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioBitrate') is not None:
            self.audio_bitrate = m.get('AudioBitrate')

        if m.get('AudioChannels') is not None:
            self.audio_channels = m.get('AudioChannels')

        if m.get('AudioSampleRate') is not None:
            self.audio_sample_rate = m.get('AudioSampleRate')

        if m.get('FrameFillType') is not None:
            self.frame_fill_type = m.get('FrameFillType')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')

        if m.get('VideoFramerate') is not None:
            self.video_framerate = m.get('VideoFramerate')

        if m.get('VideoGop') is not None:
            self.video_gop = m.get('VideoGop')

        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')

        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')

        return self

class StartRtcCloudRecordingRequestMixLayoutParams(DaraModel):
    def __init__(
        self,
        mix_background: main_models.StartRtcCloudRecordingRequestMixLayoutParamsMixBackground = None,
        user_panes: List[main_models.StartRtcCloudRecordingRequestMixLayoutParamsUserPanes] = None,
    ):
        self.mix_background = mix_background
        self.user_panes = user_panes

    def validate(self):
        if self.mix_background:
            self.mix_background.validate()
        if self.user_panes:
            for v1 in self.user_panes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mix_background is not None:
            result['MixBackground'] = self.mix_background.to_map()

        result['UserPanes'] = []
        if self.user_panes is not None:
            for k1 in self.user_panes:
                result['UserPanes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MixBackground') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestMixLayoutParamsMixBackground()
            self.mix_background = temp_model.from_map(m.get('MixBackground'))

        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k1 in m.get('UserPanes'):
                temp_model = main_models.StartRtcCloudRecordingRequestMixLayoutParamsUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        return self

class StartRtcCloudRecordingRequestMixLayoutParamsUserPanes(DaraModel):
    def __init__(
        self,
        height: str = None,
        source_type: int = None,
        sub_background: main_models.StartRtcCloudRecordingRequestMixLayoutParamsUserPanesSubBackground = None,
        user_id: str = None,
        width: str = None,
        x: str = None,
        y: str = None,
        zorder: int = None,
    ):
        self.height = height
        self.source_type = source_type
        self.sub_background = sub_background
        self.user_id = user_id
        self.width = width
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        if self.sub_background:
            self.sub_background.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.sub_background is not None:
            result['SubBackground'] = self.sub_background.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SubBackground') is not None:
            temp_model = main_models.StartRtcCloudRecordingRequestMixLayoutParamsUserPanesSubBackground()
            self.sub_background = temp_model.from_map(m.get('SubBackground'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class StartRtcCloudRecordingRequestMixLayoutParamsUserPanesSubBackground(DaraModel):
    def __init__(
        self,
        render_mode: int = None,
        url: str = None,
    ):
        self.render_mode = render_mode
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.render_mode is not None:
            result['RenderMode'] = self.render_mode

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderMode') is not None:
            self.render_mode = m.get('RenderMode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class StartRtcCloudRecordingRequestMixLayoutParamsMixBackground(DaraModel):
    def __init__(
        self,
        render_mode: int = None,
        url: str = None,
    ):
        self.render_mode = render_mode
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.render_mode is not None:
            result['RenderMode'] = self.render_mode

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderMode') is not None:
            self.render_mode = m.get('RenderMode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

