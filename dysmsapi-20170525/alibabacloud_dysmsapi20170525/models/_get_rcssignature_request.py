# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRCSSignatureRequest(DaraModel):
    def __init__(
        self,
        sign_name: str = None,
    ):
        # 签名名称
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        return self

