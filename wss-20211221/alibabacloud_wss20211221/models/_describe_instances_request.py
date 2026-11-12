# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        no_resource_id: bool = None,
        property_key_list: List[str] = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        state_list: List[str] = None,
    ):
        # The list of sold instance IDs, which is used to specify the instances for this operation.
        self.instance_ids = instance_ids
        # The maximum number of records to return per query.
        self.max_results = max_results
        # The pagination token. Leave it empty for the first query. For subsequent queries, pass the NextToken value returned in the previous response as is. Do not construct or decode it yourself.
        self.next_token = next_token
        # Specifies whether to query only instances that are not associated with a business resource ID. Valid values:
        # - true: Queries only unassociated instances.
        # - false or empty: Does not filter by this condition.
        self.no_resource_id = no_resource_id
        # The list of instance property names to be filtered.
        self.property_key_list = property_key_list
        # The list of associated business resource IDs.
        self.resource_ids = resource_ids
        # The resource type. For example, CorePackage indicates a core-hour package. It must be consistent with the resource type of the target instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of instance statuses used for filtering. You can use NORMAL, DELETED, PENDING, and EXPIRED. ARCHIVED indicates the historical archived status.
        self.state_list = state_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.no_resource_id is not None:
            result['NoResourceId'] = self.no_resource_id

        if self.property_key_list is not None:
            result['PropertyKeyList'] = self.property_key_list

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.state_list is not None:
            result['StateList'] = self.state_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NoResourceId') is not None:
            self.no_resource_id = m.get('NoResourceId')

        if m.get('PropertyKeyList') is not None:
            self.property_key_list = m.get('PropertyKeyList')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StateList') is not None:
            self.state_list = m.get('StateList')

        return self

