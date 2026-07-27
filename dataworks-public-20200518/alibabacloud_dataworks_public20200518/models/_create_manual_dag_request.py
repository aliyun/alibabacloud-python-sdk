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
        # The value of the business date must be less than or equal to the current date minus one day. For example, if today is November 11, 2020, the business date must be 2020-11-10 00:00:00 or an earlier date. The hour, minute, and second fields of the business date must all be set to 00.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        # The workflow parameters. These parameters are synchronized to all instances of the current DAG. If the scheduling parameters of an internal node reference the workflow parameters in DagParameters, the corresponding parameter values of the node are replaced with the workflow parameters in DagParameters.
        self.dag_parameters = dag_parameters
        # The list of IDs of the nodes that do not need to be run.
        self.exclude_node_ids = exclude_node_ids
        # The name of the manual workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The list of IDs of the nodes to be run.
        self.include_node_ids = include_node_ids
        # The node parameter information passed when the manual workflow is executed, in JSON format:
        # `
        # {
        #      "<A node ID inside the manual workflow>": "The scheduling parameter information of the node, consistent with the parameter format in the data development scheduling configuration", 
        #      "<A node ID inside the manual workflow>": "The scheduling parameter information of the node, consistent with the parameter format in the data development scheduling configuration"
        # }
        # `
        self.node_parameters = node_parameters
        # The environment identifier of the Scheduling Operation Center. PROD indicates the production environment, and DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The English name of the workspace to which the manual workflow belongs.
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

