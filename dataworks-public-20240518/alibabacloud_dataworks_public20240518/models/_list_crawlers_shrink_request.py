# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCrawlersShrinkRequest(DaraModel):
    def __init__(
        self,
        data_source_ids_shrink: str = None,
        env_type: str = None,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        type: str = None,
    ):
        # The list of data source IDs. Up to 10 IDs are supported.
        self.data_source_ids_shrink = data_source_ids_shrink
        # The DataWorks environment type. Dev indicates the development environment. Prod indicates the production environment.
        self.env_type = env_type
        # The metadata crawler name. Supports fuzzy match.
        self.name = name
        # The DataWorks user ID of the crawler owner.
        self.owner = owner
        # The page number. Starts from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The crawler type. Call GetCrawlerTypeCapabilities to query the valid values supported in the current region.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

