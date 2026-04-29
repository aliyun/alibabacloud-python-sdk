# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolarClawCronJobShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        delete_after_run: bool = None,
        delivery_shrink: str = None,
        description: str = None,
        enabled: bool = None,
        failure_alert_shrink: str = None,
        job_id: str = None,
        name: str = None,
        payload_shrink: str = None,
        restart: bool = None,
        schedule_shrink: str = None,
        session_key: str = None,
        session_target: str = None,
        wake_mode: str = None,
    ):
        self.agent_id = agent_id
        # This parameter is required.
        self.application_id = application_id
        self.delete_after_run = delete_after_run
        self.delivery_shrink = delivery_shrink
        self.description = description
        self.enabled = enabled
        self.failure_alert_shrink = failure_alert_shrink
        # This parameter is required.
        self.job_id = job_id
        self.name = name
        self.payload_shrink = payload_shrink
        self.restart = restart
        self.schedule_shrink = schedule_shrink
        self.session_key = session_key
        self.session_target = session_target
        self.wake_mode = wake_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.delete_after_run is not None:
            result['DeleteAfterRun'] = self.delete_after_run

        if self.delivery_shrink is not None:
            result['Delivery'] = self.delivery_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.failure_alert_shrink is not None:
            result['FailureAlert'] = self.failure_alert_shrink

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink

        if self.session_key is not None:
            result['SessionKey'] = self.session_key

        if self.session_target is not None:
            result['SessionTarget'] = self.session_target

        if self.wake_mode is not None:
            result['WakeMode'] = self.wake_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DeleteAfterRun') is not None:
            self.delete_after_run = m.get('DeleteAfterRun')

        if m.get('Delivery') is not None:
            self.delivery_shrink = m.get('Delivery')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FailureAlert') is not None:
            self.failure_alert_shrink = m.get('FailureAlert')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')

        if m.get('SessionKey') is not None:
            self.session_key = m.get('SessionKey')

        if m.get('SessionTarget') is not None:
            self.session_target = m.get('SessionTarget')

        if m.get('WakeMode') is not None:
            self.wake_mode = m.get('WakeMode')

        return self

