# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BridgeRtcCallRequest(DaraModel):
    def __init__(
        self,
        callee: str = None,
        caller: str = None,
        device_id: str = None,
        instance_id: str = None,
        service_provider: str = None,
        tags: str = None,
        timeout_seconds: int = None,
        user_id: str = None,
        video_enabled: bool = None,
    ):
        # This parameter is required.
        self.callee = callee
        self.caller = caller
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        self.service_provider = service_provider
        self.tags = tags
        self.timeout_seconds = timeout_seconds
        self.user_id = user_id
        self.video_enabled = video_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.video_enabled is not None:
            result['VideoEnabled'] = self.video_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VideoEnabled') is not None:
            self.video_enabled = m.get('VideoEnabled')

        return self

