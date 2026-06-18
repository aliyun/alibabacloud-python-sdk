# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListRobotNodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListRobotNodeResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Request status code. A return value of OK indicates that the request succeeded.
        self.code = code
        # List of robot nodes.
        self.data = data
        # Description of the status code.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Whether the API invocation succeeded. Valid values:
        # - **true**: Succeeded.
        # - **false**: Failed.
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
                temp_model = main_models.ListRobotNodeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRobotNodeResponseBodyData(DaraModel):
    def __init__(
        self,
        is_output: int = None,
        model_name: str = None,
        node_identifier: str = None,
        node_name: str = None,
        process_name: str = None,
    ):
        # Whether it is an output. Valid values:
        # 
        # - **1**: Yes.
        # - **0**: No.
        self.is_output = is_output
        # Model name.
        self.model_name = model_name
        # Output ID.
        self.node_identifier = node_identifier
        # Node name.
        self.node_name = node_name
        # Flow name.
        self.process_name = process_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_output is not None:
            result['IsOutput'] = self.is_output

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.node_identifier is not None:
            result['NodeIdentifier'] = self.node_identifier

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOutput') is not None:
            self.is_output = m.get('IsOutput')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('NodeIdentifier') is not None:
            self.node_identifier = m.get('NodeIdentifier')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        return self

