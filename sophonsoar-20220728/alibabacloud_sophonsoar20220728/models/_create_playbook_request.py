# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePlaybookRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        input_params: str = None,
        lang: str = None,
        output_params: str = None,
        taskflow_type: str = None,
    ):
        # Description of the playbook.
        self.description = description
        # Name of the playbook.
        # 
        # This parameter is required.
        self.display_name = display_name
        self.input_params = input_params
        # Language type for receiving messages. Values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        self.output_params = output_params
        # Playbook TaskFlow type.
        # - **x6** : x6
        # - **bpmn**: bpmn
        self.taskflow_type = taskflow_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.input_params is not None:
            result['InputParams'] = self.input_params

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.output_params is not None:
            result['OutputParams'] = self.output_params

        if self.taskflow_type is not None:
            result['TaskflowType'] = self.taskflow_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')

        if m.get('TaskflowType') is not None:
            self.taskflow_type = m.get('TaskflowType')

        return self

