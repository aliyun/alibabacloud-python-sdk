# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePlaybookShrinkRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        playbook_description: str = None,
        playbook_input_configs_shrink: str = None,
        playbook_name: str = None,
        playbook_output_configs_shrink: str = None,
        playbook_param_type: str = None,
        playbook_task_flow: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
    ):
        # The language type for requests and received messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Description of the playbook.
        self.playbook_description = playbook_description
        # List of input parameter configurations for the playbook.
        self.playbook_input_configs_shrink = playbook_input_configs_shrink
        # The name of the playbook.
        self.playbook_name = playbook_name
        # List of output parameter configurations for the playbook.
        self.playbook_output_configs_shrink = playbook_output_configs_shrink
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
        # Content of the playbook.
        self.playbook_task_flow = playbook_task_flow
        # UUID of the playbook.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The user ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.playbook_description is not None:
            result['PlaybookDescription'] = self.playbook_description

        if self.playbook_input_configs_shrink is not None:
            result['PlaybookInputConfigs'] = self.playbook_input_configs_shrink

        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name

        if self.playbook_output_configs_shrink is not None:
            result['PlaybookOutputConfigs'] = self.playbook_output_configs_shrink

        if self.playbook_param_type is not None:
            result['PlaybookParamType'] = self.playbook_param_type

        if self.playbook_task_flow is not None:
            result['PlaybookTaskFlow'] = self.playbook_task_flow

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PlaybookDescription') is not None:
            self.playbook_description = m.get('PlaybookDescription')

        if m.get('PlaybookInputConfigs') is not None:
            self.playbook_input_configs_shrink = m.get('PlaybookInputConfigs')

        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')

        if m.get('PlaybookOutputConfigs') is not None:
            self.playbook_output_configs_shrink = m.get('PlaybookOutputConfigs')

        if m.get('PlaybookParamType') is not None:
            self.playbook_param_type = m.get('PlaybookParamType')

        if m.get('PlaybookTaskFlow') is not None:
            self.playbook_task_flow = m.get('PlaybookTaskFlow')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

