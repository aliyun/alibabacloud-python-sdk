# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class StartLiveMPUTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        max_idle_time: str = None,
        mix_mode: str = None,
        multi_stream_url: List[main_models.StartLiveMPUTaskRequestMultiStreamURL] = None,
        region: str = None,
        sei_params: main_models.StartLiveMPUTaskRequestSeiParams = None,
        single_sub_params: main_models.StartLiveMPUTaskRequestSingleSubParams = None,
        stream_url: str = None,
        task_id: str = None,
        transcode_params: main_models.StartLiveMPUTaskRequestTranscodeParams = None,
    ):
        # The application ID. Only one ID is supported. It can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The channel ID. Only one ID is supported. It can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The idle timeout period. Unit: seconds. The value must be in the range of [10, 86400].
        # 
        # > If you set this parameter, the task is automatically stopped when it has been idle for a period longer than MaxIdleTime. If you do not set this parameter, the task is stopped immediately after the channel is closed.
        self.max_idle_time = max_idle_time
        # The stream mixing mode. Valid values:
        # 
        # - **0**: Single-stream ingest. The original single stream is ingested without stream mixing or transcoding. You do not need to configure stream mixing and transcoding parameters.
        # 
        # - **1** (default): Stream mixing and transcoding.
        # 
        # This parameter is required.
        self.mix_mode = mix_mode
        # The parameters for ingesting to multiple URLs. You can specify multiple live ingest URLs.
        # 
        # > When you set the ingest URL for a task, you must configure either the StreamURL parameter or the MultiStreamURL parameter, but not both.
        self.multi_stream_url = multi_stream_url
        # The region where the stream mixing service is located. Valid values:
        # 
        # - **CN-Shanghai<props="china">(default)**: Shanghai.
        # 
        # - **AP-Singapore<props="intl">(default)**: Singapore.
        # 
        # - **EMAA-Saudi**: Saudi Arabia.
        self.region = region
        # The SEI configuration parameters.
        self.sei_params = sei_params
        # The parameters for single-stream ingest. This parameter is required when MixMode is set to 0. Do not set this parameter for stream mixing and transcoding.
        self.single_sub_params = single_sub_params
        # The live ingest URL. Only the RTMP protocol is supported. Only one URL is supported. The maximum length is 2048 characters. For information about how to generate the URL, see [Ingest URLs and playback URLs](https://help.aliyun.com/document_detail/199339.html).
        # 
        # > - For domain names with hotlink protection enabled, the ingest URL must include an access token.
        # 
        # - Do not use the same StreamURL in different tasks at the same time.
        # 
        # - Do not use the same StreamURL within 10 seconds after a task stops.
        self.stream_url = stream_url
        # The task ID. Only one ID is supported. It can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 55 characters. This ID is the unique identifier for the bypass ingest task.
        # If a task with the same ID still exists and has not been cleared when you start a new task, \\`InvalidParam\\` is returned.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The parameters for stream mixing and transcoding. This parameter is required when MixMode is set to 1. Do not set this parameter for single-stream ingest.
        self.transcode_params = transcode_params

    def validate(self):
        if self.multi_stream_url:
            for v1 in self.multi_stream_url:
                 if v1:
                    v1.validate()
        if self.sei_params:
            self.sei_params.validate()
        if self.single_sub_params:
            self.single_sub_params.validate()
        if self.transcode_params:
            self.transcode_params.validate()

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

        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode

        result['MultiStreamURL'] = []
        if self.multi_stream_url is not None:
            for k1 in self.multi_stream_url:
                result['MultiStreamURL'].append(k1.to_map() if k1 else None)

        if self.region is not None:
            result['Region'] = self.region

        if self.sei_params is not None:
            result['SeiParams'] = self.sei_params.to_map()

        if self.single_sub_params is not None:
            result['SingleSubParams'] = self.single_sub_params.to_map()

        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.transcode_params is not None:
            result['TranscodeParams'] = self.transcode_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')

        self.multi_stream_url = []
        if m.get('MultiStreamURL') is not None:
            for k1 in m.get('MultiStreamURL'):
                temp_model = main_models.StartLiveMPUTaskRequestMultiStreamURL()
                self.multi_stream_url.append(temp_model.from_map(k1))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SeiParams') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestSeiParams()
            self.sei_params = temp_model.from_map(m.get('SeiParams'))

        if m.get('SingleSubParams') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestSingleSubParams()
            self.single_sub_params = temp_model.from_map(m.get('SingleSubParams'))

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TranscodeParams') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestTranscodeParams()
            self.transcode_params = temp_model.from_map(m.get('TranscodeParams'))

        return self

