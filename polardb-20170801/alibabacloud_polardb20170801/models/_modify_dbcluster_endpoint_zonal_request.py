# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterEndpointZonalRequest(DaraModel):
    def __init__(
        self,
        auto_add_new_nodes: str = None,
        client_token: str = None,
        dbcluster_id: str = None,
        dbendpoint_description: str = None,
        dbendpoint_id: str = None,
        endpoint_config: str = None,
        nodes: str = None,
        owner_account: str = None,
        owner_id: int = None,
        polar_scc_timeout_action: str = None,
        polar_scc_wait_timeout: str = None,
        read_write_mode: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scc_mode: str = None,
    ):
        # Specifies whether to automatically add new nodes to this endpoint. Valid values: 
        # 
        # - **Enable**: Yes.
        # - **Disable**: No (default).
        self.auto_add_new_nodes = auto_add_new_nodes
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value of this parameter on the client side. The value must be unique across different requests and is case-sensitive. The value can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The edge cloud cluster ID. You can call DescribeDBClustersZonal to query the ID. The ID of a common PolarDB cluster returned by DescribeDBClusters is not supported.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The endpoint name.
        self.dbendpoint_description = dbendpoint_description
        # The cluster endpoint ID.
        # 
        # This parameter is required.
        self.dbendpoint_id = dbendpoint_id
        # The advanced configurations of the cluster endpoint. The value is in JSON format. You can configure the consistency level, transaction splitting, whether to offload offload reads from primary node, and the connection pool.
        # 
        # * To set the load balancing policy, use the format `{"LoadBalancePolicy":"Load balancing policy"}`. Valid values:   
        #     * **0**: load balancing based on the number of connections (default).
        #     * **1**: load balancing based on the number of active requests.
        # 
        # * To set whether to offload offload reads from primary node, use the format `{"MasterAcceptReads":"Whether to offload offload reads from primary node"}`. Valid values:
        #     * **on**: The primary node accepts reads (default).
        #     * **off**: Reads are offloaded from the primary node.
        # 
        # * To set transaction splitting, use the format `{"DistributedTransaction":"Transaction splitting"}`. Valid values:
        #     * **on**: enables transaction splitting (default).
        #     * **off**: disables transaction splitting.
        # 
        # * To set the consistency level, use the format `{"ConsistLevel":"Consistency level"}`. Valid values:
        #     * **0**: eventual consistency (weak).
        #     * **1**: session consistency (medium) (default).
        #     * **2**: global consistency (strong).
        # 
        # * To set the global consistency read timeout period, use the format `{"ConsistTimeout":"Global consistency read timeout period"}`. Valid values: 0 to 60000. Default value: 20. Unit: milliseconds.
        # 
        # * To set the session consistency read timeout period, use the format `{"ConsistSessionTimeout":"Session consistency read timeout period"}`. Valid values: 0 to 60000. Default value: 0. Unit: milliseconds.
        # 
        # * To set the global (or session) consistency read timeout policy, use the format `{"ConsistTimeoutAction":"Global consistency read timeout policy"}`. Valid values:
        #     * **0**: forwards read requests to the primary node (default).
        #     * **1**: The proxy returns an error message `wait replication complete timeout, please retry` to the application.
        # 
        # * To set the connection pool, use the format `{"ConnectionPersist":"Connection pool"}`. Valid values:
        #     * **off**: disables the connection pool (default).
        #     * **Session**: enables the session-level connection pool.
        #     * **Transaction**: enables transaction-level connection pooling.
        # 
        # * To set parallel query, use the format `{"MaxParallelDegree":"Parallel query"}`. Valid values:
        #     * **on**: enables parallel query.
        #     * **off**: disables parallel query (default).
        # 
        # * To set automatic request distribution between row store and column store nodes, use the format `{"EnableHtapImci":"Automatic request distribution between row store and column store nodes"}`. Valid values:
        #     * **on**: enables automatic request distribution between row store and column store nodes.
        #     * **off**: disables automatic request distribution between row store and column store nodes (default).
        # 
        # 
        # * To set whether to enable overload protection, use the format `{"EnableOverloadThrottle":"Whether to enable overload protection"}`. Valid values:
        #     * **on**: enables overload protection.
        #     * **off**: disables overload protection (default).
        # 
        # > * You can configure transaction splitting, whether to offload offload reads from primary node, the connection pool, and whether to enable overload protection only when the read/write mode of the PolarDB for MySQL cluster endpoint is set to **Read/write (automatic read/write splitting)**.
        # > * When the read/write mode of the PolarDB for MySQL cluster endpoint is set to **Read-only**, both **load balancing based on the number of connections** and **load balancing based on the number of active requests** are supported. Cluster endpoints in **Read/write (automatic read/write splitting)** mode support only **load balancing based on the number of active requests**.
        # > * You can configure automatic request distribution between row store and column store nodes when the read/write mode of the PolarDB for MySQL cluster endpoint is set to **Read/write (automatic read/write splitting)**, or when the read/write mode is set to **Read-only** and the load balancing policy is set to **load balancing based on the number of active requests**.
        # > * Only PolarDB for MySQL supports setting the consistency level to global consistency.
        # > * If **ReadWriteMode** is set to **ReadOnly**, the consistency level can only be set to **0**.
        # > * You can configure the consistency level, transaction splitting, whether to offload offload reads from primary node, and the connection pool at the same time. Example: `{"ConsistLevel":"1","DistributedTransaction":"on","ConnectionPersist":"Session","MasterAcceptReads":"on"}`.
        # > * The transaction splitting configuration is restricted by the consistency level configuration. For example, if the consistency level is set to **0**, transaction splitting cannot be enabled. If the consistency level is set to **1** or **2**, transaction splitting can be enabled.
        self.endpoint_config = endpoint_config
        # The read-only nodes to be added to the destination endpoint. Separate multiple nodes with commas (,). Default value: the original nodes.
        # 
        # > * For PolarDB for MySQL, you must specify node IDs.
        # > * For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle), you must specify node role names, such as `Writer,Reader1,Reader2`.
        # > * If **ReadWriteMode** is set to **ReadOnly**, you can mount only one node. However, if this node fails, the endpoint may be unavailable for up to 1 hour. Do not use this configuration in production environments. Therefore, select at least two nodes to improve availability.
        # > * If **ReadWriteMode** is set to **ReadWrite**, you must select at least two nodes.
        #     * For PolarDB for MySQL, you can select any two nodes. If both nodes are read-only nodes, write requests are forwarded to the primary node.
        #     * For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle), the primary node must be included.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The global consistency timeout policy. Valid values:
        # 
        # - **0**: send the request to the primary node.
        # 
        # - **2**: timeout degradation. If a global consistency read times out, the current query operation is automatically downgraded to regular requests, and the client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The global consistency timeout period.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - **ReadWrite**: read/write (automatic read/write splitting).
        # - **ReadOnly**: read-only.
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values: on (enabled) and off (disabled).
        self.scc_mode = scc_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_add_new_nodes is not None:
            result['AutoAddNewNodes'] = self.auto_add_new_nodes

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbendpoint_description is not None:
            result['DBEndpointDescription'] = self.dbendpoint_description

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.polar_scc_timeout_action is not None:
            result['PolarSccTimeoutAction'] = self.polar_scc_timeout_action

        if self.polar_scc_wait_timeout is not None:
            result['PolarSccWaitTimeout'] = self.polar_scc_wait_timeout

        if self.read_write_mode is not None:
            result['ReadWriteMode'] = self.read_write_mode

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scc_mode is not None:
            result['SccMode'] = self.scc_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAddNewNodes') is not None:
            self.auto_add_new_nodes = m.get('AutoAddNewNodes')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBEndpointDescription') is not None:
            self.dbendpoint_description = m.get('DBEndpointDescription')

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('EndpointConfig') is not None:
            self.endpoint_config = m.get('EndpointConfig')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PolarSccTimeoutAction') is not None:
            self.polar_scc_timeout_action = m.get('PolarSccTimeoutAction')

        if m.get('PolarSccWaitTimeout') is not None:
            self.polar_scc_wait_timeout = m.get('PolarSccWaitTimeout')

        if m.get('ReadWriteMode') is not None:
            self.read_write_mode = m.get('ReadWriteMode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SccMode') is not None:
            self.scc_mode = m.get('SccMode')

        return self

