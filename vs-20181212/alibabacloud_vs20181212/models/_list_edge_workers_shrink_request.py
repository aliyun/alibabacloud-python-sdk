# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEdgeWorkersShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        hive_ids_shrink: str = None,
        instance_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        plan_ids_shrink: str = None,
        spec: str = None,
        start_time: str = None,
        statuses_shrink: str = None,
    ):
        self.end_time = end_time
        self.hive_ids_shrink = hive_ids_shrink
        self.instance_ids_shrink = instance_ids_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.plan_ids_shrink = plan_ids_shrink
        self.spec = spec
        self.start_time = start_time
        self.statuses_shrink = statuses_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hive_ids_shrink is not None:
            result['HiveIds'] = self.hive_ids_shrink

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plan_ids_shrink is not None:
            result['PlanIds'] = self.plan_ids_shrink

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HiveIds') is not None:
            self.hive_ids_shrink = m.get('HiveIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanIds') is not None:
            self.plan_ids_shrink = m.get('PlanIds')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')

        return self

