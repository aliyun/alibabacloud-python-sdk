# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerSophonPlaybookRequest(DaraModel):
    def __init__(
        self,
        command_name: str = None,
        input_params: str = None,
        sophon_task_id: str = None,
        trigger_type: str = None,
        uuid: str = None,
    ):
        # The name of the command that you want to trigger.
        # 
        # >  You can call the [DescribeSophonCommands](~~DescribeSophonCommands~~) operation to query the command name.
        self.command_name = command_name
        # The input parameters of the command or playbook that you want to trigger.
        # 
        # This parameter is required.
        self.input_params = input_params
        # The custom ID. If you do not specify this parameter when the playbook is triggered, a random ID is generated for fault locating and troubleshooting.
        self.sophon_task_id = sophon_task_id
        # The task type. Valid values:
        # 
        # *   **command**
        # *   **playbook**
        self.trigger_type = trigger_type
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.input_params is not None:
            result['InputParams'] = self.input_params

        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')

        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

