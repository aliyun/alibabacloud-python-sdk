# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class UpdateNodesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instances: List[main_models.UpdateNodesRequestInstances] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The information about the compute nodes that you want to update.
        self.instances = instances

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.UpdateNodesRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        return self

class UpdateNodesRequestInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        keep_alive: bool = None,
    ):
        # The instance ID of the compute node.
        self.instance_id = instance_id
        # Specifies whether to enable deletion protection for the compute node.
        self.keep_alive = keep_alive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')

        return self

