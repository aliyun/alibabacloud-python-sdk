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
        # Specifies whether to automatically add new nodes to the endpoint. Valid values:
        # 
        # - Enable: New nodes are automatically added to the endpoint.
        # - Disable: New nodes are not automatically added to the endpoint. This is the default value.
        self.auto_add_new_nodes = auto_add_new_nodes
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value of this parameter on the client side. The value must be unique across different requests and is case-sensitive. The value can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The ID of the PolarDB on ENS cluster. You can call the DescribeDBClustersZonal operation to obtain the ID. Standard PolarDB cluster IDs are not supported. Usage notes: This operation applies only to PolarDB on ENS clusters. It outlines the concepts of edge clouds, activation methods, and how to obtain the edge cluster ID, noting that the CreateDBClusterZonal operation is unavailable and clusters must be created through alternative methods.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the custom cluster endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The advanced configurations of the cluster endpoint. The value is a JSON string. Currently, settings for the consistency level, transaction splitting, offload reads from primary node, and connection pool are supported.
        # * Configure the load balancing policy. Format: {"LoadBalancePolicy":"load balancing policy"}. Valid values:
        #    * **0**: load balancing based on the number of connections. This is the default value.
        #    * **1**: load balancing based on the number of active requests.
        # * Configure the consistency level. Format: `{"ConsistLevel":"consistency level"}`. Valid values:
        #     * **0**: eventual consistency.
        #     * **1**: session consistency. This is the default value.
        #     * **2**: global consistency.
        # * Configure transaction splitting. Format: `{"DistributedTransaction":"transaction splitting"}`. Valid values:
        #     * **on**: enables transaction splitting. This is the default value.
        #     * **off**: disables transaction splitting.
        # * Configure whether the primary node accepts read requests. Format: `{"MasterAcceptReads":"offload reads from primary node"}`. Valid values:
        #     * **on**: The primary node accepts read requests.
        #     * **off**: The primary node does not accept read requests. This is the default value.
        # * Configure the connection pool. Format: `{"ConnectionPersist":"connection pool"}`. Valid values:
        #     * **off**: disables the connection pool. This is the default value.
        #     * **Session**: enables the session-level connection pool.
        #     * **Transaction**: enables the transaction-level connection pool.
        # * Configure parallel query. Format: {"MaxParallelDegree":"parallel query"}. Valid values:
        #     * A specific number of concurrent queries. Example: "MaxParallelDegree":"2".
        #     * **off**: disables parallel query. This is the default value.
        # * Configure automatic request distribution among row store and column store nodes. Format: {"EnableHtapImci":"automatic request distribution among row store and column store nodes"}. Valid values:
        #     * **on**: enables automatic request distribution among row store and column store nodes.
        #     * **off**: disables automatic request distribution among row store and column store nodes. This is the default value.
        # * Configure whether to enable overload protection. Format: {"EnableOverloadThrottle":"overload protection"}. Valid values:
        #    * **on**: enables overload protection.
        #    * **off**: disables overload protection. This is the default value.
        # 
        # > * Transaction splitting, whether the primary node accepts read requests, the connection pool, and overload protection can be configured only when the read/write mode of the PolarDB for MySQL cluster endpoint is set to **read and write (automatic read/write splitting)**.
        # >* When the read/write mode of the PolarDB for MySQL cluster endpoint is set to **read-only**, both **load balancing based on the number of connections** and **load balancing based on the number of active requests** are supported. Cluster endpoints in the **read and write (automatic read/write splitting) mode** only support the **load balancing based on the number of active requests** policy.
        # >* Automatic request distribution among row store and column store nodes can be configured when the read/write mode of the PolarDB for MySQL cluster endpoint is set to **read and write (automatic read/write splitting)**, or when the read/write mode is set to **read-only** and the load balancing policy is set to **load balancing based on the number of active requests**.
        # >* Only PolarDB for MySQL supports setting the consistency level to global consistency.
        # >* If the ReadWriteMode parameter is set to **ReadOnly**, the consistency level can only be set to **0**.
        # >* You can configure the consistency level, transaction splitting, whether the primary node accepts read requests, and the connection pool at the same time. Example: `{"ConsistLevel":"1","DistributedTransaction":"on","ConnectionPersist":"Session","MasterAcceptReads":"on"}`.
        # >* The configuration of transaction splitting is constrained by the consistency level. For example, if the consistency level is set to **0**, transaction splitting cannot be enabled. If the consistency level is set to **1** or **2**, transaction splitting can be enabled.
        self.endpoint_config = endpoint_config
        # The type of the custom cluster endpoint. Set the value to **Custom**.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The read-only nodes to add to the endpoint. Separate multiple node IDs with commas (,). By default, all nodes are added.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The timeout policy for global consistency. Valid values:
        # 
        # - 0: sends the request to the primary node.
        # 
        # - 2: degrades the request upon timeout. If a global consistency read times out, the query is automatically downgraded to regular requests, and the client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - ReadWrite: read and write (automatic read/write splitting).
        # - ReadOnly: read-only. This is the default value.
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values:
        # 
        # - ON: enables the feature.
        # 
        # - OFF: disables the feature.
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

