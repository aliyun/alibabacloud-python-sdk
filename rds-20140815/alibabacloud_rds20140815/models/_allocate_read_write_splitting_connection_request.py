# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateReadWriteSplittingConnectionRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        distribution_type: str = None,
        max_delay_time: str = None,
        net_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        weight: str = None,
    ):
        # The prefix of the read-only routing endpoint. The prefix must be unique. It can be up to 30 characters in length and can contain lowercase letters and hyphens (-). It must start with a lowercase letter.
        # 
        # >  The default prefix consists of the name of the primary instance followed by the letters rw.
        self.connection_string_prefix = connection_string_prefix
        # The primary instance ID. You can call the DescribeDBInstances operation to query the primary instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The method that is used to assign read weights. Valid values:
        # 
        # *   **Standard**: The system automatically assigns read weights to the primary and read-only instances based on the specifications of these instances.
        # *   **Custom**: You must manually assign a read weight to each instance.
        self.distribution_type = distribution_type
        # The threshold of the latency that is allowed on the read-only instances. Valid values: 0 to 7200. Default value: 30. Unit: seconds.
        # 
        # >  If the latency on a read-only instance exceeds the specified threshold, ApsaraDB RDS does not forward read requests to the read-only instance.
        self.max_delay_time = max_delay_time
        # The network type of the read-only routing endpoint. Valid values:
        # 
        # *   **Internet**
        # *   **Intranet**
        # 
        # >  The default value is Intranet. Make sure that the network type of the read-only routing endpoint is the same as that of the primary instance.
        self.net_type = net_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port that is associated with the read-only routing endpoint. Valid values: 1000 to 5999. Default value: 1433.
        self.port = port
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The read weights of the primary instance and its read-only instances. The read weight is increased in increments of 100. The maximum value is 10000.
        # 
        # *   For ApsaraDB RDS instances, the value of this parameter is in the following format: `{"<ID of the read-only instance >":<Weight>,"master":<Weight>,"slave":<Weight>}`.
        # *   For ApsaraDB MyBase instances, the value of this parameter is in the following format: `[{"instanceName":"<Primary instance ID>","weight":<Weight>,"role":"master"},{"instanceName":"<Primary instance ID>","weight":<Weight>,"role":"slave"},{"instanceName":"<Read-only instance ID>","weight":<Weight>,"role":"master"}]`
        # 
        # > 
        # 
        # *   This parameter must be specified when **DistributionType** is set to **Custom**.
        # 
        # *   If **DistributionType** is set to **Standard**, this parameter is invalid.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type

        if self.max_delay_time is not None:
            result['MaxDelayTime'] = self.max_delay_time

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')

        if m.get('MaxDelayTime') is not None:
            self.max_delay_time = m.get('MaxDelayTime')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

