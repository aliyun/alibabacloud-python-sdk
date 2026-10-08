# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        app_name: str = None,
        cluster_id: str = None,
        current_page: int = None,
        logical_region_id: str = None,
        logical_region_id_filter: str = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The list of application IDs.
        self.app_ids = app_ids
        # Filters the application list by application name.
        self.app_name = app_name
        # Filters the application list by cluster.
        self.cluster_id = cluster_id
        # The number of the page to return in a paged query. Default value: 1.
        self.current_page = current_page
        # Filters the application list by microservices namespace.
        self.logical_region_id = logical_region_id
        # Filters applications by exact match of the microservices namespace.
        self.logical_region_id_filter = logical_region_id_filter
        # The number of entries to return on each page in a paged query.
        self.page_size = page_size
        # Filters the application list by resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.logical_region_id_filter is not None:
            result['LogicalRegionIdFilter'] = self.logical_region_id_filter

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('LogicalRegionIdFilter') is not None:
            self.logical_region_id_filter = m.get('LogicalRegionIdFilter')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

