# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallAssetListResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVpcFirewallAssetListResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVpcFirewallAssetListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallAssetListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        asset_ip: str = None,
        asset_instance_id: str = None,
        asset_instance_name: str = None,
        in_bytes: int = None,
        ips_hit_cnt: int = None,
        out_bytes: int = None,
        port_list: List[str] = None,
        region_no: str = None,
        risk_level: int = None,
        risk_reason: str = None,
        session_count: int = None,
        total_bytes: int = None,
    ):
        self.asset_ip = asset_ip
        self.asset_instance_id = asset_instance_id
        self.asset_instance_name = asset_instance_name
        self.in_bytes = in_bytes
        self.ips_hit_cnt = ips_hit_cnt
        self.out_bytes = out_bytes
        self.port_list = port_list
        self.region_no = region_no
        self.risk_level = risk_level
        self.risk_reason = risk_reason
        self.session_count = session_count
        self.total_bytes = total_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip

        if self.asset_instance_id is not None:
            result['AssetInstanceId'] = self.asset_instance_id

        if self.asset_instance_name is not None:
            result['AssetInstanceName'] = self.asset_instance_name

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.ips_hit_cnt is not None:
            result['IpsHitCnt'] = self.ips_hit_cnt

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.port_list is not None:
            result['PortList'] = self.port_list

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_reason is not None:
            result['RiskReason'] = self.risk_reason

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')

        if m.get('AssetInstanceId') is not None:
            self.asset_instance_id = m.get('AssetInstanceId')

        if m.get('AssetInstanceName') is not None:
            self.asset_instance_name = m.get('AssetInstanceName')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('IpsHitCnt') is not None:
            self.ips_hit_cnt = m.get('IpsHitCnt')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('PortList') is not None:
            self.port_list = m.get('PortList')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskReason') is not None:
            self.risk_reason = m.get('RiskReason')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        return self

