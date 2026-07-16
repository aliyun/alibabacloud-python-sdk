# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnvironmentRequest(DaraModel):
    def __init__(
        self,
        environment_name: str = None,
        next_environment_name: str = None,
        rule: str = None,
        site_id: int = None,
    ):
        # The environment name.
        # 
        # This parameter is required.
        self.environment_name = environment_name
        # The name of the environment with the next priority.
        # 
        # This parameter is required.
        self.next_environment_name = next_environment_name
        # The environment rule.
        # 
        # This parameter is required.
        self.rule = rule
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

        if self.next_environment_name is not None:
            result['NextEnvironmentName'] = self.next_environment_name

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('NextEnvironmentName') is not None:
            self.next_environment_name = m.get('NextEnvironmentName')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

