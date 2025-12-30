# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMediaConnectFlowInputRequest(DaraModel):
    def __init__(
        self,
        cidrs: str = None,
        flow_id: str = None,
        input_from_url: str = None,
        input_name: str = None,
        input_protocol: str = None,
        max_bitrate: int = None,
        pair_flow_id: str = None,
        pair_output_name: str = None,
        srt_latency: int = None,
        srt_passphrase: str = None,
        srt_pbkey_len: str = None,
    ):
        # The IP address whitelist in CIDR format. Separate multiple CIDR blocks with commas (,).
        self.cidrs = cidrs
        # The flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id
        # The source URL. This parameter is required when the source type is RTMP-PULL or SRT-Listener.
        self.input_from_url = input_from_url
        # The source name.
        # 
        # This parameter is required.
        self.input_name = input_name
        # The source type.
        # 
        # Valid values:
        # 
        # *   RTMP-PUSH
        # *   SRT-Caller
        # *   RTMP-PULL
        # *   SRT-Listener
        # *   Flow
        # 
        # This parameter is required.
        self.input_protocol = input_protocol
        # The maximum bitrate. Unit: bit/s.
        self.max_bitrate = max_bitrate
        # The ID of the source flow. This parameter is required when the source type is Flow.
        self.pair_flow_id = pair_flow_id
        # The output of the source flow. This parameter is required when the source type is Flow.
        self.pair_output_name = pair_output_name
        # The latency for the SRT stream. This parameter is required the source type is SRT-Listener or SRT-Caller.
        self.srt_latency = srt_latency
        # The SRT key. This parameter is required when the source type is SRT-Listener or SRT-Caller.
        self.srt_passphrase = srt_passphrase
        # The encryption key length. This parameter is required when the source type is SRT-Listener or SRT-Caller.
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

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.input_from_url is not None:
            result['InputFromUrl'] = self.input_from_url

        if self.input_name is not None:
            result['InputName'] = self.input_name

        if self.input_protocol is not None:
            result['InputProtocol'] = self.input_protocol

        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate

        if self.pair_flow_id is not None:
            result['PairFlowId'] = self.pair_flow_id

        if self.pair_output_name is not None:
            result['PairOutputName'] = self.pair_output_name

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

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('InputFromUrl') is not None:
            self.input_from_url = m.get('InputFromUrl')

        if m.get('InputName') is not None:
            self.input_name = m.get('InputName')

        if m.get('InputProtocol') is not None:
            self.input_protocol = m.get('InputProtocol')

        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')

        if m.get('PairFlowId') is not None:
            self.pair_flow_id = m.get('PairFlowId')

        if m.get('PairOutputName') is not None:
            self.pair_output_name = m.get('PairOutputName')

        if m.get('SrtLatency') is not None:
            self.srt_latency = m.get('SrtLatency')

        if m.get('SrtPassphrase') is not None:
            self.srt_passphrase = m.get('SrtPassphrase')

        if m.get('SrtPbkeyLen') is not None:
            self.srt_pbkey_len = m.get('SrtPbkeyLen')

        return self

