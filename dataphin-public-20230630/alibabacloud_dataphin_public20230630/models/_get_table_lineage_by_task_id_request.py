# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTableLineageByTaskIdRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        table_lineage_by_task_id_query: main_models.GetTableLineageByTaskIdRequestTableLineageByTaskIdQuery = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.table_lineage_by_task_id_query = table_lineage_by_task_id_query

    def validate(self):
        if self.table_lineage_by_task_id_query:
            self.table_lineage_by_task_id_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.table_lineage_by_task_id_query is not None:
            result['TableLineageByTaskIdQuery'] = self.table_lineage_by_task_id_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('TableLineageByTaskIdQuery') is not None:
            temp_model = main_models.GetTableLineageByTaskIdRequestTableLineageByTaskIdQuery()
            self.table_lineage_by_task_id_query = temp_model.from_map(m.get('TableLineageByTaskIdQuery'))

        return self

class GetTableLineageByTaskIdRequestTableLineageByTaskIdQuery(DaraModel):
    def __init__(
        self,
        need_not_exist_object: bool = None,
        task_env: str = None,
        task_id: str = None,
    ):
        self.need_not_exist_object = need_not_exist_object
        self.task_env = task_env
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_not_exist_object is not None:
            result['NeedNotExistObject'] = self.need_not_exist_object

        if self.task_env is not None:
            result['TaskEnv'] = self.task_env

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedNotExistObject') is not None:
            self.need_not_exist_object = m.get('NeedNotExistObject')

        if m.get('TaskEnv') is not None:
            self.task_env = m.get('TaskEnv')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

