# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryReceiverByParamRequest(DaraModel):
    def __init__(
        self,
        key_word: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        # The keyword to search for recipient lists. If omitted, all recipient lists are returned.
        self.key_word = key_word
        self.owner_id = owner_id
        # This deprecated field is kept for backward compatibility. You can omit this parameter.
        # 
        # The page number.
        self.page_no = page_no
        # The page size. Default value: 100.
        # 
        # Omitting this parameter returns all results. However, because the PageNo parameter is deprecated, the effect of PageSize on pagination is limited.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This deprecated field is kept for backward compatibility. You can omit this parameter.
        # 
        # The list status. Valid values:
        # 
        # - 0: uploading
        # 
        # - 1: upload complete
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

