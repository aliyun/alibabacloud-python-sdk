# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentResponsePlanForView(DaraModel):
    def __init__(
        self,
        auto_recover_seconds: int = None,
        create_time: str = None,
        description: str = None,
        enabled: bool = None,
        escalation_id: List[str] = None,
        mode: str = None,
        name: str = None,
        pushing_setting: main_models.PushingSetting = None,
        repeat_notify_setting: main_models.RepeatNotifySetting = None,
        source: str = None,
        sync_from_type: str = None,
        type: str = None,
        update_time: str = None,
        uuid: str = None,
        workspace: str = None,
    ):
        self.auto_recover_seconds = auto_recover_seconds
        self.create_time = create_time
        self.description = description
        self.enabled = enabled
        self.escalation_id = escalation_id
        self.mode = mode
        self.name = name
        self.pushing_setting = pushing_setting
        self.repeat_notify_setting = repeat_notify_setting
        self.source = source
        self.sync_from_type = sync_from_type
        self.type = type
        self.update_time = update_time
        self.uuid = uuid
        self.workspace = workspace

    def validate(self):
        if self.pushing_setting:
            self.pushing_setting.validate()
        if self.repeat_notify_setting:
            self.repeat_notify_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover_seconds is not None:
            result['autoRecoverSeconds'] = self.auto_recover_seconds

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.escalation_id is not None:
            result['escalationId'] = self.escalation_id

        if self.mode is not None:
            result['mode'] = self.mode

        if self.name is not None:
            result['name'] = self.name

        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()

        if self.repeat_notify_setting is not None:
            result['repeatNotifySetting'] = self.repeat_notify_setting.to_map()

        if self.source is not None:
            result['source'] = self.source

        if self.sync_from_type is not None:
            result['syncFromType'] = self.sync_from_type

        if self.type is not None:
            result['type'] = self.type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverSeconds') is not None:
            self.auto_recover_seconds = m.get('autoRecoverSeconds')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('escalationId') is not None:
            self.escalation_id = m.get('escalationId')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pushingSetting') is not None:
            temp_model = main_models.PushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('pushingSetting'))

        if m.get('repeatNotifySetting') is not None:
            temp_model = main_models.RepeatNotifySetting()
            self.repeat_notify_setting = temp_model.from_map(m.get('repeatNotifySetting'))

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('syncFromType') is not None:
            self.sync_from_type = m.get('syncFromType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

