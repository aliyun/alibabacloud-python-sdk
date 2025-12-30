# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateMediaLiveInputRequest(DaraModel):
    def __init__(
        self,
        input_id: str = None,
        input_settings: List[main_models.UpdateMediaLiveInputRequestInputSettings] = None,
        name: str = None,
        security_group_ids: List[str] = None,
    ):
        # The ID of the input.
        # 
        # This parameter is required.
        self.input_id = input_id
        # The input settings. An input can have up to two sources: primary and backup sources.
        # 
        # This parameter is required.
        self.input_settings = input_settings
        # The name of the input. Letters, digits, hyphens (-), and underscores (_) are supported. It can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The IDs of the security groups to be associated with the input. This parameter is required for PUSH inputs.
        self.security_group_ids = security_group_ids

    def validate(self):
        if self.input_settings:
            for v1 in self.input_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_id is not None:
            result['InputId'] = self.input_id

        result['InputSettings'] = []
        if self.input_settings is not None:
            for k1 in self.input_settings:
                result['InputSettings'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')

        self.input_settings = []
        if m.get('InputSettings') is not None:
            for k1 in m.get('InputSettings'):
                temp_model = main_models.UpdateMediaLiveInputRequestInputSettings()
                self.input_settings.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        return self

class UpdateMediaLiveInputRequestInputSettings(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        flow_output_name: str = None,
        source_url: str = None,
        srt_latency: int = None,
        srt_max_bitrate: int = None,
        srt_passphrase: str = None,
        srt_pb_key_len: int = None,
        stream_name: str = None,
    ):
        # The ID of the flow from MediaConnect. This parameter is required when Type is set to MEDIA_CONNECT.
        self.flow_id = flow_id
        # The output name of the MediaConnect flow. This parameter is required when Type is set to MEDIA_CONNECT.
        self.flow_output_name = flow_output_name
        # The source URL from which the stream is pulled. This parameter is required for PULL inputs.
        self.source_url = source_url
        self.srt_latency = srt_latency
        self.srt_max_bitrate = srt_max_bitrate
        self.srt_passphrase = srt_passphrase
        self.srt_pb_key_len = srt_pb_key_len
        # The name of the pushed stream. This parameter is required for PUSH inputs. It can be up to 255 characters in length.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_output_name is not None:
            result['FlowOutputName'] = self.flow_output_name

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        if self.srt_latency is not None:
            result['SrtLatency'] = self.srt_latency

        if self.srt_max_bitrate is not None:
            result['SrtMaxBitrate'] = self.srt_max_bitrate

        if self.srt_passphrase is not None:
            result['SrtPassphrase'] = self.srt_passphrase

        if self.srt_pb_key_len is not None:
            result['SrtPbKeyLen'] = self.srt_pb_key_len

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowOutputName') is not None:
            self.flow_output_name = m.get('FlowOutputName')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        if m.get('SrtLatency') is not None:
            self.srt_latency = m.get('SrtLatency')

        if m.get('SrtMaxBitrate') is not None:
            self.srt_max_bitrate = m.get('SrtMaxBitrate')

        if m.get('SrtPassphrase') is not None:
            self.srt_passphrase = m.get('SrtPassphrase')

        if m.get('SrtPbKeyLen') is not None:
            self.srt_pb_key_len = m.get('SrtPbKeyLen')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

