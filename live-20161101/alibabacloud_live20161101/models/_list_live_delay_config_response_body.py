# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveDelayConfigResponseBody(DaraModel):
    def __init__(
        self,
        delay_config_list: main_models.ListLiveDelayConfigResponseBodyDelayConfigList = None,
        request_id: str = None,
        total: int = None,
    ):
        # The stream delay configurations.
        self.delay_config_list = delay_config_list
        # The request ID.
        self.request_id = request_id
        # The number of stream delay configurations.
        self.total = total

    def validate(self):
        if self.delay_config_list:
            self.delay_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_config_list is not None:
            result['DelayConfigList'] = self.delay_config_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayConfigList') is not None:
            temp_model = main_models.ListLiveDelayConfigResponseBodyDelayConfigList()
            self.delay_config_list = temp_model.from_map(m.get('DelayConfigList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListLiveDelayConfigResponseBodyDelayConfigList(DaraModel):
    def __init__(
        self,
        delay_config: List[main_models.ListLiveDelayConfigResponseBodyDelayConfigListDelayConfig] = None,
    ):
        self.delay_config = delay_config

    def validate(self):
        if self.delay_config:
            for v1 in self.delay_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DelayConfig'] = []
        if self.delay_config is not None:
            for k1 in self.delay_config:
                result['DelayConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delay_config = []
        if m.get('DelayConfig') is not None:
            for k1 in m.get('DelayConfig'):
                temp_model = main_models.ListLiveDelayConfigResponseBodyDelayConfigListDelayConfig()
                self.delay_config.append(temp_model.from_map(k1))

        return self

class ListLiveDelayConfigResponseBodyDelayConfigListDelayConfig(DaraModel):
    def __init__(
        self,
        app: str = None,
        delay_time: str = None,
        domain: str = None,
        stream: str = None,
        task_trigger_mode: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The duration for which the playback of the live stream is delayed. Unit: seconds.
        self.delay_time = delay_time
        # The main streaming domain.
        self.domain = domain
        # The name of the live stream.
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

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TaskTriggerMode') is not None:
            self.task_trigger_mode = m.get('TaskTriggerMode')

        return self

