# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BridgeWebCallRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        business_unit_id: str = None,
        caller: str = None,
        device_id: str = None,
        sample_rate: int = None,
        sandbox: bool = None,
        tags: str = None,
        timeout_seconds: int = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.business_unit_id = business_unit_id
        self.caller = caller
        # This parameter is required.
        self.device_id = device_id
        self.sample_rate = sample_rate
        self.sandbox = sandbox
        self.tags = tags
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

