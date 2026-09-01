# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPlaybookInputOutputRequest(DaraModel):
    def __init__(
        self,
        exe_config: str = None,
        input_params: str = None,
        lang: str = None,
        output_params: str = None,
        param_type: str = None,
        playbook_uuid: str = None,
    ):
        # The execution method for the playbook. This parameter is in the JSONObject format.
        self.exe_config = exe_config
        # The input parameter configuration for the playbook. This parameter is in the JSONArray format.
        # 
        # This parameter is required.
        self.input_params = input_params
        # The language of the request and response messages.
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # Playbooks do not support output parameter configurations. This parameter is fixed to an empty value.
        # 
        # This parameter is required.
        self.output_params = output_params
        # The type of the input parameter for the playbook.
        # 
        # - **template-ip**: IP request template.
        # 
        # - **template-file**: file request template.
        # 
        # - **template-process**: process request template.
        # 
        # - **custom**: custom parameter.
        self.param_type = param_type
        # The UUID of the playbook.
        # 
        # > Call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exe_config is not None:
            result['ExeConfig'] = self.exe_config

        if self.input_params is not None:
            result['InputParams'] = self.input_params

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.output_params is not None:
            result['OutputParams'] = self.output_params

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExeConfig') is not None:
            self.exe_config = m.get('ExeConfig')

        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        return self

