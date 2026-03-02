# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMonitorTasksRequest(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        env: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        pbc_id: str = None,
        service_group_id: str = None,
        type: str = None,
    ):
        self.alert_name = alert_name
        # This parameter is required.
        self.env = env
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.pbc_id = pbc_id
        self.service_group_id = service_group_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['alertName'] = self.alert_name

        if self.env is not None:
            result['env'] = self.env

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertName') is not None:
            self.alert_name = m.get('alertName')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

