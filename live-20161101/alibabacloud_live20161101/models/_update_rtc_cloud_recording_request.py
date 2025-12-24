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
        self.mix_layout_params = mix_layout_params
        # This parameter is required.
        self.subscribe_params = subscribe_params
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

class UpdateRtcCloudRecordingRequestMixLayoutParams(DaraModel):
    def __init__(
        self,
        mix_background: main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsMixBackground = None,
        user_panes: List[main_models.UpdateRtcCloudRecordingRequestMixLayoutParamsUserPanes] = None,
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

class UpdateRtcCloudRecordingRequestMixLayoutParamsMixBackground(DaraModel):
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

