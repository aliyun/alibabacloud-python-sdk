# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSharedTargetsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_owner: str = None,
        resource_share_ids: List[str] = None,
        resource_type: str = None,
        targets: List[str] = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        self.resource_arn = resource_arn
        # The ID of the shared resource.
        self.resource_id = resource_id
        # The owner of the resource share.
        # 
        # *   Self: your account. If you set the value to Self, the principals that are associated with your resource shares are queried.
        # *   OtherAccounts: another account. If you set the value to OtherAccounts, the resource shares with which your account is associated and the owners of the resource shares are queried.
        # 
        # This parameter is required.
        self.resource_owner = resource_owner
        # The ID of a resource share.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five resource shares can be specified at a time.
        self.resource_share_ids = resource_share_ids
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        self.resource_type = resource_type
        # The information about the principals.
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.targets is not None:
            result['Targets'] = self.targets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        return self

