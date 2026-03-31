# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeFreeUserAssetCountResponseBody(DaraModel):
    def __init__(
        self,
        asset: main_models.DescribeFreeUserAssetCountResponseBodyAsset = None,
        request_id: str = None,
    ):
        # The asset statistics provided by basic detection.
        self.asset = asset
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.asset:
            self.asset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = main_models.DescribeFreeUserAssetCountResponseBodyAsset()
            self.asset = temp_model.from_map(m.get('Asset'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFreeUserAssetCountResponseBodyAsset(DaraModel):
    def __init__(
        self,
        asset_active: int = None,
        asset_count: int = None,
        asset_offline: int = None,
    ):
        # The number of active APIs.
        self.asset_active = asset_active
        # The total number of APIs.
        self.asset_count = asset_count
        # The number of deactivated APIs.
        self.asset_offline = asset_offline

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetActive') is not None:
            self.asset_active = m.get('AssetActive')

        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('AssetOffline') is not None:
            self.asset_offline = m.get('AssetOffline')

        return self

