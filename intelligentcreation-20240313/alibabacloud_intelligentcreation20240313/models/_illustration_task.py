# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class IllustrationTask(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        illustration_ids: List[int] = None,
        illustration_task_id: int = None,
        task_status: str = None,
        text_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.illustration_ids = illustration_ids
        self.illustration_task_id = illustration_task_id
        self.task_status = task_status
        self.text_id = text_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.illustration_ids is not None:
            result['illustrationIds'] = self.illustration_ids

        if self.illustration_task_id is not None:
            result['illustrationTaskId'] = self.illustration_task_id

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        if self.text_id is not None:
            result['textId'] = self.text_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('illustrationIds') is not None:
            self.illustration_ids = m.get('illustrationIds')

        if m.get('illustrationTaskId') is not None:
            self.illustration_task_id = m.get('illustrationTaskId')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        if m.get('textId') is not None:
            self.text_id = m.get('textId')

        return self

