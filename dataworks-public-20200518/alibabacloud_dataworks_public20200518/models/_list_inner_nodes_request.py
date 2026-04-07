# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInnerNodesRequest(DaraModel):
    def __init__(
        self,
        node_name: str = None,
        outer_node_id: int = None,
        page_number: int = None,
        page_size: int = None,
        program_type: str = None,
        project_env: str = None,
        project_id: int = None,
    ):
        # The name of the node to which the inner nodes belong.
        self.node_name = node_name
        # The ID of the node group to which the inner nodes belong.
        # 
        # This parameter is required.
        self.outer_node_id = outer_node_id
        # The page number. Valid values: 1 to 100.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The type of the node to which the inner nodes belong.
        # 
        # Valid values: 6 (Shell), 10 (ODPS SQL), 11 (ODPS MR), 23 (Data Integration), 24 (ODPS Script), 97 (PAI), 98 (node group), 99 (zero load), 221 (PyODPS 2), 225 (ODPS Spark), 227 (EMR Hive), 228 (EMR Spark), 229 (EMR Spark SQL), 230 (EMR MR), 239 (OSS object inspection), 257 (EMR Shell), 258 (EMR Spark Shell), 259 (EMR Presto), 260 (EMR Impala), 900 (real-time synchronization), 1002 (PAI inner node), 1089 (cross-tenant collaboration), 1091 (Hologres development), 1093 (Hologres SQL), 1100 (assignment), 1106 (for-each), and 1221 (PyODPS 3). You can call the ListNodes operation to query the type of the node.
        self.program_type = program_type
        # The environment in which the node is run. Valid values: DEV and PROD. Default value: PROD.
        self.project_env = project_env
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.outer_node_id is not None:
            result['OuterNodeId'] = self.outer_node_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OuterNodeId') is not None:
            self.outer_node_id = m.get('OuterNodeId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

