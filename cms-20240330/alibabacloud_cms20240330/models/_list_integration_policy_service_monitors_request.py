# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntegrationPolicyServiceMonitorsRequest(DaraModel):
    def __init__(
        self,
        addon_release_name: str = None,
        encrypt_yaml: bool = None,
        namespace: str = None,
    ):
        self.addon_release_name = addon_release_name
        self.encrypt_yaml = encrypt_yaml
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_release_name is not None:
            result['addonReleaseName'] = self.addon_release_name

        if self.encrypt_yaml is not None:
            result['encryptYaml'] = self.encrypt_yaml

        if self.namespace is not None:
            result['namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonReleaseName') is not None:
            self.addon_release_name = m.get('addonReleaseName')

        if m.get('encryptYaml') is not None:
            self.encrypt_yaml = m.get('encryptYaml')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        return self

