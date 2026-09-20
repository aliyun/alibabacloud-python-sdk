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
        # The business date. The value must be less than or equal to the current date minus 1 day. For example, if today is November 11, 2020, the business date must be 00:00:00 on November 10, 2020 or an earlier date. The hour, minute, and second values of the business date must all be set to 00.
        # 
        # This parameter is used together with the StartBizDate and EndBizDate parameters. You can configure only one of BizDate or the StartBizDate and EndBizDate pair.
        # 
        # Format: `yyyy-MM-dd HH:mm:ss`. Example: `2020-11-11 00:00:00`.
        self.biz_date = biz_date
        # This parameter is synchronized to all instances of the current dagrun. If the scheduling parameters of internal nodes ([supported node types](https://help.aliyun.com/document_detail/147245.html)) reference workflow parameters in DagParameters, the corresponding parameter values of the nodes are replaced with the workflow parameters in DagParameters.
        self.dag_parameters = dag_parameters
        # The business end date. Format: yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is used together with the StartBizDate parameter. You can configure only one of the StartBizDate and EndBizDate pair or the BizDate parameter.
        self.end_biz_date = end_biz_date
        # The IDs of nodes that you do not want to run within the workflow. The specified nodes generate dry-run instances during execution. After a dry-run instance is scheduled, it immediately succeeds without executing the script content. Separate multiple node IDs with commas (,).
        # 
        # The ExcludeNodeIds parameter takes effect only when used together with the IncludeNodeIds parameter.
        self.exclude_node_ids = exclude_node_ids
        # The name of the manual workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The IDs of specific nodes to run within the manual workflow. Separate multiple node IDs with commas (,).
        self.include_node_ids = include_node_ids
        # The node parameter information passed when the manual workflow is executed. This corresponds to the **scheduling parameters** configured in the **Properties** of nodes within the manual workflow.
        # 
        # A JSON format: { "<Node ID within the manual workflow>": "Scheduling parameter information of the node, in the same format as the parameters in the data development scheduling configuration", "<Node ID within the manual workflow>": "Scheduling parameter information of the node, in the same format as the parameters in the data development scheduling configuration" }
        self.node_parameters = node_parameters
        # The environment identifier of the Operation Center. PROD indicates the production environment. DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The project ID.
        self.project_id = project_id
        # The name of the workspace to which the manual workflow belongs.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The business start date. Format: yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is used together with the EndBizDate parameter. You can configure only one of the StartBizDate and EndBizDate pair or the BizDate parameter.
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

