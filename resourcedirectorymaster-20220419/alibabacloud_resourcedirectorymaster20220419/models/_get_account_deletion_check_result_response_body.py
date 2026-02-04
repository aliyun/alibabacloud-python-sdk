# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class GetAccountDeletionCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        account_deletion_check_result_info: main_models.GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo = None,
        request_id: str = None,
    ):
        # The result of the deletion check for the member.
        self.account_deletion_check_result_info = account_deletion_check_result_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account_deletion_check_result_info:
            self.account_deletion_check_result_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_deletion_check_result_info is not None:
            result['AccountDeletionCheckResultInfo'] = self.account_deletion_check_result_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDeletionCheckResultInfo') is not None:
            temp_model = main_models.GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo()
            self.account_deletion_check_result_info = temp_model.from_map(m.get('AccountDeletionCheckResultInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo(DaraModel):
    def __init__(
        self,
        abandonable_checks: List[main_models.GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks] = None,
        allow_delete: str = None,
        not_allow_reason: List[main_models.GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason] = None,
        status: str = None,
    ):
        # The check items that you can choose to ignore for the member deletion.
        # 
        # > This parameter may be returned if the value of AllowDelete is true.
        self.abandonable_checks = abandonable_checks
        # Indicates whether the member can be deleted. Valid values:
        # 
        # *   true: The member can be deleted.
        # *   false: The member cannot be deleted.
        self.allow_delete = allow_delete
        # The reasons why the member cannot be deleted.
        # 
        # > This parameter is returned only if the value of AllowDelete is false.
        self.not_allow_reason = not_allow_reason
        # The status of the check. Valid values:
        # 
        # *   PreCheckComplete: The check is complete.
        # *   PreChecking: The check is in progress.
        self.status = status

    def validate(self):
        if self.abandonable_checks:
            for v1 in self.abandonable_checks:
                 if v1:
                    v1.validate()
        if self.not_allow_reason:
            for v1 in self.not_allow_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AbandonableChecks'] = []
        if self.abandonable_checks is not None:
            for k1 in self.abandonable_checks:
                result['AbandonableChecks'].append(k1.to_map() if k1 else None)

        if self.allow_delete is not None:
            result['AllowDelete'] = self.allow_delete

        result['NotAllowReason'] = []
        if self.not_allow_reason is not None:
            for k1 in self.not_allow_reason:
                result['NotAllowReason'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abandonable_checks = []
        if m.get('AbandonableChecks') is not None:
            for k1 in m.get('AbandonableChecks'):
                temp_model = main_models.GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks()
                self.abandonable_checks.append(temp_model.from_map(k1))

        if m.get('AllowDelete') is not None:
            self.allow_delete = m.get('AllowDelete')

        self.not_allow_reason = []
        if m.get('NotAllowReason') is not None:
            for k1 in m.get('NotAllowReason'):
                temp_model = main_models.GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason()
                self.not_allow_reason.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        check_name: str = None,
        description: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The name of the cloud service to which the check item belongs.
        self.check_name = check_name
        # The description of the check item.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        check_name: str = None,
        description: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The name of the cloud service to which the check item belongs.
        self.check_name = check_name
        # The description of the check item.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

