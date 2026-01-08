# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppModeRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_ids: str = None,
        enable_idle: bool = None,
        idle_hour: str = None,
        namespace_id: str = None,
    ):
        # The app ID.
        self.app_id = app_id
        self.app_ids = app_ids
        # Enable Idle Mode?
        # 
        # Enumeration value:
        # 
        # *   true: enables.
        # *   false: disables.
        self.enable_idle = enable_idle
        self.idle_hour = idle_hour
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.enable_idle is not None:
            result['EnableIdle'] = self.enable_idle

        if self.idle_hour is not None:
            result['IdleHour'] = self.idle_hour

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('EnableIdle') is not None:
            self.enable_idle = m.get('EnableIdle')

        if m.get('IdleHour') is not None:
            self.idle_hour = m.get('IdleHour')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

