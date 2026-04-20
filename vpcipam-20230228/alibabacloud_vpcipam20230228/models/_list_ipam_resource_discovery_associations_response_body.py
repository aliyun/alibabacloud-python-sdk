# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamResourceDiscoveryAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_resource_discovery_associations: List[main_models.ListIpamResourceDiscoveryAssociationsResponseBodyIpamResourceDiscoveryAssociations] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries on each page.
        self.count = count
        # The list of associations.
        self.ipam_resource_discovery_associations = ipam_resource_discovery_associations
        # The maximum number of entries on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If a value of **NextToken** is returned, it indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_resource_discovery_associations:
            for v1 in self.ipam_resource_discovery_associations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamResourceDiscoveryAssociations'] = []
        if self.ipam_resource_discovery_associations is not None:
            for k1 in self.ipam_resource_discovery_associations:
                result['IpamResourceDiscoveryAssociations'].append(k1.to_map() if k1 else None)

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

        self.ipam_resource_discovery_associations = []
        if m.get('IpamResourceDiscoveryAssociations') is not None:
            for k1 in m.get('IpamResourceDiscoveryAssociations'):
                temp_model = main_models.ListIpamResourceDiscoveryAssociationsResponseBodyIpamResourceDiscoveryAssociations()
                self.ipam_resource_discovery_associations.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamResourceDiscoveryAssociationsResponseBodyIpamResourceDiscoveryAssociations(DaraModel):
    def __init__(
        self,
        ipam_id: str = None,
        ipam_resource_discovery_id: str = None,
        ipam_resource_discovery_owner_id: str = None,
        ipam_resource_discovery_status: str = None,
        ipam_resource_discovery_type: str = None,
        status: str = None,
    ):
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The ID of resource discovery instance.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The ID of the Alibaba Cloud account to which the resource discovery belongs.
        self.ipam_resource_discovery_owner_id = ipam_resource_discovery_owner_id
        # The status of the resource discovery instance. Valid values:
        # 
        # *   **Creating**
        # *   **Created**
        # *   **Modifying**
        # *   **Deleting**
        # *   **Deleted**
        self.ipam_resource_discovery_status = ipam_resource_discovery_status
        # The type of resource discovery. Valid values:
        # 
        # *   **system**: default resource discovery created by the system.
        # *   **custom**: custom resource discovery created by users.
        self.ipam_resource_discovery_type = ipam_resource_discovery_type
        # The status of the associations. Valid values:
        # 
        # *   **Created**
        # *   **Deleted**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id

        if self.ipam_resource_discovery_owner_id is not None:
            result['IpamResourceDiscoveryOwnerId'] = self.ipam_resource_discovery_owner_id

        if self.ipam_resource_discovery_status is not None:
            result['IpamResourceDiscoveryStatus'] = self.ipam_resource_discovery_status

        if self.ipam_resource_discovery_type is not None:
            result['IpamResourceDiscoveryType'] = self.ipam_resource_discovery_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')

        if m.get('IpamResourceDiscoveryOwnerId') is not None:
            self.ipam_resource_discovery_owner_id = m.get('IpamResourceDiscoveryOwnerId')

        if m.get('IpamResourceDiscoveryStatus') is not None:
            self.ipam_resource_discovery_status = m.get('IpamResourceDiscoveryStatus')

        if m.get('IpamResourceDiscoveryType') is not None:
            self.ipam_resource_discovery_type = m.get('IpamResourceDiscoveryType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

