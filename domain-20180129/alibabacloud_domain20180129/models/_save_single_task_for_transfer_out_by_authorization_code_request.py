# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForTransferOutByAuthorizationCodeRequest(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        domain_name: str = None,
    ):
        # Schema of Response
        # 
        # This parameter is required.
        self.authorization_code = authorization_code
        # The transfer key.
        # 
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

