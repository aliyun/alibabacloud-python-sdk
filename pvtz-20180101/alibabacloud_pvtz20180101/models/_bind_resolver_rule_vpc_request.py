# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class BindResolverRuleVpcRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        rule_id: str = None,
        vpc: List[main_models.BindResolverRuleVpcRequestVpc] = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The VPCs that you want to associate with the forwarding rule.
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for v1 in self.vpc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        result['Vpc'] = []
        if self.vpc is not None:
            for k1 in self.vpc:
                result['Vpc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        self.vpc = []
        if m.get('Vpc') is not None:
            for k1 in m.get('Vpc'):
                temp_model = main_models.BindResolverRuleVpcRequestVpc()
                self.vpc.append(temp_model.from_map(k1))

        return self

class BindResolverRuleVpcRequestVpc(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        # The region ID of the outbound VPC.
        self.region_id = region_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

