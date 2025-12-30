# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListFilesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListFilesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListFilesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListFilesRequestListQuery(DaraModel):
    def __init__(
        self,
        category: str = None,
        directory: str = None,
        env: str = None,
        project_id: int = None,
        recursive: bool = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.directory = directory
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.recursive = recursive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.env is not None:
            result['Env'] = self.env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.recursive is not None:
            result['Recursive'] = self.recursive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')

        return self

