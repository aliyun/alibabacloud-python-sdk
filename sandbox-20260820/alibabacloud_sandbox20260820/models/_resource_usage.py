# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class ResourceUsage(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        granularity: str = None,
        group_by: List[str] = None,
        groups: List[main_models.ResourceUsageGroups] = None,
        start_time: str = None,
    ):
        # The end time of the requested interval, exclusive.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The aggregation granularity used for this query. Valid values: All, Hour, and Day.
        # 
        # This parameter is required.
        self.granularity = granularity
        # The grouping key used for this query. An empty array is returned when no grouping is applied.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The usage for each group. If no grouping is applied, the usage for the entire query range is returned. An empty array is returned if there are no usage records within the query range.
        # 
        # This parameter is required.
        self.groups = groups
        # The start time of the requested interval, inclusive.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.groups is not None:
            result['groups'] = []
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('groups') is not None:
            self.groups = []
            for k1 in m.get('groups'):
                temp_model = main_models.ResourceUsageGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class ResourceUsageGroups(DaraModel):
    def __init__(
        self,
        dimensions: Dict[str, str] = None,
        items: List[main_models.ResourceUsageGroupsItems] = None,
    ):
        # The team, template, or sandbox version corresponding to the usage of this group.
        # 
        # This parameter is required.
        self.dimensions = dimensions
        # The query result for each requested usage item in this group.
        # 
        # This parameter is required.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['dimensions'] = self.dimensions

        if self.items is not None:
            result['items'] = []
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dimensions') is not None:
            self.dimensions = m.get('dimensions')

        if m.get('items') is not None:
            self.items = []
            for k1 in m.get('items'):
                temp_model = main_models.ResourceUsageGroupsItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ResourceUsageGroupsItems(DaraModel):
    def __init__(
        self,
        buckets: List[main_models.ResourceUsageGroupsItemsBuckets] = None,
        total: float = None,
        unit: str = None,
        usage_name: str = None,
    ):
        # The hourly or daily usage arranged in chronological order. Only time periods with records are returned. This field is omitted when granularity is set to All.
        self.buckets = buckets
        # The cumulative usage of this usage item over the entire query interval. This field is omitted if there are no usage records for the item within the interval.
        self.total = total
        # The unit of usage. The unit is CoreSecond for CPU, and GiBSecond for memory and cloud disks.
        # 
        # This parameter is required.
        self.unit = unit
        # The name of the usage item specified in the request.
        # 
        # This parameter is required.
        self.usage_name = usage_name

    def validate(self):
        if self.buckets:
            for v1 in self.buckets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buckets is not None:
            result['buckets'] = []
            for k1 in self.buckets:
                result['buckets'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        if self.unit is not None:
            result['unit'] = self.unit

        if self.usage_name is not None:
            result['usageName'] = self.usage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buckets') is not None:
            self.buckets = []
            for k1 in m.get('buckets'):
                temp_model = main_models.ResourceUsageGroupsItemsBuckets()
                self.buckets.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('usageName') is not None:
            self.usage_name = m.get('usageName')

        return self

class ResourceUsageGroupsItemsBuckets(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        quantity: float = None,
        start_time: str = None,
    ):
        # The end time of this usage statistics period, exclusive.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The cumulative usage within this time period. The unit is specified by unit.
        # 
        # This parameter is required.
        self.quantity = quantity
        # The start time of this usage statistics period, inclusive.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

