# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserAssetResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.DescribeUserAssetResponseBodyAssets] = None,
        request_id: str = None,
    ):
        # The API statistics.
        self.assets = assets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.assets:
            for v1 in self.assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assets'] = []
        if self.assets is not None:
            for k1 in self.assets:
                result['Assets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.DescribeUserAssetResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserAssetResponseBodyAssets(DaraModel):
    def __init__(
        self,
        asset_num: int = None,
        time_stamp: int = None,
    ):
        # The number of APIs returned.
        self.asset_num = asset_num
        # The time at which the API was called. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

