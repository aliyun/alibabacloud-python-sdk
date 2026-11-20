# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListXTelephonesRequest(DaraModel):
    def __init__(
        self,
        caller_parent_id: int = None,
        customer_pool_key: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        req_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The customer UID. This parameter is automatically obtained by the system and does not need to be specified.
        self.caller_parent_id = caller_parent_id
        # The number pool key.
        self.customer_pool_key = customer_pool_key
        self.owner_id = owner_id
        # The page number for the paged query. Paging starts from 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request deduplication ID. The maximum length is 20 characters. Ensure the atomicity of the request ID.
        # 
        # This parameter is required.
        self.req_id = req_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id

        if self.customer_pool_key is not None:
            result['CustomerPoolKey'] = self.customer_pool_key

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')

        if m.get('CustomerPoolKey') is not None:
            self.customer_pool_key = m.get('CustomerPoolKey')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

