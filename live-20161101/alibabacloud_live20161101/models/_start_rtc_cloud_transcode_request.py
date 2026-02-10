# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class StartRtcCloudTranscodeRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        input_param: main_models.StartRtcCloudTranscodeRequestInputParam = None,
        max_idle_time: int = None,
        output_params: List[main_models.StartRtcCloudTranscodeRequestOutputParams] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.input_param = input_param
        self.max_idle_time = max_idle_time
        # This parameter is required.
        self.output_params = output_params

    def validate(self):
        if self.input_param:
            self.input_param.validate()
        if self.output_params:
            for v1 in self.output_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.input_param is not None:
            result['InputParam'] = self.input_param.to_map()

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        result['OutputParams'] = []
        if self.output_params is not None:
            for k1 in self.output_params:
                result['OutputParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('InputParam') is not None:
            temp_model = main_models.StartRtcCloudTranscodeRequestInputParam()
            self.input_param = temp_model.from_map(m.get('InputParam'))

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        self.output_params = []
        if m.get('OutputParams') is not None:
            for k1 in m.get('OutputParams'):
                temp_model = main_models.StartRtcCloudTranscodeRequestOutputParams()
                self.output_params.append(temp_model.from_map(k1))

        return self

class StartRtcCloudTranscodeRequestOutputParams(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        transcode_template: str = None,
        user_id: str = None,
        user_token: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.transcode_template = transcode_template
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.user_token = user_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.transcode_template is not None:
            result['TranscodeTemplate'] = self.transcode_template

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_token is not None:
            result['UserToken'] = self.user_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('TranscodeTemplate') is not None:
            self.transcode_template = m.get('TranscodeTemplate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserToken') is not None:
            self.user_token = m.get('UserToken')

        return self

class StartRtcCloudTranscodeRequestInputParam(DaraModel):
    def __init__(
        self,
        single_sub_user_param: main_models.StartRtcCloudTranscodeRequestInputParamSingleSubUserParam = None,
    ):
        # This parameter is required.
        self.single_sub_user_param = single_sub_user_param

    def validate(self):
        if self.single_sub_user_param:
            self.single_sub_user_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.single_sub_user_param is not None:
            result['SingleSubUserParam'] = self.single_sub_user_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SingleSubUserParam') is not None:
            temp_model = main_models.StartRtcCloudTranscodeRequestInputParamSingleSubUserParam()
            self.single_sub_user_param = temp_model.from_map(m.get('SingleSubUserParam'))

        return self

class StartRtcCloudTranscodeRequestInputParamSingleSubUserParam(DaraModel):
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

