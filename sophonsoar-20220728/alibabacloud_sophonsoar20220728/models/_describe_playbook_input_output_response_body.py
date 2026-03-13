# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePlaybookInputOutputResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.DescribePlaybookInputOutputResponseBodyConfig = None,
        request_id: str = None,
    ):
        # The configurations.
        self.config = config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.DescribePlaybookInputOutputResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePlaybookInputOutputResponseBodyConfig(DaraModel):
    def __init__(
        self,
        exe_config: str = None,
        input_params: str = None,
        output_params: str = None,
        param_type: str = None,
        playbook_uuid: str = None,
    ):
        # The execution method of the playbook is in JSONObject format.
        self.exe_config = exe_config
        # The input parameter configuration of the playbook. The value is a JSON array.
        self.input_params = input_params
        # The output parameter configuration. This parameter is unavailable and is always left empty.
        self.output_params = output_params
        # The input parameter type of the playbook. Valid values:
        # 
        # *   **template-ip**
        # *   **template-file**
        # *   **template-process**
        # *   **custom**
        self.param_type = param_type
        # The UUID of the playbook.
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

        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        return self

