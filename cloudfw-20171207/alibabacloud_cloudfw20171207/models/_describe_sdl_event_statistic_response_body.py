# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSdlEventStatisticResponseBody(DaraModel):
    def __init__(
        self,
        ai_sensitive_data_count: int = None,
        asset_count: int = None,
        request_id: str = None,
        sensitive_data_count: int = None,
        total_count: int = None,
        total_traffic: int = None,
    ):
        self.ai_sensitive_data_count = ai_sensitive_data_count
        self.asset_count = asset_count
        self.request_id = request_id
        self.sensitive_data_count = sensitive_data_count
        self.total_count = total_count
        self.total_traffic = total_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_sensitive_data_count is not None:
            result['AiSensitiveDataCount'] = self.ai_sensitive_data_count

        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sensitive_data_count is not None:
            result['SensitiveDataCount'] = self.sensitive_data_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiSensitiveDataCount') is not None:
            self.ai_sensitive_data_count = m.get('AiSensitiveDataCount')

        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SensitiveDataCount') is not None:
            self.sensitive_data_count = m.get('SensitiveDataCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')

        return self

