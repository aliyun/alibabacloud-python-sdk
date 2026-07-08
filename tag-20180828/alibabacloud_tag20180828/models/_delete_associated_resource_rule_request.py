# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAssociatedResourceRuleRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        setting_name: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The name of the associated resource tagging rule.
        # 
        # For more information, see the **Rule Name** column in [Resource types that support the Associated Resource Tagging feature](https://help.aliyun.com/document_detail/2586330.html).
        self.setting_name = setting_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

