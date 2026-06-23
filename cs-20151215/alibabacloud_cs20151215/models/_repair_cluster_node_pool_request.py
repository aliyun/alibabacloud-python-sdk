# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class RepairClusterNodePoolRequest(DaraModel):
    def __init__(
        self,
        auto_restart: bool = None,
        nodes: List[str] = None,
        operations: List[main_models.RepairClusterNodePoolRequestOperations] = None,
    ):
        # [This field is deprecated] Specifies whether to allow instance restart.
        self.auto_restart = auto_restart
        # The list of nodes.
        self.nodes = nodes
        # The repair operations to perform. If not specified, all repair operations are performed by default. In most scenarios, you do not need to specify this parameter.
        self.operations = operations

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_restart is not None:
            result['auto_restart'] = self.auto_restart

        if self.nodes is not None:
            result['nodes'] = self.nodes

        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_restart') is not None:
            self.auto_restart = m.get('auto_restart')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.RepairClusterNodePoolRequestOperations()
                self.operations.append(temp_model.from_map(k1))

        return self

class RepairClusterNodePoolRequestOperations(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        operation_id: str = None,
    ):
        # The list of repair operation parameters.
        self.args = args
        # The repair operation ID. Valid values:
        # 
        # - restart.kubelet: restart kubelet.
        # - restart.docker: restart Docker.
        # - restart.containerd: restart Containerd.
        # - restart.ntp: restart ntpd or chronyd.
        # - remove.containerdContainerInSandbox: delete a specified sandbox container under Containerd.
        # - remove.dockerContainerInSandbox: delete a specified sandbox container under Docker.
        # - remove.containerdContainer: delete a specified container under Containerd.
        # - remove.dockerContainer: delete a specified container under Docker.
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['args'] = self.args

        if self.operation_id is not None:
            result['operation_id'] = self.operation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')

        if m.get('operation_id') is not None:
            self.operation_id = m.get('operation_id')

        return self

