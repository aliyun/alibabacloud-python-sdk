# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutMetricRuleTargetsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        rule_id: str = None,
        targets: List[main_models.PutMetricRuleTargetsRequestTargets] = None,
    ):
        self.region_id = region_id
        # The ID of the alert rule.
        # 
        # For information about how to obtain the alert rule ID, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # None.
        # 
        # This parameter is required.
        self.targets = targets

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.PutMetricRuleTargetsRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class PutMetricRuleTargetsRequestTargets(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        json_params: str = None,
        level: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the resource. Simple Message Queue (formerly MNS), elastic scaling (ESS), Simple Log Service (SLS), and Function Compute (FC) are supported.
        # 
        # The following section describes the ARN parameter metric description for Simple Message Queue (formerly MNS):
        # 
        # `acs:mns:{regionId}:{userId}:/{Resource type}/{Resource name}/message`
        # 
        # - {regionId}: the region where the MSMQ or topic of Simple Message Queue (formerly MNS) resides.
        # - {userId}: the Alibaba Cloud account that owns the resource.
        # - {Resource type}: the type of the resource that accepts alert notifications. Valid values:
        # 
        #   - **queues**: queue.
        #   - **topics**: topic.
        # 
        # - {Resource name}: the name of the resource.
        # 
        #   - If the resource type is **queues**, the resource name is the queue name.
        #   - If the resource type is **topics**, the resource name is the topic name.
        # 
        # ARN for elastic scaling:
        # 
        # acs:ess:{regionId}:{userId}:scalingGroupId/{Scaling group ID}:scalingRuleId/{Scaling rule ID}
        # 
        # ARN for Simple Log Service:
        # 
        # acs:log:{regionId}:{userId}:project/{Project name}/logstore/{Logstore name}
        # 
        # ARN for Function Compute:
        # 
        # acs:fc:{regionId}:{userId}:services/{Service name}/functions/{Function name}.
        # 
        # This parameter is required.
        self.arn = arn
        # The ID of the alert trigger target.
        # 
        # For information about how to obtain the alert trigger target ID, see [DescribeMetricRuleTargets](https://help.aliyun.com/document_detail/121592.html).
        # 
        # This parameter is required.
        self.id = id
        # The JSON-formatted parameters of the alert callback.
        self.json_params = json_params
        # The alert level. Valid values:
        # 
        # - INFO: information.
        # - WARN: warning.
        # - CRITICAL: critical.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.id is not None:
            result['Id'] = self.id

        if self.json_params is not None:
            result['JsonParams'] = self.json_params

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JsonParams') is not None:
            self.json_params = m.get('JsonParams')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

