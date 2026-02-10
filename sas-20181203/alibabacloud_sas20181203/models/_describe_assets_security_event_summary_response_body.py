# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetsSecurityEventSummaryResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.DescribeAssetsSecurityEventSummaryResponseBodyAssets] = None,
        request_id: str = None,
    ):
        # An array that consists of risk information about containers.
        self.assets = assets
        # The ID of the request, which is used to locate and troubleshoot issues.
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
                temp_model = main_models.DescribeAssetsSecurityEventSummaryResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAssetsSecurityEventSummaryResponseBodyAssets(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        risk_count: int = None,
        total_count: int = None,
    ):
        # The type of the asset. Valid values:
        # 
        # *   **namespace**
        # *   **clusters**
        # *   **applications**
        # *   **pods**
        # *   **containers**
        # *   **images**
        # *   **hosts**
        self.asset_type = asset_type
        # The number of potential risky assets.
        self.risk_count = risk_count
        # The total number of assets.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

