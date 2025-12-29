# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUsageStatisticsByTagIdRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_id: int = None,
    ):
        # The beginning of the time range to query.
        self.begin_time = begin_time
        # The end of the time range to query.
        self.end_time = end_time
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag ID.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

