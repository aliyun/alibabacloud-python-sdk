# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribePolicyInstancesStatusResponseBody(DaraModel):
    def __init__(
        self,
        instances_severity_count: Dict[str, Any] = None,
        policy_instances: List[main_models.DescribePolicyInstancesStatusResponseBodyPolicyInstances] = None,
    ):
        # The number of policy instances that are deployed in the cluster at different severity levels.
        self.instances_severity_count = instances_severity_count
        # The number of policy instances of each policy type.
        self.policy_instances = policy_instances

    def validate(self):
        if self.policy_instances:
            for v1 in self.policy_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances_severity_count is not None:
            result['instances_severity_count'] = self.instances_severity_count

        result['policy_instances'] = []
        if self.policy_instances is not None:
            for k1 in self.policy_instances:
                result['policy_instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances_severity_count') is not None:
            self.instances_severity_count = m.get('instances_severity_count')

        self.policy_instances = []
        if m.get('policy_instances') is not None:
            for k1 in m.get('policy_instances'):
                temp_model = main_models.DescribePolicyInstancesStatusResponseBodyPolicyInstances()
                self.policy_instances.append(temp_model.from_map(k1))

        return self

class DescribePolicyInstancesStatusResponseBodyPolicyInstances(DaraModel):
    def __init__(
        self,
        policy_category: str = None,
        policy_description: str = None,
        policy_instances_count: int = None,
        policy_name: str = None,
        policy_severity: str = None,
    ):
        # The type of the policy. For more information about different types of policies and their descriptions, see [Predefined security policies of ACK](https://help.aliyun.com/document_detail/359819.html).
        self.policy_category = policy_category
        # The description of the policy.
        self.policy_description = policy_description
        # The number of policy instances that are deployed. If this parameter is empty, no policy instance is deployed.
        self.policy_instances_count = policy_instances_count
        # The name of the policy.
        self.policy_name = policy_name
        # The severity level of the policy.
        self.policy_severity = policy_severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_category is not None:
            result['policy_category'] = self.policy_category

        if self.policy_description is not None:
            result['policy_description'] = self.policy_description

        if self.policy_instances_count is not None:
            result['policy_instances_count'] = self.policy_instances_count

        if self.policy_name is not None:
            result['policy_name'] = self.policy_name

        if self.policy_severity is not None:
            result['policy_severity'] = self.policy_severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policy_category') is not None:
            self.policy_category = m.get('policy_category')

        if m.get('policy_description') is not None:
            self.policy_description = m.get('policy_description')

        if m.get('policy_instances_count') is not None:
            self.policy_instances_count = m.get('policy_instances_count')

        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')

        if m.get('policy_severity') is not None:
            self.policy_severity = m.get('policy_severity')

        return self

