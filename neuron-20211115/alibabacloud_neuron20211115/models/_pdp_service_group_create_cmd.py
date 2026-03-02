# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpServiceGroupCreateCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        alias: str = None,
        description: str = None,
        env: str = None,
        group_type: str = None,
        name: str = None,
        service_id: int = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.alias = alias
        self.description = description
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.group_type = group_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.env is not None:
            result['env'] = self.env

        if self.group_type is not None:
            result['groupType'] = self.group_type

        if self.name is not None:
            result['name'] = self.name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

