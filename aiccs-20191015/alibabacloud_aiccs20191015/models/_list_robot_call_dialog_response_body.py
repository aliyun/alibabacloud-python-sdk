# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListRobotCallDialogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListRobotCallDialogResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRobotCallDialogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRobotCallDialogResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        node_type: str = None,
        role: str = None,
        tag: str = None,
        time: str = None,
    ):
        self.content = content
        self.node_type = node_type
        self.role = role
        self.tag = tag
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.role is not None:
            result['Role'] = self.role

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

