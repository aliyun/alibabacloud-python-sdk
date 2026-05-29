# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetRuntimeChannelResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetRuntimeChannelResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetRuntimeChannelResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetRuntimeChannelResponseBodyData(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        channel_type: str = None,
        code: str = None,
        config: str = None,
        config_mode: str = None,
        qr_code_notify_url: str = None,
        qr_code_status: str = None,
        risk_type: str = None,
        status: str = None,
    ):
        self.avatar_url = avatar_url
        self.channel_type = channel_type
        self.code = code
        self.config = config
        self.config_mode = config_mode
        self.qr_code_notify_url = qr_code_notify_url
        self.qr_code_status = qr_code_status
        self.risk_type = risk_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.qr_code_notify_url is not None:
            result['QrCodeNotifyUrl'] = self.qr_code_notify_url

        if self.qr_code_status is not None:
            result['QrCodeStatus'] = self.qr_code_status

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('QrCodeNotifyUrl') is not None:
            self.qr_code_notify_url = m.get('QrCodeNotifyUrl')

        if m.get('QrCodeStatus') is not None:
            self.qr_code_status = m.get('QrCodeStatus')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

