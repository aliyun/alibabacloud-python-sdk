# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableResourceDirectoryRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        enable_mode: str = None,
        maname: str = None,
        masecure_mobile_phone: str = None,
        verification_code: str = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The mode in which you enable a resource directory. Valid values:
        # 
        # *   CurrentAccount: The current account is used to enable a resource directory.
        # *   NewManagementAccount: A newly created account is used to enable a resource directory. If you select this mode, you must configure the `MAName`, `MASecureMobilePhone`, and `VerificationCode` parameters.
        # 
        # This parameter is required.
        self.enable_mode = enable_mode
        # The name of the newly created account.
        # 
        # Specify the name in the `<Prefix>@rdadmin.aliyunid.com` format. The prefix can contain letters, digits, and special characters but cannot contain consecutive special characters. The prefix must start and end with a letter or digit. Valid special characters include underscores (`_`), periods (.), and hyphens (-). The prefix must be 2 to 50 characters in length.
        self.maname = maname
        # The mobile phone number that is bound to the newly created account.
        # 
        # If you leave this parameter empty, the mobile phone number that is bound to the current account is used. The mobile phone number you specify must be the same as the mobile phone number that you specify when you call the [SendVerificationCodeForEnableRD](~~SendVerificationCodeForEnableRD~~) operation to obtain a verification code.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # > Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        self.masecure_mobile_phone = masecure_mobile_phone
        # The verification code.
        # 
        # You can call the [SendVerificationCodeForEnableRD](~~SendVerificationCodeForEnableRD~~) operation to obtain the verification code.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_mode is not None:
            result['EnableMode'] = self.enable_mode

        if self.maname is not None:
            result['MAName'] = self.maname

        if self.masecure_mobile_phone is not None:
            result['MASecureMobilePhone'] = self.masecure_mobile_phone

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableMode') is not None:
            self.enable_mode = m.get('EnableMode')

        if m.get('MAName') is not None:
            self.maname = m.get('MAName')

        if m.get('MASecureMobilePhone') is not None:
            self.masecure_mobile_phone = m.get('MASecureMobilePhone')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        return self

