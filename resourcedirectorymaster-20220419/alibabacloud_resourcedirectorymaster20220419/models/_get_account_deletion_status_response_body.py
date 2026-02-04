# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class GetAccountDeletionStatusResponseBody(DaraModel):
    def __init__(
        self,
        rd_account_deletion_status: main_models.GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus = None,
        request_id: str = None,
    ):
        # The deletion status of the member.
        self.rd_account_deletion_status = rd_account_deletion_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.rd_account_deletion_status:
            self.rd_account_deletion_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rd_account_deletion_status is not None:
            result['RdAccountDeletionStatus'] = self.rd_account_deletion_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RdAccountDeletionStatus') is not None:
            temp_model = main_models.GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus()
            self.rd_account_deletion_status = temp_model.from_map(m.get('RdAccountDeletionStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        deletion_time: str = None,
        deletion_type: str = None,
        fail_reason_list: List[main_models.GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList] = None,
        status: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The start time of the deletion.
        self.create_time = create_time
        # The end time of the deletion.
        # 
        # This parameter is required.
        self.deletion_time = deletion_time
        # The type of the deletion. Valid values:
        # 
        # *   0: direct deletion. If the member does not have pay-as-you-go resources that are purchased within the previous 30 days, the system directly deletes the member.
        # *   1: deletion with a silence period. If the member has pay-as-you-go resources that are purchased within the previous 30 days, the member enters a silence period of 45 days. The system starts to delete the member until the silence period ends. For more information about the silence period, see [What is the silence period for member deletion?](https://help.aliyun.com/document_detail/446079.html)
        self.deletion_type = deletion_type
        # The reasons why the member fails to be deleted.
        self.fail_reason_list = fail_reason_list
        # The status. Valid values:
        # 
        # *   Success: The member is deleted.
        # *   Checking: A deletion check is being performed for the member.
        # *   Deleting: The member is being deleted.
        # *   CheckFailed: The deletion check for the member fails.
        # *   DeleteFailed: The member fails to be deleted.
        self.status = status

    def validate(self):
        if self.fail_reason_list:
            for v1 in self.fail_reason_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_time is not None:
            result['DeletionTime'] = self.deletion_time

        if self.deletion_type is not None:
            result['DeletionType'] = self.deletion_type

        result['FailReasonList'] = []
        if self.fail_reason_list is not None:
            for k1 in self.fail_reason_list:
                result['FailReasonList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionTime') is not None:
            self.deletion_time = m.get('DeletionTime')

        if m.get('DeletionType') is not None:
            self.deletion_type = m.get('DeletionType')

        self.fail_reason_list = []
        if m.get('FailReasonList') is not None:
            for k1 in m.get('FailReasonList'):
                temp_model = main_models.GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList()
                self.fail_reason_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The description of the check item.
        self.description = description
        # The name of the cloud service to which the check item belongs.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

