# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchTracesByPageRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        env: str = None,
        min_duration: int = None,
        operation_name: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        service_group_id: int = None,
        service_name: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.env = env
        self.min_duration = min_duration
        self.operation_name = operation_name
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.service_group_id = service_group_id
        self.service_name = service_name
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

        if self.env is not None:
            result['env'] = self.env

        if self.min_duration is not None:
            result['minDuration'] = self.min_duration

        if self.operation_name is not None:
            result['operationName'] = self.operation_name

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')

        if m.get('operationName') is not None:
            self.operation_name = m.get('operationName')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

