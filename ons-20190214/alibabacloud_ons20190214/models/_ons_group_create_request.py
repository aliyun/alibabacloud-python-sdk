# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsGroupCreateRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_type: str = None,
        instance_id: str = None,
        remark: str = None,
    ):
        # The ID of the consumer group that you want to create. The group ID must meet the following rules:
        # 
        # *   The group ID must be 2 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores (_).
        # *   If the ApsaraMQ for RocketMQ instance in which you want to create the consumer group uses a namespace, the group ID must be unique in the instance. The group ID cannot be the same as an existing group ID or a topic name in the instance. The group ID can be the same as a group ID or a topic name in another instance that uses a different namespace. For example, if Instance A and Instance B use different namespaces, a group ID in Instance A can be the same as a group ID or a topic name in Instance B.
        # *   If the instance does not use a namespace, the group ID must be globally unique across instances and regions. The group ID cannot be the same as an existing group ID or topic name in ApsaraMQ for RocketMQ instances that belong to your Alibaba Cloud account.
        # 
        # > 
        # 
        # *   After the consumer group is created, the group ID cannot be changed.
        # 
        # *   To check whether an instance uses a namespace, log on to the ApsaraMQ for RocketMQ console, go to the **Instance Details** page, and then view the value of the Namespace field in the **Basic Information** section.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The protocol over which clients in the consumer group communicate with the ApsaraMQ for RocketMQ broker. All clients in a consumer group communicate with the ApsaraMQ for RocketMQ broker over the same protocol. You must create different groups for TCP clients and HTTP clients. Valid values:
        # 
        # *   **tcp**: Clients in the consumer group consume messages over TCP. This is the default value.
        # *   **http**: Clients in the consumer group consume messages over HTTP.
        self.group_type = group_type
        # The ID of the instance in which you want to create the consumer group.
        self.instance_id = instance_id
        # The description of the consumer group.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

