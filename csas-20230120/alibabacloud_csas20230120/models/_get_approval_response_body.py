# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetApprovalResponseBody(DaraModel):
    def __init__(
        self,
        approval: List[main_models.GetApprovalResponseBodyApproval] = None,
        request_id: str = None,
    ):
        # The approval instance.
        self.approval = approval
        # The request ID.
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
                temp_model = main_models.GetApprovalResponseBodyApproval()
                self.approval.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApprovalResponseBodyApproval(DaraModel):
    def __init__(
        self,
        approval_detail: str = None,
        approval_id: str = None,
        approval_progresses: List[main_models.GetApprovalResponseBodyApprovalApprovalProgresses] = None,
        approval_type: int = None,
        backend_report_detail: main_models.GetApprovalResponseBodyApprovalBackendReportDetail = None,
        create_time: str = None,
        create_time_unix: int = None,
        creator_department: str = None,
        creator_dev_tag: str = None,
        creator_user_id: str = None,
        creator_username: str = None,
        effect_status: str = None,
        end_timestamp: int = None,
        policy_type: str = None,
        process_id: str = None,
        process_name: str = None,
        reason: str = None,
        report_type: str = None,
        schema_content: str = None,
        schema_id: str = None,
        schema_name: str = None,
        status: str = None,
        validity_type: str = None,
    ):
        # The details of the approval instance.
        self.approval_detail = approval_detail
        # The approval instance ID.
        self.approval_id = approval_id
        # The list of approval progress nodes.
        self.approval_progresses = approval_progresses
        self.approval_type = approval_type
        # The backend report details. This parameter is returned only when ReportType is set to BackendReport.
        self.backend_report_detail = backend_report_detail
        # The time when the approval instance was created.
        self.create_time = create_time
        self.create_time_unix = create_time_unix
        # The department of the user who created the approval instance.
        self.creator_department = creator_department
        # The device ID of the terminal that created the approval instance.
        self.creator_dev_tag = creator_dev_tag
        # The ID of the user who created the approval instance.
        self.creator_user_id = creator_user_id
        # The username of the user who created the approval instance.
        self.creator_username = creator_username
        # The effective status of the report. Enabled indicates that the report is active, and Expired indicates that the report has expired.
        self.effect_status = effect_status
        # The expiration time of the approval instance. The value is a UNIX timestamp in seconds.
        self.end_timestamp = end_timestamp
        # The policy type associated with the approval instance. Valid values:
        # - **DomainBlacklist**: Domain name blacklist.
        # - **DomainWhitelist**: Domain name whitelist.
        # - **SoftwareBlock**: Software blocking.
        # - **AppUninstall**: Agent uninstallation.
        # - **DlpSend**: File outbound transfer.
        # - **PeripheralBlock**: Peripheral device control.
        self.policy_type = policy_type
        # The ID of the process associated with the approval instance.
        self.process_id = process_id
        # The name of the process associated with the approval instance.
        self.process_name = process_name
        # The reason for creating the approval instance.
        self.reason = reason
        # The report type. ApprovalReport indicates an approval report, and BackendReport indicates a backend report.
        self.report_type = report_type
        # The content of the template associated with the approval instance.
        self.schema_content = schema_content
        # The ID of the template associated with the approval instance.
        self.schema_id = schema_id
        # The name of the template associated with the approval instance.
        self.schema_name = schema_name
        # The instance status. Valid values:
        # - **Pending**: Pending approval.
        # - **Approved**: Approved.
        # - **Rejected**: Denied.
        # - **Revoked**: Revoked.
        # - **Expired**: Expired.
        self.status = status
        # The validity duration type. When the value is Permanent, EndTimestamp returns 0.
        self.validity_type = validity_type

    def validate(self):
        if self.approval_progresses:
            for v1 in self.approval_progresses:
                 if v1:
                    v1.validate()
        if self.backend_report_detail:
            self.backend_report_detail.validate()

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

        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.backend_report_detail is not None:
            result['BackendReportDetail'] = self.backend_report_detail.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_unix is not None:
            result['CreateTimeUnix'] = self.create_time_unix

        if self.creator_department is not None:
            result['CreatorDepartment'] = self.creator_department

        if self.creator_dev_tag is not None:
            result['CreatorDevTag'] = self.creator_dev_tag

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.creator_username is not None:
            result['CreatorUsername'] = self.creator_username

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

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

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.schema_content is not None:
            result['SchemaContent'] = self.schema_content

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.status is not None:
            result['Status'] = self.status

        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type

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
                temp_model = main_models.GetApprovalResponseBodyApprovalApprovalProgresses()
                self.approval_progresses.append(temp_model.from_map(k1))

        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('BackendReportDetail') is not None:
            temp_model = main_models.GetApprovalResponseBodyApprovalBackendReportDetail()
            self.backend_report_detail = temp_model.from_map(m.get('BackendReportDetail'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeUnix') is not None:
            self.create_time_unix = m.get('CreateTimeUnix')

        if m.get('CreatorDepartment') is not None:
            self.creator_department = m.get('CreatorDepartment')

        if m.get('CreatorDevTag') is not None:
            self.creator_dev_tag = m.get('CreatorDevTag')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('CreatorUsername') is not None:
            self.creator_username = m.get('CreatorUsername')

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

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

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('SchemaContent') is not None:
            self.schema_content = m.get('SchemaContent')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class GetApprovalResponseBodyApprovalBackendReportDetail(DaraModel):
    def __init__(
        self,
        associated_policy_name: str = None,
        associated_policy_type: str = None,
        remark: str = None,
        report_object: Any = None,
        target_user: main_models.GetApprovalResponseBodyApprovalBackendReportDetailTargetUser = None,
    ):
        self.associated_policy_name = associated_policy_name
        self.associated_policy_type = associated_policy_type
        self.remark = remark
        self.report_object = report_object
        self.target_user = target_user

    def validate(self):
        if self.target_user:
            self.target_user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_policy_name is not None:
            result['AssociatedPolicyName'] = self.associated_policy_name

        if self.associated_policy_type is not None:
            result['AssociatedPolicyType'] = self.associated_policy_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.report_object is not None:
            result['ReportObject'] = self.report_object

        if self.target_user is not None:
            result['TargetUser'] = self.target_user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPolicyName') is not None:
            self.associated_policy_name = m.get('AssociatedPolicyName')

        if m.get('AssociatedPolicyType') is not None:
            self.associated_policy_type = m.get('AssociatedPolicyType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ReportObject') is not None:
            self.report_object = m.get('ReportObject')

        if m.get('TargetUser') is not None:
            temp_model = main_models.GetApprovalResponseBodyApprovalBackendReportDetailTargetUser()
            self.target_user = temp_model.from_map(m.get('TargetUser'))

        return self

class GetApprovalResponseBodyApprovalBackendReportDetailTargetUser(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        username: str = None,
    ):
        self.user_id = user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetApprovalResponseBodyApprovalApprovalProgresses(DaraModel):
    def __init__(
        self,
        action: str = None,
        comment: str = None,
        executor: str = None,
        operators: List[main_models.GetApprovalResponseBodyApprovalApprovalProgressesOperators] = None,
        status: str = None,
        timestamp: int = None,
    ):
        # The action performed on the approval progress node. Valid values:
        # - **Approve**: Approved.
        # - **Reject**: Rejected.
        # - **Revoke**: Revoked.
        # - **Comment**: Commented.
        self.action = action
        # The comment on the approval progress node.
        self.comment = comment
        # The executor ID of the approval progress node.
        self.executor = executor
        # The list of operators for the approval progress node.
        self.operators = operators
        # The status of the approval progress node. Valid values:
        # - **Pending**: Pending approval.
        # - **Approved**: Approved.
        # - **Rejected**: Rejected.
        # - **Revoked**: Revoked.
        self.status = status
        # The time when the action was performed on the approval progress node. The value is a UNIX timestamp in seconds.
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
                temp_model = main_models.GetApprovalResponseBodyApprovalApprovalProgressesOperators()
                self.operators.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetApprovalResponseBodyApprovalApprovalProgressesOperators(DaraModel):
    def __init__(
        self,
        sase_user_id: str = None,
        username: str = None,
    ):
        # The ID of the operator for the approval progress node.
        self.sase_user_id = sase_user_id
        # The username of the operator for the approval progress node.
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

