# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class MoveContactToGroupRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        contacts: str = None,
        link_exist_groups: str = None,
        link_new_groups: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_code = biz_code
        self.biz_extend = biz_extend
        # This parameter is required.
        self.contacts = contacts
        self.link_exist_groups = link_exist_groups
        self.link_new_groups = link_new_groups
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend

        if self.contacts is not None:
            result['Contacts'] = self.contacts

        if self.link_exist_groups is not None:
            result['LinkExistGroups'] = self.link_exist_groups

        if self.link_new_groups is not None:
            result['LinkNewGroups'] = self.link_new_groups

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')

        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')

        if m.get('LinkExistGroups') is not None:
            self.link_exist_groups = m.get('LinkExistGroups')

        if m.get('LinkNewGroups') is not None:
            self.link_new_groups = m.get('LinkNewGroups')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

