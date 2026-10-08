# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetScalingRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        update_time: int = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The time when the scaling rule was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetScalingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_type: int = None,
        oversold_factor: int = None,
        rule_list: main_models.GetScalingRulesResponseBodyDataRuleList = None,
        update_time: int = None,
        vpc_id: str = None,
    ):
        # The type of the cluster. Valid values:
        # 
        # - 0: regular Docker cluster
        # 
        # - 1: Swarm cluster (deprecated)
        # 
        # - 2: Elastic Compute Service (ECS) cluster
        # 
        # - 3: self-managed Kubernetes cluster in EDAS
        # 
        # - 4: cluster in which Pandora automatically registers applications
        # 
        # - 5: Container Service for Kubernetes (ACK) clusters
        self.cluster_type = cluster_type
        # The overcommit ratio supported by a Docker cluster. Valid values:
        # 
        # - 1: 1:1, which means that resources are not overcommitted.
        # 
        # - 2: 1:2, which means that resources are overcommitted by 1:2.
        # 
        # - 4: 1:4, which means that resources are overcommitted by 1:4.
        # 
        # - 8: 1:8, which means that resources are overcommitted by 1:8.
        self.oversold_factor = oversold_factor
        self.rule_list = rule_list
        # The time when the scaling rule was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.oversold_factor is not None:
            result['OversoldFactor'] = self.oversold_factor

        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('OversoldFactor') is not None:
            self.oversold_factor = m.get('OversoldFactor')

        if m.get('RuleList') is not None:
            temp_model = main_models.GetScalingRulesResponseBodyDataRuleList()
            self.rule_list = temp_model.from_map(m.get('RuleList'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetScalingRulesResponseBodyDataRuleList(DaraModel):
    def __init__(
        self,
        rule: List[main_models.GetScalingRulesResponseBodyDataRuleListRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.GetScalingRulesResponseBodyDataRuleListRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class GetScalingRulesResponseBodyDataRuleListRule(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cond: str = None,
        cpu: int = None,
        create_time: int = None,
        duration: int = None,
        enable: bool = None,
        group_id: str = None,
        inst_num: int = None,
        load_num: int = None,
        metric_type: str = None,
        mode: str = None,
        multi_az_policy: str = None,
        resource_from: str = None,
        rt: int = None,
        spec_id: str = None,
        step: int = None,
        template_id: str = None,
        template_version: int = None,
        update_time: int = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.app_id = app_id
        self.cond = cond
        self.cpu = cpu
        self.create_time = create_time
        self.duration = duration
        self.enable = enable
        self.group_id = group_id
        self.inst_num = inst_num
        self.load_num = load_num
        self.metric_type = metric_type
        self.mode = mode
        self.multi_az_policy = multi_az_policy
        self.resource_from = resource_from
        self.rt = rt
        self.spec_id = spec_id
        self.step = step
        self.template_id = template_id
        self.template_version = template_version
        self.update_time = update_time
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cond is not None:
            result['Cond'] = self.cond

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.inst_num is not None:
            result['InstNum'] = self.inst_num

        if self.load_num is not None:
            result['LoadNum'] = self.load_num

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.multi_az_policy is not None:
            result['MultiAzPolicy'] = self.multi_az_policy

        if self.resource_from is not None:
            result['ResourceFrom'] = self.resource_from

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.step is not None:
            result['Step'] = self.step

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Cond') is not None:
            self.cond = m.get('Cond')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstNum') is not None:
            self.inst_num = m.get('InstNum')

        if m.get('LoadNum') is not None:
            self.load_num = m.get('LoadNum')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('MultiAzPolicy') is not None:
            self.multi_az_policy = m.get('MultiAzPolicy')

        if m.get('ResourceFrom') is not None:
            self.resource_from = m.get('ResourceFrom')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

