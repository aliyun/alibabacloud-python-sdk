# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateApprovalStatusResponseBody(DaraModel):
    def __init__(
        self,
        approval: List[main_models.UpdateApprovalStatusResponseBodyApproval] = None,
        request_id: str = None,
    ):
        self.approval = approval
        self.request_id = request_id

    def validate(self):
        if self.approval:
            for v1 in self.approval:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Approval'] = []
        if self.approval is not None:
            for k1 in self.approval:
                result['Approval'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approval = []
        if m.get('Approval') is not None:
            for k1 in m.get('Approval'):
                temp_model = main_models.UpdateApprovalStatusResponseBodyApproval()
                self.approval.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateApprovalStatusResponseBodyApproval(DaraModel):
    def __init__(
        self,
        approval_detail: str = None,
        approval_id: str = None,
        approval_progresses: List[main_models.UpdateApprovalStatusResponseBodyApprovalApprovalProgresses] = None,
        create_time: str = None,
        creator_dev_tag: str = None,
        creator_user_id: str = None,
        end_timestamp: int = None,
        policy_type: str = None,
        process_id: str = None,
        process_name: str = None,
        reason: str = None,
        schema_content: str = None,
        schema_id: str = None,
        schema_name: str = None,
        status: str = None,
    ):
        self.approval_detail = approval_detail
        self.approval_id = approval_id
        self.approval_progresses = approval_progresses
        self.create_time = create_time
        self.creator_dev_tag = creator_dev_tag
        self.creator_user_id = creator_user_id
        self.end_timestamp = end_timestamp
        self.policy_type = policy_type
        self.process_id = process_id
        self.process_name = process_name
        self.reason = reason
        self.schema_content = schema_content
        self.schema_id = schema_id
        self.schema_name = schema_name
        self.status = status

    def validate(self):
        if self.approval_progresses:
            for v1 in self.approval_progresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_detail is not None:
            result['ApprovalDetail'] = self.approval_detail

        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        result['ApprovalProgresses'] = []
        if self.approval_progresses is not None:
            for k1 in self.approval_progresses:
                result['ApprovalProgresses'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_dev_tag is not None:
            result['CreatorDevTag'] = self.creator_dev_tag

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.schema_content is not None:
            result['SchemaContent'] = self.schema_content

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalDetail') is not None:
            self.approval_detail = m.get('ApprovalDetail')

        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        self.approval_progresses = []
        if m.get('ApprovalProgresses') is not None:
            for k1 in m.get('ApprovalProgresses'):
                temp_model = main_models.UpdateApprovalStatusResponseBodyApprovalApprovalProgresses()
                self.approval_progresses.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorDevTag') is not None:
            self.creator_dev_tag = m.get('CreatorDevTag')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SchemaContent') is not None:
            self.schema_content = m.get('SchemaContent')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateApprovalStatusResponseBodyApprovalApprovalProgresses(DaraModel):
    def __init__(
        self,
        action: str = None,
        comment: str = None,
        executor: str = None,
        operators: List[main_models.UpdateApprovalStatusResponseBodyApprovalApprovalProgressesOperators] = None,
        status: str = None,
        timestamp: int = None,
    ):
        self.action = action
        self.comment = comment
        self.executor = executor
        self.operators = operators
        self.status = status
        self.timestamp = timestamp

    def validate(self):
        if self.operators:
            for v1 in self.operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.executor is not None:
            result['Executor'] = self.executor

        result['Operators'] = []
        if self.operators is not None:
            for k1 in self.operators:
                result['Operators'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        self.operators = []
        if m.get('Operators') is not None:
            for k1 in m.get('Operators'):
                temp_model = main_models.UpdateApprovalStatusResponseBodyApprovalApprovalProgressesOperators()
                self.operators.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class UpdateApprovalStatusResponseBodyApprovalApprovalProgressesOperators(DaraModel):
    def __init__(
        self,
        sase_user_id: str = None,
        username: str = None,
    ):
        self.sase_user_id = sase_user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

