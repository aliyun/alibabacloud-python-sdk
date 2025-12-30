# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListNodeDownStreamRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        list_query: main_models.ListNodeDownStreamRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.env = env
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
        if self.env is not None:
            result['Env'] = self.env

        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ListQuery') is not None:
            temp_model = main_models.ListNodeDownStreamRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListNodeDownStreamRequestListQuery(DaraModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        filter_list: List[main_models.ListNodeDownStreamRequestListQueryFilterList] = None,
        node_id_list: List[main_models.ListNodeDownStreamRequestListQueryNodeIdList] = None,
        project_id: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.filter_list = filter_list
        # This parameter is required.
        self.node_id_list = node_id_list
        self.project_id = project_id

    def validate(self):
        if self.filter_list:
            for v1 in self.filter_list:
                 if v1:
                    v1.validate()
        if self.node_id_list:
            for v1 in self.node_id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth

        result['FilterList'] = []
        if self.filter_list is not None:
            for k1 in self.filter_list:
                result['FilterList'].append(k1.to_map() if k1 else None)

        result['NodeIdList'] = []
        if self.node_id_list is not None:
            for k1 in self.node_id_list:
                result['NodeIdList'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')

        self.filter_list = []
        if m.get('FilterList') is not None:
            for k1 in m.get('FilterList'):
                temp_model = main_models.ListNodeDownStreamRequestListQueryFilterList()
                self.filter_list.append(temp_model.from_map(k1))

        self.node_id_list = []
        if m.get('NodeIdList') is not None:
            for k1 in m.get('NodeIdList'):
                temp_model = main_models.ListNodeDownStreamRequestListQueryNodeIdList()
                self.node_id_list.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ListNodeDownStreamRequestListQueryNodeIdList(DaraModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_id_list = field_id_list
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class ListNodeDownStreamRequestListQueryFilterList(DaraModel):
    def __init__(
        self,
        exclude: bool = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        self.exclude = exclude
        self.key = key
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.key is not None:
            result['Key'] = self.key

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

