# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class ListResourceSharesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        permission_name: str = None,
        resource_group_id: str = None,
        resource_owner: str = None,
        resource_share_ids: List[str] = None,
        resource_share_name: str = None,
        resource_share_status: str = None,
        tag: List[main_models.ListResourceSharesRequestTag] = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The `token` that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The information about the permissions. For more information, see [Permission library](https://help.aliyun.com/document_detail/465474.html).
        self.permission_name = permission_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The owner of the resource shares. Valid values:
        # 
        # *   Self: the current account
        # *   OtherAccounts: an account other than the current account
        # 
        # This parameter is required.
        self.resource_owner = resource_owner
        # The IDs of the resource shares.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five resource shares can be specified at a time.
        self.resource_share_ids = resource_share_ids
        # The name of the resource share.
        self.resource_share_name = resource_share_name
        # The status of the resource shares. Valid values:
        # 
        # *   Active
        # *   Pending
        # *   Deleting
        # *   Deleted
        # 
        # >  The system automatically deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids

        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name

        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')

        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')

        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListResourceSharesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListResourceSharesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  The tag key can be 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # >  The tag value can be 128 characters in length and cannot start with `acs:`. The tag value cannot contain `http://` or `https://`.
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

