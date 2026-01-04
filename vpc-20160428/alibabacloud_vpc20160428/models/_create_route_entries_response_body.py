# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        failed_route_entries: List[main_models.CreateRouteEntriesResponseBodyFailedRouteEntries] = None,
        request_id: str = None,
        route_entry_ids: List[str] = None,
        success_count: int = None,
    ):
        # The number of custom route entries that failed to be added.
        self.failed_count = failed_count
        # The details about the custom route entry that failed to be added.
        self.failed_route_entries = failed_route_entries
        # The request ID.
        self.request_id = request_id
        # The information about the ID of the custom route entry that was successfully added.
        self.route_entry_ids = route_entry_ids
        # The number of custom route entries that were successfully added.
        self.success_count = success_count

    def validate(self):
        if self.failed_route_entries:
            for v1 in self.failed_route_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['FailedRouteEntries'] = []
        if self.failed_route_entries is not None:
            for k1 in self.failed_route_entries:
                result['FailedRouteEntries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_entry_ids is not None:
            result['RouteEntryIds'] = self.route_entry_ids

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.failed_route_entries = []
        if m.get('FailedRouteEntries') is not None:
            for k1 in m.get('FailedRouteEntries'):
                temp_model = main_models.CreateRouteEntriesResponseBodyFailedRouteEntries()
                self.failed_route_entries.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteEntryIds') is not None:
            self.route_entry_ids = m.get('RouteEntryIds')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class CreateRouteEntriesResponseBodyFailedRouteEntries(DaraModel):
    def __init__(
        self,
        dst_cidr_block: str = None,
        failed_code: str = None,
        failed_message: str = None,
        next_hop: str = None,
    ):
        # The destination CIDR block of the custom route entry that failed to be added.
        self.dst_cidr_block = dst_cidr_block
        # The error code.
        self.failed_code = failed_code
        # The error message.
        self.failed_message = failed_message
        # The ID of the next hop of the custom route entry that failed to be added.
        self.next_hop = next_hop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_cidr_block is not None:
            result['DstCidrBlock'] = self.dst_cidr_block

        if self.failed_code is not None:
            result['FailedCode'] = self.failed_code

        if self.failed_message is not None:
            result['FailedMessage'] = self.failed_message

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstCidrBlock') is not None:
            self.dst_cidr_block = m.get('DstCidrBlock')

        if m.get('FailedCode') is not None:
            self.failed_code = m.get('FailedCode')

        if m.get('FailedMessage') is not None:
            self.failed_message = m.get('FailedMessage')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        return self

