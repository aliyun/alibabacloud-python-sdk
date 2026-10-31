# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetApprovalTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        detail_info: main_models.GetApprovalTaskDetailResponseBodyDetailInfo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The approval task details.
        self.detail_info = detail_info
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend response exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DetailInfo') is not None:
            temp_model = main_models.GetApprovalTaskDetailResponseBodyDetailInfo()
            self.detail_info = temp_model.from_map(m.get('DetailInfo'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetApprovalTaskDetailResponseBodyDetailInfo(DaraModel):
    def __init__(
        self,
        applicant_id: str = None,
        applicant_name: str = None,
        approval_type: str = None,
        approve_process_steps: List[main_models.GetApprovalTaskDetailResponseBodyDetailInfoApproveProcessSteps] = None,
        biz_content: str = None,
        finished_at: str = None,
        id: int = None,
        source_system: str = None,
        status: str = None,
        submitted_at: str = None,
        title: str = None,
    ):
        # The ID of the applicant.
        self.applicant_id = applicant_id
        # The name of the applicant.
        self.applicant_name = applicant_name
        # The approval type. Valid values:
        # - APPROVE: Permission approval.
        # - MANAGE: Management.
        # - OTHERS: Others.
        # - ATOMIC: Atomic metric approval.
        # - BIZ_OBJECT: Business object approval.
        # - BIZ_PROCESS: Business activity approval.
        # - PUBLISH_APPROVE: Publish approval.
        # - BASELINE_APPROVE: Baseline approval.
        # - CODE_REVIEW: Asset approval.
        # - OBJECT_CODE_REVIEW: Code review.
        # - STANDARD_APPROVAL: Standard online approval.
        # - BATCH_STANDARD_APPROVAL: Batch standard online approval.
        # - STANDARD_OFFLINE_APPROVAL: Standard offline approval.
        # - BATCH_STANDARD_OFFLINE_APPROVAL: Batch standard offline approval.
        # - PRIVILEGE_TRANSFER_APPROVAL: Privilege transfer approval.
        # - QD_FEATURE_ONLINE: Tag listing.
        # - QD_FEATURE_OFFLINE: Tag delisting.
        # - QD_CLUSTER_ONLINE: Group online.
        # - QD_CLUSTER_OFFLINE: Group offline.
        # - QD_MEMBER_ADD_APP: Member added to application.
        # - QD_FEATURE_ADD_APP: Tag added to application.
        # - QD_CLUSTER_ADD_APP: Group added to application.
        # - QD_FEATURE_ADD_PROJECT: Tag added to project.
        # - QD_CLUSTER_ADD_PROJECT: Group added to project.
        # - TASK_DATA_DOWNLOAD: Data download.
        # - CUSTOM_OPERATE: Custom operation.
        # - PRIVACY_COMPUTING: Privacy-preserving computation.
        # - MDC_TOPIC_DIR_PUBLISH: Asset topic directory publishing.
        # - ASSET_PUBLISH: Asset listing approval.
        # - ASSET_UN_PUBLISH: Asset delisting approval.
        # - APPLICATION_CREATE: Application creation approval.
        self.approval_type = approval_type
        # The list of approval process steps.
        self.approve_process_steps = approve_process_steps
        # The JSON string of the task details.
        self.biz_content = biz_content
        # The completion time. Format: yyyy-MM-dd HH:mm:ss. This field is empty if the task is not completed.
        self.finished_at = finished_at
        # The approval flow ID.
        self.id = id
        # The source system.
        self.source_system = source_system
        # The approval status. Valid values:
        # - APPROVING: Approving.
        # - APPROVED: Approved.
        # - REJECTED: Rejected.
        # - REVOKED: Revoked.
        self.status = status
        # The submission time. Format: yyyy-MM-dd HH:mm:ss.
        self.submitted_at = submitted_at
        # The task name.
        self.title = title

    def validate(self):
        if self.approve_process_steps:
            for v1 in self.approve_process_steps:
                 if v1:
                    v1.validate()

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

        result['ApproveProcessSteps'] = []
        if self.approve_process_steps is not None:
            for k1 in self.approve_process_steps:
                result['ApproveProcessSteps'].append(k1.to_map() if k1 else None)

        if self.biz_content is not None:
            result['BizContent'] = self.biz_content

        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at

        if self.id is not None:
            result['Id'] = self.id

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

        self.approve_process_steps = []
        if m.get('ApproveProcessSteps') is not None:
            for k1 in m.get('ApproveProcessSteps'):
                temp_model = main_models.GetApprovalTaskDetailResponseBodyDetailInfoApproveProcessSteps()
                self.approve_process_steps.append(temp_model.from_map(k1))

        if m.get('BizContent') is not None:
            self.biz_content = m.get('BizContent')

        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SourceSystem') is not None:
            self.source_system = m.get('SourceSystem')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmittedAt') is not None:
            self.submitted_at = m.get('SubmittedAt')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetApprovalTaskDetailResponseBodyDetailInfoApproveProcessSteps(DaraModel):
    def __init__(
        self,
        approve_user_ids: str = None,
        approve_user_names: str = None,
        operate_time: str = None,
        operate_user_id: str = None,
        operate_user_name: str = None,
        operation: str = None,
        process_step_name: str = None,
        reason: str = None,
        result: str = None,
    ):
        # The list of candidate approver IDs.
        self.approve_user_ids = approve_user_ids
        # The list of candidate approver names.
        self.approve_user_names = approve_user_names
        # The operation time. Format: yyyy-MM-dd HH:mm:ss.
        self.operate_time = operate_time
        # The ID of the operator.
        self.operate_user_id = operate_user_id
        # The name of the operator.
        self.operate_user_name = operate_user_name
        # The operation.
        self.operation = operation
        # The step name.
        self.process_step_name = process_step_name
        # The approval comment.
        self.reason = reason
        # The approval result.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_user_ids is not None:
            result['ApproveUserIds'] = self.approve_user_ids

        if self.approve_user_names is not None:
            result['ApproveUserNames'] = self.approve_user_names

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.operate_user_id is not None:
            result['OperateUserId'] = self.operate_user_id

        if self.operate_user_name is not None:
            result['OperateUserName'] = self.operate_user_name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.process_step_name is not None:
            result['ProcessStepName'] = self.process_step_name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveUserIds') is not None:
            self.approve_user_ids = m.get('ApproveUserIds')

        if m.get('ApproveUserNames') is not None:
            self.approve_user_names = m.get('ApproveUserNames')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('OperateUserId') is not None:
            self.operate_user_id = m.get('OperateUserId')

        if m.get('OperateUserName') is not None:
            self.operate_user_name = m.get('OperateUserName')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('ProcessStepName') is not None:
            self.process_step_name = m.get('ProcessStepName')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

