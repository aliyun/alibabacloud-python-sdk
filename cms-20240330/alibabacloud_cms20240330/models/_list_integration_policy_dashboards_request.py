# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntegrationPolicyDashboardsRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        language: str = None,
        scene: str = None,
    ):
        # Addon Name.
        self.addon_name = addon_name
        # Query Language
        self.language = language
        # Component Scenario.
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.language is not None:
            result['language'] = self.language

        if self.scene is not None:
            result['scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        return self

