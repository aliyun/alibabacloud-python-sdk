# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryApprovalInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryApprovalInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return the result of the interface execution.
        self.result = result
        # Indicates whether the API call was successful. Possible values are:
        # - true: success
        # - false: failure
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryApprovalInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryApprovalInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryApprovalInfoResponseBodyResultData] = None,
        page: int = None,
        page_size: int = None,
        start: int = None,
        total: int = None,
        total_pages: int = None,
    ):
        # Array of approval flow information.
        self.data = data
        # The current page number.
        self.page = page
        # The number of records requested per page.
        self.page_size = page_size
        # The starting position of the current page.
        self.start = start
        # The total number of items.
        self.total = total
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start is not None:
            result['Start'] = self.start

        if self.total is not None:
            result['Total'] = self.total

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryApprovalInfoResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class QueryApprovalInfoResponseBodyResultData(DaraModel):
    def __init__(
        self,
        applicant_id: str = None,
        applicant_name: str = None,
        application_id: str = None,
        apply_reason: str = None,
        approver_id: str = None,
        approver_name: str = None,
        delete_flag: bool = None,
        expire_date: int = None,
        flag_status: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        handle_reason: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        workspace_name: str = None,
    ):
        # Applicant\\"s user ID, qbi user ID.
        self.applicant_id = applicant_id
        # Applicant\\"s nickname.
        self.applicant_name = applicant_name
        # Application ID.
        self.application_id = application_id
        # Application reason.
        self.apply_reason = apply_reason
        # Approver\\"s user ID, qbi user ID.
        self.approver_id = approver_id
        # Approver\\"s nickname.
        self.approver_name = approver_name
        # Whether the resource has been deleted:
        # - true: Deleted
        # - false: Not deleted
        self.delete_flag = delete_flag
        # Permission expiration date, timestamp.
        self.expire_date = expire_date
        # Permission approval status:
        # - 0: Under review, corresponding to 0 in the request parameters
        # - 1: Approved, corresponding to 1 in the request parameters
        # - 2: Rejected, corresponding to 1 in the request parameters
        self.flag_status = flag_status
        # Application creation time, timestamp.
        self.gmt_create = gmt_create
        # Application modification time, timestamp.
        self.gmt_modified = gmt_modified
        # Handling reason.
        self.handle_reason = handle_reason
        # The ID of the resource for which permission is requested.
        self.resource_id = resource_id
        # The name of the resource for which permission is requested (e.g., report name, space name...).
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The name of the workspace.
        self.workspace_name = workspace_name

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

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason

        if self.approver_id is not None:
            result['ApproverId'] = self.approver_id

        if self.approver_name is not None:
            result['ApproverName'] = self.approver_name

        if self.delete_flag is not None:
            result['DeleteFlag'] = self.delete_flag

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.flag_status is not None:
            result['FlagStatus'] = self.flag_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.handle_reason is not None:
            result['HandleReason'] = self.handle_reason

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')

        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')

        if m.get('ApproverId') is not None:
            self.approver_id = m.get('ApproverId')

        if m.get('ApproverName') is not None:
            self.approver_name = m.get('ApproverName')

        if m.get('DeleteFlag') is not None:
            self.delete_flag = m.get('DeleteFlag')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('FlagStatus') is not None:
            self.flag_status = m.get('FlagStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HandleReason') is not None:
            self.handle_reason = m.get('HandleReason')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

