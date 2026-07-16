# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteServiceInstancesRequest(DaraModel):
    def __init__(
        self,
        container: str = None,
        instance_list: str = None,
        is_replica: bool = None,
        soft_restart: bool = None,
    ):
        # The name of the container in which to restart the process. This parameter is valid only when \\`SoftRestart\\` is set to \\`true\\`.
        self.container = container
        # The instances to restart. Separate multiple instance names with a comma (,). For more information, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.instance_list = instance_list
        # Specifies whether the instance is a replica.
        self.is_replica = is_replica
        # Specifies whether to restart only the container process without rebuilding the instance. The default value is false.
        self.soft_restart = soft_restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container is not None:
            result['Container'] = self.container

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list

        if self.is_replica is not None:
            result['IsReplica'] = self.is_replica

        if self.soft_restart is not None:
            result['SoftRestart'] = self.soft_restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')

        if m.get('IsReplica') is not None:
            self.is_replica = m.get('IsReplica')

        if m.get('SoftRestart') is not None:
            self.soft_restart = m.get('SoftRestart')

        return self

