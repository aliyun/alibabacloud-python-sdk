# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetVpcRouteEntrySummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        route_entry_summarys: List[main_models.GetVpcRouteEntrySummaryResponseBodyRouteEntrySummarys] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the routes in the route tables.
        self.route_entry_summarys = route_entry_summarys

    def validate(self):
        if self.route_entry_summarys:
            for v1 in self.route_entry_summarys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteEntrySummarys'] = []
        if self.route_entry_summarys is not None:
            for k1 in self.route_entry_summarys:
                result['RouteEntrySummarys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_entry_summarys = []
        if m.get('RouteEntrySummarys') is not None:
            for k1 in m.get('RouteEntrySummarys'):
                temp_model = main_models.GetVpcRouteEntrySummaryResponseBodyRouteEntrySummarys()
                self.route_entry_summarys.append(temp_model.from_map(k1))

        return self

class GetVpcRouteEntrySummaryResponseBodyRouteEntrySummarys(DaraModel):
    def __init__(
        self,
        entry_summarys: List[main_models.GetVpcRouteEntrySummaryResponseBodyRouteEntrySummarysEntrySummarys] = None,
        route_table_id: str = None,
    ):
        # The information about the routes of different types in one route table.
        self.entry_summarys = entry_summarys
        # The ID of the route table.
        self.route_table_id = route_table_id

    def validate(self):
        if self.entry_summarys:
            for v1 in self.entry_summarys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EntrySummarys'] = []
        if self.entry_summarys is not None:
            for k1 in self.entry_summarys:
                result['EntrySummarys'].append(k1.to_map() if k1 else None)

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entry_summarys = []
        if m.get('EntrySummarys') is not None:
            for k1 in m.get('EntrySummarys'):
                temp_model = main_models.GetVpcRouteEntrySummaryResponseBodyRouteEntrySummarysEntrySummarys()
                self.entry_summarys.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class GetVpcRouteEntrySummaryResponseBodyRouteEntrySummarysEntrySummarys(DaraModel):
    def __init__(
        self,
        count: int = None,
        route_entry_type: str = None,
    ):
        # The number of entries returned.
        self.count = count
        # The type of the route. Valid values:
        # 
        # *   **All**: all route types
        # *   **Custom**: a custom route
        # *   **System**: a system route
        # *   **BGP**: a BGP route
        # *   **CEN**: a CEN route
        self.route_entry_type = route_entry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')

        return self

