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
        # Specifies whether to automatically add new nodes to the endpoint. Valid values:
        # 
        # - **Enable**: Automatically adds new nodes.
        # 
        # - **Disable**: Does not automatically add new nodes. This is the default value.
        self.auto_add_new_nodes = auto_add_new_nodes
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
        # The advanced configurations of the cluster endpoint in JSON format. You can set the consistency level, transaction splitting, whether the primary node accepts read requests, the connection pool, and other settings.
        # 
        # - Sets the load balancing policy. Format: `{\\"LoadBalancePolicy\\":\\"policy\\"}`. Valid values:
        # 
        #   - **0**: Connections-based load balancing (default)
        # 
        #   - **1**: Active requests-based load balancing
        # 
        # - Specifies whether the primary node accepts read requests. Format: `{\\"MasterAcceptReads\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: The primary node accepts read requests (default).
        # 
        #   - **off**: The primary node does not accept read requests.
        # 
        # - Enables or disables transaction splitting. Format: `{\\"DistributedTransaction\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: Enables transaction splitting (default).
        # 
        #   - **off**: Disables transaction splitting.
        # 
        # - Sets the consistency level. Format: `{\\"ConsistLevel\\":\\"level\\"}`. Valid values:
        # 
        #   - **0**: Eventual consistency (weak)
        # 
        #   - **1**: Session consistency (medium) (default)
        # 
        #   - **2**: Global consistency (strong)
        # 
        # - Sets the timeout period for a global consistency read. Format: `{\\"ConsistTimeout\\":\\"timeout\\"}`. Valid values: 0 to 60000. Default value: 20. Unit: ms.
        # 
        # - Sets the timeout period for a session consistency read. Format: `{\\"ConsistSessionTimeout\\":\\"timeout\\"}`. Valid values: 0 to 60000. Default value: 0. Unit: ms.
        # 
        # - Sets the policy for handling timeouts of global or session consistency reads. Format: `{\\"ConsistTimeoutAction\\":\\"policy\\"}`. Valid values:
        # 
        #   - **0**: Forwards read requests to the primary node (default).
        # 
        #   - **1**: The proxy returns the error message \\`wait replication complete timeout, please retry\\` to the application.
        # 
        # - Sets the connection pool type. Format: `{\\"ConnectionPersist\\":\\"type\\"}`. Valid values:
        # 
        #   - **off**: Disables the connection pool (default).
        # 
        #   - **Session**: Enables the session-level connection pool.
        # 
        #   - **Transaction**: Enables the transaction-level connection pool.
        # 
        # - Enables or disables parallel query. Format: `{\\"MaxParallelDegree\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: Enables parallel query.
        # 
        #   - **off**: Disables parallel query (default).
        # 
        # - Enables or disables automatic routing of requests to the row store or column store. Format: `{\\"EnableHtapImci\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: Enables automatic routing.
        # 
        #   - **off**: Disables automatic routing (default).
        # 
        # - Enables or disables overload protection. Format: `{\\"EnableOverloadThrottle\\":\\"value\\"}`. Valid values:
        # 
        #   - **on**: Enables overload protection.
        # 
        #   - **off**: Disables overload protection (default).
        # 
        # > * You can set transaction splitting, whether the primary node accepts read requests, the connection pool, and overload protection only when the read/write mode of the cluster endpoint for PolarDB for MySQL is set to ReadWrite (automatic read/write splitting).
        # >
        # > * If the read/write mode of a cluster endpoint for PolarDB for MySQL is **ReadOnly**, both **connections-based** and **active requests-based** load balancing policies are supported. If the read/write mode is **ReadWrite** (automatic read/write splitting), only the **active requests-based** load balancing policy is supported.
        # >
        # > * You can enable automatic routing to the row store or column store if the read/write mode of the cluster endpoint for PolarDB for MySQL is **ReadWrite** (automatic read/write splitting), or if the read/write mode is **ReadOnly** and the load balancing policy is **active requests-based**.
        # >
        # > * Only PolarDB for MySQL supports global consistency.
        # >
        # > * If you set the **ReadWriteMode** parameter to **ReadOnly**, you can only set the consistency level to **0**.
        # >
        # > * You can set the consistency level, transaction splitting, whether the primary node accepts read requests, and the connection pool at the same time. For example: `{\\"ConsistLevel\\":\\"1\\",\\"DistributedTransaction\\":\\"on\\",\\"ConnectionPersist\\":\\"Session\\",\\"MasterAcceptReads\\":\\"on\\"}`.
        # >
        # > * The transaction splitting setting is constrained by the consistency level. For example, you cannot enable transaction splitting if the consistency level is **0** (eventual consistency). You can enable transaction splitting if the consistency level is **1** (session consistency) or **2** (global consistency).
        self.endpoint_config = endpoint_config
        # The nodes to be added to the endpoint for read request distribution. Separate multiple node IDs with commas (,). The original nodes are used by default.
        # 
        # > - For PolarDB for MySQL, specify the node IDs.
        # >
        # > - For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Oracle Compatible), specify the node roles, such as `Writer,Reader1,Reader2`.
        # >
        # > - If you set **ReadWriteMode** to **ReadOnly**, you can attach only one node. However, if this node fails, the endpoint may be unavailable for up to one hour. Do not use this configuration in a production environment. Select at least two nodes to improve availability.
        # >
        # > - If you set **ReadWriteMode** to **ReadWrite**, you must select at least two nodes.
        # >   \\* For PolarDB for MySQL, you can select any two nodes. If both nodes are read-only nodes, write requests are sent to the primary node.
        # >   \\* For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Oracle Compatible), you must include the primary node.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy for handling global consistency timeouts. Valid values:
        # 
        # - **0**: Forwards the request to the primary node.
        # 
        # - **2**: Degrades the request. If a global consistency read times out, the query is automatically degraded to a regular request. The client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - **ReadWrite**: Read/write (automatic read/write splitting)
        # 
        # - **ReadOnly**: Read-only
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values:
        # 
        # - **ON**: Enable
        # 
        # - **OFF**: Disable
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

