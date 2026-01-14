# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class IsCompletedResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.IsCompletedResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
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
            temp_model = main_models.IsCompletedResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class IsCompletedResponseBodyData(DaraModel):
    def __init__(
        self,
        modified_time: int = None,
        task_key: str = None,
        task_short_result: str = None,
        task_status: str = None,
    ):
        # Modified time in milliseconds, e.g. 1711438780000.
        self.modified_time = modified_time
        # The unique key of this generation task.
        self.task_key = task_key
        # Unused temporarily.
        self.task_short_result = task_short_result
        # The status of the report generation task. The possible values are `running`, `success`, and `error`, which mean generating, generating succeeded, and generating failed, respectively. If you encounter a result generation failure, check the model, correct the model, and then generate the result again.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.task_key is not None:
            result['taskKey'] = self.task_key

        if self.task_short_result is not None:
            result['taskShortResult'] = self.task_short_result

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('taskKey') is not None:
            self.task_key = m.get('taskKey')

        if m.get('taskShortResult') is not None:
            self.task_short_result = m.get('taskShortResult')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

