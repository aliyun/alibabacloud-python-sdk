# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportAnalysisTagDetailByTaskIdRequest(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        category: str = None,
        task_id: str = None,
    ):
        self.categories = categories
        self.category = category
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['categories'] = self.categories

        if self.category is not None:
            result['category'] = self.category

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

