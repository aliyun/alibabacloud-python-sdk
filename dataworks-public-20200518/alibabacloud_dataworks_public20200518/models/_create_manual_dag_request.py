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
        # The data timestamp. The value of the data timestamp must be one or more days before the current date. For example, if the current date is November 11, 2020, set the value to 2020-11-10 00:00:00 or earlier. Configure this parameter in the YYYY-MM-DD 00:00:00 format.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        # The parameters of the manually triggered workflow, which are synchronized to all the instances in the directed acyclic graph (DAG) of the workflow. If a workflow parameter specified in DagParameters is referenced as a scheduling parameter of a node, the value of the scheduling parameter is replaced with the value of the workflow parameter.
        self.dag_parameters = dag_parameters
        # The IDs of the nodes that do not need to be run.
        self.exclude_node_ids = exclude_node_ids
        # The name of the manually triggered workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The IDs of the nodes that you want to run.
        self.include_node_ids = include_node_ids
        # The parameters transmitted between nodes in the manually triggered workflow. The parameters are in the following JSON format: `{ "<ID of a node in the manually triggered workflow>": "Scheduling parameter settings of the node, which are in the same format as the parameters in the Scheduling Parameter section on the Properties tab of the DataStudio page", "<ID of a node in the manually triggered workflow>": "Scheduling parameter settings of the node, which are in the same format as the parameters in the Scheduling Parameter section on the Properties tab of the DataStudio page" }`
        self.node_parameters = node_parameters
        # The environment type of Operation Center. Valid values: PROD and DEV.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The name of the workspace to which the manually triggered workflow belongs.
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

