# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListPendingApprovalsRequest(DaraModel):
    def __init__(
        self,
        access_types: List[str] = None,
        def_schema: str = None,
        end_time: int = None,
        grantee: main_models.ListPendingApprovalsRequestGrantee = None,
        next_token: str = None,
        page_size: int = None,
        resource: main_models.ListPendingApprovalsRequestResource = None,
        resource_type: List[str] = None,
        start_time: int = None,
    ):
        self.access_types = access_types
        # This parameter is required.
        self.def_schema = def_schema
        self.end_time = end_time
        self.grantee = grantee
        self.next_token = next_token
        self.page_size = page_size
        self.resource = resource
        # This parameter is required.
        self.resource_type = resource_type
        self.start_time = start_time

    def validate(self):
        if self.grantee:
            self.grantee.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_types is not None:
            result['AccessTypes'] = self.access_types

        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.grantee is not None:
            result['Grantee'] = self.grantee.to_map()

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTypes') is not None:
            self.access_types = m.get('AccessTypes')

        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Grantee') is not None:
            temp_model = main_models.ListPendingApprovalsRequestGrantee()
            self.grantee = temp_model.from_map(m.get('Grantee'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Resource') is not None:
            temp_model = main_models.ListPendingApprovalsRequestResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListPendingApprovalsRequestResource(DaraModel):
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

class ListPendingApprovalsRequestGrantee(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        self.principal_id = principal_id
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

