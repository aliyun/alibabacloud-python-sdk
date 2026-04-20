# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BridgeWebCallRequest(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        caller: str = None,
        device_id: str = None,
        draft_version: bool = None,
        instance_id: str = None,
        sample_rate: int = None,
        script_id: str = None,
        tags: str = None,
        timeout_seconds: int = None,
    ):
        self.access_channel_id = access_channel_id
        self.access_channel_type = access_channel_type
        self.caller = caller
        self.device_id = device_id
        self.draft_version = draft_version
        self.instance_id = instance_id
        self.sample_rate = sample_rate
        self.script_id = script_id
        self.tags = tags
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DraftVersion') is not None:
            self.draft_version = m.get('DraftVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

