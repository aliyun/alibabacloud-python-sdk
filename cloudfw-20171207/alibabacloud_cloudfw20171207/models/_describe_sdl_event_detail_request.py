# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSdlEventDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dst_ip: str = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        src_ip: str = None,
        start_time: int = None,
        uuid: str = None,
    ):
        self.current_page = current_page
        self.dst_ip = dst_ip
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.src_ip = src_ip
        self.start_time = start_time
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

