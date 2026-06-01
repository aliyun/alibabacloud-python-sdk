# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetUnknownThreatDetectStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetUnknownThreatDetectStatisticResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetUnknownThreatDetectStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetUnknownThreatDetectStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        block_event_machine_count: int = None,
        block_machine_count: int = None,
        machine_count: int = None,
        monitor_machine_count: int = None,
        open_machine_count: int = None,
        studying_machine_count: int = None,
    ):
        self.block_event_machine_count = block_event_machine_count
        self.block_machine_count = block_machine_count
        self.machine_count = machine_count
        self.monitor_machine_count = monitor_machine_count
        self.open_machine_count = open_machine_count
        self.studying_machine_count = studying_machine_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_event_machine_count is not None:
            result['BlockEventMachineCount'] = self.block_event_machine_count

        if self.block_machine_count is not None:
            result['BlockMachineCount'] = self.block_machine_count

        if self.machine_count is not None:
            result['MachineCount'] = self.machine_count

        if self.monitor_machine_count is not None:
            result['MonitorMachineCount'] = self.monitor_machine_count

        if self.open_machine_count is not None:
            result['OpenMachineCount'] = self.open_machine_count

        if self.studying_machine_count is not None:
            result['StudyingMachineCount'] = self.studying_machine_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockEventMachineCount') is not None:
            self.block_event_machine_count = m.get('BlockEventMachineCount')

        if m.get('BlockMachineCount') is not None:
            self.block_machine_count = m.get('BlockMachineCount')

        if m.get('MachineCount') is not None:
            self.machine_count = m.get('MachineCount')

        if m.get('MonitorMachineCount') is not None:
            self.monitor_machine_count = m.get('MonitorMachineCount')

        if m.get('OpenMachineCount') is not None:
            self.open_machine_count = m.get('OpenMachineCount')

        if m.get('StudyingMachineCount') is not None:
            self.studying_machine_count = m.get('StudyingMachineCount')

        return self

