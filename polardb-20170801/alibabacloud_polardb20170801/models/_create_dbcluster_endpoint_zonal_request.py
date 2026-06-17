# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBClusterEndpointZonalRequest(DaraModel):
    def __init__(
        self,
        auto_add_new_nodes: str = None,
        client_token: str = None,
        dbcluster_id: str = None,
        dbendpoint_description: str = None,
        endpoint_config: str = None,
        endpoint_type: str = None,
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
        # - Enable: New nodes are automatically added to this endpoint.
        # 
        # - Disable: New nodes are not automatically added to this endpoint. This is the default value.
        self.auto_add_new_nodes = auto_add_new_nodes
        # A client token that is used to ensure the idempotence of the request. The client generates the value, which must be unique among different requests. The token is case-sensitive and can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the custom cluster endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The advanced configurations of the cluster endpoint, specified in the JSON format. This parameter supports settings for consistency level, transaction splitting, offloading reads from the primary node, and the connection pool.
        # 
        # - Sets the load balancing policy. The format is {"LoadBalancePolicy":"policy"}. Valid values:
        # 
        #   - **0**: Connections-based load balancing. This is the default value.
        # 
        #   - **1**: Active requests-based load balancing.
        # 
        # - Sets the consistency level. The format is `{"ConsistLevel":"level"}`. Valid values:
        # 
        #   - **0**: Eventual consistency.
        # 
        #   - **1**: Session consistency. This is the default value.
        # 
        #   - **2**: Global consistency.
        # 
        # - Sets transaction splitting. The format is `{"DistributedTransaction":"on/off"}`. Valid values:
        # 
        #   - **on**: Enables transaction splitting. This is the default value.
        # 
        #   - **off**: Disables transaction splitting.
        # 
        # - Specifies whether the primary node accepts read requests. The format is `{"MasterAcceptReads":"on/off"}`. Valid values:
        # 
        #   - **on**: The primary node accepts read requests.
        # 
        #   - **off**: The primary node does not accept read requests. This is the default value.
        # 
        # - Sets the connection pool. The format is `{"ConnectionPersist":"type"}`. Valid values:
        # 
        #   - **off**: Disables the connection pool. This is the default value.
        # 
        #   - **Session**: Enables the session-level connection pool.
        # 
        #   - **Transaction**: Enables transaction-level connection pooling.
        # 
        # - Sets parallel query. The format is {"MaxParallelDegree":"degree"}. Valid values:
        # 
        #   - A specific number of concurrent queries. Example: "MaxParallelDegree":"2".
        # 
        #   - **off**: Disables parallel query. This is the default value.
        # 
        # - Sets automatic routing for row store and column store. The format is {"EnableHtapImci":"on/off"}. Valid values:
        # 
        #   - **on**: Enables automatic routing for row store and column store.
        # 
        #   - **off**: Disables automatic routing for row store and column store. This is the default value.
        # 
        # - Specifies whether to enable overload protection. The format is {"EnableOverloadThrottle":"on/off"}. Valid values:
        # 
        #   - **on**: Enables overload protection.
        # 
        #   - **off**: Disables overload protection. This is the default value.
        # 
        # > * You can set transaction splitting, specify whether the primary node accepts read requests, configure the connection pool, and enable overload protection only when the read/write mode of the cluster endpoint for a PolarDB for MySQL cluster is set to \\*\\*ReadWrite\\*\\* (automatic read/write splitting).
        # >
        # > * When the read/write mode of the cluster endpoint for a PolarDB for MySQL cluster is set to **ReadOnly**, both **connections-based load balancing** and **active requests-based load balancing** are supported. When the read/write mode is set to **ReadWrite** (automatic read/write splitting), only **active requests-based load balancing** is supported.
        # >
        # > * You can enable automatic routing for row store and column store when the read/write mode of the cluster endpoint for a PolarDB for MySQL cluster is set to **ReadWrite** (automatic read/write splitting), or when the read/write mode is set to **ReadOnly** and the load balancing policy is set to **active requests-based load balancing**.
        # >
        # > * Only PolarDB for MySQL supports setting the consistency level to global consistency.
        # >
        # > * If you set the **ReadWriteMode** parameter to **ReadOnly**, you can only set the consistency level to **0**.
        # >
        # > * You can configure the consistency level, transaction splitting, whether the primary node accepts reads, and the connection pool at the same time. For example: `{"ConsistLevel":"1","DistributedTransaction":"on","ConnectionPersist":"Session","MasterAcceptReads":"on"}`.
        # >
        # > * The transaction splitting setting is constrained by the consistency level. For example, if the consistency level is set to **0**, you cannot enable transaction splitting. If the consistency level is set to **1** or **2**, you can enable transaction splitting.
        self.endpoint_config = endpoint_config
        # The type of the custom cluster endpoint. The value is fixed to **Custom**.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The read-only nodes to be added to the endpoint. Separate multiple node IDs with commas (,). By default, all nodes are added.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy for handling global consistency timeouts. Valid values:
        # 
        # - 0: Sends the request to the primary node.
        # 
        # - 2: Degrades to regular requests. If a global consistency read times out, the query is automatically degraded to a regular request, and the client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - ReadWrite: read and write (automatic read/write splitting).
        # 
        # - ReadOnly: read-only. This is the default value.
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values:
        # 
        # - ON: Enables the feature.
        # 
        # - OFF: Disables the feature.
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

        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

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

        if m.get('EndpointConfig') is not None:
            self.endpoint_config = m.get('EndpointConfig')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

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

