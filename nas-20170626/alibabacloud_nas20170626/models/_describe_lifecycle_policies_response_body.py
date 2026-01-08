# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeLifecyclePoliciesResponseBody(DaraModel):
    def __init__(
        self,
        lifecycle_policies: List[main_models.DescribeLifecyclePoliciesResponseBodyLifecyclePolicies] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried lifecycle policies.
        self.lifecycle_policies = lifecycle_policies
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of lifecycle policies.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_policies:
            for v1 in self.lifecycle_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LifecyclePolicies'] = []
        if self.lifecycle_policies is not None:
            for k1 in self.lifecycle_policies:
                result['LifecyclePolicies'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_policies = []
        if m.get('LifecyclePolicies') is not None:
            for k1 in m.get('LifecyclePolicies'):
                temp_model = main_models.DescribeLifecyclePoliciesResponseBodyLifecyclePolicies()
                self.lifecycle_policies.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLifecyclePoliciesResponseBodyLifecyclePolicies(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        lifecycle_policy_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_policy_type: str = None,
        lifecycle_rule_name: str = None,
        path: str = None,
        paths: List[str] = None,
        retrieve_rules: List[main_models.DescribeLifecyclePoliciesResponseBodyLifecyclePoliciesRetrieveRules] = None,
        storage_type: str = None,
        transit_rules: List[main_models.DescribeLifecyclePoliciesResponseBodyLifecyclePoliciesTransitRules] = None,
    ):
        # The time when the lifecycle policy was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        self.description = description
        # The ID of the file system.
        self.file_system_id = file_system_id
        self.lifecycle_policy_id = lifecycle_policy_id
        # The name of the lifecycle policy.
        self.lifecycle_policy_name = lifecycle_policy_name
        self.lifecycle_policy_type = lifecycle_policy_type
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name
        # The absolute path of a directory with which the lifecycle policy is associated.
        self.path = path
        # The absolute paths to multiple directories associated with the lifecycle policy.
        self.paths = paths
        self.retrieve_rules = retrieve_rules
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type
        self.transit_rules = transit_rules

    def validate(self):
        if self.retrieve_rules:
            for v1 in self.retrieve_rules:
                 if v1:
                    v1.validate()
        if self.transit_rules:
            for v1 in self.transit_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.lifecycle_policy_id is not None:
            result['LifecyclePolicyId'] = self.lifecycle_policy_id

        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name

        if self.lifecycle_policy_type is not None:
            result['LifecyclePolicyType'] = self.lifecycle_policy_type

        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name

        if self.path is not None:
            result['Path'] = self.path

        if self.paths is not None:
            result['Paths'] = self.paths

        result['RetrieveRules'] = []
        if self.retrieve_rules is not None:
            for k1 in self.retrieve_rules:
                result['RetrieveRules'].append(k1.to_map() if k1 else None)

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['TransitRules'] = []
        if self.transit_rules is not None:
            for k1 in self.transit_rules:
                result['TransitRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('LifecyclePolicyId') is not None:
            self.lifecycle_policy_id = m.get('LifecyclePolicyId')

        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')

        if m.get('LifecyclePolicyType') is not None:
            self.lifecycle_policy_type = m.get('LifecyclePolicyType')

        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        self.retrieve_rules = []
        if m.get('RetrieveRules') is not None:
            for k1 in m.get('RetrieveRules'):
                temp_model = main_models.DescribeLifecyclePoliciesResponseBodyLifecyclePoliciesRetrieveRules()
                self.retrieve_rules.append(temp_model.from_map(k1))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.transit_rules = []
        if m.get('TransitRules') is not None:
            for k1 in m.get('TransitRules'):
                temp_model = main_models.DescribeLifecyclePoliciesResponseBodyLifecyclePoliciesTransitRules()
                self.transit_rules.append(temp_model.from_map(k1))

        return self

class DescribeLifecyclePoliciesResponseBodyLifecyclePoliciesTransitRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        self.attribute = attribute
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeLifecyclePoliciesResponseBodyLifecyclePoliciesRetrieveRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        self.attribute = attribute
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

