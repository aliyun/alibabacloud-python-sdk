# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class GetUpgradeStatusResponseBody(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        precheck_report_id: str = None,
        status: str = None,
        upgrade_step: str = None,
        upgrade_task: main_models.GetUpgradeStatusResponseBodyUpgradeTask = None,
    ):
        # The error message during the cluster upgrade.
        self.error_message = error_message
        # The ID of the precheck report.
        self.precheck_report_id = precheck_report_id
        # The current upgrade status of the cluster. Valid values:
        # 
        # - `success`: The upgrade is successful.
        # - `fail`: The upgrade has failed.
        # - `pause`: The upgrade is paused.
        # - `running`: The upgrade is in progress.
        self.status = status
        # The current upgrade phase of the cluster. Valid values:
        # 
        # - `not_start`: Not started.
        # - `prechecking`: Prechecking is in progress.
        # - `upgrading`: The upgrade is in progress.
        # - `pause`: The upgrade is paused.
        # - `success`: The upgrade is successful.
        self.upgrade_step = upgrade_step
        # The upgrade task details.
        self.upgrade_task = upgrade_task

    def validate(self):
        if self.upgrade_task:
            self.upgrade_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['error_message'] = self.error_message

        if self.precheck_report_id is not None:
            result['precheck_report_id'] = self.precheck_report_id

        if self.status is not None:
            result['status'] = self.status

        if self.upgrade_step is not None:
            result['upgrade_step'] = self.upgrade_step

        if self.upgrade_task is not None:
            result['upgrade_task'] = self.upgrade_task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')

        if m.get('precheck_report_id') is not None:
            self.precheck_report_id = m.get('precheck_report_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('upgrade_step') is not None:
            self.upgrade_step = m.get('upgrade_step')

        if m.get('upgrade_task') is not None:
            temp_model = main_models.GetUpgradeStatusResponseBodyUpgradeTask()
            self.upgrade_task = temp_model.from_map(m.get('upgrade_task'))

        return self

class GetUpgradeStatusResponseBodyUpgradeTask(DaraModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        # The description of the upgrade task.
        self.message = message
        # The upgrade task status. Valid values:
        # - `running`: The task is running.
        # - `Success`: The task is successful.
        # - `Failed`: The task has failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

