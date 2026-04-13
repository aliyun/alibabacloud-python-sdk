# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringRequest(DaraModel):
    def __init__(
        self,
        current_connection_string: str = None,
        dbinstance_id: str = None,
        force_modify_suffix: bool = None,
        network_type: str = None,
        new_connection_string: str = None,
        new_port: int = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_modify_only: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The current endpoint that is to be modified.
        self.current_connection_string = current_connection_string
        # The instance ID.
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.force_modify_suffix = force_modify_suffix
        self.network_type = network_type
        # The new endpoint. It must be 8 to 64 characters in length and can contain letters and digits. It must start with a lowercase letter.
        # 
        # > You need only to specify the prefix of the endpoint. The content other than the prefix cannot be modified.
        self.new_connection_string = new_connection_string
        # The new port number of the instance. The port number must be within the range from 1000 to 65535.
        # 
        # >  This parameter is available only when you set the **DBInstanceId** parameter to the ID of an instance that uses cloud disks.
        self.new_port = new_port
        # The ID of the mongos in the specified sharded cluster instance. Only one mongos ID can be specified in each call.
        # 
        # > This parameter is valid only when you specify the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.port_modify_only = port_modify_only
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.force_modify_suffix is not None:
            result['ForceModifySuffix'] = self.force_modify_suffix

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string

        if self.new_port is not None:
            result['NewPort'] = self.new_port

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_modify_only is not None:
            result['PortModifyOnly'] = self.port_modify_only

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ForceModifySuffix') is not None:
            self.force_modify_suffix = m.get('ForceModifySuffix')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')

        if m.get('NewPort') is not None:
            self.new_port = m.get('NewPort')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortModifyOnly') is not None:
            self.port_modify_only = m.get('PortModifyOnly')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

