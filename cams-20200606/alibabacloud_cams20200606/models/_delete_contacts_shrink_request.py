# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContactsShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        contact_details: str = None,
        contact_name: str = None,
        country: str = None,
        file_path: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_code = biz_code
        self.biz_extend_shrink = biz_extend_shrink
        self.contact_details = contact_details
        self.contact_name = contact_name
        self.country = country
        self.file_path = file_path
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

        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink

        if self.contact_details is not None:
            result['ContactDetails'] = self.contact_details

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.country is not None:
            result['Country'] = self.country

        if self.file_path is not None:
            result['FilePath'] = self.file_path

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
            self.biz_extend_shrink = m.get('BizExtend')

        if m.get('ContactDetails') is not None:
            self.contact_details = m.get('ContactDetails')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

