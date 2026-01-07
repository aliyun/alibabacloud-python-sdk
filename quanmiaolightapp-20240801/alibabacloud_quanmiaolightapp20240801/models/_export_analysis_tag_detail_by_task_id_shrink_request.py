# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportAnalysisTagDetailByTaskIdShrinkRequest(DaraModel):
    def __init__(
        self,
        categories_shrink: str = None,
        category: str = None,
        task_id: str = None,
    ):
        self.categories_shrink = categories_shrink
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
        if self.categories_shrink is not None:
            result['categories'] = self.categories_shrink

        if self.category is not None:
            result['category'] = self.category

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories_shrink = m.get('categories')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

