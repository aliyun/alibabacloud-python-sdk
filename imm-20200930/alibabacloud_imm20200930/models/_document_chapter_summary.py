# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DocumentChapterSummary(DaraModel):
    def __init__(
        self,
        data: List[main_models.ChapterSummary] = None,
        next_marker: int = None,
        version: str = None,
    ):
        self.data = data
        self.next_marker = next_marker
        self.version = version

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ChapterSummary()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

