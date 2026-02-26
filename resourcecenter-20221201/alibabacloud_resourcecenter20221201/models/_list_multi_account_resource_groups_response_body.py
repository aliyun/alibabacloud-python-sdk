# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListMultiAccountResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_groups: List[main_models.ListMultiAccountResourceGroupsResponseBodyResourceGroups] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resource groups.
        self.resource_groups = resource_groups

    def validate(self):
        if self.resource_groups:
            for v1 in self.resource_groups:
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

        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.ListMultiAccountResourceGroupsResponseBodyResourceGroups()
                self.resource_groups.append(temp_model.from_map(k1))

        return self

class ListMultiAccountResourceGroupsResponseBodyResourceGroups(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
    ):
        # The ID of the management account or a member in the resource directory.
        self.account_id = account_id
        # The time when the resource group was created.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The resource group ID.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        # The status of the resource group.
        # 
        # - Creating: The resource group is being created.
        # 
        # - OK: The resource group is created.
        # 
        # - PendingDelete: The resource group is pending deletion.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

