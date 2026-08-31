# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListApprovalTasksByUserRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListApprovalTasksByUserRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query conditions.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListApprovalTasksByUserRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListApprovalTasksByUserRequestListQuery(DaraModel):
    def __init__(
        self,
        approval_type: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        relation_type: str = None,
        status: str = None,
        submitted_from: str = None,
        submitted_to: str = None,
    ):
        # The approval task type. Valid values:
        # - APPROVE: Permission approval.
        # - MANAGE: Management.
        # - OTHERS: Others.
        # - ATOMIC: Atomic metric approval.
        # - BIZ_OBJECT: Business object approval.
        # - BIZ_PROCESS: Business process approval.
        # - PUBLISH_APPROVE: Publish approval.
        # - BASELINE_APPROVE: Baseline approval.
        # - CODE_REVIEW: Asset approval.
        # - OBJECT_CODE_REVIEW: Code review.
        # - STANDARD_APPROVAL: Standard online approval.
        # - BATCH_STANDARD_APPROVAL: Batch standard online approval.
        # - STANDARD_OFFLINE_APPROVAL: Standard offline approval.
        # - BATCH_STANDARD_OFFLINE_APPROVAL: Batch standard offline approval.
        # - PRIVILEGE_TRANSFER_APPROVAL: Permission transfer approval.
        # - QD_FEATURE_ONLINE: Label listing.
        # - QD_FEATURE_OFFLINE: Label delisting.
        # - QD_CLUSTER_ONLINE: Group online.
        # - QD_CLUSTER_OFFLINE: Group offline.
        # - QD_MEMBER_ADD_APP: Add member to application.
        # - QD_FEATURE_ADD_APP: Add label to application.
        # - QD_CLUSTER_ADD_APP: Add group to application.
        # - QD_FEATURE_ADD_PROJECT: Add label to project.
        # - QD_CLUSTER_ADD_PROJECT: Add group to project.
        # - TASK_DATA_DOWNLOAD: Data download.
        # - CUSTOM_OPERATE: Custom operation.
        # - PRIVACY_COMPUTING: Privacy-preserving computation.
        # - MDC_TOPIC_DIR_PUBLISH: Asset topic directory publish.
        # - ASSET_PUBLISH: Asset listing approval.
        # - ASSET_UN_PUBLISH: Asset delisting approval.
        # - APPLICATION_CREATE: Application creation approval.
        self.approval_type = approval_type
        # The keyword for fuzzy match on the task name.
        self.keyword = keyword
        # The page number, starting from 1. Default value: 1.
        self.page = page
        # The number of records per page. Default value: 20. Maximum value: 100. Values greater than 100 are automatically adjusted to 100.
        self.page_size = page_size
        # The relationship type between the current user and the approval task. This parameter is required. Valid values:
        # - SUBMITTED: Submitted by me.
        # - PENDING_APPROVAL: Pending my approval.
        # - PROCESSED: Processed by me.
        # 
        # This parameter is required.
        self.relation_type = relation_type
        # The approval status filter. Status filtering is not supported in the pending scenario. Valid values:
        # - APPROVING: Approving.
        # - APPROVED: Approved.
        # - REJECTED: Rejected.
        # - REVOKED: Revoked.
        self.status = status
        # The start of the submission time range, in the format yyyy-MM-dd HH:mm:ss.
        self.submitted_from = submitted_from
        # The end of the submission time range, in the format yyyy-MM-dd HH:mm:ss.
        self.submitted_to = submitted_to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.status is not None:
            result['Status'] = self.status

        if self.submitted_from is not None:
            result['SubmittedFrom'] = self.submitted_from

        if self.submitted_to is not None:
            result['SubmittedTo'] = self.submitted_to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmittedFrom') is not None:
            self.submitted_from = m.get('SubmittedFrom')

        if m.get('SubmittedTo') is not None:
            self.submitted_to = m.get('SubmittedTo')

        return self

