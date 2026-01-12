# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class DataJuicerConfig(DaraModel):
    def __init__(
        self,
        command_type: str = None,
        enable_resource_estimation: bool = None,
        execution_mode: str = None,
        resource_limit: main_models.ResourceLimit = None,
    ):
        self.command_type = command_type
        self.enable_resource_estimation = enable_resource_estimation
        self.execution_mode = execution_mode
        self.resource_limit = resource_limit

    def validate(self):
        if self.resource_limit:
            self.resource_limit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.enable_resource_estimation is not None:
            result['EnableResourceEstimation'] = self.enable_resource_estimation

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.resource_limit is not None:
            result['ResourceLimit'] = self.resource_limit.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('EnableResourceEstimation') is not None:
            self.enable_resource_estimation = m.get('EnableResourceEstimation')

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('ResourceLimit') is not None:
            temp_model = main_models.ResourceLimit()
            self.resource_limit = temp_model.from_map(m.get('ResourceLimit'))

        return self

