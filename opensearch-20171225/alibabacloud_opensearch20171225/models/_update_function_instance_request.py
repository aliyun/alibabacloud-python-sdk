# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class UpdateFunctionInstanceRequest(DaraModel):
    def __init__(
        self,
        create_parameters: List[main_models.UpdateFunctionInstanceRequestCreateParameters] = None,
        cron: str = None,
        description: str = None,
        usage_parameters: List[main_models.UpdateFunctionInstanceRequestUsageParameters] = None,
    ):
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters
        # The cron expression used to schedule periodic training, in the format of (Minutes Hours DayofMonth Month DayofWeek). The default value is empty, which indicates that no periodic training is performed. DayofWeek 0 indicates Sunday.
        self.cron = cron
        # The description of the instance.
        self.description = description
        # The parameters that are used.
        self.usage_parameters = usage_parameters

    def validate(self):
        if self.create_parameters:
            for v1 in self.create_parameters:
                 if v1:
                    v1.validate()
        if self.usage_parameters:
            for v1 in self.usage_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['createParameters'] = []
        if self.create_parameters is not None:
            for k1 in self.create_parameters:
                result['createParameters'].append(k1.to_map() if k1 else None)

        if self.cron is not None:
            result['cron'] = self.cron

        if self.description is not None:
            result['description'] = self.description

        result['usageParameters'] = []
        if self.usage_parameters is not None:
            for k1 in self.usage_parameters:
                result['usageParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k1 in m.get('createParameters'):
                temp_model = main_models.UpdateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k1))

        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.usage_parameters = []
        if m.get('usageParameters') is not None:
            for k1 in m.get('usageParameters'):
                temp_model = main_models.UpdateFunctionInstanceRequestUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k1))

        return self

class UpdateFunctionInstanceRequestUsageParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class UpdateFunctionInstanceRequestCreateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

