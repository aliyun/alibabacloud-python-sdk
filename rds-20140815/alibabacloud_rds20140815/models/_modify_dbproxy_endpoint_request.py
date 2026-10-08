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
        db_endpoint_cost_threshold_for_duckdb: str = None,
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
        # The timeout period for read consistency. Unit: milliseconds. Default value: **10**. Valid values: **0 to 60000**.
        self.causal_consist_read_timeout = causal_consist_read_timeout
        # The proxy features that you want to enable for the proxy endpoint. Separate multiple features with semicolons (;). Format: `Feature 1:Status;Feature 2:Status;...`. Do not add a semicolon (;) at the end.
        # 
        # Valid values for features:
        # * **ReadWriteSpliting**: Read/write splitting.
        # * **ConnectionPersist**: Connection pool.
        # * **TransactionReadSqlRouteOptimizeStatus**: Transaction splitting.
        # * **AZProximityAccess**: Nearest access.
        # * **CausalConsistRead**: Read consistency.
        # * **HtapFilter**: HTAP automatic request distribution among row store and column store nodes.
        # 
        # Valid values for status:
        # * **1**: Enabled.
        # * **0**: Disabled.
        # 
        # > - ApsaraDB RDS for PostgreSQL supports only **ReadWriteSpliting**.
        # > - The nearest access feature is supported only by the dedicated database proxy for MySQL.
        self.config_dbproxy_features = config_dbproxy_features
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the proxy endpoint. You can call DescribeDBProxyEndpoint to query the ID.
        # 
        # > - MySQL: This parameter is required when **DbEndpointOperator** is set to **Delete** or **Modify**.
        # > - PostgreSQL: This parameter is required when **DbEndpointOperator** is set to **Delete**, **Modify**, or **Create**.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # A deprecated parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The description of the proxy endpoint.
        self.db_endpoint_aliases = db_endpoint_aliases
        self.db_endpoint_cost_threshold_for_duckdb = db_endpoint_cost_threshold_for_duckdb
        # The minimum number of reserved instances.
        self.db_endpoint_min_slave_count = db_endpoint_min_slave_count
        # The type of operation. Valid values:
        # * **Modify**: The default value. Modifies the proxy endpoint.
        # * **Create**: Creates a proxy endpoint.
        # * **Delete**: Deletes a proxy endpoint.
        self.db_endpoint_operator = db_endpoint_operator
        # The read/write mode. Valid values:
        # * **ReadWrite**: Connects to the primary instance and can accept write requests.
        # * **ReadOnly**: The default value. Does not connect to the primary instance and cannot accept write requests.
        # 
        # > * This parameter is required when **DbEndpointOperator** is set to **Create**.
        # > * For ApsaraDB RDS for MySQL instances, if you change this parameter from **ReadWrite** to **ReadOnly**, the transaction splitting feature is disabled.
        self.db_endpoint_read_write_mode = db_endpoint_read_write_mode
        # The type of the proxy endpoint. This is a reserved parameter. You do not need to specify this parameter.
        self.db_endpoint_type = db_endpoint_type
        # The specified time at which the change takes effect. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > This parameter is required when **EffectiveTime** is set to **SpecificTime**.
        self.effective_specific_time = effective_specific_time
        # The effective period. Valid values:
        # 
        # * **Immediate**: The change takes effect immediately.
        # * **MaintainTime**: The change takes effect during the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # * **SpecificTime**: The change takes effect at a specified time.
        # 
        # Default value: **MaintainTime**.
        self.effective_time = effective_time
        self.owner_id = owner_id
        # The mode used to allocate read weights. Valid values:
        # 
        # * **Standard**: The default value. Read weights are automatically allocated based on instance specifications.
        # * **Custom**: Custom read weights.
        # 
        # > This parameter is required only when read/write splitting is enabled. For more information about read weight allocation, see [Read weight allocation](https://help.aliyun.com/document_detail/96076.html) for MySQL and [Enable and configure the database proxy service](https://help.aliyun.com/document_detail/418272.html) for PostgreSQL.
        self.read_only_instance_distribution_type = read_only_instance_distribution_type
        # The maximum latency threshold for read-only instances in read/write splitting. If the latency of a read-only instance exceeds this value, read traffic is not routed to the instance. Unit: seconds. If you do not specify this parameter, the current value is retained. Valid values: **0** to **3600**.
        # 
        # >- This parameter is required only when read/write splitting is enabled.
        # >- Default value: **30** seconds when the read/write mode is set to read/write (read/write splitting), and **-1** (disabled) when the read/write mode is set to read-only.
        self.read_only_instance_max_delay_time = read_only_instance_max_delay_time
        # The custom read weights to allocate to the primary instance and read-only instances. The value must be in increments of 100. Maximum value: 10000. Format:
        # 
        # - Regular instance: `{"PrimaryInstanceID":"Weight","ReadOnlyInstanceID":"Weight"...}`
        # 
        #     Example: `{"rm-uf6wjk5****":"500","rr-tfhfgk5xxx":"200"...}`
        # - ApsaraDB RDS for MySQL cluster instance: `{"ReadOnlyInstanceID":"Weight","DBClusterNode":{"PrimaryNodeID":"Weight","SecondaryNodeID":"Weight","SecondaryNodeID":"Weight"...}}`
        # 
        #     Example: `{"rr-tfhfgk5****":"200","DBClusterNode":{"rn-2z****":"0","rn-2z****":"400","rn-2z****":"400"...}}`
        #     > **DBClusterNode** is a request parameter specific to cluster instances. It contains the **NodeID** and **Weight** of the primary and secondary nodes.
        self.read_only_instance_weight = read_only_instance_weight
        # The region ID. You can call DescribeRegions to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The vSwitch ID that corresponds to the zone of the proxy endpoint. Default value: the vSwitch ID of the default endpoint of the proxy instance. You can call DescribeVSwitches to query available vSwitches.
        self.v_switch_id = v_switch_id
        # The VPC ID that corresponds to the zone of the proxy endpoint. Default value: the VPC ID of the default endpoint of the proxy instance. You can call DescribeDBInstanceAttribute to query the default VPC of the instance.
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

        if self.db_endpoint_cost_threshold_for_duckdb is not None:
            result['DbEndpointCostThresholdForDuckdb'] = self.db_endpoint_cost_threshold_for_duckdb

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

        if m.get('DbEndpointCostThresholdForDuckdb') is not None:
            self.db_endpoint_cost_threshold_for_duckdb = m.get('DbEndpointCostThresholdForDuckdb')

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

