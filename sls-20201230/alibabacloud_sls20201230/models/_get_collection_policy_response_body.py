# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetCollectionPolicyResponseBody(DaraModel):
    def __init__(
        self,
        collection_policy: main_models.GetCollectionPolicyResponseBodyCollectionPolicy = None,
    ):
        self.collection_policy = collection_policy

    def validate(self):
        if self.collection_policy:
            self.collection_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_policy is not None:
            result['collectionPolicy'] = self.collection_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectionPolicy') is not None:
            temp_model = main_models.GetCollectionPolicyResponseBodyCollectionPolicy()
            self.collection_policy = temp_model.from_map(m.get('collectionPolicy'))

        return self

class GetCollectionPolicyResponseBodyCollectionPolicy(DaraModel):
    def __init__(
        self,
        centralize_config: main_models.GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig = None,
        centralize_enabled: bool = None,
        data_code: str = None,
        data_config: main_models.GetCollectionPolicyResponseBodyCollectionPolicyDataConfig = None,
        enabled: bool = None,
        internal_policy: bool = None,
        policy_config: main_models.GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig = None,
        policy_name: str = None,
        policy_uid: str = None,
        product_code: str = None,
        resource_directory: main_models.GetCollectionPolicyResponseBodyCollectionPolicyResourceDirectory = None,
    ):
        self.centralize_config = centralize_config
        self.centralize_enabled = centralize_enabled
        self.data_code = data_code
        self.data_config = data_config
        self.enabled = enabled
        self.internal_policy = internal_policy
        self.policy_config = policy_config
        self.policy_name = policy_name
        self.policy_uid = policy_uid
        self.product_code = product_code
        self.resource_directory = resource_directory

    def validate(self):
        if self.centralize_config:
            self.centralize_config.validate()
        if self.data_config:
            self.data_config.validate()
        if self.policy_config:
            self.policy_config.validate()
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()

        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled

        if self.data_code is not None:
            result['dataCode'] = self.data_code

        if self.data_config is not None:
            result['dataConfig'] = self.data_config.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.internal_policy is not None:
            result['internalPolicy'] = self.internal_policy

        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.policy_uid is not None:
            result['policyUid'] = self.policy_uid

        if self.product_code is not None:
            result['productCode'] = self.product_code

        if self.resource_directory is not None:
            result['resourceDirectory'] = self.resource_directory.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centralizeConfig') is not None:
            temp_model = main_models.GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig()
            self.centralize_config = temp_model.from_map(m.get('centralizeConfig'))

        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')

        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')

        if m.get('dataConfig') is not None:
            temp_model = main_models.GetCollectionPolicyResponseBodyCollectionPolicyDataConfig()
            self.data_config = temp_model.from_map(m.get('dataConfig'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('internalPolicy') is not None:
            self.internal_policy = m.get('internalPolicy')

        if m.get('policyConfig') is not None:
            temp_model = main_models.GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig()
            self.policy_config = temp_model.from_map(m.get('policyConfig'))

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyUid') is not None:
            self.policy_uid = m.get('policyUid')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('resourceDirectory') is not None:
            temp_model = main_models.GetCollectionPolicyResponseBodyCollectionPolicyResourceDirectory()
            self.resource_directory = temp_model.from_map(m.get('resourceDirectory'))

        return self

class GetCollectionPolicyResponseBodyCollectionPolicyResourceDirectory(DaraModel):
    def __init__(
        self,
        account_group_type: str = None,
        members: List[str] = None,
    ):
        self.account_group_type = account_group_type
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_group_type is not None:
            result['accountGroupType'] = self.account_group_type

        if self.members is not None:
            result['members'] = self.members

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountGroupType') is not None:
            self.account_group_type = m.get('accountGroupType')

        if m.get('members') is not None:
            self.members = m.get('members')

        return self

class GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        regions: List[str] = None,
        resource_mode: str = None,
        resource_tags: Dict[str, Any] = None,
    ):
        self.instance_ids = instance_ids
        self.regions = regions
        self.resource_mode = resource_mode
        self.resource_tags = resource_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        if self.regions is not None:
            result['regions'] = self.regions

        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode

        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        if m.get('regions') is not None:
            self.regions = m.get('regions')

        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')

        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')

        return self

class GetCollectionPolicyResponseBodyCollectionPolicyDataConfig(DaraModel):
    def __init__(
        self,
        data_project: str = None,
        data_region: str = None,
    ):
        self.data_project = data_project
        self.data_region = data_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_project is not None:
            result['dataProject'] = self.data_project

        if self.data_region is not None:
            result['dataRegion'] = self.data_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataProject') is not None:
            self.data_project = m.get('dataProject')

        if m.get('dataRegion') is not None:
            self.data_region = m.get('dataRegion')

        return self

class GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig(DaraModel):
    def __init__(
        self,
        dest_logstore: str = None,
        dest_project: str = None,
        dest_region: str = None,
        dest_ttl: int = None,
    ):
        self.dest_logstore = dest_logstore
        self.dest_project = dest_project
        self.dest_region = dest_region
        self.dest_ttl = dest_ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore

        if self.dest_project is not None:
            result['destProject'] = self.dest_project

        if self.dest_region is not None:
            result['destRegion'] = self.dest_region

        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')

        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')

        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')

        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')

        return self

