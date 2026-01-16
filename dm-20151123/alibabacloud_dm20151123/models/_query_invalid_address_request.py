# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInvalidAddressRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        key_word: str = None,
        length: int = None,
        next_start: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # End time, with a span from the start time that cannot exceed 30 days, in the format yyyy-MM-dd.
        self.end_time = end_time
        # Keyword. If not provided, it represents all invalid addresses.
        self.key_word = key_word
        # Number of items per request.
        self.length = length
        # Request starting position.
        self.next_start = next_start
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time, which cannot be earlier than 30 days ago, in the format yyyy-MM-dd.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.length is not None:
            result['Length'] = self.length

        if self.next_start is not None:
            result['NextStart'] = self.next_start

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

