# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSetsShrinkRequest(DaraModel):
    def __init__(
        self,
        data_set_id: str = None,
        data_set_ids_shrink: str = None,
        data_set_name: str = None,
        data_set_status: int = None,
        data_set_type: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_ids_shrink = data_set_ids_shrink
        self.data_set_name = data_set_name
        self.data_set_status = data_set_status
        self.data_set_type = data_set_type
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_ids_shrink is not None:
            result['DataSetIds'] = self.data_set_ids_shrink

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status

        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction

        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetIds') is not None:
            self.data_set_ids_shrink = m.get('DataSetIds')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')

        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')

        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

