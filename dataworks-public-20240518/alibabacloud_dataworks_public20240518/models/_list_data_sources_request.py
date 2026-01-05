# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDataSourcesRequest(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        tags: str = None,
        types: List[str] = None,
    ):
        # The environment in which the data sources are used. Valid values:
        # 
        # *   Dev: development environment
        # *   Prod: production environment
        self.env_type = env_type
        # The name of the data source. Fuzzy match by data source name is supported.
        self.name = name
        # The order in which you want to sort the data sources. Valid values:
        # 
        # *   Desc: descending order
        # *   Asc: ascending order
        # 
        # Default value: Desc
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The field that you want to use to sort the data sources. Valid values:
        # 
        # *   CreateTime
        # *   Id
        # *   Name
        # 
        # Default value: CreateTime
        self.sort_by = sort_by
        # The tag of the data source. This parameter specifies a filter condition.
        # 
        # *   You can specify multiple tags, which are in the logical AND relation. For example, you can query the data sources that contain the following tags: `["tag1", "tag2", "tag3"]`.
        # *   If you do not configure this parameter, tag-based filtering is not performed. You can specify up to 10 tags.
        self.tags = tags
        # The data source types. This parameter specifies a filter condition. You can specify multiple data source types.
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

        if self.tags is not None:
            result['Tags'] = self.tags

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

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

