# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTableColumnLineagesRequest(DaraModel):
    def __init__(
        self,
        filter_query: main_models.GetTableColumnLineagesRequestFilterQuery = None,
        op_tenant_id: int = None,
        table_guid: str = None,
    ):
        self.filter_query = filter_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        if self.filter_query:
            self.filter_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_query is not None:
            result['FilterQuery'] = self.filter_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterQuery') is not None:
            temp_model = main_models.GetTableColumnLineagesRequestFilterQuery()
            self.filter_query = temp_model.from_map(m.get('FilterQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

class GetTableColumnLineagesRequestFilterQuery(DaraModel):
    def __init__(
        self,
        need_downstream: bool = None,
        need_not_exist_object: bool = None,
        need_upstream: bool = None,
        node_env: str = None,
        node_id_list: List[str] = None,
    ):
        self.need_downstream = need_downstream
        self.need_not_exist_object = need_not_exist_object
        self.need_upstream = need_upstream
        self.node_env = node_env
        self.node_id_list = node_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_downstream is not None:
            result['NeedDownstream'] = self.need_downstream

        if self.need_not_exist_object is not None:
            result['NeedNotExistObject'] = self.need_not_exist_object

        if self.need_upstream is not None:
            result['NeedUpstream'] = self.need_upstream

        if self.node_env is not None:
            result['NodeEnv'] = self.node_env

        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedDownstream') is not None:
            self.need_downstream = m.get('NeedDownstream')

        if m.get('NeedNotExistObject') is not None:
            self.need_not_exist_object = m.get('NeedNotExistObject')

        if m.get('NeedUpstream') is not None:
            self.need_upstream = m.get('NeedUpstream')

        if m.get('NodeEnv') is not None:
            self.node_env = m.get('NodeEnv')

        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')

        return self

