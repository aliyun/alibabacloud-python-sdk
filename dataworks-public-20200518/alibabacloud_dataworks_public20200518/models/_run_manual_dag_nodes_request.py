# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunManualDagNodesRequest(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        dag_parameters: str = None,
        end_biz_date: str = None,
        exclude_node_ids: str = None,
        flow_name: str = None,
        include_node_ids: str = None,
        node_parameters: str = None,
        project_env: str = None,
        project_id: int = None,
        project_name: str = None,
        start_biz_date: str = None,
    ):
        # The data timestamp. The value of the data timestamp must be one or more days before the current date. For example, if the current date is November 11, 2020, set the value to 2020-11-10 00:00:00 or earlier. Configure this parameter in the YYYY-MM-DD 00:00:00 format. The StartBizDate parameter is used together with the EndBizDate parameter. You can configure only the BizDate parameter or the StartBizDate and EndBizDate parameters.
        self.biz_date = biz_date
        # The parameters are synchronized to all the instances in the directed acyclic graph (DAG) of the workflow. If a workflow parameter specified in DagParameters is referenced as a scheduling parameter of a [node](https://help.aliyun.com/document_detail/147245.html), the value of the scheduling parameter is replaced with the value of the workflow parameter.
        self.dag_parameters = dag_parameters
        # The end of the time range in which data generated needs to be processed. Configure this parameter in the yyyy-MM-dd HH:mm:ss format. The StartBizDate parameter is used together with the EndBizDate parameter. You can configure only the BizDate parameter or the StartBizDate and EndBizDate parameters.
        self.end_biz_date = end_biz_date
        # The IDs of the nodes that you do not need to run in the manually triggered workflow. DataWorks generates dry-run instances for all these nodes. After the dry-run instances are scheduled, the states of these instances are directly set to successful, but the scripts are not run. Separate multiple node IDs with commas (,). The ExcludeNodeIds parameter must be used together with the IncludeNodeIds parameter. This way, the settings of the ExcludeNodeIds parameter can take effect.
        self.exclude_node_ids = exclude_node_ids
        # The name of the manually triggered workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The IDs of the nodes that you need to run in the manually triggered workflow. Separate multiple node IDs with commas (,).
        self.include_node_ids = include_node_ids
        # The scheduling parameters of nodes in the manually triggered workflow. Configure NodeParameters in the following JSON format: {"\\<ID of a node in the manually triggered workflow>": "Scheduling parameter settings of the node, which are in the same format as the parameter settings in the Scheduling Parameter section of the Properties tab on the DataStudio page", "\\<ID of a node in the manually triggered workflow>": "Scheduling parameter settings of the node, which are in the same format as the parameter settings in the Scheduling Parameter section of the Properties tab on the DataStudio page"}.
        self.node_parameters = node_parameters
        # The environment type of Operation Center. Valid values: PROD and DEV. The value PROD indicates the production environment. The value DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The ID of the workspace to which the manually triggered workflow belongs.
        self.project_id = project_id
        # The name of the workspace to which the manually triggered workflow belongs.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The beginning of the time range in which data generated needs to be processed. Configure this parameter in the yyyy-MM-dd HH:mm:ss format. The StartBizDate parameter is used together with the EndBizDate parameter. You can configure only the BizDate parameter or the StartBizDate and EndBizDate parameters.
        self.start_biz_date = start_biz_date

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

        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date

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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('DagParameters') is not None:
            self.dag_parameters = m.get('DagParameters')

        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')

        return self

