# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecAssetTrendResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecAssetTrendResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # Id of the request.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecAssetTrendResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApisecAssetTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        asset_active: int = None,
        asset_count: int = None,
        asset_offline: int = None,
        timestamp: int = None,
    ):
        # The number of active assets.
        self.asset_active = asset_active
        # The total number of assets.
        self.asset_count = asset_count
        # The number of deactivated assets.
        self.asset_offline = asset_offline
        # The time for statistics. Specify a UNIX timestamp in UTC. Unit: seconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_active is not None:
            result['AssetActive'] = self.asset_active

        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.asset_offline is not None:
            result['AssetOffline'] = self.asset_offline

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetActive') is not None:
            self.asset_active = m.get('AssetActive')

        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('AssetOffline') is not None:
            self.asset_offline = m.get('AssetOffline')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

