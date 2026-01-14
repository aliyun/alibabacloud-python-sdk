# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ExecuteMigrationOperationRequest(DaraModel):
    def __init__(
        self,
        operation_param: main_models.ExecuteMigrationOperationRequestOperationParam = None,
        instance_id: str = None,
    ):
        self.operation_param = operation_param
        self.instance_id = instance_id

    def validate(self):
        if self.operation_param:
            self.operation_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_param is not None:
            result['operationParam'] = self.operation_param.to_map()

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationParam') is not None:
            temp_model = main_models.ExecuteMigrationOperationRequestOperationParam()
            self.operation_param = temp_model.from_map(m.get('operationParam'))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

class ExecuteMigrationOperationRequestOperationParam(DaraModel):
    def __init__(
        self,
        param_data: Any = None,
    ):
        self.param_data = param_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_data is not None:
            result['paramData'] = self.param_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramData') is not None:
            self.param_data = m.get('paramData')

        return self

