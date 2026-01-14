# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class SubmitVLExtractionTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SubmitVLExtractionTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data structure.
        self.data = data
        # Request ID.
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.SubmitVLExtractionTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SubmitVLExtractionTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

