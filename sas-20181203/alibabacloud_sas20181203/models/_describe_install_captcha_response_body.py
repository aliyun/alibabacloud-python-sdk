# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstallCaptchaResponseBody(DaraModel):
    def __init__(
        self,
        captcha_code: str = None,
        deadline: str = None,
        request_id: str = None,
    ):
        # The installation verification code for you to manually install the Security Center agent.
        self.captcha_code = captcha_code
        # The validity period of the installation verification code.
        # 
        # >  The installation verification code is valid only within the validity period. An expired installation verification code cannot be used to install the agent.
        self.deadline = deadline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captcha_code is not None:
            result['CaptchaCode'] = self.captcha_code

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptchaCode') is not None:
            self.captcha_code = m.get('CaptchaCode')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

