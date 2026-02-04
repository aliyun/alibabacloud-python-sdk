# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_ids_shrink: str = None,
        data_source_name: str = None,
        data_source_status: str = None,
        data_source_store_status: str = None,
        data_source_template_ids_shrink: str = None,
        data_source_type: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_ids_shrink = data_source_ids_shrink
        self.data_source_name = data_source_name
        self.data_source_status = data_source_status
        self.data_source_store_status = data_source_store_status
        self.data_source_template_ids_shrink = data_source_template_ids_shrink
        self.data_source_type = data_source_type
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_ids_shrink = log_user_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        self.order_field = order_field
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
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from

        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status

        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status

        if self.data_source_template_ids_shrink is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids_shrink

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

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
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')

        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')

        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')

        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids_shrink = m.get('DataSourceTemplateIds')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

