# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateEmailRequest(DaraModel):
    def __init__(
        self,
        check_graylist: bool = None,
        email: str = None,
        probe_type: str = None,
        timeout: int = None,
    ):
        # Specifies whether to check the graylist. Default value: false. Results will be sent as asynchronous notifications through EventBridge.
        self.check_graylist = check_graylist
        # The email address to validate
        # 
        # This parameter is required.
        self.email = email
        # The detection type:
        # 
        # - FULL: Enables all detection capabilities, including SMTP probing. Since SMTP probing involves remote connections, the overall latency is higher. This is suitable for scenarios that are not sensitive to response time. Each detection consumes 1 address validation quota.
        # - BASIC_ONLY: Enables all detection capabilities except SMTP probing, with low latency. This is suitable for scenarios sensitive to response time, such as real-time validation during registration to check whether an email address is a disposable email or an abnormal address such as MX forwarding, to defend against mass registration by malicious actors. Each detection consumes 1/3 of an address validation quota.
        self.probe_type = probe_type
        # Timeout period. Default value: 60 seconds.
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

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckGraylist') is not None:
            self.check_graylist = m.get('CheckGraylist')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

