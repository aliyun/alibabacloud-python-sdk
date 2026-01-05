# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListComputeResourcesRequest(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        types: List[str] = None,
    ):
        # The environment type of the computing resource. Valid values:
        # 
        # *   Dev
        # *   Prod
        self.env_type = env_type
        # The name of the computing resource.
        self.name = name
        # The sort direction of the computing resource list. Valid values:
        # 
        # *   Desc: descending order.
        # *   Asc: ascending order.
        # 
        # Default value: Desc
        self.order = order
        # The page number to query. The default value is 1, which indicates the first page.
        self.page_number = page_number
        # The number of entries per page. The default value is 10, and the maximum value is 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The field to sort the computing resource list by. Supported fields include name, creation time, and computing resource ID.
        # 
        # *   CreateTime: Sorts by creation time
        # *   Id: Sorts by computing resource ID
        # *   Name: Sorts by computing resource name.
        # *   CreateTimeWithDefaultFirst: Sorts based on whether it is the default resource and by creation time, with the default computing resource listed first.
        # 
        # Default value: CreateTime
        self.sort_by = sort_by
        # The filter for computing resource types. You can configure multiple types for filtering.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

