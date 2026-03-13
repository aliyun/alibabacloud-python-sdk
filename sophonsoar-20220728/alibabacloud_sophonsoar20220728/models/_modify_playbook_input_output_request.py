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
        # The executed mode of a playbook. The value is a JSON array.
        self.exe_config = exe_config
        # The configuration of the input parameters. The value is a JSON array.
        # 
        # This parameter is required.
        self.input_params = input_params
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The configuration of the output parameters. This parameter is unavailable. Leave it empty.
        # 
        # This parameter is required.
        self.output_params = output_params
        # The input parameter type.
        # 
        # *   **template-ip**
        # *   **template-file**
        # *   **template-process**
        # *   **custom**
        self.param_type = param_type
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~)operation to query the playbook UUID.
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

