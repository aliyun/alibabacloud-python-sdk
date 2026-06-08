# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMyApplicationsRequest(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        end_time: int = None,
        next_token: str = None,
        page_size: int = None,
        resource: main_models.ListMyApplicationsRequestResource = None,
        resource_type: List[str] = None,
        start_time: int = None,
        statuses: List[str] = None,
    ):
        # This parameter is required.
        self.def_schema = def_schema
        # This parameter is required.
        self.end_time = end_time
        self.next_token = next_token
        self.page_size = page_size
        self.resource = resource
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.start_time = start_time
        self.statuses = statuses

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Resource') is not None:
            temp_model = main_models.ListMyApplicationsRequestResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

class ListMyApplicationsRequestResource(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        def_version: str = None,
        meta_data: Dict[str, Any] = None,
    ):
        self.def_schema = def_schema
        self.def_version = def_version
        self.meta_data = meta_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.def_version is not None:
            result['DefVersion'] = self.def_version

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('DefVersion') is not None:
            self.def_version = m.get('DefVersion')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        return self

