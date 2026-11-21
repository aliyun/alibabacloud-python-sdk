# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntegrationPolicyStorageRequirementsRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_release_name: str = None,
        storage_type: str = None,
    ):
        # The name of the add-on release.
        self.addon_name = addon_name
        # The name of the AddonRelease.
        self.addon_release_name = addon_release_name
        # The storage type. Valid values: LogStore, Prometheus, TraceStore, EventStore, and EntityStore.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.addon_release_name is not None:
            result['addonReleaseName'] = self.addon_release_name

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('addonReleaseName') is not None:
            self.addon_release_name = m.get('addonReleaseName')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        return self

