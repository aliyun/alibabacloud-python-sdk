# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetBwmMigrationTaskWriterWorkflowListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetBwmMigrationTaskWriterWorkflowListResponseBodyData] = None,
        empty: bool = None,
        err_code: str = None,
        err_message: str = None,
        not_empty: bool = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_pages: int = None,
    ):
        # The response data.
        self.data = data
        # Indicates whether the result is empty.
        self.empty = empty
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # Indicates whether the result is not empty.
        self.not_empty = not_empty
        # The page number.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, check errCode and errMessage for details.
        self.success = success
        # The total number of entries.
        self.total_count = total_count
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.empty is not None:
            result['empty'] = self.empty

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.not_empty is not None:
            result['notEmpty'] = self.not_empty

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetBwmMigrationTaskWriterWorkflowListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('empty') is not None:
            self.empty = m.get('empty')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('notEmpty') is not None:
            self.not_empty = m.get('notEmpty')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        return self

class GetBwmMigrationTaskWriterWorkflowListResponseBodyData(DaraModel):
    def __init__(
        self,
        cron: str = None,
        id: int = None,
        submit_detail: str = None,
        submit_status: str = None,
        target_workflow_id: str = None,
        target_workflow_name: str = None,
        task_node_count: int = None,
        workflow_id: str = None,
        workflow_name: str = None,
    ):
        # The cron expression.
        self.cron = cron
        # The database primary key ID.
        self.id = id
        # The submit failure error message.
        self.submit_detail = submit_detail
        # Filter by status. Valid values:
        # - WRT_INIT: Submit not started.
        # - WRT_RUN: Submitting.
        # - WRT_SUCC: All submitted successfully.
        # - WRT_FAIL: All submissions failed.
        # - WRT_PART_FAIL: Some submissions failed.
        # - DPY_SUCC: Published successfully.
        # - DPY_FAIL: Publish failed.
        self.submit_status = submit_status
        # The workflow ID written to the target side.
        self.target_workflow_id = target_workflow_id
        # The workflow name on the target side.
        self.target_workflow_name = target_workflow_name
        # The number of nodes.
        self.task_node_count = task_node_count
        # The actual workflow ID.
        self.workflow_id = workflow_id
        # The workflow name.
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.id is not None:
            result['id'] = self.id

        if self.submit_detail is not None:
            result['submitDetail'] = self.submit_detail

        if self.submit_status is not None:
            result['submitStatus'] = self.submit_status

        if self.target_workflow_id is not None:
            result['targetWorkflowId'] = self.target_workflow_id

        if self.target_workflow_name is not None:
            result['targetWorkflowName'] = self.target_workflow_name

        if self.task_node_count is not None:
            result['taskNodeCount'] = self.task_node_count

        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id

        if self.workflow_name is not None:
            result['workflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('submitDetail') is not None:
            self.submit_detail = m.get('submitDetail')

        if m.get('submitStatus') is not None:
            self.submit_status = m.get('submitStatus')

        if m.get('targetWorkflowId') is not None:
            self.target_workflow_id = m.get('targetWorkflowId')

        if m.get('targetWorkflowName') is not None:
            self.target_workflow_name = m.get('targetWorkflowName')

        if m.get('taskNodeCount') is not None:
            self.task_node_count = m.get('taskNodeCount')

        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')

        if m.get('workflowName') is not None:
            self.workflow_name = m.get('workflowName')

        return self

