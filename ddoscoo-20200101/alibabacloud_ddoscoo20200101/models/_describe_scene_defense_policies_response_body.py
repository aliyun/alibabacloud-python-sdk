# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSceneDefensePoliciesResponseBody(DaraModel):
    def __init__(
        self,
        policies: List[main_models.DescribeSceneDefensePoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # An array that consists of the configurations of the scenario-specific custom policy.
        self.policies = policies
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeSceneDefensePoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSceneDefensePoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        done: int = None,
        end_time: int = None,
        name: str = None,
        object_count: int = None,
        policy_id: str = None,
        runtime_policies: List[main_models.DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies] = None,
        start_time: int = None,
        status: int = None,
        template: str = None,
    ):
        # The execution status of the policy. Valid values:
        # 
        # *   **1**: not executed or execution completed
        # *   **0**: being executed
        # *   **-1**: execution failed
        self.done = done
        # The time at which the policy expires. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The name of the policy.
        self.name = name
        # The number of objects that are protected by the policy.
        self.object_count = object_count
        # The ID of the policy.
        self.policy_id = policy_id
        # The running rules of the policy.
        self.runtime_policies = runtime_policies
        # The time at which the policy takes effect. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The status of the policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: pending enabling
        # *   **2**: enabled
        # *   **3**: expired
        self.status = status
        # The type of the template that is used to create the policy. Valid values:
        # 
        # *   **promotion**: the Important Activity template
        # *   **bypass**: the Forward All template
        self.template = template

    def validate(self):
        if self.runtime_policies:
            for v1 in self.runtime_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.done is not None:
            result['Done'] = self.done

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.object_count is not None:
            result['ObjectCount'] = self.object_count

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        result['RuntimePolicies'] = []
        if self.runtime_policies is not None:
            for k1 in self.runtime_policies:
                result['RuntimePolicies'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        self.runtime_policies = []
        if m.get('RuntimePolicies') is not None:
            for k1 in m.get('RuntimePolicies'):
                temp_model = main_models.DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies()
                self.runtime_policies.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

class DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies(DaraModel):
    def __init__(
        self,
        new_value: str = None,
        policy_type: int = None,
        status: int = None,
        old_value: str = None,
    ):
        # The protection rule that is applied when the policy takes effect.
        # 
        # If you set **PolicyType** to **1**, the value is **{"cc_rule_enable": false }**. The value indicates that the Frequency Control policy is disabled.
        # 
        # If you set **PolicyType** to **2**, the value is **{"ai_rule_enable": 0}**. The value indicates that the Intelligent Protection policy is disabled.
        self.new_value = new_value
        # The protection policy whose status is changed when the policy takes effect. Valid values:
        # 
        # *   **1**: indicates that the Frequency Control policy is changed.
        # *   **2**: indicates that the Intelligent Protection policy is changed.
        self.policy_type = policy_type
        # The running status of the policy. Valid values:
        # 
        # *   **0**: The policy has not been issued or is restored.
        # *   **1**: The policy is pending.
        # *   **2**: The policy is being restored.
        # *   **3**: The policy takes effect.
        # *   **4**: The policy fails to take effect.
        # *   **5**:The policy fails to be restored.
        # *   **6**: The configurations of the protected objects for the policy does not exist because the configurations may be deleted.
        self.status = status
        # The protection rule that is applied before the policy takes effect.
        # 
        # If you set **PolicyType** to **1**, the value is **{"cc_rule_enable": true}**. The value indicates that the Frequency Control policy is enabled.
        # 
        # If you set **PolicyType** to **2**, the value is **{"ai_rule_enable": 1}**. The value indicates that the Intelligent Protection policy is enabled.
        self.old_value = old_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.status is not None:
            result['Status'] = self.status

        if self.old_value is not None:
            result['oldValue'] = self.old_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('oldValue') is not None:
            self.old_value = m.get('oldValue')

        return self

