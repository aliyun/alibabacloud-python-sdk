# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAssociatedResourceRulesRequest(DaraModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        setting_name: List[str] = None,
        status: str = None,
    ):
        # The number of entries to return on each page.
        # 
        # Default Value: 50. Maximum Value: 100.
        self.max_result = max_result
        # The token returned from a previous call to retrieve the next page of results.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The Region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The names of the associated resource rules.
        self.setting_name = setting_name
        # The status of the associated resource rules to query. Valid values:
        # 
        # - Enable: The rule is enabled.
        # 
        # - Disable: The rule is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.setting_name is not None:
            result['SettingName'] = self.setting_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('SettingName') is not None:
            self.setting_name = m.get('SettingName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

