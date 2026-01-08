# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskSecurityGroupDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        risk_sg_detail: List[main_models.DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetail] = None,
        total_count: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.risk_sg_detail = risk_sg_detail
        self.total_count = total_count

    def validate(self):
        if self.risk_sg_detail:
            for v1 in self.risk_sg_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskSgDetail'] = []
        if self.risk_sg_detail is not None:
            for k1 in self.risk_sg_detail:
                result['RiskSgDetail'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_sg_detail = []
        if m.get('RiskSgDetail') is not None:
            for k1 in m.get('RiskSgDetail'):
                temp_model = main_models.DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetail()
                self.risk_sg_detail.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetail(DaraModel):
    def __init__(
        self,
        ecs_count: int = None,
        ecs_info: List[main_models.DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetailEcsInfo] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_no: str = None,
        risk_level: str = None,
        rule_info: List[main_models.DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetailRuleInfo] = None,
        vpc_id: str = None,
    ):
        self.ecs_count = ecs_count
        self.ecs_info = ecs_info
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.region_no = region_no
        self.risk_level = risk_level
        self.rule_info = rule_info
        self.vpc_id = vpc_id

    def validate(self):
        if self.ecs_info:
            for v1 in self.ecs_info:
                 if v1:
                    v1.validate()
        if self.rule_info:
            for v1 in self.rule_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        result['EcsInfo'] = []
        if self.ecs_info is not None:
            for k1 in self.ecs_info:
                result['EcsInfo'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        result['RuleInfo'] = []
        if self.rule_info is not None:
            for k1 in self.rule_info:
                result['RuleInfo'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        self.ecs_info = []
        if m.get('EcsInfo') is not None:
            for k1 in m.get('EcsInfo'):
                temp_model = main_models.DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetailEcsInfo()
                self.ecs_info.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        self.rule_info = []
        if m.get('RuleInfo') is not None:
            for k1 in m.get('RuleInfo'):
                temp_model = main_models.DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetailRuleInfo()
                self.rule_info.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetailRuleInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        risk_level: str = None,
        rule_name: str = None,
        rule_status: str = None,
        rule_uuid: str = None,
        suggestion: str = None,
    ):
        self.description = description
        self.risk_level = risk_level
        self.rule_name = rule_name
        self.rule_status = rule_status
        self.rule_uuid = rule_uuid
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        if self.rule_uuid is not None:
            result['RuleUuid'] = self.rule_uuid

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('RuleUuid') is not None:
            self.rule_uuid = m.get('RuleUuid')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class DescribeRiskSecurityGroupDetailResponseBodyRiskSgDetailEcsInfo(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        private_ip: str = None,
        public_ip: str = None,
    ):
        self.ecs_instance_id = ecs_instance_id
        self.ecs_instance_name = ecs_instance_name
        self.private_ip = private_ip
        self.public_ip = public_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        return self

