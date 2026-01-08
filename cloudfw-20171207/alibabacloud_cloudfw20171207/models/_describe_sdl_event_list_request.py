# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSdlEventListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dst_ip: str = None,
        end_time: int = None,
        lang: str = None,
        location: str = None,
        only_ai_evt: int = None,
        order: str = None,
        page_size: int = None,
        sensitive_level: str = None,
        sort: str = None,
        src_ip: str = None,
        start_time: int = None,
        uuid: str = None,
    ):
        self.current_page = current_page
        self.dst_ip = dst_ip
        self.end_time = end_time
        self.lang = lang
        self.location = location
        self.only_ai_evt = only_ai_evt
        self.order = order
        self.page_size = page_size
        self.sensitive_level = sensitive_level
        self.sort = sort
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

        if self.location is not None:
            result['Location'] = self.location

        if self.only_ai_evt is not None:
            result['OnlyAiEvt'] = self.only_ai_evt

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sort is not None:
            result['Sort'] = self.sort

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

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('OnlyAiEvt') is not None:
            self.only_ai_evt = m.get('OnlyAiEvt')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

