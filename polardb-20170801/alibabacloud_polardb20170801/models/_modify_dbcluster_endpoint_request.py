# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterEndpointRequest(DaraModel):
    def __init__(
        self,
        auto_add_new_nodes: str = None,
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
        # Specifies whether new nodes are automatically added to the endpoint. Valid values: 
        # 
        # - **Enable**: New nodes are automatically added.
        # - **Disable**: New nodes are not automatically added. (Default)
        self.auto_add_new_nodes = auto_add_new_nodes
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The cluster endpoint ID.
        # 
        # This parameter is required.
        self.dbendpoint_id = dbendpoint_id
        # The advanced configuration of the cluster endpoint in JSON format. You can configure the consistency level, transaction splitting, whether the primary node accepts read requests, and connection pooling.
        # 
        # * To set the load balancing policy, use the format `{\\"LoadBalancePolicy\\":\\"Load balancing policy\\"}`. Valid values:   
        #     * **0**: connection-based load balancing (default)
        #     * **1**: active-request-based load balancing
        # 
        # * To set whether the primary node accepts read requests, use the format `{\\"MasterAcceptReads\\":\\"Whether the primary node accepts reads\\"}`. Valid values:
        #     * **on**: The primary node accepts read requests. (Default)
        #     * **off**: The primary node does not accept read requests.
        # 
        # * To set transaction splitting, use the format `{\\"DistributedTransaction\\":\\"Transaction splitting\\"}`. Valid values:
        #     * **on**: Transaction splitting is enabled. (Default)
        #     * **off**: Transaction splitting is disabled.
        # 
        # * To set the consistency level, use the format `{\\"ConsistLevel\\":\\"Consistency level\\"}`. Valid values:
        #     * **0**: eventual consistency (weak)
        #     * **1**: session consistency (medium) (default)
        #     * **2**: global consistency (strong)
        # 
        # * To set the global consistency read timeout period, use the format `{\\"ConsistTimeout\\":\\"Global consistency read timeout\\"}`. Valid values: 0 to 60000. Default value: 20. Unit: ms.
        # 
        # * To set the session consistency read timeout period, use the format `{\\"ConsistSessionTimeout\\":\\"Session consistency read timeout\\"}`. Valid values: 0 to 60000. Default value: 0. Unit: ms.
        # 
        # * To set the global (or session) consistency read timeout policy, use the format `{\\"ConsistTimeoutAction\\":\\"Global consistency read timeout policy\\"}`. Valid values:
        #     * **0**: Forward the read request to the primary node. (Default)
        #     * **1**: The proxy returns the error message `wait replication complete timeout, please retry` to the application.
        # 
        # * To set the connection pool, use the format `{\\"ConnectionPersist\\":\\"Connection pool\\"}`. Valid values:
        #     * **off**: The connection pool is disabled. (Default)
        #     * **Session**: The session-level connection pool is enabled.
        #     * **Transaction**: The transaction-level connection pooling is enabled.
        # 
        # * To set parallel query, use the format `{\\"MaxParallelDegree\\":\\"Parallel query\\"}`. Valid values:
        #     * **on**: Parallel query is enabled.
        #     * **off**: Parallel query is disabled. (Default)
        # 
        # * To set automatic request distribution among row offload reads from primary nodes, use the format `{\\"EnableHtapImci\\":\\"Automatic request distribution among row store and column store\\"}`. Valid values:
        #     * **on**: Automatic request distribution among row offload reads from primary nodes is enabled.
        #     * **off**: Automatic request distribution among row offload reads from primary nodes is disabled. (Default)
        # 
        # 
        # * To set whether to enable overload protection, use the format `{\\"EnableOverloadThrottle\\":\\"Whether to enable overload protection\\"}`. Valid values:
        #     * **on**: Overload protection is enabled.
        #     * **off**: Overload protection is disabled. (Default)
        # 
        # * To set node weights, use the format `{\\"NodesWeight\\":{\\"Node ID\\":\\"Weight value\\"}}`.
        # 
        # > * Transaction splitting, whether the primary node accepts read requests, connection pooling, and overload protection can be configured only when the read/write mode of the PolarDB for MySQL cluster endpoint is **ReadWrite (automatic read/write splitting)**.
        # > * When the read/write mode of the PolarDB for MySQL cluster endpoint is **ReadOnly**, both **connection-based load balancing** and **active-request-based load balancing** policies are supported. The **ReadWrite (automatic read/write splitting)** mode supports only the **active-request-based load balancing** policy.
        # > * Automatic request distribution among row offload reads from primary nodes can be configured when the read/write mode of the PolarDB for MySQL cluster endpoint is **ReadWrite (automatic read/write splitting)**, or when the read/write mode is **ReadOnly** and the load balancing policy is **active-request-based load balancing**.
        # > * Only PolarDB for MySQL supports setting the consistency level to global consistency.
        # > * If **ReadWriteMode** is set to **ReadOnly**, the consistency level can only be set to **0**.
        # > * You can configure the consistency level, transaction splitting, whether the primary node accepts read requests, and connection pooling at the same time. Example: `{\\"ConsistLevel\\":\\"1\\",\\"DistributedTransaction\\":\\"on\\",\\"ConnectionPersist\\":\\"Session\\",\\"MasterAcceptReads\\":\\"on\\"}`.
        # > * Transaction splitting is constrained by the consistency level. For example, transaction splitting cannot be enabled when the consistency level is **0**. Transaction splitting can be enabled when the consistency level is **1** or **2**.
        self.endpoint_config = endpoint_config
        # The read load nodes to add to the endpoint. Separate multiple nodes with commas (,). Default value: the existing nodes.
        # 
        # > * For PolarDB for MySQL, specify node IDs.
        # > * For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle), specify node role names, such as `Writer,Reader1,Reader2`.
        # > * If **ReadWriteMode** is set to **ReadOnly**, you can mount only one node. However, if this node fails, the endpoint may be unavailable for up to 1 hour. Do not use this configuration in production environments. Select at least 2 nodes to improve availability.
        # > * If **ReadWriteMode** is set to **ReadWrite**, select at least 2 nodes.
        #     * PolarDB for MySQL allows you to select any two nodes. If both nodes are read-only nodes, write requests are forwarded to the primary node.
        #     * PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle) require the primary node to be included.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The timeout policy for global consistency. Valid values:
        # 
        # - **0**: Send the request to the primary node.
        # 
        # - **2**: Timeout degradation. When the global consistency read times out, the query is automatically degraded to regular requests, and the client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - **ReadWrite**: read/write (automatic read/write splitting)
        # - **ReadOnly**: read-only
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values:
        # 
        # - **ON**: Enabled.
        # 
        # - **OFF**: Disabled.
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

