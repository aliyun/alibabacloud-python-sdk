# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class GetTrialInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trial_info: main_models.GetTrialInfoResponseBodyTrialInfo = None,
    ):
        # The return code. A value of 200 indicates success.
        self.code = code
        # The returned message. The value "successful" is returned on success. An error message is returned on failure.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success
        # The free trial properties. This parameter is returned only when a free trial record exists for the data source.
        self.trial_info = trial_info

    def validate(self):
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TrialInfo') is not None:
            temp_model = main_models.GetTrialInfoResponseBodyTrialInfo()
            self.trial_info = temp_model.from_map(m.get('TrialInfo'))

        return self

class GetTrialInfoResponseBodyTrialInfo(DaraModel):
    def __init__(
        self,
        keep_after_trial_expiration: bool = None,
        trial_backup_plan_quota: int = None,
        trial_expire_time: int = None,
        trial_start_time: int = None,
        trial_vault_quota: int = None,
        trial_vault_release_time: int = None,
    ):
        # Indicates whether the service is converted to pay-as-you-go after the free trial expires.
        self.keep_after_trial_expiration = keep_after_trial_expiration
        # The remaining number of free trial backup plans that can be created. The value 1 is returned if the free trial has not expired and no free trial backup plan has been created. Otherwise, the value 0 is returned.
        self.trial_backup_plan_quota = trial_backup_plan_quota
        # The expiration time of the free trial. UNIX timestamp, in seconds.
        self.trial_expire_time = trial_expire_time
        # The start time of the free trial. UNIX timestamp, in seconds.
        self.trial_start_time = trial_start_time
        # The remaining number of free trial backup vaults that can be created. The value 1 is returned if the free trial has not expired and no free trial backup vault has been created. Otherwise, the value 0 is returned.
        self.trial_vault_quota = trial_vault_quota
        # The release time of the free trial backup vault. UNIX timestamp, in seconds.
        self.trial_vault_release_time = trial_vault_release_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration

        if self.trial_backup_plan_quota is not None:
            result['TrialBackupPlanQuota'] = self.trial_backup_plan_quota

        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time

        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time

        if self.trial_vault_quota is not None:
            result['TrialVaultQuota'] = self.trial_vault_quota

        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')

        if m.get('TrialBackupPlanQuota') is not None:
            self.trial_backup_plan_quota = m.get('TrialBackupPlanQuota')

        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')

        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')

        if m.get('TrialVaultQuota') is not None:
            self.trial_vault_quota = m.get('TrialVaultQuota')

        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')

        return self

