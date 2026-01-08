# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingDestinationCategoryRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        dst_type: str = None,
        end_time: str = None,
        lang: str = None,
        source_ip: str = None,
        start_time: str = None,
        type_id: str = None,
    ):
        self.category_id = category_id
        self.dst_type = dst_type
        # This parameter is required.
        self.end_time = end_time
        self.lang = lang
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time
        self.type_id = type_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type_id is not None:
            result['TypeId'] = self.type_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')

        return self

