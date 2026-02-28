# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnalyzeConversationRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        field_list_json: str = None,
        instance_id: str = None,
        task_list_json: str = None,
    ):
        self.contact_id = contact_id
        self.field_list_json = field_list_json
        # This parameter is required.
        self.instance_id = instance_id
        self.task_list_json = task_list_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.field_list_json is not None:
            result['FieldListJson'] = self.field_list_json

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_list_json is not None:
            result['TaskListJson'] = self.task_list_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('FieldListJson') is not None:
            self.field_list_json = m.get('FieldListJson')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskListJson') is not None:
            self.task_list_json = m.get('TaskListJson')

        return self

