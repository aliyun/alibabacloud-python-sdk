# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        end_time_ms: int = None,
        instance_ids: List[str] = None,
        instance_status: List[str] = None,
        limit: str = None,
        qualifier: str = None,
        start_key: str = None,
        start_time_ms: int = None,
        with_all_active: bool = None,
    ):
        self.end_time_ms = end_time_ms
        self.instance_ids = instance_ids
        self.instance_status = instance_status
        self.limit = limit
        # The function version or alias.
        self.qualifier = qualifier
        self.start_key = start_key
        self.start_time_ms = start_time_ms
        # Specifies whether to list all instances. Valid values: true and false.
        self.with_all_active = with_all_active

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time_ms is not None:
            result['endTimeMs'] = self.end_time_ms

        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status

        if self.limit is not None:
            result['limit'] = self.limit

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.start_key is not None:
            result['startKey'] = self.start_key

        if self.start_time_ms is not None:
            result['startTimeMs'] = self.start_time_ms

        if self.with_all_active is not None:
            result['withAllActive'] = self.with_all_active

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTimeMs') is not None:
            self.end_time_ms = m.get('endTimeMs')

        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')

        if m.get('startTimeMs') is not None:
            self.start_time_ms = m.get('startTimeMs')

        if m.get('withAllActive') is not None:
            self.with_all_active = m.get('withAllActive')

        return self

