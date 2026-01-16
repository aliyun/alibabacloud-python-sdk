# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiagnoseReportRequest(DaraModel):
    def __init__(
        self,
        detail: bool = None,
        end_time: int = None,
        lang: str = None,
        page: int = None,
        size: int = None,
        start_time: int = None,
        trigger: str = None,
    ):
        # SYSTEM
        self.detail = detail
        # 1
        # 
        # This parameter is required.
        self.end_time = end_time
        # 1594569600000
        self.lang = lang
        # 20
        self.page = page
        # true
        self.size = size
        # 1595174399999
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the request.
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['detail'] = self.detail

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.lang is not None:
            result['lang'] = self.lang

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.trigger is not None:
            result['trigger'] = self.trigger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')

        return self

