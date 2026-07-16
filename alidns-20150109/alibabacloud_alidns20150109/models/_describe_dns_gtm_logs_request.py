# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmLogsRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        instance_id: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
    ):
        # The end of the time range to query. This is a UNIX timestamp.
        self.end_timestamp = end_timestamp
        # The instance ID. Call the [DescribeDnsGtmInstances](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describednsgtminstances?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The keyword. The search is performed in the \\`%KeyWord%\\` pattern and is not case-sensitive.
        self.keyword = keyword
        # The language of some returned parameters. The default value is en. Valid values: en, zh, and ja.
        self.lang = lang
        # The page number. The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is 100. The default value is 20.
        self.page_size = page_size
        # The start of the time range to query. This is a UNIX timestamp.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

