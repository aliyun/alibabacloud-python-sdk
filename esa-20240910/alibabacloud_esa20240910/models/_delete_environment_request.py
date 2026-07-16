# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEnvironmentRequest(DaraModel):
    def __init__(
        self,
        environment_name: str = None,
        site_id: int = None,
    ):
        # The environment name.
        # 
        # This parameter is required.
        self.environment_name = environment_name
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

