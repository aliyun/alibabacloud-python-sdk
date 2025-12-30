# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaConnectFlowOutputResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.GetMediaConnectFlowOutputResponseBodyContent = None,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
    ):
        # The response body.
        self.content = content
        # The call description.
        self.description = description
        # The ID of the request.
        self.request_id = request_id
        # The returned error code. A value of 0 indicates the call is successful.
        self.ret_code = ret_code

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.GetMediaConnectFlowOutputResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        return self

class GetMediaConnectFlowOutputResponseBodyContent(DaraModel):
    def __init__(
        self,
        cidrs: str = None,
        create_time: str = None,
        forbid: str = None,
        output_name: str = None,
        output_protocol: str = None,
        output_url: str = None,
        pair_flow_id: str = None,
        pair_input_name: str = None,
        player_limit: int = None,
        srt_latency: int = None,
        srt_passphrase: str = None,
        srt_pbkey_len: int = None,
    ):
        # The IP address whitelist in CIDR format. CIDR blocks are separated with commas (,).
        self.cidrs = cidrs
        # The time when the flow was created.
        self.create_time = create_time
        self.forbid = forbid
        # The output name.
        self.output_name = output_name
        # The output type.
        # 
        # Valid values:
        # 
        # *   RTMP-PUSH
        # *   SRT-Caller
        # *   RTMP-PULL
        # *   SRT-Listener
        # *   Flow
        self.output_protocol = output_protocol
        # The output URL.
        self.output_url = output_url
        # The ID of the destination flow. This parameter is returned when the output type is Flow.
        self.pair_flow_id = pair_flow_id
        # The source name of the destination flow. This parameter is returned when the output type is Flow.
        self.pair_input_name = pair_input_name
        # The maximum number of viewers.
        self.player_limit = player_limit
        # The latency for the SRT stream. Unit: milliseconds. This parameter is returned when the source type is SRT-Listener or SRT-Caller.
        self.srt_latency = srt_latency
        # The SRT key. This parameter is returned when the source type is SRT-Listener or SRT-Caller.
        self.srt_passphrase = srt_passphrase
        # The encryption key length. This parameter is returned when the source type is SRT-Listener or SRT-Caller.
        # 
        # Valid values:
        # 
        # *   0
        # *   16
        # *   24
        # *   32
        self.srt_pbkey_len = srt_pbkey_len

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.forbid is not None:
            result['Forbid'] = self.forbid

        if self.output_name is not None:
            result['OutputName'] = self.output_name

        if self.output_protocol is not None:
            result['OutputProtocol'] = self.output_protocol

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        if self.pair_flow_id is not None:
            result['PairFlowId'] = self.pair_flow_id

        if self.pair_input_name is not None:
            result['PairInputName'] = self.pair_input_name

        if self.player_limit is not None:
            result['PlayerLimit'] = self.player_limit

        if self.srt_latency is not None:
            result['SrtLatency'] = self.srt_latency

        if self.srt_passphrase is not None:
            result['SrtPassphrase'] = self.srt_passphrase

        if self.srt_pbkey_len is not None:
            result['SrtPbkeyLen'] = self.srt_pbkey_len

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Forbid') is not None:
            self.forbid = m.get('Forbid')

        if m.get('OutputName') is not None:
            self.output_name = m.get('OutputName')

        if m.get('OutputProtocol') is not None:
            self.output_protocol = m.get('OutputProtocol')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        if m.get('PairFlowId') is not None:
            self.pair_flow_id = m.get('PairFlowId')

        if m.get('PairInputName') is not None:
            self.pair_input_name = m.get('PairInputName')

        if m.get('PlayerLimit') is not None:
            self.player_limit = m.get('PlayerLimit')

        if m.get('SrtLatency') is not None:
            self.srt_latency = m.get('SrtLatency')

        if m.get('SrtPassphrase') is not None:
            self.srt_passphrase = m.get('SrtPassphrase')

        if m.get('SrtPbkeyLen') is not None:
            self.srt_pbkey_len = m.get('SrtPbkeyLen')

        return self

