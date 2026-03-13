# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeSophonCommandsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSophonCommandsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The commands.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeSophonCommandsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSophonCommandsResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        param_config: List[main_models.DescribeSophonCommandsResponseBodyDataParamConfig] = None,
    ):
        # The description of the command.
        self.description = description
        # The display name of the command.
        self.display_name = display_name
        # The name of the command.
        self.name = name
        # The parameter configurations.
        self.param_config = param_config

    def validate(self):
        if self.param_config:
            for v1 in self.param_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        result['ParamConfig'] = []
        if self.param_config is not None:
            for k1 in self.param_config:
                result['ParamConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.param_config = []
        if m.get('ParamConfig') is not None:
            for k1 in m.get('ParamConfig'):
                temp_model = main_models.DescribeSophonCommandsResponseBodyDataParamConfig()
                self.param_config.append(temp_model.from_map(k1))

        return self

class DescribeSophonCommandsResponseBodyDataParamConfig(DaraModel):
    def __init__(
        self,
        check_field: str = None,
        field: str = None,
        necessary: bool = None,
        value: str = None,
    ):
        # The regular expression that is used to check the format of the parameter value. If the parameter is left empty, the check is not performed.
        self.check_field = check_field
        # The name of the parameter.
        self.field = field
        # Indicates whether the parameter is required. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.necessary = necessary
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_field is not None:
            result['CheckField'] = self.check_field

        if self.field is not None:
            result['Field'] = self.field

        if self.necessary is not None:
            result['Necessary'] = self.necessary

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckField') is not None:
            self.check_field = m.get('CheckField')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Necessary') is not None:
            self.necessary = m.get('Necessary')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

