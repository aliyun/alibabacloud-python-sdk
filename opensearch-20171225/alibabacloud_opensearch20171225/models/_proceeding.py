# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class Proceeding(DaraModel):
    def __init__(
        self,
        detail: Dict[str, Any] = None,
        progress: float = None,
        status: str = None,
        sub_tasks: main_models.Proceeding = None,
        type: str = None,
    ):
        self.detail = detail
        self.progress = progress
        self.status = status
        self.sub_tasks = sub_tasks
        self.type = type

    def validate(self):
        if self.sub_tasks:
            self.sub_tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['detail'] = self.detail

        if self.progress is not None:
            result['progress'] = self.progress

        if self.status is not None:
            result['status'] = self.status

        if self.sub_tasks is not None:
            result['subTasks'] = self.sub_tasks.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subTasks') is not None:
            temp_model = main_models.Proceeding()
            self.sub_tasks = temp_model.from_map(m.get('subTasks'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

