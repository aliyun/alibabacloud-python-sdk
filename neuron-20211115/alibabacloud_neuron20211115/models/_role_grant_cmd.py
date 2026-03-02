# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class RoleGrantCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        authorization_resource_list: List[main_models.AuthorizationResource] = None,
        role_id: int = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.authorization_resource_list = authorization_resource_list
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.authorization_resource_list:
            for v1 in self.authorization_resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        result['authorizationResourceList'] = []
        if self.authorization_resource_list is not None:
            for k1 in self.authorization_resource_list:
                result['authorizationResourceList'].append(k1.to_map() if k1 else None)

        if self.role_id is not None:
            result['roleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        self.authorization_resource_list = []
        if m.get('authorizationResourceList') is not None:
            for k1 in m.get('authorizationResourceList'):
                temp_model = main_models.AuthorizationResource()
                self.authorization_resource_list.append(temp_model.from_map(k1))

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        return self

