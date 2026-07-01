# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaConnectFlowInputResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.GetMediaConnectFlowInputResponseBodyContent = None,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
    ):
        # The response body.
        self.content = content
        # The description of the API call.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The error code returned. A value of 0 indicates success.
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
            temp_model = main_models.GetMediaConnectFlowInputResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        return self

class GetMediaConnectFlowInputResponseBodyContent(DaraModel):
    def __init__(
        self,
        backup_cidrs: str = None,
        backup_create_time: str = None,
        backup_inner_input_url: str = None,
        backup_input_name: str = None,
        backup_input_status: str = None,
        backup_input_url: str = None,
        backup_max_bitrate: int = None,
        backup_srt_latency: int = None,
        backup_srt_passphrase: str = None,
        backup_srt_pbkey_len: int = None,
        cidrs: str = None,
        create_time: str = None,
        inner_input_url: str = None,
        input_name: str = None,
        input_protocol: str = None,
        input_status: str = None,
        input_url: str = None,
        max_bitrate: int = None,
        pair_flow_id: str = None,
        pair_output_name: str = None,
        srt_latency: int = None,
        srt_passphrase: str = None,
        srt_pbkey_len: int = None,
    ):
        # The IP address whitelist for the backup input.
        self.backup_cidrs = backup_cidrs
        # The time when the backup input was created.
        self.backup_create_time = backup_create_time
        self.backup_inner_input_url = backup_inner_input_url
        # The name of the backup input.
        self.backup_input_name = backup_input_name
        # The status of the backup input. It indicates whether the backup stream is being pushed.
        self.backup_input_status = backup_input_status
        # The URL of the backup input.
        self.backup_input_url = backup_input_url
        # The bitrate of the backup input.
        self.backup_max_bitrate = backup_max_bitrate
        # The SRT latency for the backup input.
        self.backup_srt_latency = backup_srt_latency
        # The SRT encryption key for the backup input.
        self.backup_srt_passphrase = backup_srt_passphrase
        # The SRT encryption key length for the backup input.
        self.backup_srt_pbkey_len = backup_srt_pbkey_len
        # The IP address whitelist in CIDR format. Separate multiple IP address segments with commas.
        self.cidrs = cidrs
        # The time when the input was created.
        self.create_time = create_time
        self.inner_input_url = inner_input_url
        # The input name.
        self.input_name = input_name
        # The input type.
        self.input_protocol = input_protocol
        # The input status. It indicates whether the primary stream is being pushed.
        self.input_status = input_status
        # The input URL.
        self.input_url = input_url
        # The input bitrate, in bps.
        self.max_bitrate = max_bitrate
        # The ID of the peer Flow instance. This parameter is required only if the output type is Flow.
        self.pair_flow_id = pair_flow_id
        # The output name of the peer Flow. This parameter is required only when the input type is Flow.
        self.pair_output_name = pair_output_name
        # The SRT latency in milliseconds (ms). This parameter is required only when the input type is SRT-Listener or SRT-Caller.
        self.srt_latency = srt_latency
        # The SRT encryption key. This parameter is required only when the input type is SRT-Listener or SRT-Caller.
        self.srt_passphrase = srt_passphrase
        # The SRT encryption key length. This parameter is required only when the input type is SRT-Listener or SRT-Caller.
        self.srt_pbkey_len = srt_pbkey_len

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_cidrs is not None:
            result['BackupCidrs'] = self.backup_cidrs

        if self.backup_create_time is not None:
            result['BackupCreateTime'] = self.backup_create_time

        if self.backup_inner_input_url is not None:
            result['BackupInnerInputUrl'] = self.backup_inner_input_url

        if self.backup_input_name is not None:
            result['BackupInputName'] = self.backup_input_name

        if self.backup_input_status is not None:
            result['BackupInputStatus'] = self.backup_input_status

        if self.backup_input_url is not None:
            result['BackupInputUrl'] = self.backup_input_url

        if self.backup_max_bitrate is not None:
            result['BackupMaxBitrate'] = self.backup_max_bitrate

        if self.backup_srt_latency is not None:
            result['BackupSrtLatency'] = self.backup_srt_latency

        if self.backup_srt_passphrase is not None:
            result['BackupSrtPassphrase'] = self.backup_srt_passphrase

        if self.backup_srt_pbkey_len is not None:
            result['BackupSrtPbkeyLen'] = self.backup_srt_pbkey_len

        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.inner_input_url is not None:
            result['InnerInputUrl'] = self.inner_input_url

        if self.input_name is not None:
            result['InputName'] = self.input_name

        if self.input_protocol is not None:
            result['InputProtocol'] = self.input_protocol

        if self.input_status is not None:
            result['InputStatus'] = self.input_status

        if self.input_url is not None:
            result['InputUrl'] = self.input_url

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
        if m.get('BackupCidrs') is not None:
            self.backup_cidrs = m.get('BackupCidrs')

        if m.get('BackupCreateTime') is not None:
            self.backup_create_time = m.get('BackupCreateTime')

        if m.get('BackupInnerInputUrl') is not None:
            self.backup_inner_input_url = m.get('BackupInnerInputUrl')

        if m.get('BackupInputName') is not None:
            self.backup_input_name = m.get('BackupInputName')

        if m.get('BackupInputStatus') is not None:
            self.backup_input_status = m.get('BackupInputStatus')

        if m.get('BackupInputUrl') is not None:
            self.backup_input_url = m.get('BackupInputUrl')

        if m.get('BackupMaxBitrate') is not None:
            self.backup_max_bitrate = m.get('BackupMaxBitrate')

        if m.get('BackupSrtLatency') is not None:
            self.backup_srt_latency = m.get('BackupSrtLatency')

        if m.get('BackupSrtPassphrase') is not None:
            self.backup_srt_passphrase = m.get('BackupSrtPassphrase')

        if m.get('BackupSrtPbkeyLen') is not None:
            self.backup_srt_pbkey_len = m.get('BackupSrtPbkeyLen')

        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InnerInputUrl') is not None:
            self.inner_input_url = m.get('InnerInputUrl')

        if m.get('InputName') is not None:
            self.input_name = m.get('InputName')

        if m.get('InputProtocol') is not None:
            self.input_protocol = m.get('InputProtocol')

        if m.get('InputStatus') is not None:
            self.input_status = m.get('InputStatus')

        if m.get('InputUrl') is not None:
            self.input_url = m.get('InputUrl')

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

