# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListMediaLiveInputsResponseBody(DaraModel):
    def __init__(
        self,
        inputs: List[main_models.ListMediaLiveInputsResponseBodyInputs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The inputs.
        self.inputs = inputs
        # The number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.inputs:
            for v1 in self.inputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Inputs'] = []
        if self.inputs is not None:
            for k1 in self.inputs:
                result['Inputs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inputs = []
        if m.get('Inputs') is not None:
            for k1 in m.get('Inputs'):
                temp_model = main_models.ListMediaLiveInputsResponseBodyInputs()
                self.inputs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMediaLiveInputsResponseBodyInputs(DaraModel):
    def __init__(
        self,
        channel_ids: List[str] = None,
        create_time: str = None,
        input_id: str = None,
        input_infos: List[main_models.ListMediaLiveInputsResponseBodyInputsInputInfos] = None,
        name: str = None,
        security_group_ids: List[str] = None,
        type: str = None,
    ):
        # The IDs of the channels associated with the input.
        self.channel_ids = channel_ids
        # The time when the input was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the input.
        self.input_id = input_id
        # The input configurations.
        self.input_infos = input_infos
        # The name of the input.
        self.name = name
        # The IDs of the security groups associated with the input.
        self.security_group_ids = security_group_ids
        # The input type.
        self.type = type

    def validate(self):
        if self.input_infos:
            for v1 in self.input_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.input_id is not None:
            result['InputId'] = self.input_id

        result['InputInfos'] = []
        if self.input_infos is not None:
            for k1 in self.input_infos:
                result['InputInfos'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')

        self.input_infos = []
        if m.get('InputInfos') is not None:
            for k1 in m.get('InputInfos'):
                temp_model = main_models.ListMediaLiveInputsResponseBodyInputsInputInfos()
                self.input_infos.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListMediaLiveInputsResponseBodyInputsInputInfos(DaraModel):
    def __init__(
        self,
        dest_host: str = None,
        flow_id: str = None,
        flow_output_name: str = None,
        monitor_url: str = None,
        source_url: str = None,
        srt_latency: int = None,
        srt_max_bitrate: int = None,
        srt_passphrase: str = None,
        srt_pb_key_len: int = None,
        stream_name: str = None,
    ):
        # The endpoint that the stream is pushed to. This parameter is returned for PUSH inputs.
        self.dest_host = dest_host
        # The ID of the flow from MediaConnect.
        self.flow_id = flow_id
        # The output name of the MediaConnect flow.
        self.flow_output_name = flow_output_name
        # The URL for input monitoring.
        self.monitor_url = monitor_url
        # The source URL where the stream is pulled from. This parameter is returned for PULL inputs.
        self.source_url = source_url
        self.srt_latency = srt_latency
        self.srt_max_bitrate = srt_max_bitrate
        self.srt_passphrase = srt_passphrase
        self.srt_pb_key_len = srt_pb_key_len
        # The name of the pushed stream. This parameter is returned for PUSH inputs.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_host is not None:
            result['DestHost'] = self.dest_host

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_output_name is not None:
            result['FlowOutputName'] = self.flow_output_name

        if self.monitor_url is not None:
            result['MonitorUrl'] = self.monitor_url

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
        if m.get('DestHost') is not None:
            self.dest_host = m.get('DestHost')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowOutputName') is not None:
            self.flow_output_name = m.get('FlowOutputName')

        if m.get('MonitorUrl') is not None:
            self.monitor_url = m.get('MonitorUrl')

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

