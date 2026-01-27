# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class OperateNodeRequest(DaraModel):
    def __init__(
        self,
        operation: str = None,
        operation_parameters: main_models.NodeOperationParameters = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.operation = operation
        self.operation_parameters = operation_parameters
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.operation_parameters:
            self.operation_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['Operation'] = self.operation

        if self.operation_parameters is not None:
            result['OperationParameters'] = self.operation_parameters.to_map()

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('OperationParameters') is not None:
            temp_model = main_models.NodeOperationParameters()
            self.operation_parameters = temp_model.from_map(m.get('OperationParameters'))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

