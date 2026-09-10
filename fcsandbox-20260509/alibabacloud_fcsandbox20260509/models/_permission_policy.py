# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class PermissionPolicy(DaraModel):
    def __init__(
        self,
        allow: main_models.PermissionPolicyAllow = None,
        catalog_version: int = None,
        deny: main_models.PermissionPolicyDeny = None,
        schema_version: int = None,
    ):
        # The allow policy.
        self.allow = allow
        # catalog version
        self.catalog_version = catalog_version
        # The deny policy.
        self.deny = deny
        # schema version
        self.schema_version = schema_version

    def validate(self):
        if self.allow:
            self.allow.validate()
        if self.deny:
            self.deny.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow is not None:
            result['allow'] = self.allow.to_map()

        if self.catalog_version is not None:
            result['catalogVersion'] = self.catalog_version

        if self.deny is not None:
            result['deny'] = self.deny.to_map()

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow') is not None:
            temp_model = main_models.PermissionPolicyAllow()
            self.allow = temp_model.from_map(m.get('allow'))

        if m.get('catalogVersion') is not None:
            self.catalog_version = m.get('catalogVersion')

        if m.get('deny') is not None:
            temp_model = main_models.PermissionPolicyDeny()
            self.deny = temp_model.from_map(m.get('deny'))

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        return self

class PermissionPolicyDeny(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        capabilities: List[str] = None,
    ):
        # The actions.
        self.actions = actions
        # The capabilities.
        self.capabilities = capabilities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.capabilities is not None:
            result['capabilities'] = self.capabilities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')

        return self

class PermissionPolicyAllow(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        capabilities: List[str] = None,
    ):
        # The actions.
        self.actions = actions
        # The capabilities.
        self.capabilities = capabilities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.capabilities is not None:
            result['capabilities'] = self.capabilities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')

        return self

