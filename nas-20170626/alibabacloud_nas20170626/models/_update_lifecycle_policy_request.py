# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class UpdateLifecyclePolicyRequest(DaraModel):
    def __init__(
        self,
        delete_rules: List[main_models.UpdateLifecyclePolicyRequestDeleteRules] = None,
        description: str = None,
        file_system_id: str = None,
        lifecycle_policy_id: str = None,
        paths: List[str] = None,
        retrieve_rules: List[main_models.UpdateLifecyclePolicyRequestRetrieveRules] = None,
        storage_type: str = None,
        transit_rules: List[main_models.UpdateLifecyclePolicyRequestTransitRules] = None,
    ):
        # The file data expiration and deletion rules.
        self.delete_rules = delete_rules
        # The description of the lifecycle policy.
        # 
        # Format:
        # The description must be 3 to 64 characters in length, start with a letter, and can contain letters, digits, underscores (_), or hyphens (-).
        # > Only CPFS for Lingjun is supported.
        self.description = description
        # The file system ID. The ID starts with bmcpfs-, such as bmcpfs-290w65p03ok64ya****.
        # > This parameter is supported only when LifecyclePolicyType is set to OnDemand in the lifecycle management policy of a CPFS for Lingjun file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the lifecycle policy.
        # > This parameter is required for CPFS for Lingjun file systems.
        # 
        # This parameter is required.
        self.lifecycle_policy_id = lifecycle_policy_id
        # The absolute paths of the directories associated with the lifecycle management policy.
        self.paths = paths
        # The file data retrieval rules. You can configure up to one rule.
        # > Only CPFS for Lingjun file systems are supported.
        self.retrieve_rules = retrieve_rules
        # The tiered storage type.
        # 
        # Valid values:
        # - InfrequentAccess: IA storage class. This is the default value.
        # - Archive: Archive storage.
        self.storage_type = storage_type
        # The file data transit rules. You can configure up to one rule.
        # 
        # > This parameter is supported only when LifecyclePolicyType is set to Auto for a CPFS for Lingjun file system.
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

        if self.lifecycle_policy_id is not None:
            result['LifecyclePolicyId'] = self.lifecycle_policy_id

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
                temp_model = main_models.UpdateLifecyclePolicyRequestDeleteRules()
                self.delete_rules.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('LifecyclePolicyId') is not None:
            self.lifecycle_policy_id = m.get('LifecyclePolicyId')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        self.retrieve_rules = []
        if m.get('RetrieveRules') is not None:
            for k1 in m.get('RetrieveRules'):
                temp_model = main_models.UpdateLifecyclePolicyRequestRetrieveRules()
                self.retrieve_rules.append(temp_model.from_map(k1))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.transit_rules = []
        if m.get('TransitRules') is not None:
            for k1 in m.get('TransitRules'):
                temp_model = main_models.UpdateLifecyclePolicyRequestTransitRules()
                self.transit_rules.append(temp_model.from_map(k1))

        return self

class UpdateLifecyclePolicyRequestTransitRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The attribute of the rule.
        # 
        # Valid values:
        # - Atime: the access time of the file.
        self.attribute = attribute
        # The threshold of the rule.
        # 
        # Valid values:
        # - If Attribute is set to Atime, the value specifies the number of days since the file was last accessed. Valid values: 1 to 365.
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

class UpdateLifecyclePolicyRequestRetrieveRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The attribute of the rule.
        # 
        # Valid values:
        # - RetrieveType: the retrieval method.
        self.attribute = attribute
        # The threshold of the rule.
        # 
        # Valid values:
        # - RetrieveType
        #     - AfterVisit: supported when LifecyclePolicyType is set to Auto. Indicates best-effort recall on visit.
        #     - All: supported when LifecyclePolicyType is set to OnDemand. Indicates retrieval of all data.
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

class UpdateLifecyclePolicyRequestDeleteRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The attribute of the rule.
        # 
        # Valid values:
        # - Atime: the access time of the file.
        self.attribute = attribute
        # The threshold of the rule.
        # 
        # Valid values:
        # - If Attribute is set to Atime, the value specifies the number of days since the file was last accessed. Valid values: 1 to 365.
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

