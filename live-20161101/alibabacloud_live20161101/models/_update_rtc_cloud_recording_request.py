# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class UpdateRtcCloudRecordingRequest(DaraModel):
    def __init__(
        self,
        mix_layout_params: main_models.UpdateRtcCloudRecordingRequestMixLayoutParams = None,
        subscribe_params: main_models.UpdateRtcCloudRecordingRequestSubscribeParams = None,
        task_id: str = None,
    ):
        # The updated layout parameters. Leave this parameter empty in single-stream recording mode. This parameter is required in stream mixing recording mode when the transcoding output is not audio-only.
        self.mix_layout_params = mix_layout_params
        # The updated subscription parameters.
        # 
        # This parameter is required.
        self.subscribe_params = subscribe_params
        # The task ID. This ID is returned by StartRtcCloudRecording. Only tasks in the running or abnormal state can be updated.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.mix_layout_params:
            self.mix_layout_params.validate()
        if self.subscribe_params:
            self.subscribe_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mix_layout_params is not None:
            result['MixLayoutParams'] = self.mix_layout_params.to_map()

        if self.subscribe_params is not None:
            result['SubscribeParams'] = self.subscribe_params.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MixLayoutParams') is not None:
            temp_model = main_models.UpdateRtcCloudRecordingRequestMixLayoutParams()
            self.mix_layout_params = temp_model.from_map(m.get('MixLayoutParams'))

        if m.get('SubscribeParams') is not None:
            temp_model = main_models.UpdateRtcCloudRecordingRequestSubscribeParams()
            self.subscribe_params = temp_model.from_map(m.get('SubscribeParams'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class UpdateRtcCloudRecordingRequestSubscribeParams(DaraModel):
    def __init__(
        self,
        subscribe_user_id_list: List[main_models.UpdateRtcCloudRecordingRequestSubscribeParamsSubscribeUserIdList] = None,
    ):
        # The list of subscribed UserId entries. In single-stream recording mode, each UserId is recorded separately. In stream mixing recording mode, the audio and video of all UserIds are mixed into a single set of audio and video.
        # > 
        # > - The array supports a maximum of 17 elements.
        # 
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
                temp_model = main_models.UpdateRtcCloudRecordingRequestSubscribeParamsSubscribeUserIdList()
                self.subscribe_user_id_list.append(temp_model.from_map(k1))

        return self

class UpdateRtcCloudRecordingRequestSubscribeParamsSubscribeUserIdList(DaraModel):
    def __init__(
        self,
        source_type: int = None,
        stream_type: int = None,
        user_id: str = None,
    ):
        # The video input stream type of the UserId. This parameter takes effect only when the video stream is subscribed (StreamType=2). Valid values:
        # 
        # - 0: camera. (Default)
        # 
        # - 1: screen sharing.
        self.source_type = source_type
        # The media type of the subscribed UserId. Valid values:
        # 
        # - 0: original stream, which includes both audio and video. (Default)
        # 
        # - 1: audio-only stream.
        # 
        # - 2: video-only stream.
        self.stream_type = stream_type
        # The subscribed UserId.
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

class UpdateRtcCloudRecordingRequestMixLayoutParams(DaraModel):
    def __init__(
        self,
        mix_background: main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsMixBackground = None,
        user_panes: List[main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanes] = None,
    ):
        # The global background image for stream mixing.
        self.mix_background = mix_background
        # The window layout information of the subscribed users. Only UserIds with layout information configured are placed in the output. This parameter is required in stream mixing mode when recording non-audio-only files.
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
            temp_model = main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsMixBackground()
            self.mix_background = temp_model.from_map(m.get('MixBackground'))

        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k1 in m.get('UserPanes'):
                temp_model = main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        return self

class UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanes(DaraModel):
    def __init__(
        self,
        height: str = None,
        source_type: int = None,
        sub_background: main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanesSubBackground = None,
        user_id: str = None,
        width: str = None,
        x: str = None,
        y: str = None,
        zorder: int = None,
    ):
        # The pane height as a normalized percentage. The value must be in the range of [0, 1]. (Default: 0)
        self.height = height
        # The video input stream type of the UserId. This parameter is invalid if UserId is not specified. Valid values:
        # - 0: camera. (Default)
        # - 1: screen sharing.
        # 
        # The combination of UserId and SourceType specified here must be included in SubscribeUserIdList.
        self.source_type = source_type
        # The sub-pane background image. When a user turns off the camera, has not started stream ingest after joining, or leaves the channel midway, the corresponding image is displayed at the layout position.
        self.sub_background = sub_background
        # The UserId corresponding to this window.
        # - If UserId is not specified, windows are filled in the order in which subscribed users join the channel.
        # - The combination of UserId and SourceType specified here must be included in SubscribeUserIdList.
        # - Audio-only streams cannot be added to the layout.
        self.user_id = user_id
        # The pane width as a normalized percentage. The value must be in the range of [0, 1]. (Default: 0)
        self.width = width
        # The X coordinate as a normalized percentage. The value must be in the range of [0, 1]. (Default: 0)
        self.x = x
        # The Y coordinate as a normalized percentage. The value must be in the range of [0, 1]. (Default: 0)
        self.y = y
        # The stacking order. 0 is the bottom layer, layer 1 is above layer 0, and so on. (Default: 0)
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
            temp_model = main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanesSubBackground()
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

class UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanesSubBackground(DaraModel):
    def __init__(
        self,
        render_mode: int = None,
        url: str = None,
    ):
        # The display mode for the sub-pane output. Valid values:
        # - 0: crop. (Default)
        # - 1: scale and display with black borders.
        self.render_mode = render_mode
        # The URL of the background image. The maximum length is 2048 characters.
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

class UpdateRtcCloudRecordingRequestMixLayoutParamsMixBackground(DaraModel):
    def __init__(
        self,
        render_mode: int = None,
        url: str = None,
    ):
        # The display mode for the output. Valid values:
        # - 0: crop. (Default)
        # - 1: scale and display with black borders.
        self.render_mode = render_mode
        # The URL of the background image. The maximum length is 2048 characters.
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

