# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class Task(DaraModel):
    def __init__(
        self,
        actions: List[main_models.Action] = None,
        description: str = None,
        gmt_activated_time: str = None,
        gmt_created_time: str = None,
        gmt_modified_time: str = None,
        gmt_stopped_time: str = None,
        quota_id: str = None,
        rules: main_models.Rules = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.actions = actions
        self.description = description
        self.gmt_activated_time = gmt_activated_time
        self.gmt_created_time = gmt_created_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_stopped_time = gmt_stopped_time
        self.quota_id = quota_id
        self.rules = rules
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_activated_time is not None:
            result['GmtActivatedTime'] = self.gmt_activated_time

        if self.gmt_created_time is not None:
            result['GmtCreatedTime'] = self.gmt_created_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.Action()
                self.actions.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtActivatedTime') is not None:
            self.gmt_activated_time = m.get('GmtActivatedTime')

        if m.get('GmtCreatedTime') is not None:
            self.gmt_created_time = m.get('GmtCreatedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('Rules') is not None:
            temp_model = main_models.Rules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

