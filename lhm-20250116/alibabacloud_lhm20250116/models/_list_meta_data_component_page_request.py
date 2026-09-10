# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMetaDataComponentPageRequest(DaraModel):
    def __init__(
        self,
        category_type: str = None,
        component_type: int = None,
        ds_name: str = None,
        ds_status: List[int] = None,
        ds_type: str = None,
        ds_type_list: List[str] = None,
        group_by: str = None,
        need_total_count: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
        src_component_id: int = None,
    ):
        # The category type of the data source. Valid values: DATASET, WORKFLOW, and ENGINE. For scheduling scenarios, this parameter is set to WORKFLOW.
        self.category_type = category_type
        # The entry component type. In some operations, this parameter is used as a backward compatible field for version 1.1.0. Valid values:
        # - 0: source
        # - 1: destination
        self.component_type = component_type
        # The data source name. Exact match and fuzzy match are supported.
        self.ds_name = ds_name
        # The connectivity status of the data source. Valid values:
        # - 0: Not tested.
        # - 1: Connected.
        # - 2: Connection failed.
        # - -1: Connectivity test not supported.
        self.ds_status = ds_status
        # The data source type, such as Hive or MaxCompute.
        self.ds_type = ds_type
        # The list of data source types.
        self.ds_type_list = ds_type_list
        # The grouping field (GROUP BY condition). Set this parameter as needed.
        self.group_by = group_by
        # Specifies whether to return the total number of records in the paginated result.
        self.need_total_count = need_total_count
        # The sort field. Set this parameter as needed.
        self.order_by = order_by
        # The sort direction. Valid values:
        # - ASC: ascending order
        # - DESC: descending order
        self.order_direction = order_direction
        # The page number, starting from 1.
        self.page_index = page_index
        # The page size, which is the number of records returned per page.
        self.page_size = page_size
        # The source component ID, which is the primary key of the source data source component.
        self.src_component_id = src_component_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_type is not None:
            result['categoryType'] = self.category_type

        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        if self.ds_status is not None:
            result['dsStatus'] = self.ds_status

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.ds_type_list is not None:
            result['dsTypeList'] = self.ds_type_list

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.src_component_id is not None:
            result['srcComponentId'] = self.src_component_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryType') is not None:
            self.category_type = m.get('categoryType')

        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        if m.get('dsStatus') is not None:
            self.ds_status = m.get('dsStatus')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('dsTypeList') is not None:
            self.ds_type_list = m.get('dsTypeList')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('srcComponentId') is not None:
            self.src_component_id = m.get('srcComponentId')

        return self

