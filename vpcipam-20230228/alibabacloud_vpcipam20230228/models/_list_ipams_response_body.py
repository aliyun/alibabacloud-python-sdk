# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipams: List[main_models.ListIpamsResponseBodyIpams] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IPAMs.
        self.ipams = ipams
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries.
        self.total_count = total_count

    def validate(self):
        if self.ipams:
            for v1 in self.ipams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Ipams'] = []
        if self.ipams is not None:
            for k1 in self.ipams:
                result['Ipams'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ipams = []
        if m.get('Ipams') is not None:
            for k1 in m.get('Ipams'):
                temp_model = main_models.ListIpamsResponseBodyIpams()
                self.ipams.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamsResponseBodyIpams(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_resource_discovery_association_id: str = None,
        default_resource_discovery_id: str = None,
        ipam_description: str = None,
        ipam_id: str = None,
        ipam_name: str = None,
        ipam_status: str = None,
        operating_region_list: List[str] = None,
        owner_id: int = None,
        private_default_scope_id: str = None,
        public_default_scope_id: str = None,
        region_id: str = None,
        resource_discovery_association_count: int = None,
        resource_group_id: str = None,
        scope_count: int = None,
        tags: List[main_models.ListIpamsResponseBodyIpamsTags] = None,
    ):
        # The time when the IPAM was created.
        self.create_time = create_time
        # Default resource discovery association ID.
        self.default_resource_discovery_association_id = default_resource_discovery_association_id
        # Default resource discovery instance ID.
        self.default_resource_discovery_id = default_resource_discovery_id
        # The description of the IPAM.
        self.ipam_description = ipam_description
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The name of the IPAM.
        self.ipam_name = ipam_name
        # The status of the IPAM. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Deleting**
        # *   **Deleted**
        self.ipam_status = ipam_status
        # The effective regions of the IPAM.
        self.operating_region_list = operating_region_list
        # The Alibaba Cloud account that owns the IPAM.
        self.owner_id = owner_id
        # The default private scope created by the system after the IPAM is created.
        self.private_default_scope_id = private_default_scope_id
        # The default public scope created by the system after the IPAM is created.
        self.public_default_scope_id = public_default_scope_id
        # The region ID of the IPAM.
        self.region_id = region_id
        # Number of resource discovery associations.
        self.resource_discovery_association_count = resource_discovery_association_count
        # The resource group ID of the IPAM.
        self.resource_group_id = resource_group_id
        # The number of IPAM scopes. Value: **2 to 5**.
        self.scope_count = scope_count
        # The tag list.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_resource_discovery_association_id is not None:
            result['DefaultResourceDiscoveryAssociationId'] = self.default_resource_discovery_association_id

        if self.default_resource_discovery_id is not None:
            result['DefaultResourceDiscoveryId'] = self.default_resource_discovery_id

        if self.ipam_description is not None:
            result['IpamDescription'] = self.ipam_description

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_name is not None:
            result['IpamName'] = self.ipam_name

        if self.ipam_status is not None:
            result['IpamStatus'] = self.ipam_status

        if self.operating_region_list is not None:
            result['OperatingRegionList'] = self.operating_region_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_default_scope_id is not None:
            result['PrivateDefaultScopeId'] = self.private_default_scope_id

        if self.public_default_scope_id is not None:
            result['PublicDefaultScopeId'] = self.public_default_scope_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_discovery_association_count is not None:
            result['ResourceDiscoveryAssociationCount'] = self.resource_discovery_association_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scope_count is not None:
            result['ScopeCount'] = self.scope_count

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultResourceDiscoveryAssociationId') is not None:
            self.default_resource_discovery_association_id = m.get('DefaultResourceDiscoveryAssociationId')

        if m.get('DefaultResourceDiscoveryId') is not None:
            self.default_resource_discovery_id = m.get('DefaultResourceDiscoveryId')

        if m.get('IpamDescription') is not None:
            self.ipam_description = m.get('IpamDescription')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamName') is not None:
            self.ipam_name = m.get('IpamName')

        if m.get('IpamStatus') is not None:
            self.ipam_status = m.get('IpamStatus')

        if m.get('OperatingRegionList') is not None:
            self.operating_region_list = m.get('OperatingRegionList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateDefaultScopeId') is not None:
            self.private_default_scope_id = m.get('PrivateDefaultScopeId')

        if m.get('PublicDefaultScopeId') is not None:
            self.public_default_scope_id = m.get('PublicDefaultScopeId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDiscoveryAssociationCount') is not None:
            self.resource_discovery_association_count = m.get('ResourceDiscoveryAssociationCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScopeCount') is not None:
            self.scope_count = m.get('ScopeCount')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListIpamsResponseBodyIpamsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListIpamsResponseBodyIpamsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

