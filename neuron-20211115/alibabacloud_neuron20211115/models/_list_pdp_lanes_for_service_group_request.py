# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPdpLanesForServiceGroupRequest(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        env: str = None,
        keyword: str = None,
        lane_ids: List[int] = None,
        operator: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        service_group_id: int = None,
        service_id: int = None,
    ):
        self.company_id = company_id
        self.env = env
        self.keyword = keyword
        self.lane_ids = lane_ids
        self.operator = operator
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.service_group_id = service_group_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.env is not None:
            result['env'] = self.env

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.lane_ids is not None:
            result['laneIds'] = self.lane_ids

        if self.operator is not None:
            result['operator'] = self.operator

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

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('laneIds') is not None:
            self.lane_ids = m.get('laneIds')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

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

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

