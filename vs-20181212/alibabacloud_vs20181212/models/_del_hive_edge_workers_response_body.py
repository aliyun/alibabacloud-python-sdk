# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DelHiveEdgeWorkersResponseBody(DaraModel):
    def __init__(
        self,
        failed_instance_count: int = None,
        failed_instances: List[main_models.DelHiveEdgeWorkersResponseBodyFailedInstances] = None,
        request_id: str = None,
        success_instance_count: int = None,
        success_instances: List[main_models.DelHiveEdgeWorkersResponseBodySuccessInstances] = None,
    ):
        self.failed_instance_count = failed_instance_count
        self.failed_instances = failed_instances
        self.request_id = request_id
        self.success_instance_count = success_instance_count
        self.success_instances = success_instances

    def validate(self):
        if self.failed_instances:
            for v1 in self.failed_instances:
                 if v1:
                    v1.validate()
        if self.success_instances:
            for v1 in self.success_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_instance_count is not None:
            result['FailedInstanceCount'] = self.failed_instance_count

        result['FailedInstances'] = []
        if self.failed_instances is not None:
            for k1 in self.failed_instances:
                result['FailedInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_instance_count is not None:
            result['SuccessInstanceCount'] = self.success_instance_count

        result['SuccessInstances'] = []
        if self.success_instances is not None:
            for k1 in self.success_instances:
                result['SuccessInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedInstanceCount') is not None:
            self.failed_instance_count = m.get('FailedInstanceCount')

        self.failed_instances = []
        if m.get('FailedInstances') is not None:
            for k1 in m.get('FailedInstances'):
                temp_model = main_models.DelHiveEdgeWorkersResponseBodyFailedInstances()
                self.failed_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessInstanceCount') is not None:
            self.success_instance_count = m.get('SuccessInstanceCount')

        self.success_instances = []
        if m.get('SuccessInstances') is not None:
            for k1 in m.get('SuccessInstances'):
                temp_model = main_models.DelHiveEdgeWorkersResponseBodySuccessInstances()
                self.success_instances.append(temp_model.from_map(k1))

        return self

class DelHiveEdgeWorkersResponseBodySuccessInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message: str = None,
    ):
        self.instance_id = instance_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class DelHiveEdgeWorkersResponseBodyFailedInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message: str = None,
    ):
        self.instance_id = instance_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

