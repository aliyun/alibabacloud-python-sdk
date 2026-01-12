# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuotaConfig(DaraModel):
    def __init__(
        self,
        allowed_max_priority: int = None,
        enable_dlc: bool = None,
        enable_dsw: bool = None,
        enable_tide_resource: bool = None,
        resource_level: str = None,
    ):
        self.allowed_max_priority = allowed_max_priority
        self.enable_dlc = enable_dlc
        self.enable_dsw = enable_dsw
        self.enable_tide_resource = enable_tide_resource
        self.resource_level = resource_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_max_priority is not None:
            result['AllowedMaxPriority'] = self.allowed_max_priority

        if self.enable_dlc is not None:
            result['EnableDLC'] = self.enable_dlc

        if self.enable_dsw is not None:
            result['EnableDSW'] = self.enable_dsw

        if self.enable_tide_resource is not None:
            result['EnableTideResource'] = self.enable_tide_resource

        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedMaxPriority') is not None:
            self.allowed_max_priority = m.get('AllowedMaxPriority')

        if m.get('EnableDLC') is not None:
            self.enable_dlc = m.get('EnableDLC')

        if m.get('EnableDSW') is not None:
            self.enable_dsw = m.get('EnableDSW')

        if m.get('EnableTideResource') is not None:
            self.enable_tide_resource = m.get('EnableTideResource')

        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')

        return self

