# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20250903 import models as main_models
from darabonba.model import DaraModel

class CreatePlaybookRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        playbook_description: str = None,
        playbook_input_configs: List[main_models.FieldInputConfig] = None,
        playbook_name: str = None,
        playbook_output_configs: List[main_models.FieldOutputConfig] = None,
        playbook_param_type: str = None,
        playbook_task_flow: str = None,
        role_for: int = None,
        src_playbook_uuid: str = None,
    ):
        # Language type for receiving messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Description of the playbook.
        self.playbook_description = playbook_description
        # Input parameter configuration of the playbook.
        self.playbook_input_configs = playbook_input_configs
        # Name of the playbook, without special characters.
        # 
        # This parameter is required.
        self.playbook_name = playbook_name
        # Output parameter configuration of the playbook.
        self.playbook_output_configs = playbook_output_configs
        # Type of input parameters for the playbook.
        # 
        # - **template-ip**: IP entity.
        # - **template-file**: File entity.
        # - **template-process**: Process entity.
        # - **template-host**: Host entity.
        # - **template-domain**: Domain entity.
        # - **template-container**: Container entity.
        # - **template-incident**: Security incident.
        # - **template-alert**: Security alert.
        # - **custom**: Custom.
        self.playbook_param_type = playbook_param_type
        # Workflow of the playbook.
        self.playbook_task_flow = playbook_task_flow
        # Resource directory member account ID.
        self.role_for = role_for
        # In a copy scenario, the UUID of the source playbook needs to be filled in. When this parameter has a value, all other parameters except the playbook name and description are invalid.
        self.src_playbook_uuid = src_playbook_uuid

    def validate(self):
        if self.playbook_input_configs:
            for v1 in self.playbook_input_configs:
                 if v1:
                    v1.validate()
        if self.playbook_output_configs:
            for v1 in self.playbook_output_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description

        result['PlaybookInputConfigs'] = []
        if self.playbook_input_configs is not None:
            for k1 in self.playbook_input_configs:
                result['PlaybookInputConfigs'].append(k1.to_map() if k1 else None)

        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name

        result['PlaybookOutputConfigs'] = []
        if self.playbook_output_configs is not None:
            for k1 in self.playbook_output_configs:
                result['PlaybookOutputConfigs'].append(k1.to_map() if k1 else None)

        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type

        if self.playbook_task_flow is not None:
            result['PlaybookTaskFlow'] = self.playbook_task_flow

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.src_playbook_uuid is not None:
            result['SrcPlaybookUuid'] = self.src_playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')

        self.playbook_input_configs = []
        if m.get('PlaybookInputConfigs') is not None:
            for k1 in m.get('PlaybookInputConfigs'):
                temp_model = main_models.FieldInputConfig()
                self.playbook_input_configs.append(temp_model.from_map(k1))

        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')

        self.playbook_output_configs = []
        if m.get('PlaybookOutputConfigs') is not None:
            for k1 in m.get('PlaybookOutputConfigs'):
                temp_model = main_models.FieldOutputConfig()
                self.playbook_output_configs.append(temp_model.from_map(k1))

        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')

        if m.get('PlaybookTaskFlow') is not None:
            self.playbook_task_flow = m.get('PlaybookTaskFlow')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('SrcPlaybookUuid') is not None:
            self.src_playbook_uuid = m.get('SrcPlaybookUuid')

        return self

