# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddonRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_version: str = None,
    ):
        # This parameter is required.
        self.addon_name = addon_name
        self.addon_version = addon_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        return self

