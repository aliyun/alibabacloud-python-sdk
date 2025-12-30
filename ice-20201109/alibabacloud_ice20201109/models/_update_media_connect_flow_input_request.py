# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaConnectFlowInputRequest(DaraModel):
    def __init__(
        self,
        cidrs: str = None,
        flow_id: str = None,
        input_from_url: str = None,
        input_name: str = None,
        max_bitrate: int = None,
        srt_latency: int = None,
        srt_passphrase: str = None,
        srt_pbkey_len: int = None,
    ):
        # The IP address whitelist.
        self.cidrs = cidrs
        # The flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id
        # The source URL. You can modify this parameter only when the source type is RTMP-PULL or SRT-Listener.
        self.input_from_url = input_from_url
        self.input_name = input_name
        # The maximum bitrate. Unit: bit/s.
        self.max_bitrate = max_bitrate
        # The latency for the SRT stream. You can modify this parameter only when the source type is SRT-Listener or SRT-Caller.
        self.srt_latency = srt_latency
        # The SRT key. You can modify this parameter only when the source type is SRT-Listener or SRT-Caller.
        self.srt_passphrase = srt_passphrase
        # The encryption key length. You can modify this parameter only when the source type is SRT-Listener or SRT-Caller.
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

        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate

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

        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')

        if m.get('SrtLatency') is not None:
            self.srt_latency = m.get('SrtLatency')

        if m.get('SrtPassphrase') is not None:
            self.srt_passphrase = m.get('SrtPassphrase')

        if m.get('SrtPbkeyLen') is not None:
            self.srt_pbkey_len = m.get('SrtPbkeyLen')

        return self

