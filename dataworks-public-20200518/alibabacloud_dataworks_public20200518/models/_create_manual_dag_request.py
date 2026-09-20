# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateManualDagRequest(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        dag_parameters: str = None,
        exclude_node_ids: str = None,
        flow_name: str = None,
        include_node_ids: str = None,
        node_parameters: str = None,
        project_env: str = None,
        project_name: str = None,
    ):
        # The business date. The value must be less than or equal to the current date minus 1 day. For example, if today is November 11, 2020, the business date must be 00:00:00 on November 10, 2020 or an earlier date. The hour, minute, and second values of the business date must all be set to 00.
        # 
        # Format example: `yyyy-MM-dd HH:mm:ss`, such as `2020-11-11 00:00:00`.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        # The business process parameters. These parameters are synchronized to all instances of the current dagrun. If the scheduling parameters of internal nodes reference the business process parameters in DagParameters, the corresponding parameter values of the nodes are replaced with the business process parameters in DagParameters.
        self.dag_parameters = dag_parameters
        # The list of node IDs that do not need to be executed.
        self.exclude_node_ids = exclude_node_ids
        # The name of the manual business process.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The list of node IDs that need to be executed.
        self.include_node_ids = include_node_ids
        # The node parameter information passed when the manual business process is executed. The value is in JSON format:
        # `
        # {
        #      "<Node ID within the manual business process>": "Scheduling parameter information of the node, in the same format as the parameters in the scheduling configuration of DataStudio", 
        #      "<Node ID within the manual business process>": "Scheduling parameter information of the node, in the same format as the parameters in the scheduling configuration of DataStudio"
        # }
        # `
        self.node_parameters = node_parameters
        # The environment identifier of the O&M center. PROD indicates the production environment. DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The English name of the workspace to which the manual business process belongs.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.dag_parameters is not None:
            result['DagParameters'] = self.dag_parameters

        if self.exclude_node_ids is not None:
            result['ExcludeNodeIds'] = self.exclude_node_ids

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.include_node_ids is not None:
            result['IncludeNodeIds'] = self.include_node_ids

        if self.node_parameters is not None:
            result['NodeParameters'] = self.node_parameters

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('DagParameters') is not None:
            self.dag_parameters = m.get('DagParameters')

        if m.get('ExcludeNodeIds') is not None:
            self.exclude_node_ids = m.get('ExcludeNodeIds')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('IncludeNodeIds') is not None:
            self.include_node_ids = m.get('IncludeNodeIds')

        if m.get('NodeParameters') is not None:
            self.node_parameters = m.get('NodeParameters')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

