# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class SourceCodeAccount(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        id: str = None,
        name: str = None,
        organizations: List[main_models.SourceCodeAccountOrganizations] = None,
    ):
        self.avatar_url = avatar_url
        self.id = id
        self.name = name
        self.organizations = organizations

    def validate(self):
        if self.organizations:
            for v1 in self.organizations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['Organizations'] = []
        if self.organizations is not None:
            for k1 in self.organizations:
                result['Organizations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.organizations = []
        if m.get('Organizations') is not None:
            for k1 in m.get('Organizations'):
                temp_model = main_models.SourceCodeAccountOrganizations()
                self.organizations.append(temp_model.from_map(k1))

        return self

class SourceCodeAccountOrganizations(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        id: str = None,
        name: str = None,
    ):
        self.avatar_url = avatar_url
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

