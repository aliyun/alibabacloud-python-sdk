# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id2MetaPeriodVerifyRequest(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
        validity_end_date: str = None,
        validity_start_date: str = None,
    ):
        # The ID card number.
        # 
        # - If paramType is set to normal, enter the ID card number in plaintext.
        # - If paramType is set to md5, the value is in the following format: first 6 digits of the ID card number (plaintext) + date of birth (ciphertext) + last 4 digits of the ID card number (plaintext).
        self.identify_num = identify_num
        # The parameter type. Valid values:
        # 
        # - normal: not encrypted.
        # - md5: MD5-encrypted.
        self.param_type = param_type
        # The name.
        # 
        # - paramType = normal: enter the name in plaintext.
        # - paramType = md5: the first character of the name is MD5-encrypted (32-bit lowercase MD5) + the remaining characters of the name in plaintext.
        self.user_name = user_name
        # The expiration date of the ID card validity period. Format: YYYYMMDD.
        self.validity_end_date = validity_end_date
        # The start date of the ID card validity period. Format: YYYYMMDD.
        self.validity_start_date = validity_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.validity_end_date is not None:
            result['ValidityEndDate'] = self.validity_end_date

        if self.validity_start_date is not None:
            result['ValidityStartDate'] = self.validity_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ValidityEndDate') is not None:
            self.validity_end_date = m.get('ValidityEndDate')

        if m.get('ValidityStartDate') is not None:
            self.validity_start_date = m.get('ValidityStartDate')

        return self

