# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveDelayConfigRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        delay_time: int = None,
        domain: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream: str = None,
        task_trigger_mode: str = None,
    ):
        # The name of the application to which the live stream belongs. You can specify an asterisk (\\*) as the value to match all applications that belong to the domain name.
        # 
        # This parameter is required.
        self.app = app
        # The duration for which the playback of the live stream is delayed. The value must be an integer. Valid values: 16 to 3600. Unit: seconds.
        # 
        # This parameter is required.
        self.delay_time = delay_time
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the live stream. You can use the wildcard (\\*) to specify all streams of the application.
        # 
        # This parameter is required.
        self.stream = stream
        # The trigger mode. Valid values:
        # 
        # *   **PUBLISH_ONLY**: Stream delay can be triggered only by specifying the stream delay parameter in the ingest URL.
        # *   **CONFIG_ONLY**: Stream delay can be triggered only by the stream delay configuration.
        # *   **PUBLISH_CONFIG**: Stream delay can be triggered by the stream delay parameter in the ingest URL or the stream delay configuration. The stream delay parameter takes precedence over the stream delay configuration.
        self.task_trigger_mode = task_trigger_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.task_trigger_mode is not None:
            result['TaskTriggerMode'] = self.task_trigger_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TaskTriggerMode') is not None:
            self.task_trigger_mode = m.get('TaskTriggerMode')

        return self

