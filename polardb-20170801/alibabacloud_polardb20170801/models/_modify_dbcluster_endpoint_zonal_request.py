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
        # - **Enable**: yes
        # 
        # - **Disable**: no (default)
        self.auto_add_new_nodes = auto_add_new_nodes
        # A client token to ensure the idempotence of the request. The client generates the value, but you must make sure that the value is unique among different requests. The token is case-sensitive and can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The ID of the cluster endpoint.
        # 
        # This parameter is required.
        self.dbendpoint_id = dbendpoint_id
        # The advanced configurations of the cluster endpoint, which are specified in the JSON format. You can set the consistency level, transaction splitting, whether the primary node accepts read requests, the connection pool, and more.
        # 
        # - To set the load balancing policy, use the format `{\\"LoadBalancePolicy\\":\\"policy\\"}`. Valid values:
        # 
        #   - **0**: connection-based load balancing (default)
        # 
        #   - **1**: active request-based load balancing
        # 
        # - To specify whether the primary node accepts read requests, use the format `{\\"MasterAcceptReads\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: The primary node accepts read requests (default).
        # 
        #   - **off**: The primary node does not accept read requests.
        # 
        # - To configure transaction splitting, use the format `{\\"DistributedTransaction\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: enables transaction splitting (default)
        # 
        #   - **off**: disables transaction splitting
        # 
        # - To set the consistency level, use the format `{\\"ConsistLevel\\":\\"level\\"}`. Valid values:
        # 
        #   - **0**: eventual consistency (weak)
        # 
        #   - **1**: session consistency (medium) (default)
        # 
        #   - **2**: global consistency (strong)
        # 
        # - To set the timeout period for a global consistency read, use the format `{\\"ConsistTimeout\\":\\"timeout\\"}`. Valid values: 0 to 60000. Default value: 20. Unit: ms.
        # 
        # - To set the timeout period for a session consistency read, use the format `{\\"ConsistSessionTimeout\\":\\"timeout\\"}`. Valid values: 0 to 60000. Default value: 0. Unit: ms.
        # 
        # - To set the policy for a global or session consistency read timeout, use the format `{\\"ConsistTimeoutAction\\":\\"policy\\"}`. Valid values:
        # 
        #   - **0**: Sends the read request to the primary node (default).
        # 
        #   - **1**: The proxy returns a \\`wait replication complete timeout, please retry\\` error message to the application.
        # 
        # - To configure the connection pool, use the format `{\\"ConnectionPersist\\":\\"pool_type\\"}`. Valid values:
        # 
        #   - **off**: disables the connection pool (default)
        # 
        #   - **Session**: enables the session-level connection pool
        # 
        #   - **Transaction**: enables transaction-level connection pooling
        # 
        # - To configure parallel queries, use the format `{\\"MaxParallelDegree\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: enables parallel queries
        # 
        #   - **off**: disables parallel queries (default)
        # 
        # - To configure automatic routing between row store and column store, use the format `{\\"EnableHtapImci\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: enables automatic routing between row store and column store
        # 
        #   - **off**: disables automatic routing between row store and column store (default)
        # 
        # - To specify whether to enable overload protection, use the format `{\\"EnableOverloadThrottle\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: enables overload protection
        # 
        #   - **off**: disables overload protection (default)
        # 
        # > * You can configure transaction splitting, specify whether the primary node accepts read requests, configure the connection pool, and enable overload protection only when the read/write mode of the cluster endpoint for PolarDB for MySQL is set to **ReadWrite** (automatic read/write splitting).
        # >
        # > * If the read/write mode of a cluster endpoint for PolarDB for MySQL is **ReadOnly**, both connection-based and active request-based load balancing policies are supported. If the read/write mode is **ReadWrite** (automatic read/write splitting), only the active request-based load balancing policy is supported.
        # >
        # > * You can configure automatic routing between row store and column store when the read/write mode of the cluster endpoint for PolarDB for MySQL is **ReadWrite** (automatic read/write splitting), or when the read/write mode is **ReadOnly** and the load balancing policy is active request-based.
        # >
        # > * Only PolarDB for MySQL supports the global consistency level.
        # >
        # > * If you set **ReadWriteMode** to **ReadOnly**, you can set the consistency level only to **0**.
        # >
        # > * You can set the consistency level, transaction splitting, whether the primary node accepts read requests, and the connection pool at the same time. For example: `{\\"ConsistLevel\\":\\"1\\",\\"DistributedTransaction\\":\\"on\\",\\"ConnectionPersist\\":\\"Session\\",\\"MasterAcceptReads\\":\\"on\\"}`.
        # >
        # > * The transaction splitting setting is constrained by the consistency level. For example, if the consistency level is **0**, you cannot enable transaction splitting. If the consistency level is **1** or **2**, you can enable transaction splitting.
        self.endpoint_config = endpoint_config
        # The read-only nodes to add to the endpoint. Separate multiple node IDs with commas (,). If you do not specify this parameter, the original nodes are retained.
        # 
        # > - For PolarDB for MySQL, specify the node IDs.
        # >
        # > - For PolarDB for PostgreSQL and PolarDB for PostgreSQL (compatible with Oracle), specify the node role names, such as `Writer,Reader1,Reader2`.
        # >
        # > - If you set **ReadWriteMode** to **ReadOnly**, you can attach only one node. However, if this node fails, the endpoint might be unavailable for up to one hour. Do not use this configuration in a production environment. Select at least two nodes to improve availability.
        # >
        # > - If you set **ReadWriteMode** to **ReadWrite**, you must select at least two nodes.
        # >   \\* For PolarDB for MySQL, you can select any two nodes. If both nodes are read-only nodes, write requests are sent to the primary node.
        # >   \\* For PolarDB for PostgreSQL and PolarDB for PostgreSQL (compatible with Oracle), you must include the primary node.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy for a global consistency timeout. Valid values:
        # 
        # - **0**: Sends the request to the primary node.
        # 
        # - **2**: Timeout degradation. If a global consistency read times out, the query is automatically downgraded to a regular request, and the client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - **ReadWrite**: read-write (automatic read/write splitting)
        # 
        # - **ReadOnly**: read-only
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values:
        # 
        # - **ON**: enables the feature
        # 
        # - **OFF**: disables the feature
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

