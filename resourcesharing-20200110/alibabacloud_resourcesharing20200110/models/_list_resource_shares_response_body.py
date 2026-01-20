# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class ListResourceSharesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_shares: List[main_models.ListResourceSharesResponseBodyResourceShares] = None,
    ):
        # The `token` that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the resource shares.
        self.resource_shares = resource_shares

    def validate(self):
        if self.resource_shares:
            for v1 in self.resource_shares:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceShares'] = []
        if self.resource_shares is not None:
            for k1 in self.resource_shares:
                result['ResourceShares'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_shares = []
        if m.get('ResourceShares') is not None:
            for k1 in m.get('ResourceShares'):
                temp_model = main_models.ListResourceSharesResponseBodyResourceShares()
                self.resource_shares.append(temp_model.from_map(k1))

        return self

class ListResourceSharesResponseBodyResourceShares(DaraModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        create_time: str = None,
        resource_group_id: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        resource_share_status: str = None,
        tags: List[main_models.ListResourceSharesResponseBodyResourceSharesTags] = None,
        update_time: str = None,
    ):
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets
        # The time when the resource share was created.
        self.create_time = create_time
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The name of the resource share.
        self.resource_share_name = resource_share_name
        # The owner of the resource share.
        self.resource_share_owner = resource_share_owner
        # The status of the resource share. Valid values:
        # 
        # *   Active
        # *   Pending
        # *   Deleting
        # *   Deleted
        # 
        # >  The system automatically deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status
        # The tags.
        self.tags = tags
        # The time when the resource share was updated.
        self.update_time = update_time

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
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name

        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner

        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')

        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')

        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListResourceSharesResponseBodyResourceSharesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListResourceSharesResponseBodyResourceSharesTags(DaraModel):
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

