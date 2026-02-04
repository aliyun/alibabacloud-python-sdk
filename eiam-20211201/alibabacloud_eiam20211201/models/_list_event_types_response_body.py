# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListEventTypesResponseBody(DaraModel):
    def __init__(
        self,
        event_types: List[main_models.ListEventTypesResponseBodyEventTypes] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.event_types = event_types
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.event_types:
            for v1 in self.event_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventTypes'] = []
        if self.event_types is not None:
            for k1 in self.event_types:
                result['EventTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_types = []
        if m.get('EventTypes') is not None:
            for k1 in m.get('EventTypes'):
                temp_model = main_models.ListEventTypesResponseBodyEventTypes()
                self.event_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEventTypesResponseBodyEventTypes(DaraModel):
    def __init__(
        self,
        event_type: str = None,
    ):
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

