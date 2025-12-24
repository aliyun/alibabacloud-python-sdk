# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListRtcMPUTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        mputasks: List[main_models.ListRtcMPUTaskDetailResponseBodyMPUTasks] = None,
        request_id: str = None,
    ):
        # The parameters that you configured when you called the StartLiveMPUTask operation to create the tasks.
        self.mputasks = mputasks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mputasks:
            for v1 in self.mputasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MPUTasks'] = []
        if self.mputasks is not None:
            for k1 in self.mputasks:
                result['MPUTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mputasks = []
        if m.get('MPUTasks') is not None:
            for k1 in m.get('MPUTasks'):
                temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasks()
                self.mputasks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRtcMPUTaskDetailResponseBodyMPUTasks(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        max_idle_time: str = None,
        mix_mode: str = None,
        multi_stream_url: List[main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksMultiStreamURL] = None,
        region: str = None,
        sei_params: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParams = None,
        single_sub_params: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSingleSubParams = None,
        stream_url: str = None,
        task_id: str = None,
        transcode_params: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParams = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the channel.
        self.channel_id = channel_id
        # The timeout period of an idle connection. Unit: seconds.
        # 
        # >  If the task is idle for a period of time longer than the duration specified by the MaxIdleTime parameter, the task is automatically stopped. If the parameter is not specified, the task is stopped after the channel is closed.
        self.max_idle_time = max_idle_time
        # The stream mixing mode. Valid values:
        # 
        # *   0: relays the original single stream without mixing streams. If the value of this parameter is 0, the TranscodeParams parameter is empty.
        # *   1 (default): mixes multiple streams into a single stream and relays the mixed stream.
        self.mix_mode = mix_mode
        # The multiple ingest URLs relayed.
        self.multi_stream_url = multi_stream_url
        # The region in which the streams are mixed. Valid values:
        # 
        # *   **CN-shanghai**
        # *   **AP-Singapore (default)**
        # *   **EMAA-Saudi**
        self.region = region
        # The supplemental enhancement information (SEI) parameters.
        self.sei_params = sei_params
        # The parameters of the single-stream relay task.
        self.single_sub_params = single_sub_params
        # The ingest URL.
        self.stream_url = stream_url
        # The ID of the stream relay task.
        self.task_id = task_id
        # The mixed-stream relay parameters.
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
                temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksMultiStreamURL()
                self.multi_stream_url.append(temp_model.from_map(k1))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SeiParams') is not None:
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParams()
            self.sei_params = temp_model.from_map(m.get('SeiParams'))

        if m.get('SingleSubParams') is not None:
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSingleSubParams()
            self.single_sub_params = temp_model.from_map(m.get('SingleSubParams'))

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TranscodeParams') is not None:
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParams()
            self.transcode_params = temp_model.from_map(m.get('TranscodeParams'))

        return self

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParams(DaraModel):
    def __init__(
        self,
        background: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsBackground = None,
        encode_params: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsEncodeParams = None,
        layout: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayout = None,
        user_infos: List[main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsUserInfos] = None,
    ):
        # The global background image.
        self.background = background
        # The encoding parameters of the output stream.
        self.encode_params = encode_params
        # The video layout information.
        # 
        # >  The video layout information includes the x-coordinate, y-coordinate, width, height, and layer of the pane. For audio-only transcoding, no video layout information is returned.
        self.layout = layout
        # The information about the user whose stream is mixed. If an empty value is returned, streams from all users are mixed.
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
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsBackground()
            self.background = temp_model.from_map(m.get('Background'))

        if m.get('EncodeParams') is not None:
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsEncodeParams()
            self.encode_params = temp_model.from_map(m.get('EncodeParams'))

        if m.get('Layout') is not None:
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayout()
            self.layout = temp_model.from_map(m.get('Layout'))

        self.user_infos = []
        if m.get('UserInfos') is not None:
            for k1 in m.get('UserInfos'):
                temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsUserInfos()
                self.user_infos.append(temp_model.from_map(k1))

        return self

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsUserInfos(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        source_type: str = None,
        stream_type: str = None,
        user_id: str = None,
    ):
        # The ID of the channel where the user is.
        self.channel_id = channel_id
        # The source of the video. This parameter is valid only if you set StreamType to 2. Valid values:
        # 
        # *   camera (default): captures the video by using a camera.
        # *   shareScreen: captures the content displayed on a screen.
        self.source_type = source_type
        # The type of the stream that is relayed. Valid values:
        # 
        # *   0 (default): the original stream.
        # *   1: the audio-only stream.
        # *   2: the video-only stream.
        self.stream_type = stream_type
        # The ID of the user.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayout(DaraModel):
    def __init__(
        self,
        user_panes: List[main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayoutUserPanes] = None,
    ):
        # The information about the panes.
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
                temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayoutUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        return self

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayoutUserPanes(DaraModel):
    def __init__(
        self,
        background_image_url: str = None,
        height: str = None,
        render_mode: str = None,
        user_info: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayoutUserPanesUserInfo = None,
        width: str = None,
        x: str = None,
        y: str = None,
        zorder: str = None,
    ):
        # The URL of the background image of the pane. This image is displayed if the user turns off the camera or is not present in the channel.
        self.background_image_url = background_image_url
        # The height of the pane. The value is normalized.
        self.height = height
        # The display mode. Valid values:
        # 
        # *   0: proportionally scales the video or background image to fit the pane. Black bars are added to fill the extra space.
        # *   1 (default): crops the video or background image to fit the pane.
        self.render_mode = render_mode
        # The information about the user whose stream is played in the pane.
        self.user_info = user_info
        # The width of the pane. The value is normalized.
        self.width = width
        # The x-coordinate of the pane. The value is normalized.
        self.x = x
        # The y-coordinate of the pane. The value is normalized.
        self.y = y
        # The layer of the pane. A value of 0 indicates that the pane is placed at the bottom layer. A larger value indicates a higher layer.
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
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayoutUserPanesUserInfo()
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsLayoutUserPanesUserInfo(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        source_type: str = None,
        user_id: str = None,
    ):
        # The ID of the channel where the user is.
        self.channel_id = channel_id
        # The source of the video. This parameter is valid only if you set StreamType to 2. Valid values:
        # 
        # *   camera (default): captures the video by using a camera.
        # *   shareScreen: captures the content displayed on a screen.
        self.source_type = source_type
        # The ID of the user.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsEncodeParams(DaraModel):
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
        # The bitrate of the audio. Unit: Kbit/s.
        self.audio_bitrate = audio_bitrate
        # The number of audio channels. Valid values: 1 and 2.
        self.audio_channels = audio_channels
        # Indicates whether the output stream is an audio-only stream. Valid values:
        # 
        # *   true
        # *   false (default)
        self.audio_only = audio_only
        # The audio sampling rate. Unit: Hz.
        self.audio_sample_rate = audio_sample_rate
        # The parameter for advanced video encoding. The value is a JSON string. Optional fields:
        # 
        # *   profile: the encoding level. If the video encoding format is set to H.264, the valid values of this field are baseline, main, and high.
        # *   preset: adjusts the trade-off between encoding speed and video quality. Valid values: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow, and placebo. Each value specifies a level of trade-off between encoding speed and video quality. For example, the ultrafast preset has the fastest encoding speed but the lowest video quality, while the placebo preset sacrifices the encoding speed for the best video quality.
        self.enhanced_param = enhanced_param
        # The bitrate of the video. Unit: Kbit/s.
        self.video_bitrate = video_bitrate
        # The video encoding format. Default value: H.264.
        self.video_codec = video_codec
        # The frame rate of the video. Unit: frames per second (FPS).
        self.video_framerate = video_framerate
        # The group of pictures (GOP) size of the video.
        self.video_gop = video_gop
        # The height of the video. Unit: pixels.
        self.video_height = video_height
        # The width of the video. Unit: pixels.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksTranscodeParamsBackground(DaraModel):
    def __init__(
        self,
        render_mode: str = None,
        url: str = None,
    ):
        # The display mode. Valid values:
        # 
        # *   0: proportionally scales the video or background image to fit the pane. Black bars are added to fill the extra space.
        # *   1 (default): crops the video or background image to fit the pane.
        self.render_mode = render_mode
        # The URL of the global background image.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksSingleSubParams(DaraModel):
    def __init__(
        self,
        source_type: str = None,
        stream_type: str = None,
        user_id: str = None,
    ):
        # The source of the video. This parameter is valid only if you set StreamType to 2. Valid values:
        # 
        # *   camera (default): captures the video by using a camera.
        # *   shareScreen: captures the content displayed on a screen.
        self.source_type = source_type
        # The type of the stream that is relayed. Valid values:
        # 
        # *   0 (default): the original stream.
        # *   1: the audio-only stream.
        # *   2: the video-only stream.
        self.stream_type = stream_type
        # The ID of the user whose stream is relayed. In single-stream relay mode, you can relay only one stream in a request.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParams(DaraModel):
    def __init__(
        self,
        layout_volume: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParamsLayoutVolume = None,
        pass_through: main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParamsPassThrough = None,
        payload_type: str = None,
    ):
        # The layout and volume SEI. If the return value is an empty string, the default layout and volume SEI is used.
        self.layout_volume = layout_volume
        # The custom SEI.
        self.pass_through = pass_through
        # The custom payload type. Valid values: 100 to 254. Default value: 5.
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
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParamsLayoutVolume()
            self.layout_volume = temp_model.from_map(m.get('LayoutVolume'))

        if m.get('PassThrough') is not None:
            temp_model = main_models.ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParamsPassThrough()
            self.pass_through = temp_model.from_map(m.get('PassThrough'))

        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')

        return self

class ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParamsPassThrough(DaraModel):
    def __init__(
        self,
        follow_idr: str = None,
        interval: str = None,
        payload_content: str = None,
        payload_content_key: str = None,
    ):
        # Indicates whether to add SEI messages to Instantaneous Decoder Refresh (IDR) frames. Valid values:
        # 
        # *   0: does not add SEI messages.
        # *   1: adds SEI messages.
        self.follow_idr = follow_idr
        # The interval at which the SEI messages are added. Unit: milliseconds.
        self.interval = interval
        # The payload content of the custom SEI.
        self.payload_content = payload_content
        # The key of the payload content. Default value: udd.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksSeiParamsLayoutVolume(DaraModel):
    def __init__(
        self,
        follow_idr: str = None,
        interval: str = None,
    ):
        # Indicates whether to add SEI messages to Instantaneous Decoder Refresh (IDR) frames. Valid values:
        # 
        # *   0: does not add SEI messages.
        # *   1: adds SEI messages.
        self.follow_idr = follow_idr
        # The interval at which the SEI messages are added. Unit: milliseconds.
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

class ListRtcMPUTaskDetailResponseBodyMPUTasksMultiStreamURL(DaraModel):
    def __init__(
        self,
        is_ali_cdn: bool = None,
        url: str = None,
    ):
        # Indicates whether stream relay is performed by using Alibaba Cloud CDN. Valid values:
        # 
        # *   false: Stream relay is performed by using a CDN service that is not Alibaba Cloud CDN.
        # *   true: Stream relay is performed by using Alibaba Cloud CDN.
        self.is_ali_cdn = is_ali_cdn
        # The ingest URL.
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

