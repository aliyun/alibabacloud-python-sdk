# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class AttachRCInstancesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        responses: List[main_models.AttachRCInstancesResponseBodyResponses] = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.responses = responses
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.responses:
            for v1 in self.responses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Responses'] = []
        if self.responses is not None:
            for k1 in self.responses:
                result['Responses'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.responses = []
        if m.get('Responses') is not None:
            for k1 in m.get('Responses'):
                temp_model = main_models.AttachRCInstancesResponseBodyResponses()
                self.responses.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class AttachRCInstancesResponseBodyResponses(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The node ID.
        self.instance_id = instance_id
        # The message returned.
        # 
        # >  If the request is successful, **Successful** is returned. If the request fails, an error message that contains information such as an error code is returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

