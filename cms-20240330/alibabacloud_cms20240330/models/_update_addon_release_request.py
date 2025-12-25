# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateAddonReleaseRequest(DaraModel):
    def __init__(
        self,
        addon_version: str = None,
        dry_run: bool = None,
        entity_rules: main_models.EntityDiscoverRule = None,
        values: str = None,
    ):
        # Addon version information.
        self.addon_version = addon_version
        # Whether to pre-check this request.
        self.dry_run = dry_run
        # Entity discovery rules.
        self.entity_rules = entity_rules
        # Metadata information.
        self.values = values

    def validate(self):
        if self.entity_rules:
            self.entity_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_version is not None:
            result['addonVersion'] = self.addon_version

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.entity_rules is not None:
            result['entityRules'] = self.entity_rules.to_map()

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonVersion') is not None:
            self.addon_version = m.get('addonVersion')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('entityRules') is not None:
            temp_model = main_models.EntityDiscoverRule()
            self.entity_rules = temp_model.from_map(m.get('entityRules'))

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

