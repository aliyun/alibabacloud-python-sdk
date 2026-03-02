# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGrantedRolesRequest(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        authorizer_type: str = None,
        enterprise_id: int = None,
        name: str = None,
    ):
        self.authorizer_id = authorizer_id
        self.authorizer_type = authorizer_type
        self.enterprise_id = enterprise_id
        self.name = name

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

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizerId') is not None:
            self.authorizer_id = m.get('authorizerId')

        if m.get('authorizerType') is not None:
            self.authorizer_type = m.get('authorizerType')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

