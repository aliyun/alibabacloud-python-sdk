# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreatePolarClawCronJobResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        job: main_models.CreatePolarClawCronJobResponseBodyJob = None,
        message: str = None,
        ok: bool = None,
        ran_immediately: bool = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # Details of the created cron job.
        self.job = job
        # The response message.
        self.message = message
        # Indicates whether the operation was successful.
        self.ok = ok
        # Indicates whether the job ran immediately after creation.
        self.ran_immediately = ran_immediately
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.ran_immediately is not None:
            result['RanImmediately'] = self.ran_immediately

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Job') is not None:
            temp_model = main_models.CreatePolarClawCronJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('RanImmediately') is not None:
            self.ran_immediately = m.get('RanImmediately')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePolarClawCronJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        created_at_ms: int = None,
        delete_after_run: bool = None,
        delivery: main_models.CreatePolarClawCronJobResponseBodyJobDelivery = None,
        description: str = None,
        enabled: bool = None,
        id: str = None,
        name: str = None,
        payload: main_models.CreatePolarClawCronJobResponseBodyJobPayload = None,
        runs: List[main_models.CreatePolarClawCronJobResponseBodyJobRuns] = None,
        schedule: main_models.CreatePolarClawCronJobResponseBodyJobSchedule = None,
        session_key: str = None,
        session_target: str = None,
        state: main_models.CreatePolarClawCronJobResponseBodyJobState = None,
        updated_at_ms: int = None,
        wake_mode: str = None,
    ):
        # The ID of the executing agent.
        self.agent_id = agent_id
        # The creation timestamp in milliseconds.
        self.created_at_ms = created_at_ms
        # Indicates whether the cron job is deleted after its first run.
        self.delete_after_run = delete_after_run
        # The delivery configuration.
        self.delivery = delivery
        # The job description.
        self.description = description
        # Indicates whether the cron job is enabled.
        self.enabled = enabled
        # The job ID (UUID).
        self.id = id
        # The job name.
        self.name = name
        # The execution payload.
        self.payload = payload
        # The run history.
        self.runs = runs
        # The schedule configuration.
        self.schedule = schedule
        # The session key.
        self.session_key = session_key
        # The session target. Valid values: `main`, `isolated`, and `current`.
        self.session_target = session_target
        # The current state of the job.
        self.state = state
        # The update timestamp in milliseconds.
        self.updated_at_ms = updated_at_ms
        # The wake mode. Valid values: `now` and `next-heartbeat`.
        self.wake_mode = wake_mode

    def validate(self):
        if self.delivery:
            self.delivery.validate()
        if self.payload:
            self.payload.validate()
        if self.runs:
            for v1 in self.runs:
                 if v1:
                    v1.validate()
        if self.schedule:
            self.schedule.validate()
        if self.state:
            self.state.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.created_at_ms is not None:
            result['CreatedAtMs'] = self.created_at_ms

        if self.delete_after_run is not None:
            result['DeleteAfterRun'] = self.delete_after_run

        if self.delivery is not None:
            result['Delivery'] = self.delivery.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        result['Runs'] = []
        if self.runs is not None:
            for k1 in self.runs:
                result['Runs'].append(k1.to_map() if k1 else None)

        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()

        if self.session_key is not None:
            result['SessionKey'] = self.session_key

        if self.session_target is not None:
            result['SessionTarget'] = self.session_target

        if self.state is not None:
            result['State'] = self.state.to_map()

        if self.updated_at_ms is not None:
            result['UpdatedAtMs'] = self.updated_at_ms

        if self.wake_mode is not None:
            result['WakeMode'] = self.wake_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('CreatedAtMs') is not None:
            self.created_at_ms = m.get('CreatedAtMs')

        if m.get('DeleteAfterRun') is not None:
            self.delete_after_run = m.get('DeleteAfterRun')

        if m.get('Delivery') is not None:
            temp_model = main_models.CreatePolarClawCronJobResponseBodyJobDelivery()
            self.delivery = temp_model.from_map(m.get('Delivery'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Payload') is not None:
            temp_model = main_models.CreatePolarClawCronJobResponseBodyJobPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        self.runs = []
        if m.get('Runs') is not None:
            for k1 in m.get('Runs'):
                temp_model = main_models.CreatePolarClawCronJobResponseBodyJobRuns()
                self.runs.append(temp_model.from_map(k1))

        if m.get('Schedule') is not None:
            temp_model = main_models.CreatePolarClawCronJobResponseBodyJobSchedule()
            self.schedule = temp_model.from_map(m.get('Schedule'))

        if m.get('SessionKey') is not None:
            self.session_key = m.get('SessionKey')

        if m.get('SessionTarget') is not None:
            self.session_target = m.get('SessionTarget')

        if m.get('State') is not None:
            temp_model = main_models.CreatePolarClawCronJobResponseBodyJobState()
            self.state = temp_model.from_map(m.get('State'))

        if m.get('UpdatedAtMs') is not None:
            self.updated_at_ms = m.get('UpdatedAtMs')

        if m.get('WakeMode') is not None:
            self.wake_mode = m.get('WakeMode')

        return self

class CreatePolarClawCronJobResponseBodyJobState(DaraModel):
    def __init__(
        self,
        consecutive_errors: int = None,
        last_run_at_ms: int = None,
        last_run_status: str = None,
        next_run_at_ms: int = None,
    ):
        # The number of consecutive execution failures.
        self.consecutive_errors = consecutive_errors
        # The last run timestamp in milliseconds.
        self.last_run_at_ms = last_run_at_ms
        # The last run status.
        self.last_run_status = last_run_status
        # The next run timestamp in milliseconds.
        self.next_run_at_ms = next_run_at_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consecutive_errors is not None:
            result['ConsecutiveErrors'] = self.consecutive_errors

        if self.last_run_at_ms is not None:
            result['LastRunAtMs'] = self.last_run_at_ms

        if self.last_run_status is not None:
            result['LastRunStatus'] = self.last_run_status

        if self.next_run_at_ms is not None:
            result['NextRunAtMs'] = self.next_run_at_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsecutiveErrors') is not None:
            self.consecutive_errors = m.get('ConsecutiveErrors')

        if m.get('LastRunAtMs') is not None:
            self.last_run_at_ms = m.get('LastRunAtMs')

        if m.get('LastRunStatus') is not None:
            self.last_run_status = m.get('LastRunStatus')

        if m.get('NextRunAtMs') is not None:
            self.next_run_at_ms = m.get('NextRunAtMs')

        return self

class CreatePolarClawCronJobResponseBodyJobSchedule(DaraModel):
    def __init__(
        self,
        anchor_ms: int = None,
        at: str = None,
        every_ms: int = None,
        expr: str = None,
        kind: str = None,
        tz: str = None,
    ):
        # The anchor timestamp for interval alignment.
        self.anchor_ms = anchor_ms
        # The ISO 8601 timestamp.
        self.at = at
        # The interval in milliseconds.
        self.every_ms = every_ms
        # The cron expression.
        self.expr = expr
        # The schedule type. Valid values: `cron`, `every`, and `at`.
        self.kind = kind
        # The IANA time zone.
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

        if m.get('Tz') is not None:
            self.tz = m.get('Tz')

        return self

class CreatePolarClawCronJobResponseBodyJobRuns(DaraModel):
    def __init__(
        self,
        action: str = None,
        delivered: bool = None,
        delivery_status: str = None,
        duration_ms: int = None,
        job_id: str = None,
        job_name: str = None,
        model: str = None,
        next_run_at_ms: int = None,
        provider: str = None,
        run_at_ms: int = None,
        session_id: str = None,
        status: str = None,
        summary: str = None,
        ts: int = None,
        usage: main_models.CreatePolarClawCronJobResponseBodyJobRunsUsage = None,
    ):
        # The action performed. Valid values: `finished`, `error`, and `skipped`.
        self.action = action
        # Specifies whether the results were delivered.
        self.delivered = delivered
        # The delivery status.
        self.delivery_status = delivery_status
        # The execution duration in milliseconds.
        self.duration_ms = duration_ms
        # The associated job ID.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The model used for the run.
        self.model = model
        # The next run timestamp in milliseconds.
        self.next_run_at_ms = next_run_at_ms
        # The model provider.
        self.provider = provider
        # The actual execution timestamp in milliseconds.
        self.run_at_ms = run_at_ms
        # The associated session ID.
        self.session_id = session_id
        # The status of the run. Valid values: `ok`, `error`, and `skipped`.
        self.status = status
        # The run summary.
        self.summary = summary
        # The run timestamp in milliseconds.
        self.ts = ts
        # The token usage details.
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.delivered is not None:
            result['Delivered'] = self.delivered

        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status

        if self.duration_ms is not None:
            result['DurationMs'] = self.duration_ms

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.model is not None:
            result['Model'] = self.model

        if self.next_run_at_ms is not None:
            result['NextRunAtMs'] = self.next_run_at_ms

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.run_at_ms is not None:
            result['RunAtMs'] = self.run_at_ms

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.ts is not None:
            result['Ts'] = self.ts

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Delivered') is not None:
            self.delivered = m.get('Delivered')

        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')

        if m.get('DurationMs') is not None:
            self.duration_ms = m.get('DurationMs')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NextRunAtMs') is not None:
            self.next_run_at_ms = m.get('NextRunAtMs')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RunAtMs') is not None:
            self.run_at_ms = m.get('RunAtMs')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        if m.get('Usage') is not None:
            temp_model = main_models.CreatePolarClawCronJobResponseBodyJobRunsUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class CreatePolarClawCronJobResponseBodyJobRunsUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        # The number of input tokens.
        self.input_tokens = input_tokens
        # The number of output tokens.
        self.output_tokens = output_tokens
        # The total number of tokens.
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class CreatePolarClawCronJobResponseBodyJobPayload(DaraModel):
    def __init__(
        self,
        best_effort_deliver: bool = None,
        channel: str = None,
        deliver: bool = None,
        kind: str = None,
        light_context: bool = None,
        message: str = None,
        model: str = None,
        text: str = None,
        timeout_seconds: int = None,
        to: str = None,
    ):
        # Specifies whether to ignore delivery failures.
        self.best_effort_deliver = best_effort_deliver
        # The delivery channel ID.
        self.channel = channel
        # Indicates whether to deliver the output to the delivery channel.
        self.deliver = deliver
        # The payload type. Valid values: `agentTurn` and `systemEvent`.
        self.kind = kind
        # Indicates whether to use a light context.
        self.light_context = light_context
        # The agent prompt.
        self.message = message
        # The overriding model.
        self.model = model
        # The system event text.
        self.text = text
        # The execution timeout in seconds.
        self.timeout_seconds = timeout_seconds
        # The recipient.
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

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class CreatePolarClawCronJobResponseBodyJobDelivery(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        best_effort: bool = None,
        channel: str = None,
        mode: str = None,
        to: str = None,
    ):
        # The channel account ID.
        self.account_id = account_id
        # Specifies whether to ignore delivery failures.
        self.best_effort = best_effort
        # The delivery channel.
        self.channel = channel
        # The delivery mode. Valid values: `none`, `announce`, and `webhook`.
        self.mode = mode
        # The recipient.
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

