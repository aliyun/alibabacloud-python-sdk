# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseSyncJobReadinessResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContextDatabaseSyncJobReadinessResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetContextDatabaseSyncJobReadinessResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetContextDatabaseSyncJobReadinessResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_pause_reason: str = None,
        checks: main_models.GetContextDatabaseSyncJobReadinessResponseBodyDataChecks = None,
        ready: bool = None,
        ready_for_manual_run: bool = None,
        ready_for_scheduled_run: bool = None,
    ):
        # The reason for the automatic pause.
        self.auto_pause_reason = auto_pause_reason
        # The summary of check items.
        self.checks = checks
        # Indicates whether the task is ready.
        self.ready = ready
        # Indicates whether the task is ready for a manual run.
        self.ready_for_manual_run = ready_for_manual_run
        # Indicates whether the task is ready for a scheduled run.
        self.ready_for_scheduled_run = ready_for_scheduled_run

    def validate(self):
        if self.checks:
            self.checks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause_reason is not None:
            result['AutoPauseReason'] = self.auto_pause_reason

        if self.checks is not None:
            result['Checks'] = self.checks.to_map()

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.ready_for_manual_run is not None:
            result['ReadyForManualRun'] = self.ready_for_manual_run

        if self.ready_for_scheduled_run is not None:
            result['ReadyForScheduledRun'] = self.ready_for_scheduled_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPauseReason') is not None:
            self.auto_pause_reason = m.get('AutoPauseReason')

        if m.get('Checks') is not None:
            temp_model = main_models.GetContextDatabaseSyncJobReadinessResponseBodyDataChecks()
            self.checks = temp_model.from_map(m.get('Checks'))

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('ReadyForManualRun') is not None:
            self.ready_for_manual_run = m.get('ReadyForManualRun')

        if m.get('ReadyForScheduledRun') is not None:
            self.ready_for_scheduled_run = m.get('ReadyForScheduledRun')

        return self

class GetContextDatabaseSyncJobReadinessResponseBodyDataChecks(DaraModel):
    def __init__(
        self,
        connection_ready: bool = None,
        job_enabled: bool = None,
        schedule_configured: bool = None,
        schedule_not_auto_paused: bool = None,
        selection_confirmed: bool = None,
        target_ready: bool = None,
    ):
        # Indicates whether the data source is ready.
        self.connection_ready = connection_ready
        # Indicates whether the import task is enabled.
        self.job_enabled = job_enabled
        # Indicates whether scheduling is configured.
        self.schedule_configured = schedule_configured
        # Indicates whether scheduling is not automatically paused.
        self.schedule_not_auto_paused = schedule_not_auto_paused
        # Indicates whether the selection is confirmed.
        self.selection_confirmed = selection_confirmed
        # Indicates whether the target is ready.
        self.target_ready = target_ready

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_ready is not None:
            result['ConnectionReady'] = self.connection_ready

        if self.job_enabled is not None:
            result['JobEnabled'] = self.job_enabled

        if self.schedule_configured is not None:
            result['ScheduleConfigured'] = self.schedule_configured

        if self.schedule_not_auto_paused is not None:
            result['ScheduleNotAutoPaused'] = self.schedule_not_auto_paused

        if self.selection_confirmed is not None:
            result['SelectionConfirmed'] = self.selection_confirmed

        if self.target_ready is not None:
            result['TargetReady'] = self.target_ready

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionReady') is not None:
            self.connection_ready = m.get('ConnectionReady')

        if m.get('JobEnabled') is not None:
            self.job_enabled = m.get('JobEnabled')

        if m.get('ScheduleConfigured') is not None:
            self.schedule_configured = m.get('ScheduleConfigured')

        if m.get('ScheduleNotAutoPaused') is not None:
            self.schedule_not_auto_paused = m.get('ScheduleNotAutoPaused')

        if m.get('SelectionConfirmed') is not None:
            self.selection_confirmed = m.get('SelectionConfirmed')

        if m.get('TargetReady') is not None:
            self.target_ready = m.get('TargetReady')

        return self

