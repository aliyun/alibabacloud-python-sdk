# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigSetUpdateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        ip_pool_id: str = None,
        name: str = None,
    ):
        # The description. The description can be up to 50 characters long.
        self.description = description
        # The ID of the configuration set. This parameter is required.
        self.id = id
        # The ID of the associated IP pool. This parameter is optional.
        self.ip_pool_id = ip_pool_id
        # The name of the configuration. This parameter is required. The name must be unique and can be up to 50 characters long.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

