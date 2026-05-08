# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class CreateAICoachTaskReportRequest(DaraModel):
    def __init__(
        self,
        dialogue_list: List[main_models.CreateAICoachTaskReportRequestDialogueList] = None,
        idempotent_id: str = None,
        task_id: str = None,
    ):
        self.dialogue_list = dialogue_list
        self.idempotent_id = idempotent_id
        self.task_id = task_id

    def validate(self):
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['dialogueList'].append(k1.to_map() if k1 else None)

        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue_list = []
        if m.get('dialogueList') is not None:
            for k1 in m.get('dialogueList'):
                temp_model = main_models.CreateAICoachTaskReportRequestDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class CreateAICoachTaskReportRequestDialogueList(DaraModel):
    def __init__(
        self,
        message: str = None,
        role: str = None,
    ):
        self.message = message
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

