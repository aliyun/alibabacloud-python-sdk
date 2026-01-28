# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceAlertNotification(DaraModel):
    def __init__(
        self,
        id: int = None,
        is_arms: bool = None,
        is_default: bool = None,
        name: str = None,
        send_reminder: bool = None,
        settings: str = None,
        type: str = None,
        uid: str = None,
    ):
        self.id = id
        self.is_arms = is_arms
        self.is_default = is_default
        self.name = name
        self.send_reminder = send_reminder
        self.settings = settings
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.is_arms is not None:
            result['isArms'] = self.is_arms

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.name is not None:
            result['name'] = self.name

        if self.send_reminder is not None:
            result['sendReminder'] = self.send_reminder

        if self.settings is not None:
            result['settings'] = self.settings

        if self.type is not None:
            result['type'] = self.type

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isArms') is not None:
            self.is_arms = m.get('isArms')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sendReminder') is not None:
            self.send_reminder = m.get('sendReminder')

        if m.get('settings') is not None:
            self.settings = m.get('settings')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

