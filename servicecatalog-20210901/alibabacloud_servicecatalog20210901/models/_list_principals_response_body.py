# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListPrincipalsResponseBody(DaraModel):
    def __init__(
        self,
        principals: List[main_models.ListPrincipalsResponseBodyPrincipals] = None,
        request_id: str = None,
    ):
        # The RAM entities.
        self.principals = principals
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.principals:
            for v1 in self.principals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Principals'] = []
        if self.principals is not None:
            for k1 in self.principals:
                result['Principals'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.principals = []
        if m.get('Principals') is not None:
            for k1 in m.get('Principals'):
                temp_model = main_models.ListPrincipalsResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrincipalsResponseBodyPrincipals(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The ID of the RAM entity.
        self.principal_id = principal_id
        # The type of the RAM entity. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

