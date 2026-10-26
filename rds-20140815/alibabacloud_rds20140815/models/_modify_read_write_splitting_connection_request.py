# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyReadWriteSplittingConnectionRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        distribution_type: str = None,
        max_delay_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        weight: str = None,
    ):
        # The prefix of the read/write splitting endpoint. The prefix must be unique and can contain only lowercase letters and hyphens. It must start with a letter and be up to 30 characters in length.
        # > By default, the prefix consists of the instance name and the "rw" string.
        self.connection_string_prefix = connection_string_prefix
        # Instance ID of the primary instance. You can call the DescribeDBInstances operation to query instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The read weight distribution mode. Valid values:
        # * **Standard**: automatically distributes weights based on instance specifications.
        # * **Custom**: uses custom weights.
        # 
        # > You must specify at least one of the **MaxDelayTime** and **DistributionType** parameters.
        self.distribution_type = distribution_type
        # The latency threshold, in seconds. If the latency of a read-only instance exceeds this threshold, read traffic is not routed to the instance. If you do not specify this parameter, the original value is retained.
        # 
        # > * The **MaxDelayTime** parameter does not apply to SQL Server 2017 Cluster Edition instances.
        # > * You must specify at least one of the **MaxDelayTime** and **DistributionType** parameters.
        self.max_delay_time = max_delay_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port number of the read/write splitting endpoint.
        self.port = port
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The read weights of the primary and read-only instances. The weight value must be a multiple of 100 and can be up to 10000.
        # * Format for ApsaraDB RDS instances: `{"<Read-only instance ID>":<Weight>,"master":<Weight>,"slave":<Weight>}`
        # * Format for MyBase instances: `[{"instanceName":"<Primary instance ID>","weight":<Weight>,"role":"master"},{"instanceName":"<Primary instance ID>","weight":<Weight>,"role":"slave"},{"instanceName":"<Read-only instance ID>","weight":<Weight>,"role":"master"}]`
        # 
        # > * This parameter is required when **DistributionType** is set to **Custom**.
        # > * This parameter does not take effect when **DistributionType** is set to **Standard**.
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

