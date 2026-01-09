# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class MLServiceParam(DaraModel):
    def __init__(
        self,
        description: str = None,
        model: main_models.MLServiceParamModel = None,
        name: str = None,
        resource: main_models.MLServiceParamResource = None,
        service_type: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.description = description
        self.model = model
        self.name = name
        self.resource = resource
        self.service_type = service_type
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.model:
            self.model.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.model is not None:
            result['model'] = self.model.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.status is not None:
            result['status'] = self.status

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('model') is not None:
            temp_model = main_models.MLServiceParamModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resource') is not None:
            temp_model = main_models.MLServiceParamResource()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class MLServiceParamResource(DaraModel):
    def __init__(
        self,
        cpu_limit: int = None,
        gpu: int = None,
        memory_limit: int = None,
        replica: int = None,
    ):
        self.cpu_limit = cpu_limit
        self.gpu = gpu
        self.memory_limit = memory_limit
        self.replica = replica

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit

        if self.replica is not None:
            result['replica'] = self.replica

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        return self

class MLServiceParamModel(DaraModel):
    def __init__(
        self,
        model_resource_id: str = None,
        model_resource_type: str = None,
    ):
        self.model_resource_id = model_resource_id
        self.model_resource_type = model_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_resource_id is not None:
            result['modelResourceId'] = self.model_resource_id

        if self.model_resource_type is not None:
            result['modelResourceType'] = self.model_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelResourceId') is not None:
            self.model_resource_id = m.get('modelResourceId')

        if m.get('modelResourceType') is not None:
            self.model_resource_type = m.get('modelResourceType')

        return self

