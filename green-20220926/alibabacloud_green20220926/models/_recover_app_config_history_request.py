# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecoverAppConfigHistoryRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: int = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # App ID。
        self.app_id = app_id
        # The version number.
        self.app_version = app_version
        # The region ID.
        self.region_id = region_id
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

