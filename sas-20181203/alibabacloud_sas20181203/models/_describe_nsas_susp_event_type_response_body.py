# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeNsasSuspEventTypeResponseBody(DaraModel):
    def __init__(
        self,
        event_types: List[main_models.DescribeNsasSuspEventTypeResponseBodyEventTypes] = None,
        request_id: str = None,
    ):
        # An array that consists of the information about the alert type.
        self.event_types = event_types
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_types = []
        if m.get('EventTypes') is not None:
            for k1 in m.get('EventTypes'):
                temp_model = main_models.DescribeNsasSuspEventTypeResponseBodyEventTypes()
                self.event_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNsasSuspEventTypeResponseBodyEventTypes(DaraModel):
    def __init__(
        self,
        name: str = None,
        susp_event_count: int = None,
        type: str = None,
    ):
        # The name of the alert type.
        self.name = name
        # The number of assets for which an alert of the type is generated.
        self.susp_event_count = susp_event_count
        # The alert type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.susp_event_count is not None:
            result['SuspEventCount'] = self.susp_event_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SuspEventCount') is not None:
            self.susp_event_count = m.get('SuspEventCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

