# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ChangeNodeTypesResponseBody(DaraModel):
    def __init__(
        self,
        node_response: List[main_models.ChangeNodeTypesResponseBodyNodeResponse] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.node_response = node_response
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        if self.node_response:
            for v1 in self.node_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeResponse'] = []
        if self.node_response is not None:
            for k1 in self.node_response:
                result['NodeResponse'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_response = []
        if m.get('NodeResponse') is not None:
            for k1 in m.get('NodeResponse'):
                temp_model = main_models.ChangeNodeTypesResponseBodyNodeResponse()
                self.node_response.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self



class ChangeNodeTypesResponseBodyNodeResponse(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        node_id: str = None,
    ):
        self.code = code
        self.message = message
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

