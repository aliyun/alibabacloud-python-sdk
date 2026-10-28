# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagerInfoByAuthCodeRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
    ):
        # The authorization code. The code is obtained by the authorized enterprise account by calling CreateAuthCode and then used by the corresponding service provider account within the validity period. If the calling account does not match the service provider specified by the authorization code, the request is rejected.
        # 
        # This parameter is required.
        self.auth_code = auth_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        return self

