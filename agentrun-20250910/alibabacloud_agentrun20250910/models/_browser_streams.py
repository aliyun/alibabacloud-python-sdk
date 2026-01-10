# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class BrowserStreams(DaraModel):
    def __init__(
        self,
        automation_stream: main_models.BrowserAutomationStream = None,
        live_view_stream: main_models.BrowserLiveViewStream = None,
    ):
        self.automation_stream = automation_stream
        self.live_view_stream = live_view_stream

    def validate(self):
        if self.automation_stream:
            self.automation_stream.validate()
        if self.live_view_stream:
            self.live_view_stream.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automation_stream is not None:
            result['automationStream'] = self.automation_stream.to_map()

        if self.live_view_stream is not None:
            result['liveViewStream'] = self.live_view_stream.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('automationStream') is not None:
            temp_model = main_models.BrowserAutomationStream()
            self.automation_stream = temp_model.from_map(m.get('automationStream'))

        if m.get('liveViewStream') is not None:
            temp_model = main_models.BrowserLiveViewStream()
            self.live_view_stream = temp_model.from_map(m.get('liveViewStream'))

        return self

