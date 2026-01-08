# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOutgoingDestinationIPDetailResponseBody(DaraModel):
    def __init__(
        self,
        asset_list: List[main_models.DescribeOutgoingDestinationIPDetailResponseBodyAssetList] = None,
        isp_name: str = None,
        location_name: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.asset_list = asset_list
        self.isp_name = isp_name
        self.location_name = location_name
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

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.location_name is not None:
            result['LocationName'] = self.location_name

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
                temp_model = main_models.DescribeOutgoingDestinationIPDetailResponseBodyAssetList()
                self.asset_list.append(temp_model.from_map(k1))

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOutgoingDestinationIPDetailResponseBodyAssetList(DaraModel):
    def __init__(
        self,
        acl_coverage: str = None,
        first_time: int = None,
        in_bytes: int = None,
        isp_name: str = None,
        last_time: int = None,
        location_name: str = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        out_bytes: int = None,
        private_ip: str = None,
        public_ip: str = None,
        region_no: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        session_count: int = None,
        tag_list: List[main_models.DescribeOutgoingDestinationIPDetailResponseBodyAssetListTagList] = None,
        total_bytes: str = None,
        vpc_id: str = None,
    ):
        self.acl_coverage = acl_coverage
        self.first_time = first_time
        self.in_bytes = in_bytes
        self.isp_name = isp_name
        self.last_time = last_time
        self.location_name = location_name
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.out_bytes = out_bytes
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.region_no = region_no
        self.resource_instance_id = resource_instance_id
        self.resource_instance_name = resource_instance_name
        self.resource_type = resource_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.session_count = session_count
        self.tag_list = tag_list
        self.total_bytes = total_bytes
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeOutgoingDestinationIPDetailResponseBodyAssetListTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeOutgoingDestinationIPDetailResponseBodyAssetListTagList(DaraModel):
    def __init__(
        self,
        class_id: str = None,
        risk_level: int = None,
        tag_describe: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        self.class_id = class_id
        self.risk_level = risk_level
        self.tag_describe = tag_describe
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

