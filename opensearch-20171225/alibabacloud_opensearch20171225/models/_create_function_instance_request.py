# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateFunctionInstanceRequest(DaraModel):
    def __init__(
        self,
        create_parameters: List[main_models.CreateFunctionInstanceRequestCreateParameters] = None,
        cron: str = None,
        description: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
        usage_parameters: List[main_models.CreateFunctionInstanceRequestUsageParameters] = None,
    ):
        # The parameters used to create the instance.
        self.create_parameters = create_parameters
        # The CRON expression used to schedule periodic training, in the format of Minutes Hours DayofMonth Month DayofWeek. The default value is empty, which specifies that no periodic training is performed. A value of 0 for DayofWeek specifies Sunday.
        self.cron = cron
        # The description.
        self.description = description
        # The feature type.
        # 
        # *   Default value: PAAS. Training is required before you can use the feature.
        self.function_type = function_type
        # The instance name. The name must be 1 to 30 characters in length and can contain letters, digits, and underscores (_). The name is case-sensitive and must start with a letter.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The model type. The value varies based on the model.
        # 
        # *   Click-through rate (CTR) model: tf_checkpoint
        # *   Popularity model: pop
        # *   Category model: offline_inference
        # *   Hotword model: offline_inference
        # *   Hint model: offline_inference
        # *   Hotword model for real-time top searches: near_realtime
        # *   Personalized hint model: near_realtime
        # *   Drop-down suggestion model: offline_inference
        # *   Tokenization model: text
        # *   Term weight model: tf_checkpoint
        # *   Synonym model: offline_inference
        # 
        # This parameter is required.
        self.model_type = model_type
        # The parameters used to use the instance.
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

        if self.function_type is not None:
            result['functionType'] = self.function_type

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

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
                temp_model = main_models.CreateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k1))

        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        self.usage_parameters = []
        if m.get('usageParameters') is not None:
            for k1 in m.get('usageParameters'):
                temp_model = main_models.CreateFunctionInstanceRequestUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k1))

        return self

class CreateFunctionInstanceRequestUsageParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
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

class CreateFunctionInstanceRequestCreateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
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

