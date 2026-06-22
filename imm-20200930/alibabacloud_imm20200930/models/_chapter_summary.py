# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ChapterSummary(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        summary: List[main_models.Summary] = None,
        time_range: List[int] = None,
        title: str = None,
        title_id: str = None,
    ):
        self.page_number = page_number
        self.summary = summary
        self.time_range = time_range
        self.title = title
        self.title_id = title_id

    def validate(self):
        if self.summary:
            for v1 in self.summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        result['Summary'] = []
        if self.summary is not None:
            for k1 in self.summary:
                result['Summary'].append(k1.to_map() if k1 else None)

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        if self.title is not None:
            result['Title'] = self.title

        if self.title_id is not None:
            result['TitleID'] = self.title_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        self.summary = []
        if m.get('Summary') is not None:
            for k1 in m.get('Summary'):
                temp_model = main_models.Summary()
                self.summary.append(temp_model.from_map(k1))

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TitleID') is not None:
            self.title_id = m.get('TitleID')

        return self

