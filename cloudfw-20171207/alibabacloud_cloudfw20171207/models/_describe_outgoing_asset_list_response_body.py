# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOutgoingAssetListResponseBody(DaraModel):
    def __init__(
        self,
        asset_list: List[main_models.DescribeOutgoingAssetListResponseBodyAssetList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.asset_list = asset_list
        self.request_id = request_id
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
                temp_model = main_models.DescribeOutgoingAssetListResponseBodyAssetList()
                self.asset_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOutgoingAssetListResponseBodyAssetList(DaraModel):
    def __init__(
        self,
        asset_instance_id: str = None,
        asset_instance_name: str = None,
        assets_region: str = None,
        group_name: str = None,
        in_bytes: int = None,
        ips_hit_cnt: int = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        out_bytes: int = None,
        outgoing_domain_cnt: int = None,
        outgoing_dst_ipcnt: int = None,
        private_ip: str = None,
        private_iplist: List[str] = None,
        public_ip: str = None,
        resource_type: str = None,
        security_risk: str = None,
        session_count: int = None,
        total_bytes: int = None,
    ):
        self.asset_instance_id = asset_instance_id
        self.asset_instance_name = asset_instance_name
        self.assets_region = assets_region
        self.group_name = group_name
        self.in_bytes = in_bytes
        self.ips_hit_cnt = ips_hit_cnt
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.out_bytes = out_bytes
        self.outgoing_domain_cnt = outgoing_domain_cnt
        self.outgoing_dst_ipcnt = outgoing_dst_ipcnt
        self.private_ip = private_ip
        self.private_iplist = private_iplist
        self.public_ip = public_ip
        self.resource_type = resource_type
        self.security_risk = security_risk
        self.session_count = session_count
        self.total_bytes = total_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_instance_id is not None:
            result['AssetInstanceId'] = self.asset_instance_id

        if self.asset_instance_name is not None:
            result['AssetInstanceName'] = self.asset_instance_name

        if self.assets_region is not None:
            result['AssetsRegion'] = self.assets_region

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.ips_hit_cnt is not None:
            result['IpsHitCnt'] = self.ips_hit_cnt

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.outgoing_domain_cnt is not None:
            result['OutgoingDomainCnt'] = self.outgoing_domain_cnt

        if self.outgoing_dst_ipcnt is not None:
            result['OutgoingDstIPCnt'] = self.outgoing_dst_ipcnt

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.private_iplist is not None:
            result['PrivateIPList'] = self.private_iplist

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.security_risk is not None:
            result['SecurityRisk'] = self.security_risk

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetInstanceId') is not None:
            self.asset_instance_id = m.get('AssetInstanceId')

        if m.get('AssetInstanceName') is not None:
            self.asset_instance_name = m.get('AssetInstanceName')

        if m.get('AssetsRegion') is not None:
            self.assets_region = m.get('AssetsRegion')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('IpsHitCnt') is not None:
            self.ips_hit_cnt = m.get('IpsHitCnt')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('OutgoingDomainCnt') is not None:
            self.outgoing_domain_cnt = m.get('OutgoingDomainCnt')

        if m.get('OutgoingDstIPCnt') is not None:
            self.outgoing_dst_ipcnt = m.get('OutgoingDstIPCnt')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('PrivateIPList') is not None:
            self.private_iplist = m.get('PrivateIPList')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SecurityRisk') is not None:
            self.security_risk = m.get('SecurityRisk')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        return self

