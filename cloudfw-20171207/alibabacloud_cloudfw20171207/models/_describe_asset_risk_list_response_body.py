# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetRiskListResponseBody(DaraModel):
    def __init__(
        self,
        asset_list: List[main_models.DescribeAssetRiskListResponseBodyAssetList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the assets.
        self.asset_list = asset_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.asset_list:
            for v1 in self.asset_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetList'] = []
        if self.asset_list is not None:
            for k1 in self.asset_list:
                result['AssetList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_list = []
        if m.get('AssetList') is not None:
            for k1 in m.get('AssetList'):
                temp_model = main_models.DescribeAssetRiskListResponseBodyAssetList()
                self.asset_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAssetRiskListResponseBodyAssetList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        ip_version: int = None,
        reason: str = None,
        risk_level: str = None,
    ):
        # The IP address of the server.
        self.ip = ip
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The reason for the risk.
        self.reason = reason
        # The risk level. Valid values:
        # 
        # *   **low**
        # *   **middle**
        # *   **high**
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

