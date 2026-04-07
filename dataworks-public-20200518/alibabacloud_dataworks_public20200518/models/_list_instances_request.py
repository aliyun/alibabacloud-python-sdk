# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        begin_bizdate: str = None,
        biz_name: str = None,
        bizdate: str = None,
        dag_id: int = None,
        end_bizdate: str = None,
        node_id: int = None,
        node_name: str = None,
        order_by: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        program_type: str = None,
        project_env: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The parameters related to the node.
        self.begin_bizdate = begin_bizdate
        # The ID of the instance.
        self.biz_name = biz_name
        # The number of entries returned per page. Default value: 10. Maximum value: 100.
        self.bizdate = bizdate
        # The environment of the workspace. Valid values: PROD and DEV. The value PROD indicates the production environment. The value DEV indicates the development environment.
        self.dag_id = dag_id
        # The ID of the workflow.
        self.end_bizdate = end_bizdate
        # Indicates whether the instance is associated with a monitoring rule in Data Quality. Valid values:
        # 
        # *   0: The instance is associated with a monitoring rule in Data Quality.
        # *   1: The instance is not associated with a monitoring rule in Data Quality.
        self.node_id = node_id
        # Indicates whether the node can be rerun.
        self.node_name = node_name
        # The sorting rule of the instances to be returned. Valid values:
        # 
        # *   CREATE_TIME_DESC: The instances are sorted in descending order of their creation time.
        # *   INSTANCE_ID_DESC (default): The instances are sorted in descending order of their IDs.
        self.order_by = order_by
        # The connection string.
        self.owner = owner
        # The operation that you want to perform.
        self.page_number = page_number
        # The ID of the node.
        self.page_size = page_size
        # The error code returned.
        self.program_type = program_type
        # The environment in which the node runs. Valid values: DEV and PROD.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The ID of the baseline.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The status of the node. Valid values:
        # 
        # *   NOT_RUN: The node is not run.
        # *   WAIT_TIME: The node is waiting for the scheduling time to arrive.
        # *   WAIT_RESOURCE: The node is waiting for resources.
        # *   RUNNING: The node is running.
        # *   CHECKING: Data quality is being checked for the node.
        # *   CHECKING_CONDITION: Branch conditions are being checked for the node.
        # *   FAILURE: The node fails to run.
        # *   SUCCESS: The node is successfully run.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_bizdate is not None:
            result['BeginBizdate'] = self.begin_bizdate

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.end_bizdate is not None:
            result['EndBizdate'] = self.end_bizdate

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.owner is not None:
            result['Owner'] = self.owner

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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBizdate') is not None:
            self.begin_bizdate = m.get('BeginBizdate')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('EndBizdate') is not None:
            self.end_bizdate = m.get('EndBizdate')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

