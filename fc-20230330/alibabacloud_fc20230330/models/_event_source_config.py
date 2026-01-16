# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class EventSourceConfig(DaraModel):
    def __init__(
        self,
        event_source_parameters: main_models.EventSourceParameters = None,
        event_source_type: str = None,
    ):
        self.event_source_parameters = event_source_parameters
        self.event_source_type = event_source_type

    def validate(self):
        if self.event_source_parameters:
            self.event_source_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_source_parameters is not None:
            result['eventSourceParameters'] = self.event_source_parameters.to_map()

        if self.event_source_type is not None:
            result['eventSourceType'] = self.event_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventSourceParameters') is not None:
            temp_model = main_models.EventSourceParameters()
            self.event_source_parameters = temp_model.from_map(m.get('eventSourceParameters'))

        if m.get('eventSourceType') is not None:
            self.event_source_type = m.get('eventSourceType')

        return self

