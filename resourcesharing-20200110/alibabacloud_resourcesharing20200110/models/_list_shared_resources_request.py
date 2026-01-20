# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSharedResourcesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_arns: List[str] = None,
        resource_ids: List[str] = None,
        resource_owner: str = None,
        resource_share_ids: List[str] = None,
        resource_type: str = None,
        target: str = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        self.resource_arns = resource_arns
        # The ID of a shared resource.
        self.resource_ids = resource_ids
        # The owner of the resource shares. Valid values:
        # 
        # *   Self: your account. If you set the value to Self, the resources you share with other accounts are queried.
        # *   OtherAccounts: another account. If you set the value to OtherAccounts, the resources other accounts share with you are queried.
        # 
        # This parameter is required.
        self.resource_owner = resource_owner
        # The ID of a resource share.
        self.resource_share_ids = resource_share_ids
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        self.resource_type = resource_type
        # The ID of the principal or resource owner.
        # 
        # *   If the value of `ResourceOwner` is `Self`, set this parameter to the ID of a principal.
        # *   If the value of `ResourceOwner` is `OtherAccounts`, set this parameter to the ID of a resource owner.
        self.target = target

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

        if self.resource_arns is not None:
            result['ResourceArns'] = self.resource_arns

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceArns') is not None:
            self.resource_arns = m.get('ResourceArns')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

