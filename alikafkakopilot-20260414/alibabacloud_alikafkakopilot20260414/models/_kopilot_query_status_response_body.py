# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alikafkakopilot20260414 import models as main_models
from darabonba.model import DaraModel

class KopilotQueryStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.KopilotQueryStatusResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.KopilotQueryStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class KopilotQueryStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        activate_time: int = None,
        instance_id: str = None,
        life_status: str = None,
        region_id: str = None,
        uid: str = None,
    ):
        self.activate_time = activate_time
        self.instance_id = instance_id
        self.life_status = life_status
        self.region_id = region_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.life_status is not None:
            result['LifeStatus'] = self.life_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LifeStatus') is not None:
            self.life_status = m.get('LifeStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

