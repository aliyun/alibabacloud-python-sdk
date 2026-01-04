# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetVpcPrefixListAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        next_token: str = None,
        prefix_list_association: List[main_models.GetVpcPrefixListAssociationsResponseBodyPrefixListAssociation] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries.
        self.count = count
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is used to retrieve a new page of results.
        self.next_token = next_token
        # The information about the network instances that are associated with the prefix list.
        self.prefix_list_association = prefix_list_association
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.prefix_list_association:
            for v1 in self.prefix_list_association:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PrefixListAssociation'] = []
        if self.prefix_list_association is not None:
            for k1 in self.prefix_list_association:
                result['PrefixListAssociation'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.prefix_list_association = []
        if m.get('PrefixListAssociation') is not None:
            for k1 in m.get('PrefixListAssociation'):
                temp_model = main_models.GetVpcPrefixListAssociationsResponseBodyPrefixListAssociation()
                self.prefix_list_association.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetVpcPrefixListAssociationsResponseBodyPrefixListAssociation(DaraModel):
    def __init__(
        self,
        cidr_list: str = None,
        owner_id: str = None,
        prefix_list_id: str = None,
        reason: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_uid: str = None,
        status: str = None,
    ):
        # List of CIDR addresses where the prefix list is effective in the currently associated resources.
        self.cidr_list = cidr_list
        # The ID of the Alibaba Cloud account to which the prefix list belongs.
        self.owner_id = owner_id
        # The prefix list ID.
        self.prefix_list_id = prefix_list_id
        # The reason why the association failed.
        self.reason = reason
        # The region ID of the prefix list.
        self.region_id = region_id
        # The ID of the associated resource.
        self.resource_id = resource_id
        # The type of the associated resource. Valid values:
        # 
        # *   **vpcRouteTable**: virtual private cloud (VPC) route table.
        # *   **trRouteTable**: route table of a transit router.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud account to which the resource associated with the prefix list belongs.
        self.resource_uid = resource_uid
        # The status of the prefix list. Valid values:
        # 
        # *   **Created**
        # *   **ModifyFailed**
        # *   **Creating**
        # *   **Modifying**
        # *   **Deleting**
        # *   **Deleted**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

