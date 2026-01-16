# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserSuppressionRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        end_bounce_time: int = None,
        end_create_time: int = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_bounce_time: int = None,
        start_create_time: int = None,
    ):
        # Email address or domain name
        self.address = address
        # End time of the last bounce hit, timestamp, accurate to the second. The span between start and end times cannot exceed 7 days.
        self.end_bounce_time = end_bounce_time
        # End creation time, timestamp, accurate to the second. The span between start and end times cannot exceed 7 days.
        self.end_create_time = end_create_time
        self.owner_id = owner_id
        # Current page number
        self.page_no = page_no
        # Page size
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time of the last bounce hit, timestamp, accurate to the second.
        self.start_bounce_time = start_bounce_time
        # Start creation time, timestamp, accurate to the second.
        self.start_create_time = start_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.end_bounce_time is not None:
            result['EndBounceTime'] = self.end_bounce_time

        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time

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

        if self.start_bounce_time is not None:
            result['StartBounceTime'] = self.start_bounce_time

        if self.start_create_time is not None:
            result['StartCreateTime'] = self.start_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('EndBounceTime') is not None:
            self.end_bounce_time = m.get('EndBounceTime')

        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')

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

        if m.get('StartBounceTime') is not None:
            self.start_bounce_time = m.get('StartBounceTime')

        if m.get('StartCreateTime') is not None:
            self.start_create_time = m.get('StartCreateTime')

        return self

