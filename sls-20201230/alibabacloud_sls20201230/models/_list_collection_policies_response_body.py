# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListCollectionPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        current_count: int = None,
        data: List[main_models.ListCollectionPoliciesResponseBodyData] = None,
        statistics: List[main_models.ListCollectionPoliciesResponseBodyStatistics] = None,
        total_count: int = None,
    ):
        self.current_count = current_count
        # The data of the policies that are matched against the query conditions. The data is returned based on paginated results.
        self.data = data
        self.statistics = statistics
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_count is not None:
            result['currentCount'] = self.current_count

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        result['statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['statistics'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentCount') is not None:
            self.current_count = m.get('currentCount')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListCollectionPoliciesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        self.statistics = []
        if m.get('statistics') is not None:
            for k1 in m.get('statistics'):
                temp_model = main_models.ListCollectionPoliciesResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListCollectionPoliciesResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        policy_source_list: List[main_models.ListCollectionPoliciesResponseBodyStatisticsPolicySourceList] = None,
        product_code: str = None,
    ):
        self.policy_source_list = policy_source_list
        self.product_code = product_code

    def validate(self):
        if self.policy_source_list:
            for v1 in self.policy_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['policySourceList'] = []
        if self.policy_source_list is not None:
            for k1 in self.policy_source_list:
                result['policySourceList'].append(k1.to_map() if k1 else None)

        if self.product_code is not None:
            result['productCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_source_list = []
        if m.get('policySourceList') is not None:
            for k1 in m.get('policySourceList'):
                temp_model = main_models.ListCollectionPoliciesResponseBodyStatisticsPolicySourceList()
                self.policy_source_list.append(temp_model.from_map(k1))

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        return self

class ListCollectionPoliciesResponseBodyStatisticsPolicySourceList(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_uid: str = None,
    ):
        self.policy_name = policy_name
        self.policy_uid = policy_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.policy_uid is not None:
            result['policyUid'] = self.policy_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyUid') is not None:
            self.policy_uid = m.get('policyUid')

        return self

class ListCollectionPoliciesResponseBodyData(DaraModel):
    def __init__(
        self,
        centralize_config: main_models.ListCollectionPoliciesResponseBodyDataCentralizeConfig = None,
        centralize_enabled: bool = None,
        data_code: str = None,
        data_config: main_models.ListCollectionPoliciesResponseBodyDataDataConfig = None,
        enabled: bool = None,
        internal_policy: bool = None,
        policy_config: main_models.ListCollectionPoliciesResponseBodyDataPolicyConfig = None,
        policy_name: str = None,
        policy_uid: str = None,
        product_code: str = None,
        resource_directory: main_models.ListCollectionPoliciesResponseBodyDataResourceDirectory = None,
    ):
        # The configuration for centralized storage.
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
            temp_model = main_models.ListCollectionPoliciesResponseBodyDataCentralizeConfig()
            self.centralize_config = temp_model.from_map(m.get('centralizeConfig'))

        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')

        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')

        if m.get('dataConfig') is not None:
            temp_model = main_models.ListCollectionPoliciesResponseBodyDataDataConfig()
            self.data_config = temp_model.from_map(m.get('dataConfig'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('internalPolicy') is not None:
            self.internal_policy = m.get('internalPolicy')

        if m.get('policyConfig') is not None:
            temp_model = main_models.ListCollectionPoliciesResponseBodyDataPolicyConfig()
            self.policy_config = temp_model.from_map(m.get('policyConfig'))

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyUid') is not None:
            self.policy_uid = m.get('policyUid')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('resourceDirectory') is not None:
            temp_model = main_models.ListCollectionPoliciesResponseBodyDataResourceDirectory()
            self.resource_directory = temp_model.from_map(m.get('resourceDirectory'))

        return self

class ListCollectionPoliciesResponseBodyDataResourceDirectory(DaraModel):
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

class ListCollectionPoliciesResponseBodyDataPolicyConfig(DaraModel):
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

class ListCollectionPoliciesResponseBodyDataDataConfig(DaraModel):
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

class ListCollectionPoliciesResponseBodyDataCentralizeConfig(DaraModel):
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
        # The data retention period for centralized storage. Unit: days.
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

