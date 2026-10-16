# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableResourceDirectoryRequest(DaraModel):
    def __init__(
        self,
        enable_mode: str = None,
        maname: str = None,
        masecure_mobile_phone: str = None,
        verification_code: str = None,
    ):
        # The method used to enable the resource directory. Valid values:
        # 
        # - CurrentAccount: enables the resource directory by using the current logon account.
        # - NewManagementAccount: enables the resource directory by creating a new management account. If you select this method, you must configure `MAName`, `MASecureMobilePhone`, and `VerificationCode`.
        # 
        # This parameter is required.
        self.enable_mode = enable_mode
        # The name of the new management account.
        # 
        # Format: `<Prefix>@rdadmin.aliyunid.com`. The prefix can contain letters, digits, and the special characters `_.-`. The prefix must start and end with a letter or digit, and cannot contain consecutive special characters. The prefix must be 2 to 50 characters in length.
        self.maname = maname
        # The secure phone number of the new management account.
        # 
        # If you leave this parameter empty, the secure phone number of the current logon account is used. The phone number must be the same as the one used to authenticate and obtain the verification code in [SendVerificationCodeForEnableRD](https://help.aliyun.com/document_detail/364248.html).
        # 
        # Format: `<Country code>-<Phone number>`.
        # 
        # <props="intl">
        # > Phone numbers from the Chinese mainland in the format `86-<Phone number>` are not supported.
        # 
        # 
        # <props="china">
        # > Only phone numbers from the Chinese mainland in the format `86-<Phone number>` are supported.
        self.masecure_mobile_phone = masecure_mobile_phone
        # The verification code.
        # 
        # You can call [SendVerificationCodeForEnableRD](https://help.aliyun.com/document_detail/364248.html) to obtain the verification code.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('EnableMode') is not None:
            self.enable_mode = m.get('EnableMode')

        if m.get('MAName') is not None:
            self.maname = m.get('MAName')

        if m.get('MASecureMobilePhone') is not None:
            self.masecure_mobile_phone = m.get('MASecureMobilePhone')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        return self

