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
        # The name of the container whose process needs to be restarted. This parameter takes effect only if the SoftRestart parameter is set to true.
        self.container = container
        # The instances that you want to restart. Separate multiple instance names with commas (,). For more information about how to query the instance name, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.instance_list = instance_list
        self.is_replica = is_replica
        # Specifies whether to restart only the container process without recreating the instance. Default value: false. Valid values: true and false.
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

