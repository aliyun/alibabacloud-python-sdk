# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateMFAAuthenticationSettingsRequest(DaraModel):
    def __init__(
        self,
        allowed_verification_types: List[str] = None,
        directory_id: str = None,
        mfaauthentication_settings: str = None,
        operation_for_risk_login: str = None,
    ):
        self.allowed_verification_types = allowed_verification_types
        # The directory ID.
        self.directory_id = directory_id
        # The global MFA settings. Valid values:
        # 
        # - Enabled: MFA verification is enabled for all users.
        # - Byuser: MFA verification depends on the individual MFA settings of each user. For more information about individual user MFA settings, see [UpdateUserMFAAuthenticationSettings](https://help.aliyun.com/document_detail/450135.html).
        # - Disabled: MFA verification is disabled for all users.
        # - OnlyRiskyLogin: MFA verification is required only for unusual logon attempts.
        self.mfaauthentication_settings = mfaauthentication_settings
        # The action to take when the MFA settings option is set to verify only for unusual logon attempts. Valid values:
        # 
        # - Autonomous: Users can skip MFA binding during unusual logon, but users who have already bound MFA must complete MFA verification.
        # - EnforceVerify: Users who have not bound MFA are required to bind it, and users who have already bound MFA must complete verification.
        self.operation_for_risk_login = operation_for_risk_login

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_verification_types is not None:
            result['AllowedVerificationTypes'] = self.allowed_verification_types

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.mfaauthentication_settings is not None:
            result['MFAAuthenticationSettings'] = self.mfaauthentication_settings

        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedVerificationTypes') is not None:
            self.allowed_verification_types = m.get('AllowedVerificationTypes')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MFAAuthenticationSettings') is not None:
            self.mfaauthentication_settings = m.get('MFAAuthenticationSettings')

        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')

        return self

