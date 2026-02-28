# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFeedbacksRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id_list: str = None,
    ):
        self.instance_id = instance_id
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id_list is not None:
            result['TaskIdList'] = self.task_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskIdList') is not None:
            self.task_id_list = m.get('TaskIdList')

        return self

