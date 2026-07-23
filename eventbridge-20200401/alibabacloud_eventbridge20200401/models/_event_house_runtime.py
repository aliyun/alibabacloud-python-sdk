# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EventHouseRuntime(DaraModel):
    def __init__(
        self,
        cu: int = None,
        error_code: str = None,
        error_message: str = None,
        name: str = None,
        progress: int = None,
        stage: str = None,
        status: str = None,
        target_cu: int = None,
    ):
        # The number of CUs that last took effect for the EventHouse Runtime.
        self.cu = cu
        # The stable error code returned when the creation or specification change operation fails.
        self.error_code = error_code
        # The desensitized error message returned when the creation or specification change operation fails.
        self.error_message = error_message
        # The name of the EventHouse Runtime. Typically set to default in the initial phase.
        self.name = name
        # The progress of the current creation or specification change operation. Valid values: 0 to 100.
        self.progress = progress
        # The current stage of the creation or specification change operation.
        self.stage = stage
        # The current status of the EventHouse Runtime. RUNNING indicates that the Runtime is ready and can accept queries. Valid values: CREATING, RUNNING, UPDATING, RECOVERING, CLOSED, CREATE_FAILED, and UPDATE_FAILED.
        self.status = status
        # The target number of CUs during creation, specification change, or the corresponding failed state. This parameter is not returned when the Runtime is running stably.
        self.target_cu = target_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.name is not None:
            result['Name'] = self.name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.status is not None:
            result['Status'] = self.status

        if self.target_cu is not None:
            result['TargetCu'] = self.target_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetCu') is not None:
            self.target_cu = m.get('TargetCu')

        return self

