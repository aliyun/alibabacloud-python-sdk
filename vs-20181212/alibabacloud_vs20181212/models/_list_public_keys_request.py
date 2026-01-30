# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublicKeysRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        key_group: str = None,
        key_name: str = None,
        key_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.key_group = key_group
        self.key_name = key_name
        self.key_type = key_type
        self.page_number = page_number
        self.page_size = page_size
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

        if self.key_group is not None:
            result['KeyGroup'] = self.key_group

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('KeyGroup') is not None:
            self.key_group = m.get('KeyGroup')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

