# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTransferFileDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        file_ids: List[str] = None,
        task_id: str = None,
    ):
        self.file_ids = file_ids
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

