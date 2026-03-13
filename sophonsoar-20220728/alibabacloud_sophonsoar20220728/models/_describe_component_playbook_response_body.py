# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeComponentPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        playbooks: List[main_models.DescribeComponentPlaybookResponseBodyPlaybooks] = None,
        request_id: str = None,
    ):
        # The information about the predefined components.
        self.playbooks = playbooks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbooks:
            for v1 in self.playbooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Playbooks'] = []
        if self.playbooks is not None:
            for k1 in self.playbooks:
                result['Playbooks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.playbooks = []
        if m.get('Playbooks') is not None:
            for k1 in m.get('Playbooks'):
                temp_model = main_models.DescribeComponentPlaybookResponseBodyPlaybooks()
                self.playbooks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeComponentPlaybookResponseBodyPlaybooks(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        input_params: str = None,
        param_type: str = None,
    ):
        # The description of the predefined component.
        self.description = description
        # The name of the predefined component.
        self.display_name = display_name
        # The input parameter configuration of the playbook. The value is a JSON array.
        # 
        # >  For more information, see [DescribePlaybookInputOutput](~~DescribePlaybookInputOutput~~).
        self.input_params = input_params
        self.param_type = param_type

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

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

