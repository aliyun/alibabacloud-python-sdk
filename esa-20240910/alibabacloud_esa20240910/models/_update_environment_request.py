# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEnvironmentRequest(DaraModel):
    def __init__(
        self,
        environment_name: str = None,
        new_name: str = None,
        read_only: bool = None,
        rule: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The environment name.
        # 
        # This parameter is required.
        self.environment_name = environment_name
        # The new environment name.
        self.new_name = new_name
        # Specifies whether the environment is read-only.
        # 
        # This parameter is required.
        self.read_only = read_only
        # The Wireshark rule.
        # 
        # This parameter is required.
        self.rule = rule
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The new site version number. Only the environment with the highest priority can be modified.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.new_name is not None:
            result['NewName'] = self.new_name

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

