# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdatePolarClawCronJobRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        delete_after_run: bool = None,
        delivery: main_models.UpdatePolarClawCronJobRequestDelivery = None,
        description: str = None,
        enabled: bool = None,
        failure_alert: main_models.UpdatePolarClawCronJobRequestFailureAlert = None,
        job_id: str = None,
        name: str = None,
        payload: main_models.UpdatePolarClawCronJobRequestPayload = None,
        restart: bool = None,
        schedule: main_models.UpdatePolarClawCronJobRequestSchedule = None,
        session_key: str = None,
        session_target: str = None,
        wake_mode: str = None,
    ):
        self.agent_id = agent_id
        # This parameter is required.
        self.application_id = application_id
        self.delete_after_run = delete_after_run
        self.delivery = delivery
        self.description = description
        self.enabled = enabled
        self.failure_alert = failure_alert
        # This parameter is required.
        self.job_id = job_id
        self.name = name
        self.payload = payload
        self.restart = restart
        self.schedule = schedule
        self.session_key = session_key
        self.session_target = session_target
        self.wake_mode = wake_mode

    def validate(self):
        if self.delivery:
            self.delivery.validate()
        if self.failure_alert:
            self.failure_alert.validate()
        if self.payload:
            self.payload.validate()
        if self.schedule:
            self.schedule.validate()

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

        if self.delivery is not None:
            result['Delivery'] = self.delivery.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.failure_alert is not None:
            result['FailureAlert'] = self.failure_alert.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()

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
            temp_model = main_models.UpdatePolarClawCronJobRequestDelivery()
            self.delivery = temp_model.from_map(m.get('Delivery'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FailureAlert') is not None:
            temp_model = main_models.UpdatePolarClawCronJobRequestFailureAlert()
            self.failure_alert = temp_model.from_map(m.get('FailureAlert'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Payload') is not None:
            temp_model = main_models.UpdatePolarClawCronJobRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Schedule') is not None:
            temp_model = main_models.UpdatePolarClawCronJobRequestSchedule()
            self.schedule = temp_model.from_map(m.get('Schedule'))

        if m.get('SessionKey') is not None:
            self.session_key = m.get('SessionKey')

        if m.get('SessionTarget') is not None:
            self.session_target = m.get('SessionTarget')

        if m.get('WakeMode') is not None:
            self.wake_mode = m.get('WakeMode')

        return self

class UpdatePolarClawCronJobRequestSchedule(DaraModel):
    def __init__(
        self,
        anchor_ms: int = None,
        at: str = None,
        every_ms: int = None,
        expr: str = None,
        kind: str = None,
        stagger_ms: int = None,
        tz: str = None,
    ):
        self.anchor_ms = anchor_ms
        self.at = at
        self.every_ms = every_ms
        self.expr = expr
        self.kind = kind
        self.stagger_ms = stagger_ms
        self.tz = tz

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_ms is not None:
            result['AnchorMs'] = self.anchor_ms

        if self.at is not None:
            result['At'] = self.at

        if self.every_ms is not None:
            result['EveryMs'] = self.every_ms

        if self.expr is not None:
            result['Expr'] = self.expr

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.stagger_ms is not None:
            result['StaggerMs'] = self.stagger_ms

        if self.tz is not None:
            result['Tz'] = self.tz

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorMs') is not None:
            self.anchor_ms = m.get('AnchorMs')

        if m.get('At') is not None:
            self.at = m.get('At')

        if m.get('EveryMs') is not None:
            self.every_ms = m.get('EveryMs')

        if m.get('Expr') is not None:
            self.expr = m.get('Expr')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('StaggerMs') is not None:
            self.stagger_ms = m.get('StaggerMs')

        if m.get('Tz') is not None:
            self.tz = m.get('Tz')

        return self

class UpdatePolarClawCronJobRequestPayload(DaraModel):
    def __init__(
        self,
        best_effort_deliver: bool = None,
        channel: str = None,
        deliver: bool = None,
        fallbacks: List[str] = None,
        kind: str = None,
        light_context: bool = None,
        message: str = None,
        model: str = None,
        text: str = None,
        thinking: str = None,
        timeout_seconds: int = None,
        to: str = None,
    ):
        self.best_effort_deliver = best_effort_deliver
        self.channel = channel
        self.deliver = deliver
        self.fallbacks = fallbacks
        self.kind = kind
        self.light_context = light_context
        self.message = message
        self.model = model
        self.text = text
        self.thinking = thinking
        self.timeout_seconds = timeout_seconds
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.best_effort_deliver is not None:
            result['BestEffortDeliver'] = self.best_effort_deliver

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.deliver is not None:
            result['Deliver'] = self.deliver

        if self.fallbacks is not None:
            result['Fallbacks'] = self.fallbacks

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.light_context is not None:
            result['LightContext'] = self.light_context

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model

        if self.text is not None:
            result['Text'] = self.text

        if self.thinking is not None:
            result['Thinking'] = self.thinking

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BestEffortDeliver') is not None:
            self.best_effort_deliver = m.get('BestEffortDeliver')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')

        if m.get('Fallbacks') is not None:
            self.fallbacks = m.get('Fallbacks')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('LightContext') is not None:
            self.light_context = m.get('LightContext')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Thinking') is not None:
            self.thinking = m.get('Thinking')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class UpdatePolarClawCronJobRequestFailureAlert(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        after: int = None,
        channel: str = None,
        cooldown_ms: int = None,
        mode: str = None,
        to: str = None,
    ):
        self.account_id = account_id
        self.after = after
        self.channel = channel
        self.cooldown_ms = cooldown_ms
        self.mode = mode
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.after is not None:
            result['After'] = self.after

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.cooldown_ms is not None:
            result['CooldownMs'] = self.cooldown_ms

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CooldownMs') is not None:
            self.cooldown_ms = m.get('CooldownMs')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class UpdatePolarClawCronJobRequestDelivery(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        best_effort: bool = None,
        channel: str = None,
        mode: str = None,
        to: str = None,
    ):
        self.account_id = account_id
        self.best_effort = best_effort
        self.channel = channel
        self.mode = mode
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.best_effort is not None:
            result['BestEffort'] = self.best_effort

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BestEffort') is not None:
            self.best_effort = m.get('BestEffort')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