class StartLiveMPUTaskRequestTranscodeParams(DaraModel):
    def __init__(
        self,
        background: main_models.StartLiveMPUTaskRequestTranscodeParamsBackground = None,
        encode_params: main_models.StartLiveMPUTaskRequestTranscodeParamsEncodeParams = None,
        layout: main_models.StartLiveMPUTaskRequestTranscodeParamsLayout = None,
        user_infos: List[main_models.StartLiveMPUTaskRequestTranscodeParamsUserInfos] = None,
    ):
        # The global background image for the mixed stream.
        self.background = background
        # The encoding parameters for the output stream.
        self.encode_params = encode_params
        # The video layout information.
        # 
        # > For video transcoding, you must specify the video layout information, including coordinates (X, Y), pane dimensions (Width, Height), and stacking order (ZOrder). For audio-only transcoding, do not specify video layout information.
        self.layout = layout
        # The information about the users to subscribe to for stream mixing. If you do not specify users, all users are included in the mixed stream.
        self.user_infos = user_infos

    def validate(self):
        if self.background:
            self.background.validate()
        if self.encode_params:
            self.encode_params.validate()
        if self.layout:
            self.layout.validate()
        if self.user_infos:
            for v1 in self.user_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background is not None:
            result['Background'] = self.background.to_map()

        if self.encode_params is not None:
            result['EncodeParams'] = self.encode_params.to_map()

        if self.layout is not None:
            result['Layout'] = self.layout.to_map()

        result['UserInfos'] = []
        if self.user_infos is not None:
            for k1 in self.user_infos:
                result['UserInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Background') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestTranscodeParamsBackground()
            self.background = temp_model.from_map(m.get('Background'))

        if m.get('EncodeParams') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestTranscodeParamsEncodeParams()
            self.encode_params = temp_model.from_map(m.get('EncodeParams'))

        if m.get('Layout') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestTranscodeParamsLayout()
            self.layout = temp_model.from_map(m.get('Layout'))

        self.user_infos = []
        if m.get('UserInfos') is not None:
            for k1 in m.get('UserInfos'):
                temp_model = main_models.StartLiveMPUTaskRequestTranscodeParamsUserInfos()
                self.user_infos.append(temp_model.from_map(k1))

        return self

