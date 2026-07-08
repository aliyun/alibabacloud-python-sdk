# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAssociatedResourceRuleRequest(DaraModel):
    def __init__(
        self,
        existing_status: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        setting_name: str = None,
        status: str = None,
        tag_keys: List[str] = None,
    ):
        self.existing_status = existing_status
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The name of the Associated Resource Tag Rule setting.
        # 
        # For valid values, see the **Setting Name** column in [Resources that support the Associated Resource Tag Rule feature](https://help.aliyun.com/document_detail/2586330.html).
        # 
        # This parameter is required.
        self.setting_name = setting_name
        # The status of the Associated Resource Tag Rule. Valid values:
        # 
        # - Enable: The rule is enabled.
        # 
        # - Disable: The rule is disabled.
        self.status = status
        # A list of tag keys for the Associated Resource Tag Rule.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.existing_status is not None:
            result['ExistingStatus'] = self.existing_status

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

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistingStatus') is not None:
            self.existing_status = m.get('ExistingStatus')

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

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

