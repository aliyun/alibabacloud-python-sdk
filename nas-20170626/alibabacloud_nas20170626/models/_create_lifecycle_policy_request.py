# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateLifecyclePolicyRequest(DaraModel):
    def __init__(
        self,
        delete_rules: List[main_models.CreateLifecyclePolicyRequestDeleteRules] = None,
        description: str = None,
        file_system_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_policy_type: str = None,
        lifecycle_rule_name: str = None,
        path: str = None,
        paths: List[str] = None,
        retrieve_rules: List[main_models.CreateLifecyclePolicyRequestRetrieveRules] = None,
        storage_type: str = None,
        transit_rules: List[main_models.CreateLifecyclePolicyRequestTransitRules] = None,
    ):
        # The file data expiration and deletion rules. You can configure up to one rule.
        self.delete_rules = delete_rules
        # The lifecycle policy description.
        # 
        # Format:
        # The description must be 3 to 64 characters in length, start with a letter, and can contain letters, digits, underscores (_), or hyphens (-).
        # >Only CPFS for Lingjun is supported.
        self.description = description
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The lifecycle management policy name. The name must be 3 to 64 characters in length, start with an uppercase letter or lowercase letter, and can contain letters, digits, underscores (_), or hyphens (-).
        # 
        # >This parameter is required for General-purpose NAS but not required for CPFS for Lingjun.
        self.lifecycle_policy_name = lifecycle_policy_name
        # The policy type.
        # - Auto (default): automatic execution.
        # - OnDemand: on-demand execution.
        self.lifecycle_policy_type = lifecycle_policy_type
        # The management rule associated with the lifecycle management policy. Only General-purpose NAS is supported.
        # 
        # Valid values:
        # 
        # - DEFAULT_ATIME_14: files that have not been accessed for 14 days.
        # - DEFAULT_ATIME_30: files that have not been accessed for 30 days.
        # - DEFAULT_ATIME_60: files that have not been accessed for 60 days.
        # - DEFAULT_ATIME_90: files that have not been accessed for 90 days.
        # - DEFAULT_ATIME_180: files that have not been accessed for 180 days. DEFAULT_ATIME_180 is supported only when StorageType is set to Archive.
        # >- If an IA storage class policy has already been configured for the directory, the archive policy duration must be longer than the IA storage class policy duration.
        # > - Only General-purpose NAS supports this parameter.
        self.lifecycle_rule_name = lifecycle_rule_name
        # The absolute path of the directory associated with the lifecycle management policy. Only General-purpose NAS is supported.
        # 
        # - General-purpose NAS supports associating only a single directory. The path must start with a forward slash (/) and must be an existing path in the mount target.
        # 
        # > Only General-purpose NAS is supported. For General-purpose NAS, use Paths.N to associate multiple directories at the same time.
        # >- Only one of Path and Paths can be specified.
        self.path = path
        # The absolute paths of directories associated with the lifecycle management policy.
        self.paths = paths
        # The file data retrieval rules. You can configure up to one rule.
        # >Only CPFS for Lingjun file systems are supported.
        # 
        # >When LifecyclePolicyType is set to OnDemand, at least one of TransitRules or RetrieveRules must be specified.
        self.retrieve_rules = retrieve_rules
        # The storage tiering type.
        # - InfrequentAccess: IA storage class.
        # - Archive: Archive storage.
        # 
        # >General-purpose NAS supports InfrequentAccess and Archive. CPFS for Lingjun supports only InfrequentAccess.
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # The file data transit rules. You can configure up to one rule.
        # 
        # >This parameter is supported only when LifecyclePolicyType is set to Auto for CPFS for Lingjun file systems.
        self.transit_rules = transit_rules

    def validate(self):
        if self.delete_rules:
            for v1 in self.delete_rules:
                 if v1:
                    v1.validate()
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
        result['DeleteRules'] = []
        if self.delete_rules is not None:
            for k1 in self.delete_rules:
                result['DeleteRules'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

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
        self.delete_rules = []
        if m.get('DeleteRules') is not None:
            for k1 in m.get('DeleteRules'):
                temp_model = main_models.CreateLifecyclePolicyRequestDeleteRules()
                self.delete_rules.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

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
                temp_model = main_models.CreateLifecyclePolicyRequestRetrieveRules()
                self.retrieve_rules.append(temp_model.from_map(k1))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.transit_rules = []
        if m.get('TransitRules') is not None:
            for k1 in m.get('TransitRules'):
                temp_model = main_models.CreateLifecyclePolicyRequestTransitRules()
                self.transit_rules.append(temp_model.from_map(k1))

        return self

class CreateLifecyclePolicyRequestTransitRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The rule attribute.
        # 
        # Valid values:
        # - Atime: the access time of the file.
        self.attribute = attribute
        # The rule threshold.
        # 
        # Valid values:
        # - When Attribute is set to Atime, this parameter specifies the number of days that the file has not been accessed. Valid values: 0 to 365.
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

class CreateLifecyclePolicyRequestRetrieveRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The rule attribute. Valid values:
        # - RetrieveType: the retrieval method.
        self.attribute = attribute
        # The rule threshold. Valid values:
        # - RetrieveType
        #     - AfterVisit: supported when LifecyclePolicyType is set to Auto. Indicates best-effort recall on visit.
        #     - All: supported when LifecyclePolicyType is set to OnDemand. Indicates retrieving all data.
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

class CreateLifecyclePolicyRequestDeleteRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The rule attribute.
        # 
        # Valid values:
        # - Atime: the access time of the file.
        self.attribute = attribute
        # The rule threshold.
        # 
        # Valid values:
        # - When Attribute is set to Atime, this parameter specifies the number of days that the file has not been accessed. Valid values: 1 to 365.
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

