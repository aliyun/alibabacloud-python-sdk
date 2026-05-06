# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MergeDownloadRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        sub_task_ids: str = None,
    ):
        self.lang = lang
        self.reg_id = reg_id
        self.sub_task_ids = sub_task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.sub_task_ids is not None:
            result['SubTaskIds'] = self.sub_task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SubTaskIds') is not None:
            self.sub_task_ids = m.get('SubTaskIds')

        return self

