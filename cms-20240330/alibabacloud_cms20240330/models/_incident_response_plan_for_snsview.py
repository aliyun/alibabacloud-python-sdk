# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentResponsePlanForSNSView(DaraModel):
    def __init__(
        self,
        auto_recover_seconds: int = None,
        create_time: str = None,
        enable: bool = None,
        escalation_id: List[str] = None,
        mode: str = None,
        name: str = None,
        pushing_setting: main_models.IncidentResponsePlanForSNSViewPushingSetting = None,
        repeat_notify_setting: main_models.IncidentResponsePlanForSNSViewRepeatNotifySetting = None,
        source: str = None,
        sync_from_type: str = None,
        type: str = None,
        update_time: str = None,
        uuid: str = None,
    ):
        # The auto-recovery time when no incidents occur, in seconds.
        self.auto_recover_seconds = auto_recover_seconds
        # The creation time.
        self.create_time = create_time
        # Indicates whether the response plan is enabled.
        self.enable = enable
        # The list of escalation plan IDs.
        self.escalation_id = escalation_id
        # The lifecycle mode.
        self.mode = mode
        # The name.
        self.name = name
        # The push settings.
        self.pushing_setting = pushing_setting
        # The repeat notification settings.
        self.repeat_notify_setting = repeat_notify_setting
        # The source. This value must be CUSTOM within SNS.
        self.source = source
        # The synchronization source type.
        self.sync_from_type = sync_from_type
        # The response plan type. This value must be NOTIFY_STRATEGY_DEFINED within SNS.
        self.type = type
        # The update time.
        self.update_time = update_time
        # The unique identifier of the response plan.
        self.uuid = uuid

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

        if self.enable is not None:
            result['enable'] = self.enable

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverSeconds') is not None:
            self.auto_recover_seconds = m.get('autoRecoverSeconds')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('escalationId') is not None:
            self.escalation_id = m.get('escalationId')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pushingSetting') is not None:
            temp_model = main_models.IncidentResponsePlanForSNSViewPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('pushingSetting'))

        if m.get('repeatNotifySetting') is not None:
            temp_model = main_models.IncidentResponsePlanForSNSViewRepeatNotifySetting()
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

        return self

class IncidentResponsePlanForSNSViewRepeatNotifySetting(DaraModel):
    def __init__(
        self,
        end_incident_state: str = None,
        repeat_interval: int = None,
    ):
        # The setting that specifies whether to send repeat notifications when an incident ends.
        self.end_incident_state = end_incident_state
        # The repeat notification interval, in seconds.
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_incident_state is not None:
            result['endIncidentState'] = self.end_incident_state

        if self.repeat_interval is not None:
            result['repeatInterval'] = self.repeat_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endIncidentState') is not None:
            self.end_incident_state = m.get('endIncidentState')

        if m.get('repeatInterval') is not None:
            self.repeat_interval = m.get('repeatInterval')

        return self

class IncidentResponsePlanForSNSViewPushingSetting(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        # The list of response action IDs triggered by alerts.
        self.alert_action_ids = alert_action_ids
        # The list of response action IDs triggered by alert recovery.
        self.restore_action_ids = restore_action_ids
        # The UUID of the template used for pushing.
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids

        if self.restore_action_ids is not None:
            result['restoreActionIds'] = self.restore_action_ids

        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')

        if m.get('restoreActionIds') is not None:
            self.restore_action_ids = m.get('restoreActionIds')

        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')

        return self

