# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RedirectTaskRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        by_manager: str = None,
        language: str = None,
        now_action_executor_id: str = None,
        process_instance_id: str = None,
        remark: str = None,
        system_token: str = None,
        task_id: int = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        self.by_manager = by_manager
        self.language = language
        # This parameter is required.
        self.now_action_executor_id = now_action_executor_id
        # This parameter is required.
        self.process_instance_id = process_instance_id
        self.remark = remark
        # This parameter is required.
        self.system_token = system_token
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.by_manager is not None:
            result['ByManager'] = self.by_manager

        if self.language is not None:
            result['Language'] = self.language

        if self.now_action_executor_id is not None:
            result['NowActionExecutorId'] = self.now_action_executor_id

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ByManager') is not None:
            self.by_manager = m.get('ByManager')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('NowActionExecutorId') is not None:
            self.now_action_executor_id = m.get('NowActionExecutorId')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

