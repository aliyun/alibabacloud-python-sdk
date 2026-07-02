# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationAccessPointRequest(DaraModel):
    def __init__(
        self,
        authentication_method: str = None,
        description: str = None,
        name: str = None,
        policies: str = None,
    ):
        # The authentication method. Currently, only ClientKey is supported.
        self.authentication_method = authentication_method
        # The description of the AAP.
        self.description = description
        # The name of the AAP.
        # 
        # This parameter is required.
        self.name = name
        # The permission policy.
        # 
        # > You can bind up to three permission policies to each AAP.
        # 
        # This parameter is required.
        self.policies = policies

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.policies is not None:
            result['Policies'] = self.policies

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policies') is not None:
            self.policies = m.get('Policies')

        return self

