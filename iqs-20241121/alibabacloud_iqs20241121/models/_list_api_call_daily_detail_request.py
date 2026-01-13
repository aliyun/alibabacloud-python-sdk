# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiCallDailyDetailRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        end_time: str = None,
        engine_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        self.api_name = api_name
        self.end_time = end_time
        self.engine_type = engine_type
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
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

