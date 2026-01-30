# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeRenderingInstanceSettingsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        settings: List[main_models.DescribeRenderingInstanceSettingsResponseBodySettings] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.settings = settings

    def validate(self):
        if self.settings:
            for v1 in self.settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Settings'] = []
        if self.settings is not None:
            for k1 in self.settings:
                result['Settings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.settings = []
        if m.get('Settings') is not None:
            for k1 in m.get('Settings'):
                temp_model = main_models.DescribeRenderingInstanceSettingsResponseBodySettings()
                self.settings.append(temp_model.from_map(k1))

        return self

class DescribeRenderingInstanceSettingsResponseBodySettings(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')

        return self

