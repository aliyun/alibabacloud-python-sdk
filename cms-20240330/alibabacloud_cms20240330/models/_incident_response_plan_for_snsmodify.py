# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentResponsePlanForSNSModify(DaraModel):
    def __init__(
        self,
        auto_recover_seconds: int = None,
        escalation_id: List[str] = None,
        pushing_setting: main_models.IncidentResponsePlanForSNSModifyPushingSetting = None,
        repeat_notify_setting: main_models.IncidentResponsePlanForSNSModifyRepeatNotifySetting = None,
    ):
        # The auto-recovery time. Unit: seconds. After this is configured, if no new events are generated for the incident within this period, the incident is automatically marked as resolved.
        self.auto_recover_seconds = auto_recover_seconds
        # The list of escalation policy IDs. Associates with IncidentEscalationPolicy to define step-by-step escalation rules when an incident is not handled as expected, such as notifying a supervisor if the incident is not acknowledged within 30 minutes.
        self.escalation_id = escalation_id
        # The action integration execution configuration that defines automated actions to trigger when an incident occurs and when it is recovered.
        self.pushing_setting = pushing_setting
        # The repeat notification settings. When an incident remains unresolved, notifications are sent repeatedly at a fixed interval.
        self.repeat_notify_setting = repeat_notify_setting

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

        if self.escalation_id is not None:
            result['escalationId'] = self.escalation_id

        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()

        if self.repeat_notify_setting is not None:
            result['repeatNotifySetting'] = self.repeat_notify_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverSeconds') is not None:
            self.auto_recover_seconds = m.get('autoRecoverSeconds')

        if m.get('escalationId') is not None:
            self.escalation_id = m.get('escalationId')

        if m.get('pushingSetting') is not None:
            temp_model = main_models.IncidentResponsePlanForSNSModifyPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('pushingSetting'))

        if m.get('repeatNotifySetting') is not None:
            temp_model = main_models.IncidentResponsePlanForSNSModifyRepeatNotifySetting()
            self.repeat_notify_setting = temp_model.from_map(m.get('repeatNotifySetting'))

        return self

class IncidentResponsePlanForSNSModifyRepeatNotifySetting(DaraModel):
    def __init__(
        self,
        end_incident_state: str = None,
        repeat_interval: int = None,
    ):
        # The incident status at which repeat notifications stop. Repeat notifications are no longer sent after the incident reaches this status.
        self.end_incident_state = end_incident_state
        # The repeat notification interval. Unit: seconds.
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

class IncidentResponsePlanForSNSModifyPushingSetting(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        # The list of action IDs to execute when an event is triggered. Actions must be created in advance by calling CreateAlertAction.
        self.alert_action_ids = alert_action_ids
        # The list of action IDs to execute when an event is recovered.
        self.restore_action_ids = restore_action_ids
        # Deprecated. This parameter does not take effect even if a value is passed in.
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

