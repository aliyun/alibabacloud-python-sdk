# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class RemoveInstancesResponseBody(DaraModel):
    def __init__(
        self,
        ignored_instances: List[main_models.RemoveInstancesResponseBodyIgnoredInstances] = None,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.ignored_instances = ignored_instances
        # The request ID.
        self.request_id = request_id
        # The ID of the scaling activity.
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        if self.ignored_instances:
            for v1 in self.ignored_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IgnoredInstances'] = []
        if self.ignored_instances is not None:
            for k1 in self.ignored_instances:
                result['IgnoredInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ignored_instances = []
        if m.get('IgnoredInstances') is not None:
            for k1 in m.get('IgnoredInstances'):
                temp_model = main_models.RemoveInstancesResponseBodyIgnoredInstances()
                self.ignored_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        return self

class RemoveInstancesResponseBodyIgnoredInstances(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.instance_id = instance_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

