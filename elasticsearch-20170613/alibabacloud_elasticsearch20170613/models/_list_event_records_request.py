# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventRecordsRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        page: int = None,
        size: int = None,
        term_content: str = None,
        term_type: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.page = page
        self.size = size
        self.term_content = term_content
        self.term_type = term_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.term_content is not None:
            result['termContent'] = self.term_content

        if self.term_type is not None:
            result['termType'] = self.term_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('termContent') is not None:
            self.term_content = m.get('termContent')

        if m.get('termType') is not None:
            self.term_type = m.get('termType')

        return self

