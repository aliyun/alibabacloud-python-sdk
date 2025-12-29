# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCardVerifyRequest(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        # Authentication request ID.
        # You must first call the initialization interface InitCardVerify to submit an authentication request in order to get the authentication request ID.
        # 
        # This parameter is required.
        self.certify_id = certify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        return self

