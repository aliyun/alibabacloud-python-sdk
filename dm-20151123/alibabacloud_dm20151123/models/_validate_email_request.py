# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateEmailRequest(DaraModel):
    def __init__(
        self,
        check_graylist: bool = None,
        email: str = None,
        timeout: int = None,
    ):
        # Specifies whether to check the graylist. The default value is false. The result is sent through an asynchronous notification message from EventBridge.
        self.check_graylist = check_graylist
        # The email address to validate.
        # 
        # This parameter is required.
        self.email = email
        # The timeout period. The default value is 60 seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_graylist is not None:
            result['CheckGraylist'] = self.check_graylist

        if self.email is not None:
            result['Email'] = self.email

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckGraylist') is not None:
            self.check_graylist = m.get('CheckGraylist')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

