# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomAudienceRequest(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        cust_space_id: str = None,
        description: str = None,
        file_path: str = None,
        name: str = None,
        owner_id: int = None,
        page_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        upload_type: str = None,
    ):
        # This parameter is required.
        self.ad_account_id = ad_account_id
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.description = description
        self.file_path = file_path
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        # This parameter is required.
        self.page_id = page_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self

