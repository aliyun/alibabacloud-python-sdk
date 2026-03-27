# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAddonReleaseRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        force: bool = None,
        release_name: str = None,
    ):
        # Addon name. When AddonName is provided, it will ignore the ReleaseName parameter and batch uninstall all AddonReleases belonging to the same Addon.
        self.addon_name = addon_name
        # Whether to force deletion, default is false.
        self.force = force
        # The name of the AddonRelease.
        self.release_name = release_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.force is not None:
            result['force'] = self.force

        if self.release_name is not None:
            result['releaseName'] = self.release_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('force') is not None:
            self.force = m.get('force')

        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')

        return self