class StartLiveMPUTaskRequestTranscodeParamsUserInfos(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        source_type: str = None,
        stream_type: str = None,
        user_id: str = None,
    ):
        # The ID of the channel where the subscribed user is located. You do not need to set this parameter for users in the same channel. For cross-channel stream mixing, set this parameter.
        self.channel_id = channel_id
        # The type of video input stream to subscribe to for stream mixing. This parameter is valid only for video streams (StreamType=2). Valid values:
        # 
        # - **camera** (default): Camera stream.
        # 
        # - **shareScreen**: Screen sharing stream.
        self.source_type = source_type
        # The type of stream to subscribe to for stream mixing. Valid values:
        # 
        # - **0** (default): Ingest the original stream.
        # 
        # - **1**: Ingest only the audio stream.
        # 
        # - **2**: Ingest only the video stream.
        self.stream_type = stream_type
        # The ID of the user to subscribe to for stream mixing.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class StartLiveMPUTaskRequestTranscodeParamsLayout(DaraModel):
    def __init__(
        self,
        user_panes: List[main_models.StartLiveMPUTaskRequestTranscodeParamsLayoutUserPanes] = None,
    ):
        # The information about user panes in the mixed stream.
        self.user_panes = user_panes

    def validate(self):
        if self.user_panes:
            for v1 in self.user_panes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k1 in self.user_panes:
                result['UserPanes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k1 in m.get('UserPanes'):
                temp_model = main_models.StartLiveMPUTaskRequestTranscodeParamsLayoutUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        return self

class StartLiveMPUTaskRequestTranscodeParamsLayoutUserPanes(DaraModel):
    def __init__(
        self,
        background_image_url: str = None,
        height: str = None,
        render_mode: str = None,
        user_info: main_models.StartLiveMPUTaskRequestTranscodeParamsLayoutUserPanesUserInfo = None,
        width: str = None,
        x: str = None,
        y: str = None,
        zorder: str = None,
    ):
        # The URL of the background image for the video pane. The maximum length is 2048 characters. When a user turns off their camera or has not joined the channel, this image is displayed in their layout position.
        self.background_image_url = background_image_url
        # The height of the pane, as a normalized percentage.
        self.height = height
        # The display mode of the output video pane. Valid values:
        # 
        # - **0**: Scale and display a black background.
        # 
        # - **1** (default): Clip.
        self.render_mode = render_mode
        # The information about the user corresponding to this pane. If you do not set this parameter, the system automatically fills it based on the order in which streamers join the channel.
        # 
        # > - If you specify user information, that user must already be configured in the \\`TranscodeParams.UserInfos\\` parameter.
        # 
        # - This parameter is valid only for original streams and video streams.
        self.user_info = user_info
        # The width of the pane, as a normalized percentage.
        self.width = width
        # The X-coordinate, as a normalized percentage.
        self.x = x
        # The Y-coordinate, as a normalized percentage.
        self.y = y
        # The stacking order. 0 is the bottom layer. Layer 1 is on top of layer 0, and so on.
        self.zorder = zorder

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url

        if self.height is not None:
            result['Height'] = self.height

        if self.render_mode is not None:
            result['RenderMode'] = self.render_mode

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

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
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('RenderMode') is not None:
            self.render_mode = m.get('RenderMode')

        if m.get('UserInfo') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestTranscodeParamsLayoutUserPanesUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class StartLiveMPUTaskRequestTranscodeParamsLayoutUserPanesUserInfo(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        source_type: str = None,
        user_id: str = None,
    ):
        # The ID of the channel where the user is located. You do not need to set this parameter for users in the same channel. For cross-channel stream mixing, set this parameter.
        self.channel_id = channel_id
        # The type of video input stream in stream mixing and transcoding mode. This parameter is valid only for video streams (StreamType=2). Valid values:
        # 
        # - **camera** (default): Camera stream.
        # 
        # - **shareScreen**: Screen sharing stream.
        self.source_type = source_type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class StartLiveMPUTaskRequestTranscodeParamsEncodeParams(DaraModel):
    def __init__(
        self,
        audio_bitrate: str = None,
        audio_channels: str = None,
        audio_only: str = None,
        audio_sample_rate: str = None,
        enhanced_param: str = None,
        video_bitrate: str = None,
        video_codec: str = None,
        video_framerate: str = None,
        video_gop: str = None,
        video_height: str = None,
        video_width: str = None,
    ):
        # The audio bitrate. Unit: kbps. The value must be in the range of [8, 500].
        self.audio_bitrate = audio_bitrate
        # The number of audio channels. Valid values: 1, 2.
        self.audio_channels = audio_channels
        # Specifies whether the stream is audio-only. Valid values:
        # 
        # - **true**: Audio-only. You only need to set audio-related parameters.
        # 
        # - **false** (default): Not audio-only. All parameters except VideoCodec and EnhancedParam must be specified.
        self.audio_only = audio_only
        # The audio sampling rate. Unit: Hz. Valid values: 8000, 16000, 32000, 44100, 48000.
        self.audio_sample_rate = audio_sample_rate
        # The enhanced encoding parameters. This is a JSON string. The supported optional configurations include \\`profile\\` and \\`preset\\`.
        # 
        # - \\`profile\\`: The encoding profile. If the video encoding format is H.264, valid values for \\`profile\\` include "baseline", "main", and "high". If the video encoding format is H.265, the valid value for \\`profile\\` is "main".
        # 
        # - \\`preset\\`: Balances encoding speed and quality. Valid values for \\`preset\\` include "ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow", and "placebo". Each value represents a strategy for balancing encoding speed and output video quality, from "ultrafast" (fastest encoding speed) to "placebo" (highest quality, slowest encoding speed).
        # 
        # > For example, "superfast" is mainly used for real-time communication. If you are not an expert in encoders, do not set this option.
        self.enhanced_param = enhanced_param
        # The video bitrate. Unit: kbps. The value must be in the range of [1, 10000].
        self.video_bitrate = video_bitrate
        # The video encoding format. Valid values:
        # 
        # - H.264 (default).
        # 
        # - H.265.
        self.video_codec = video_codec
        # The video frame rate. Unit: fps. The value must be in the range of [1, 60].
        self.video_framerate = video_framerate
        # The video GOP size. The value must be in the range of [1, 60].
        self.video_gop = video_gop
        # The video height. Unit: pixels. The value must be in the range of [0, 1920].
        self.video_height = video_height
        # The video width. Unit: pixels. The value must be in the range of [0, 1920].
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

        if self.audio_only is not None:
            result['AudioOnly'] = self.audio_only

        if self.audio_sample_rate is not None:
            result['AudioSampleRate'] = self.audio_sample_rate

        if self.enhanced_param is not None:
            result['EnhancedParam'] = self.enhanced_param

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

        if m.get('AudioOnly') is not None:
            self.audio_only = m.get('AudioOnly')

        if m.get('AudioSampleRate') is not None:
            self.audio_sample_rate = m.get('AudioSampleRate')

        if m.get('EnhancedParam') is not None:
            self.enhanced_param = m.get('EnhancedParam')

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

class StartLiveMPUTaskRequestTranscodeParamsBackground(DaraModel):
    def __init__(
        self,
        render_mode: str = None,
        url: str = None,
    ):
        # The display mode of the output video. Valid values:
        # 
        # - **0**: Scale and display a black background.
        # 
        # - **1** (default): Clip.
        self.render_mode = render_mode
        # The URL of the global background image. The maximum length is 2048 characters.
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
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderMode') is not None:
            self.render_mode = m.get('RenderMode')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class StartLiveMPUTaskRequestSingleSubParams(DaraModel):
    def __init__(
        self,
        source_type: str = None,
        stream_type: str = None,
        user_id: str = None,
    ):
        # The type of video input stream in single-stream ingest mode. This parameter is valid only for video streams (StreamType=2). Valid values:
        # 
        # - **camera** (default): Camera stream.
        # 
        # - **shareScreen**: Screen sharing stream.
        self.source_type = source_type
        # The type of stream to ingest in single-stream ingest mode. Valid values:
        # 
        # - **0** (default): Ingest the original stream.
        # 
        # - **1**: Ingest only the audio stream.
        # 
        # - **2**: Ingest only the video stream.
        self.stream_type = stream_type
        # The ID of the user whose stream is ingested. Only one stream can be ingested at a time.
        # 
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

class StartLiveMPUTaskRequestSeiParams(DaraModel):
    def __init__(
        self,
        layout_volume: main_models.StartLiveMPUTaskRequestSeiParamsLayoutVolume = None,
        pass_through: main_models.StartLiveMPUTaskRequestSeiParamsPassThrough = None,
        payload_type: str = None,
    ):
        # The layout and volume SEI. The content of this parameter can be empty, which means the default layout and volume SEI is carried.
        self.layout_volume = layout_volume
        # The pass-through SEI.
        self.pass_through = pass_through
        # The custom payload_type of the SEI message. The value must be in the range of 100-254. If not set, the default payload_type is 5.
        self.payload_type = payload_type

    def validate(self):
        if self.layout_volume:
            self.layout_volume.validate()
        if self.pass_through:
            self.pass_through.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_volume is not None:
            result['LayoutVolume'] = self.layout_volume.to_map()

        if self.pass_through is not None:
            result['PassThrough'] = self.pass_through.to_map()

        if self.payload_type is not None:
            result['PayloadType'] = self.payload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutVolume') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestSeiParamsLayoutVolume()
            self.layout_volume = temp_model.from_map(m.get('LayoutVolume'))

        if m.get('PassThrough') is not None:
            temp_model = main_models.StartLiveMPUTaskRequestSeiParamsPassThrough()
            self.pass_through = temp_model.from_map(m.get('PassThrough'))

        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')

        return self

class StartLiveMPUTaskRequestSeiParamsPassThrough(DaraModel):
    def __init__(
        self,
        follow_idr: str = None,
        interval: str = None,
        payload_content: str = None,
        payload_content_key: str = None,
    ):
        # Specifies whether to ensure that SEI is carried when sending an IDR keyframe. Valid values:
        # 
        # - **0**: Does not ensure SEI is carried.
        # 
        # - **1**: Ensures SEI is carried.
        self.follow_idr = follow_idr
        # The SEI sending interval. Unit: milliseconds. The value must be in the range of [1000, 5000].
        self.interval = interval
        # The payload content of the pass-through SEI.
        self.payload_content = payload_content
        # The key corresponding to the payload content of the pass-through SEI. If not set, the default key is \\`udd\\`.
        self.payload_content_key = payload_content_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.follow_idr is not None:
            result['FollowIdr'] = self.follow_idr

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.payload_content is not None:
            result['PayloadContent'] = self.payload_content

        if self.payload_content_key is not None:
            result['PayloadContentKey'] = self.payload_content_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FollowIdr') is not None:
            self.follow_idr = m.get('FollowIdr')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('PayloadContent') is not None:
            self.payload_content = m.get('PayloadContent')

        if m.get('PayloadContentKey') is not None:
            self.payload_content_key = m.get('PayloadContentKey')

        return self

class StartLiveMPUTaskRequestSeiParamsLayoutVolume(DaraModel):
    def __init__(
        self,
        follow_idr: str = None,
        interval: str = None,
    ):
        # Specifies whether to ensure that SEI is carried when sending an IDR keyframe. Valid values:
        # 
        # - **0**: Does not ensure SEI is carried.
        # 
        # - **1**: Ensures SEI is carried.
        self.follow_idr = follow_idr
        # The SEI sending interval. Unit: milliseconds. The value must be in the range of [1000, 5000].
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.follow_idr is not None:
            result['FollowIdr'] = self.follow_idr

        if self.interval is not None:
            result['Interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FollowIdr') is not None:
            self.follow_idr = m.get('FollowIdr')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        return self

class StartLiveMPUTaskRequestMultiStreamURL(DaraModel):
    def __init__(
        self,
        is_ali_cdn: bool = None,
        url: str = None,
    ):
        # Specifies whether to ingest the stream to Alibaba Cloud CDN.
        # 
        # - false: Ingest to a non-Alibaba Cloud CDN.
        # 
        # - true: Ingest to Alibaba Cloud CDN.
        # 
        # > The default value is false.
        self.is_ali_cdn = is_ali_cdn
        # The live ingest URL. Only the RTMP protocol is supported. The maximum length is 2048 characters. For information about how to generate the URL, see [Ingest URLs and playback URLs](https://help.aliyun.com/document_detail/199339.html).
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_ali_cdn is not None:
            result['IsAliCdn'] = self.is_ali_cdn

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAliCdn') is not None:
            self.is_ali_cdn = m.get('IsAliCdn')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

