# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntegrationPolicyCollectorsRequest(DaraModel):
    def __init__(
        self,
        addon_release_name: str = None,
        collector_type: str = None,
        language: str = None,
    ):
        self.addon_release_name = addon_release_name
        # This parameter is required.
        self.collector_type = collector_type
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_release_name is not None:
            result['addonReleaseName'] = self.addon_release_name

        if self.collector_type is not None:
            result['collectorType'] = self.collector_type

        if self.language is not None:
            result['language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonReleaseName') is not None:
            self.addon_release_name = m.get('addonReleaseName')

        if m.get('collectorType') is not None:
            self.collector_type = m.get('collectorType')

        if m.get('language') is not None:
            self.language = m.get('language')

        return self

