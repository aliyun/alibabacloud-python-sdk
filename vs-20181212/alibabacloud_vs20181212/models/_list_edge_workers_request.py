# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListEdgeWorkersRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        hive_ids: List[str] = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        plan_ids: List[str] = None,
        spec: str = None,
        start_time: str = None,
        statuses: List[str] = None,
    ):
        self.end_time = end_time
        self.hive_ids = hive_ids
        self.instance_ids = instance_ids
        self.page_number = page_number
        self.page_size = page_size
        self.plan_ids = plan_ids
        self.spec = spec
        self.start_time = start_time
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hive_ids is not None:
            result['HiveIds'] = self.hive_ids

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plan_ids is not None:
            result['PlanIds'] = self.plan_ids

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HiveIds') is not None:
            self.hive_ids = m.get('HiveIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanIds') is not None:
            self.plan_ids = m.get('PlanIds')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

