# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBProxyEndpointRequest(DaraModel):
    def __init__(
        self,
        causal_consist_read_timeout: str = None,
        config_dbproxy_features: str = None,
        dbinstance_id: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_engine_type: str = None,
        db_endpoint_aliases: str = None,
        db_endpoint_min_slave_count: str = None,
        db_endpoint_operator: str = None,
        db_endpoint_read_write_mode: str = None,
        db_endpoint_type: str = None,
        effective_specific_time: str = None,
        effective_time: str = None,
        owner_id: int = None,
        read_only_instance_distribution_type: str = None,
        read_only_instance_max_delay_time: str = None,
        read_only_instance_weight: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The consistency read timeout period. Unit: milliseconds. Default value: **10** Unit: milliseconds. Valid values: **0 to 60000**
        self.causal_consist_read_timeout = causal_consist_read_timeout
        # The capabilities that you want to enable for the proxy endpoint. If you specify more than one capability, separate the capabilities with semicolons (;). Format: `Capability 1:Status;Capability 2:Status;...`. Do not add a semicolon (;) at the end of the value.
        # 
        # Valid capability values:
        # 
        # *   **ReadWriteSpliting**: read/write splitting
        # *   **ConnectionPersist**: connection pooling
        # *   **TransactionReadSqlRouteOptimizeStatus**: transaction splitting
        # *   **AZProximityAccess**: nearest access
        # *   **CausalConsistRead**: read consistency
        # 
        # Valid status values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        # 
        # > 
        # 
        # *   If the instance runs PostgreSQL, you can enable only read/write splitting, which is specified by **ReadWriteSpliting**.
        # 
        # *   Nearest access is supported only by dedicated database proxies for RDS instances that run MySQL.
        self.config_dbproxy_features = config_dbproxy_features
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the proxy endpoint. You can call the DescribeDBProxyEndpoint operation to query the proxy endpoint ID.
        # 
        # > *   If the instance runs MySQL and you set **DbEndpointOperator** to **Delete** or **Modify**, you must specify DBProxyEndpointId.
        # > *   If the instance runs PostgreSQL and you set **DbEndpointOperator** to **Delete**, **Modify**, or **Create**, you must specify DBProxyEndpointId.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # A deprecated parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The description of the proxy terminal.
        self.db_endpoint_aliases = db_endpoint_aliases
        # The minimum number of reserved instances.
        self.db_endpoint_min_slave_count = db_endpoint_min_slave_count
        # The type of operation that you want to perform. Valid values:
        # 
        # *   **Modify**: Modify a proxy terminal. This is the default value.
        # *   **Create**: Create a proxy terminal.
        # *   **Delete**: Delete a proxy terminal.
        self.db_endpoint_operator = db_endpoint_operator
        # The read and write attributes of the proxy terminal. Valid values:
        # 
        # *   **ReadWrite**: The proxy terminal connects to the primary instance and can receive both read and write requests.
        # *   **ReadOnly**: The proxy terminal does not connect to the primary instance and can receive only read requests. This is the default value.
        # 
        # > *   If you set **DbEndpointOperator** to **Create**, you must also specify DbEndpointReadWriteMode.
        # > *   If the instance runs MySQL and you change the value of this parameter from **ReadWrite** to **ReadOnly**, the transaction splitting feature is disabled.
        self.db_endpoint_read_write_mode = db_endpoint_read_write_mode
        # The type of the proxy terminal. This is a reserved parameter. You do not need to specify this parameter.
        self.db_endpoint_type = db_endpoint_type
        # The point in time that you want to specify. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # >  If **EffectiveTime** is set to **SpecificTime**, you must specify this parameter.
        self.effective_specific_time = effective_specific_time
        # The effective time. Valid values:
        # 
        # *   **Immediate**: The effective time is immediate.
        # *   **MaintainTime**: The effective time is within the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # *   **SpecificTime**: The effective time is a specified point in time.
        # 
        # Default value: **MaintainTime**.
        self.effective_time = effective_time
        self.owner_id = owner_id
        # The policy that is used to allocate read weights. Valid values:
        # 
        # *   **Standard** (default): The system automatically assigns read weights to the primary and read-only instances based on the specifications of these instances.
        # *   **Custom**: You must manually allocate read weights to the primary and read-only instances.
        # 
        # >  You must specify this parameter when read/write splitting is enabled. For more information about the permission allocation policy, see [Modify the latency threshold and read weights of ApsaraDB RDS for MySQL instances](https://help.aliyun.com/document_detail/96076.html) and [Enable and configure the database proxy feature for an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/418272.html).
        self.read_only_instance_distribution_type = read_only_instance_distribution_type
        # The maximum latency threshold that is allowed for read/write splitting. If the latency on a read-only instance exceeds the threshold that you specified, the system no longer forwards read requests to the read-only instance. If you do not specify this parameter, the original value of this parameter is retained. Valid values: **0** to **3600**.
        # 
        # > 
        # 
        # *   You must specify this parameter only when read/write splitting is enabled.
        # 
        # *   If the database proxy endpoint has the read and write attributes, the default value of this parameter is **30** and read/write splitting is supported. If the database proxy endpoint has the read-only attribute, the default value of this parameter is **-1** and read/write splitting is not supported. Unit: seconds.
        self.read_only_instance_max_delay_time = read_only_instance_max_delay_time
        # The read weights of the instance and its read-only instances. A read weight must be a multiple of 100 and cannot exceed 10000. Formats:
        # 
        # *   Standard instance: `{"ID of the primary instance":"Weight","ID of the read-only instance":"Weight"...}`
        # 
        #     Example: `{"rm-uf6wjk5****":"500","rr-tfhfgk5xxx":"200"...}`
        # 
        # *   Instance on RDS Cluster Edition: `{"ID of the read-only instance":"Weight","DBClusterNode":{"ID of the primary node":"Weight","ID of the secondary node":"Weight","ID of the secondary node":"Weight"...}}`
        # 
        #     Example: `{"rr-tfhfgk5****":"200","DBClusterNode":{"rn-2z****":"0","rn-2z****":"400","rn-2z****":"400"...}}`
        # 
        #     > **DBClusterNode** is required if the instance runs RDS Cluster Edition. The DBClusterNode parameter includes information about **IDs** and **weights** of the primary and secondary nodes..
        self.read_only_instance_weight = read_only_instance_weight
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the vSwitch in the zone in which the proxy endpoint is specified. The default value is the ID of the vSwitch that corresponds to the default terminal of the database proxy. You can call the DescribeVSwitches operation to query existing vSwitches.
        self.v_switch_id = v_switch_id
        # The VPC ID of the zone in which the proxy endpoint is specified. The default value is the VPC ID that corresponds to the default terminal of the database proxy. You can call the DescribeDBInstanceAttribute operation to query the default VPC of an instance.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.causal_consist_read_timeout is not None:
            result['CausalConsistReadTimeout'] = self.causal_consist_read_timeout

        if self.config_dbproxy_features is not None:
            result['ConfigDBProxyFeatures'] = self.config_dbproxy_features

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.db_endpoint_aliases is not None:
            result['DbEndpointAliases'] = self.db_endpoint_aliases

        if self.db_endpoint_min_slave_count is not None:
            result['DbEndpointMinSlaveCount'] = self.db_endpoint_min_slave_count

        if self.db_endpoint_operator is not None:
            result['DbEndpointOperator'] = self.db_endpoint_operator

        if self.db_endpoint_read_write_mode is not None:
            result['DbEndpointReadWriteMode'] = self.db_endpoint_read_write_mode

        if self.db_endpoint_type is not None:
            result['DbEndpointType'] = self.db_endpoint_type

        if self.effective_specific_time is not None:
            result['EffectiveSpecificTime'] = self.effective_specific_time

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.read_only_instance_distribution_type is not None:
            result['ReadOnlyInstanceDistributionType'] = self.read_only_instance_distribution_type

        if self.read_only_instance_max_delay_time is not None:
            result['ReadOnlyInstanceMaxDelayTime'] = self.read_only_instance_max_delay_time

        if self.read_only_instance_weight is not None:
            result['ReadOnlyInstanceWeight'] = self.read_only_instance_weight

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CausalConsistReadTimeout') is not None:
            self.causal_consist_read_timeout = m.get('CausalConsistReadTimeout')

        if m.get('ConfigDBProxyFeatures') is not None:
            self.config_dbproxy_features = m.get('ConfigDBProxyFeatures')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyEndpointId') is not None:
            self.dbproxy_endpoint_id = m.get('DBProxyEndpointId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DbEndpointAliases') is not None:
            self.db_endpoint_aliases = m.get('DbEndpointAliases')

        if m.get('DbEndpointMinSlaveCount') is not None:
            self.db_endpoint_min_slave_count = m.get('DbEndpointMinSlaveCount')

        if m.get('DbEndpointOperator') is not None:
            self.db_endpoint_operator = m.get('DbEndpointOperator')

        if m.get('DbEndpointReadWriteMode') is not None:
            self.db_endpoint_read_write_mode = m.get('DbEndpointReadWriteMode')

        if m.get('DbEndpointType') is not None:
            self.db_endpoint_type = m.get('DbEndpointType')

        if m.get('EffectiveSpecificTime') is not None:
            self.effective_specific_time = m.get('EffectiveSpecificTime')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReadOnlyInstanceDistributionType') is not None:
            self.read_only_instance_distribution_type = m.get('ReadOnlyInstanceDistributionType')

        if m.get('ReadOnlyInstanceMaxDelayTime') is not None:
            self.read_only_instance_max_delay_time = m.get('ReadOnlyInstanceMaxDelayTime')

        if m.get('ReadOnlyInstanceWeight') is not None:
            self.read_only_instance_weight = m.get('ReadOnlyInstanceWeight')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

