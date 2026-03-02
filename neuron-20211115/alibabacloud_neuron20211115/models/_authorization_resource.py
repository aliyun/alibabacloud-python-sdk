# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizationResource(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        authorizer_type: str = None,
    ):
        # This parameter is required.
        self.authorizer_id = authorizer_id
        # This parameter is required.
        self.authorizer_type = authorizer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorizer_id is not None:
            result['authorizerId'] = self.authorizer_id

        if self.authorizer_type is not None:
            result['authorizerType'] = self.authorizer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizerId') is not None:
            self.authorizer_id = m.get('authorizerId')

        if m.get('authorizerType') is not None:
            self.authorizer_type = m.get('authorizerType')

        return self

