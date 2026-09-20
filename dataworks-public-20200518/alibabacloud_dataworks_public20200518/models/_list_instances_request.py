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
        # The start date for which to retrieve the instance list. Format: yyyy-MM-dd HH:mm:ss.
        self.begin_bizdate = begin_bizdate
        # The name of the workflow. You can call [ListBusiness](https://help.aliyun.com/document_detail/173945.html) to query workflow information.
        self.biz_name = biz_name
        # The date for which to retrieve the instance list. Format: yyyy-MM-dd HH:mm:ss.
        self.bizdate = bizdate
        # The DAG ID. The DagId can be the DagId returned by operations such as [RunCycleDagNodes](https://help.aliyun.com/document_detail/212961.html) for data backfill, [RunSmokeTest](https://help.aliyun.com/document_detail/212949.html) for smoke testing, and [RunManualDagNodes](https://help.aliyun.com/document_detail/212830.html) for manual workflows.
        self.dag_id = dag_id
        # The end date for which to retrieve the instance list. Format: yyyy-MM-dd HH:mm:ss.
        self.end_bizdate = end_bizdate
        # The node ID. You can call [ListNodes](https://help.aliyun.com/document_detail/173979.html) to query the node ID.
        self.node_id = node_id
        # The node name. You can call [ListNodes](https://help.aliyun.com/document_detail/173979.html) to query the node name.
        self.node_name = node_name
        # The sorting rule for the returned results. Valid values:
        # - CREATE_TIME_DESC: sorted by creation time in descending order.
        # - INSTANCE_ID_DESC: default value. Sorted by instance ID in descending order.
        self.order_by = order_by
        # The ID of the owner, which is the UID of the workspace administrator. You can logon to the Alibaba Cloud Management Console and view the UID in the Security Settings section of the storage management page.
        self.owner = owner
        # The page number. Minimum value: 1. Maximum value: 100.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The node type. You can call [ListNodes](https://help.aliyun.com/document_detail/173979.html) to query the node type.
        self.program_type = program_type
        # The runtime environment. Valid values:
        # 
        # - PROD: production environment.
        # - DEV: development environment.
        # 
        # This parameter is required.
        self.project_env = project_env
        # The workspace ID. You can call [ListProjects](https://help.aliyun.com/document_detail/178393.html) to query the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The status of the node. Valid values:
        # 
        # - NOT_RUN: The node is not run.
        # 
        # - WAIT_TIME: The node is waiting for the scheduled time (DueTime or CycTime) to arrive.
        # 
        # - WAIT_RESOURCE: The node is waiting for resources.
        # 
        # - RUNNING: The node is running.
        # - CHECKING: The node has been sent to Data Quality for data validation.
        # - CHECKING_CONDITION: The node is undergoing branch condition verification.
        # - FAILURE: Failed to execute.
        # - SUCCESS: Execute successfully.
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

