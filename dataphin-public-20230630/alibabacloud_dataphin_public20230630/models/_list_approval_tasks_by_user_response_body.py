# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListApprovalTasksByUserResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListApprovalTasksByUserResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend error details.
        self.message = message
        # The paging query result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListApprovalTasksByUserResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApprovalTasksByUserResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        task_list: List[main_models.ListApprovalTasksByUserResponseBodyPageResultTaskList] = None,
        total_count: int = None,
    ):
        # The list of approval tasks.
        self.task_list = task_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.ListApprovalTasksByUserResponseBodyPageResultTaskList()
                self.task_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApprovalTasksByUserResponseBodyPageResultTaskList(DaraModel):
    def __init__(
        self,
        applicant_id: str = None,
        applicant_name: str = None,
        approval_type: str = None,
        id: int = None,
        relation_type: str = None,
        source_system: str = None,
        status: str = None,
        submitted_at: str = None,
        title: str = None,
    ):
        # The applicant ID.
        self.applicant_id = applicant_id
        # The applicant name.
        self.applicant_name = applicant_name
        # The approval type.
        self.approval_type = approval_type
        # The approval flow ID.
        self.id = id
        # The relationship between the current user and the approval task.
        self.relation_type = relation_type
        # The source system.
        self.source_system = source_system
        # The approval status.
        self.status = status
        # The submission time.
        self.submitted_at = submitted_at
        # The task name.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id

        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name

        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.id is not None:
            result['Id'] = self.id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.source_system is not None:
            result['SourceSystem'] = self.source_system

        if self.status is not None:
            result['Status'] = self.status

        if self.submitted_at is not None:
            result['SubmittedAt'] = self.submitted_at

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')

        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')

        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SourceSystem') is not None:
            self.source_system = m.get('SourceSystem')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmittedAt') is not None:
            self.submitted_at = m.get('SubmittedAt')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

