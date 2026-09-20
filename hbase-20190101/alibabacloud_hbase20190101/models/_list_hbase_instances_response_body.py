# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class ListHBaseInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.ListHBaseInstancesResponseBodyInstances = None,
        request_id: str = None,
    ):
        self.instances = instances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.ListHBaseInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHBaseInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.ListHBaseInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.ListHBaseInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class ListHBaseInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        is_default: bool = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        return self

