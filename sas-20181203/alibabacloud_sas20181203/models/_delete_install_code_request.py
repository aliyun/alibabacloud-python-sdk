# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstallCodeRequest(DaraModel):
    def __init__(
        self,
        captcha_code: str = None,
    ):
        # The installation command.
        # 
        # >  You can call the [DescribeInstallCodes](~~DescribeInstallCodes~~) operation to query installation commands.
        # 
        # This parameter is required.
        self.captcha_code = captcha_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captcha_code is not None:
            result['CaptchaCode'] = self.captcha_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptchaCode') is not None:
            self.captcha_code = m.get('CaptchaCode')

        return self

