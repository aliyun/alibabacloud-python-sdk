# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartDBInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_id: str = None,
        node_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parallel_restart_mongos: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_mode: str = None,
    ):
        # The instance ID. Before calling this operation, ensure that the instance is in the Running state. You can check the current status of the instance by checking the DBInstanceStatus field returned by the DescribeDBInstanceAttribute operation.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the shard or mongos node in the sharded cluster instance.
        # 
        # > If the instance is a sharded cluster instance and this parameter is not specified, the entire sharded cluster instance is restarted.
        self.node_id = node_id
        # The type of the node to be restarted in the sharded cluster instance. Valid values:
        # - **db**: shard node.
        # - **mongos**: mongos node.
        # - **cs**: Configserver node.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to restart mongos nodes in parallel. This parameter takes effect only when multiple mongos nodes are restarted in a batch.
        self.parallel_restart_mongos = parallel_restart_mongos
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time when the instance is restarted. Valid values:
        # - 0: Restarts the instance immediately.
        # - 1: Restarts the instance within the O&M window.
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parallel_restart_mongos is not None:
            result['ParallelRestartMongos'] = self.parallel_restart_mongos

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParallelRestartMongos') is not None:
            self.parallel_restart_mongos = m.get('ParallelRestartMongos')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

