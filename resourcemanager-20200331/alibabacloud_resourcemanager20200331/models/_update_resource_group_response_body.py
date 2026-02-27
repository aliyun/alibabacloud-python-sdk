# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class UpdateResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: main_models.UpdateResourceGroupResponseBodyResourceGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource group.
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroup') is not None:
            temp_model = main_models.UpdateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m.get('ResourceGroup'))

        return self

class UpdateResourceGroupResponseBodyResourceGroup(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name

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

        return self

