# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaConnectFlowOutputRequest(DaraModel):
    def __init__(
        self,
        cidrs: str = None,
        flow_id: str = None,
        output_name: str = None,
        output_to_url: str = None,
        player_limit: str = None,
        srt_latency: str = None,
        srt_passphrase: str = None,
        srt_pbkey_len: str = None,
    ):
        # The IP address whitelist.
        self.cidrs = cidrs
        # The flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id
        # The output name.
        # 
        # This parameter is required.
        self.output_name = output_name
        # The output URL. You can modify this parameter only when the output type is RTMP-PUSH or SRT-Caller.
        self.output_to_url = output_to_url
        # The maximum number of viewers.
        self.player_limit = player_limit
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

        if self.output_name is not None:
            result['OutputName'] = self.output_name

        if self.output_to_url is not None:
            result['OutputToUrl'] = self.output_to_url

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

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('OutputName') is not None:
            self.output_name = m.get('OutputName')

        if m.get('OutputToUrl') is not None:
            self.output_to_url = m.get('OutputToUrl')

        if m.get('PlayerLimit') is not None:
            self.player_limit = m.get('PlayerLimit')

        if m.get('SrtLatency') is not None:
            self.srt_latency = m.get('SrtLatency')

        if m.get('SrtPassphrase') is not None:
            self.srt_passphrase = m.get('SrtPassphrase')

        if m.get('SrtPbkeyLen') is not None:
            self.srt_pbkey_len = m.get('SrtPbkeyLen')

        return self

