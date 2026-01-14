# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetTrainTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        task_id_list_shrink: str = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.task_id_list_shrink = task_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id

        if self.task_id_list_shrink is not None:
            result['taskIdList'] = self.task_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')

        if m.get('taskIdList') is not None:
            self.task_id_list_shrink = m.get('taskIdList')

        return self

