# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class UpdateTaskDTO(DaraModel):
    def __init__(
        self,
        exif: Dict[str, str] = None,
        remark: str = None,
        tags: List[str] = None,
        task_name: str = None,
    ):
        # Extended field
        self.exif = exif
        # Remark information
        self.remark = remark
        # List of labels
        self.tags = tags
        # Task Name
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exif is not None:
            result['Exif'] = self.exif

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

