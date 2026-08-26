# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDelayConfigResponseBody(DaraModel):
    def __init__(
        self,
        app: str = None,
        delay_time: str = None,
        domain: str = None,
        request_id: str = None,
        stream: str = None,
        task_trigger_mode: str = None,
    ):
        # The application name.
        self.app = app
        # The playback latency of the stream.
        self.delay_time = delay_time
        # The streaming domain.
        self.domain = domain
        # The request ID.
        self.request_id = request_id
        # The stream name.
        self.stream = stream
        # The trigger mode for the task. Valid values:
        # 
        # - **PUBLISH_ONLY**: The task is triggered only when stream ingest parameters for delayed playback are specified.
        # - **CONFIG_ONLY**: The task is triggered only by the configuration. Stream ingest parameters are ignored.
        # - **PUBLISH_CONFIG**: The task can be triggered by both stream ingest parameters and the configuration. Stream ingest parameters have a higher priority than the configuration.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TaskTriggerMode') is not None:
            self.task_trigger_mode = m.get('TaskTriggerMode')

        return self

