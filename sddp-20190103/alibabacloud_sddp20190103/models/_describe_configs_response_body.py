# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeConfigsResponseBody(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.DescribeConfigsResponseBodyConfigList] = None,
        request_id: str = None,
    ):
        # An array that consists of common configuration items for alerts.
        self.config_list = config_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.DescribeConfigsResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeConfigsResponseBodyConfigList(DaraModel):
    def __init__(
        self,
        code: str = None,
        default_value: str = None,
        description: str = None,
        id: int = None,
        value: str = None,
    ):
        # The code of the common configuration item.
        self.code = code
        # The description of the default value for the common configuration item.
        self.default_value = default_value
        # The description of the common configuration item.
        self.description = description
        # The unique ID of the common configuration item.
        self.id = id
        # The value of the common configuration item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

