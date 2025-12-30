# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchCustomLinesRequest(DaraModel):
    def __init__(
        self,
        create_timestamp_end: int = None,
        create_timestamp_start: int = None,
        creator: List[str] = None,
        ipv_4: str = None,
        lang: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        update_timestamp_end: int = None,
        update_timestamp_start: int = None,
    ):
        # The end of the time range during which the custom lines are created to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp_end = create_timestamp_end
        # The beginning of the time range during which the custom lines are created to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp_start = create_timestamp_start
        # The IDs of the creators for the custom lines.
        self.creator = creator
        # The IPv4 address.
        self.ipv_4 = ipv_4
        # The language.
        self.lang = lang
        # The name of the custom line.
        self.name = name
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **10**.
        self.page_size = page_size
        # The end of the time range during which the custom lines are updated to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp_end = update_timestamp_end
        # The beginning of the time range during which the custom lines are updated to query. Set the time to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp_start = update_timestamp_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp_end is not None:
            result['CreateTimestampEnd'] = self.create_timestamp_end

        if self.create_timestamp_start is not None:
            result['CreateTimestampStart'] = self.create_timestamp_start

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.update_timestamp_end is not None:
            result['UpdateTimestampEnd'] = self.update_timestamp_end

        if self.update_timestamp_start is not None:
            result['UpdateTimestampStart'] = self.update_timestamp_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestampEnd') is not None:
            self.create_timestamp_end = m.get('CreateTimestampEnd')

        if m.get('CreateTimestampStart') is not None:
            self.create_timestamp_start = m.get('CreateTimestampStart')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UpdateTimestampEnd') is not None:
            self.update_timestamp_end = m.get('UpdateTimestampEnd')

        if m.get('UpdateTimestampStart') is not None:
            self.update_timestamp_start = m.get('UpdateTimestampStart')

        return self

