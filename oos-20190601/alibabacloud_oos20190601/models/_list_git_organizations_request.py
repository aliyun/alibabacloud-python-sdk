# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGitOrganizationsRequest(DaraModel):
    def __init__(
        self,
        bind_type: str = None,
        client_token: str = None,
        owner: str = None,
        platform: str = None,
        region_id: str = None,
    ):
        self.bind_type = bind_type
        self.client_token = client_token
        # This parameter is required.
        self.owner = owner
        # This parameter is required.
        self.platform = platform
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_type is not None:
            result['BindType'] = self.bind_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindType') is not None:
            self.bind_type = m.get('BindType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

