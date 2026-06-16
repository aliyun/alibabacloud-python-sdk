# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderStatusCheckJobResponseBody(DaraModel):
    def __init__(
        self,
        identity_provider_status_check_job: main_models.GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJob = None,
        request_id: str = None,
    ):
        # The information about the IdP status check job.
        self.identity_provider_status_check_job = identity_provider_status_check_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.identity_provider_status_check_job:
            self.identity_provider_status_check_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_status_check_job is not None:
            result['IdentityProviderStatusCheckJob'] = self.identity_provider_status_check_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderStatusCheckJob') is not None:
            temp_model = main_models.GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJob()
            self.identity_provider_status_check_job = temp_model.from_map(m.get('IdentityProviderStatusCheckJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJob(DaraModel):
    def __init__(
        self,
        check_result: str = None,
        end_time: int = None,
        identity_provider_id: str = None,
        identity_provider_status_check_job_id: str = None,
        instance_id: str = None,
        job_check_items: List[main_models.GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJobJobCheckItems] = None,
        start_time: int = None,
        status: str = None,
    ):
        # The result of the check task.
        self.check_result = check_result
        # The end time.
        self.end_time = end_time
        # The ID of the IdP.
        self.identity_provider_id = identity_provider_id
        # The ID of the IdP status check job.
        self.identity_provider_status_check_job_id = identity_provider_status_check_job_id
        # The instance ID.
        self.instance_id = instance_id
        # The results of the status check subtasks.
        self.job_check_items = job_check_items
        # The start time.
        self.start_time = start_time
        # The status of the check task.
        self.status = status

    def validate(self):
        if self.job_check_items:
            for v1 in self.job_check_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.identity_provider_status_check_job_id is not None:
            result['IdentityProviderStatusCheckJobId'] = self.identity_provider_status_check_job_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['JobCheckItems'] = []
        if self.job_check_items is not None:
            for k1 in self.job_check_items:
                result['JobCheckItems'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IdentityProviderStatusCheckJobId') is not None:
            self.identity_provider_status_check_job_id = m.get('IdentityProviderStatusCheckJobId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.job_check_items = []
        if m.get('JobCheckItems') is not None:
            for k1 in m.get('JobCheckItems'):
                temp_model = main_models.GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJobJobCheckItems()
                self.job_check_items.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJobJobCheckItems(DaraModel):
    def __init__(
        self,
        error_reason: main_models.GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJobJobCheckItemsErrorReason = None,
        major_check_item: str = None,
        minor_check_item: str = None,
        result: str = None,
    ):
        # The reason for the error.
        self.error_reason = error_reason
        # The major check item.
        self.major_check_item = major_check_item
        # The minor check item.
        self.minor_check_item = minor_check_item
        # The result.
        self.result = result

    def validate(self):
        if self.error_reason:
            self.error_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_reason is not None:
            result['ErrorReason'] = self.error_reason.to_map()

        if self.major_check_item is not None:
            result['MajorCheckItem'] = self.major_check_item

        if self.minor_check_item is not None:
            result['MinorCheckItem'] = self.minor_check_item

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorReason') is not None:
            temp_model = main_models.GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJobJobCheckItemsErrorReason()
            self.error_reason = temp_model.from_map(m.get('ErrorReason'))

        if m.get('MajorCheckItem') is not None:
            self.major_check_item = m.get('MajorCheckItem')

        if m.get('MinorCheckItem') is not None:
            self.minor_check_item = m.get('MinorCheckItem')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class GetIdentityProviderStatusCheckJobResponseBodyIdentityProviderStatusCheckJobJobCheckItemsErrorReason(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_level: str = None,
        error_message: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error level.
        self.error_level = error_level
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_level is not None:
            result['ErrorLevel'] = self.error_level

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorLevel') is not None:
            self.error_level = m.get('ErrorLevel')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

