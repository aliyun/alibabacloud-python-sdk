# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeCapacityReservationInstancesResponseBody(DaraModel):
    def __init__(
        self,
        capacity_reservation_item: main_models.DescribeCapacityReservationInstancesResponseBodyCapacityReservationItem = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the instances that match the capacity reservation.
        self.capacity_reservation_item = capacity_reservation_item
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.capacity_reservation_item:
            self.capacity_reservation_item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_reservation_item is not None:
            result['CapacityReservationItem'] = self.capacity_reservation_item.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityReservationItem') is not None:
            temp_model = main_models.DescribeCapacityReservationInstancesResponseBodyCapacityReservationItem()
            self.capacity_reservation_item = temp_model.from_map(m.get('CapacityReservationItem'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCapacityReservationInstancesResponseBodyCapacityReservationItem(DaraModel):
    def __init__(
        self,
        instance_id_set: List[main_models.DescribeCapacityReservationInstancesResponseBodyCapacityReservationItemInstanceIdSet] = None,
    ):
        self.instance_id_set = instance_id_set

    def validate(self):
        if self.instance_id_set:
            for v1 in self.instance_id_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceIdSet'] = []
        if self.instance_id_set is not None:
            for k1 in self.instance_id_set:
                result['InstanceIdSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_id_set = []
        if m.get('InstanceIdSet') is not None:
            for k1 in m.get('InstanceIdSet'):
                temp_model = main_models.DescribeCapacityReservationInstancesResponseBodyCapacityReservationItemInstanceIdSet()
                self.instance_id_set.append(temp_model.from_map(k1))

        return self

class DescribeCapacityReservationInstancesResponseBodyCapacityReservationItemInstanceIdSet(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

