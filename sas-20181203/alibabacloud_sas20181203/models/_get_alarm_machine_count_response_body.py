# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAlarmMachineCountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAlarmMachineCountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
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
            temp_model = main_models.GetAlarmMachineCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAlarmMachineCountResponseBodyData(DaraModel):
    def __init__(
        self,
        machine_count: int = None,
    ):
        # The number of servers on which alerts are generated.
        self.machine_count = machine_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.machine_count is not None:
            result['MachineCount'] = self.machine_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineCount') is not None:
            self.machine_count = m.get('MachineCount')

        return self

