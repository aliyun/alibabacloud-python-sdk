# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQualityEntityRequest(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        match_expression: str = None,
        project_id: int = None,
        project_name: str = None,
        table_name: str = None,
    ):
        # The type of the compute engine or data source. Valid values:
        # 
        # *   cdh
        # *   analyticdb_for_mysql
        # *   odps
        # *   emr
        # *   hadoop
        # *   holodb
        # *   hybriddb_for_postgresql
        # 
        # This parameter is required.
        self.env_type = env_type
        # The partition filter expression.
        self.match_expression = match_expression
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        self.project_id = project_id
        # The name of the compute engine instance or data source. You can obtain the name from data source configurations.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the partitioned table. You can call the [GetMetaTablePartition](https://help.aliyun.com/document_detail/173923.html) operation to obtain the name.
        # 
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.match_expression is not None:
            result['MatchExpression'] = self.match_expression

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('MatchExpression') is not None:
            self.match_expression = m.get('MatchExpression')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

