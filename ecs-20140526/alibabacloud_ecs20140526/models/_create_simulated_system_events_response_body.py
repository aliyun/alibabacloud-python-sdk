# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateSimulatedSystemEventsResponseBody(DaraModel):
    def __init__(
        self,
        event_id_set: main_models.CreateSimulatedSystemEventsResponseBodyEventIdSet = None,
        request_id: str = None,
    ):
        # The IDs of the simulated events.
        self.event_id_set = event_id_set
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.event_id_set:
            self.event_id_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id_set is not None:
            result['EventIdSet'] = self.event_id_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventIdSet') is not None:
            temp_model = main_models.CreateSimulatedSystemEventsResponseBodyEventIdSet()
            self.event_id_set = temp_model.from_map(m.get('EventIdSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateSimulatedSystemEventsResponseBodyEventIdSet(DaraModel):
    def __init__(
        self,
        event_id: List[str] = None,
    ):
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        return self

