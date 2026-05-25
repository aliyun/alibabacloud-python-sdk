# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchTlogRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        begin_date: int = None,
        device_id: str = None,
        end_date: int = None,
        keyword: str = None,
        level_json: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.begin_date = begin_date
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.end_date = end_date
        self.keyword = keyword
        self.level_json = level_json
        # This parameter is required.
        self.os = os
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.level_json is not None:
            result['LevelJson'] = self.level_json

        if self.os is not None:
            result['Os'] = self.os

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('LevelJson') is not None:
            self.level_json = m.get('LevelJson')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

