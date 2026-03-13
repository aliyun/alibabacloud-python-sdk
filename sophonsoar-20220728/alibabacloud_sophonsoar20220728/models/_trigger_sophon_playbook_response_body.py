# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class TriggerSophonPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TriggerSophonPlaybookResponseBodyData = None,
        request_id: str = None,
    ):
        # The details that is returned after the command or playbook is triggered.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TriggerSophonPlaybookResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TriggerSophonPlaybookResponseBodyData(DaraModel):
    def __init__(
        self,
        sophon_task_id: str = None,
    ):
        # The custom ID. If you do not specify this parameter when the playbook is triggered, a random ID is generated for fault locating and troubleshooting.
        self.sophon_task_id = sophon_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')

        return self

