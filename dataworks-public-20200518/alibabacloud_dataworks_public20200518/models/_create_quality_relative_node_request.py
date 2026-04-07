# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQualityRelativeNodeRequest(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        match_expression: str = None,
        node_id: int = None,
        project_id: int = None,
        project_name: str = None,
        table_name: str = None,
        target_node_project_id: int = None,
        target_node_project_name: str = None,
    ):
        # The type of the compute engine or data source.
        # 
        # This parameter is required.
        self.env_type = env_type
        # The partition filter expression.
        # 
        # This parameter is required.
        self.match_expression = match_expression
        # The node ID. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The name of the compute engine or data source.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The ID of the workspace to which the node belongs.
        # 
        # This parameter is required.
        self.target_node_project_id = target_node_project_id
        # The name of the workspace to which the node to be associated with the partition filter expression belongs.
        # 
        # This parameter is required.
        self.target_node_project_name = target_node_project_name

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

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.target_node_project_id is not None:
            result['TargetNodeProjectId'] = self.target_node_project_id

        if self.target_node_project_name is not None:
            result['TargetNodeProjectName'] = self.target_node_project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('MatchExpression') is not None:
            self.match_expression = m.get('MatchExpression')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TargetNodeProjectId') is not None:
            self.target_node_project_id = m.get('TargetNodeProjectId')

        if m.get('TargetNodeProjectName') is not None:
            self.target_node_project_name = m.get('TargetNodeProjectName')

        return self

