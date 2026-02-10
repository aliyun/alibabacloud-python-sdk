# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHoneypotAttackerPortraitRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time_stamp: int = None,
        lang: str = None,
        page_size: int = None,
        src_ip: str = None,
        start_time_stamp: int = None,
    ):
        # The page number. Default value: **1**. Pages start from page 1.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp.
        self.end_time_stamp = end_time_stamp
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The source IP address of the attack.
        self.src_ip = src_ip
        # The beginning of the time range to query. The value is a UNIX timestamp.
        self.start_time_stamp = start_time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')

        return self

