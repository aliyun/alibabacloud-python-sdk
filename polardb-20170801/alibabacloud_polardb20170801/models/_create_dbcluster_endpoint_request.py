# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBClusterEndpointRequest(DaraModel):
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
        polar_fs_instance_id: str = None,
        polar_scc_timeout_action: str = None,
        polar_scc_wait_timeout: str = None,
        read_write_mode: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scc_mode: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to automatically add new nodes to the endpoint. Valid values:
        # 
        # - **Enable**: Automatically adds new nodes to the endpoint.
        # 
        # - **Disable** (default): Does not automatically add new nodes to the endpoint.
        self.auto_add_new_nodes = auto_add_new_nodes
        # A client-generated token to ensure the idempotence of the request. The token must be unique, case-sensitive, and a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the custom cluster endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The advanced configurations for the custom cluster endpoint, specified as a JSON string. You can configure features such as consistency level, transaction splitting, whether the primary node accepts read requests, connection pool, and load balancing policy.
        # 
        # - Specifies the load balancing policy. The format is {"LoadBalancePolicy":"policy"}. Valid values:
        # 
        #   - **0**: connections-based load balancing (default).
        # 
        #   - **1**: active requests-based load balancing.
        # 
        # - Specifies the consistency level. The format is `{"ConsistLevel":"level"}`. Valid values:
        # 
        #   - **0**: eventual consistency.
        # 
        #   - **1**: session consistency (default).
        # 
        #   - **2**: global consistency.
        # 
        # - Specifies whether to enable transaction splitting. The format is `{"DistributedTransaction":"status"}`. Valid values:
        # 
        #   - **on**: enables transaction splitting (default).
        # 
        #   - **off**: disables transaction splitting.
        # 
        # - Specifies whether the primary node accepts read requests. The format is `{"MasterAcceptReads":"status"}`. Valid values:
        # 
        #   - **on**: The primary node accepts read requests.
        # 
        #   - **off**: The primary node does not accept read requests (default).
        # 
        # - Specifies whether to enable the connection pool. The format is `{"ConnectionPersist":"status"}`. Valid values:
        # 
        #   - **off**: disables the connection pool (default).
        # 
        #   - **Session**: enables the session-level connection pool.
        # 
        #   - **Transaction**: enables the transaction-level connection pool.
        # 
        # - Specifies the degree of parallelism for a parallel query. The format is {"MaxParallelDegree":"degree"}. Valid values:
        # 
        #   - A specific integer that specifies the degree of parallelism. For example: "MaxParallelDegree":"2".
        # 
        #   - **off**: disables parallel query (default).
        # 
        # - Specifies whether to enable automatic routing between row store and column store. The format is {"EnableHtapImci":"status"}. Valid values:
        # 
        #   - **on**: enables automatic routing.
        # 
        #   - **off**: disables automatic routing (default).
        # 
        # - Specifies whether to enable overload protection. The format is {"EnableOverloadThrottle":"status"}. Valid values:
        # 
        #   - **on**: enables overload protection.
        # 
        #   - **off**: disables overload protection (default).
        # 
        # > * You can configure transaction splitting, whether the primary node accepts read requests, the connection pool, and overload protection only for a PolarDB for MySQL endpoint in **ReadWrite** (automatic read/write splitting) mode.
        # >
        # > * A PolarDB for MySQL cluster endpoint in **ReadOnly** mode supports both **connections-based load balancing** and **active requests-based load balancing**. An endpoint in **ReadWrite** (automatic read/write splitting) mode supports only **active requests-based load balancing**.
        # >
        # > * You can enable automatic routing between row store and column store if the read/write mode of the cluster endpoint for PolarDB for MySQL is **ReadWrite** (automatic read/write splitting), or if the read/write mode is **ReadOnly** and the load balancing policy is **active requests-based load balancing**.
        # >
        # > * Only PolarDB for MySQL clusters support global consistency.
        # >
        # > * If you set **ReadWriteMode** to **ReadOnly**, the consistency level must be **0** (eventual consistency).
        # >
        # > * You can configure the consistency level, transaction splitting, whether the primary node accepts read requests, and the connection pool at the same time. Example: `{"ConsistLevel":"1","DistributedTransaction":"on","ConnectionPersist":"Session","MasterAcceptReads":"on"}`.
        # >
        # > * The setting for transaction splitting depends on the consistency level. For example, if you set the consistency level to **0** (eventual consistency), you cannot enable transaction splitting. If you set the consistency level to **1** (session consistency) or **2** (global consistency), you can enable transaction splitting.
        self.endpoint_config = endpoint_config
        # The type of the custom cluster endpoint. Set the value to **Custom**.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The nodes to associate with the endpoint. Separate multiple node IDs with a comma (,). If you omit this parameter, all nodes in the cluster are added by default.
        # 
        # > - For a PolarDB for MySQL cluster, specify the node IDs.
        # >
        # > - For a PolarDB for PostgreSQL cluster or a PolarDB for PostgreSQL (compatible with Oracle) cluster, specify the roles of the nodes, such as `Writer,Reader1,Reader2`.
        # >
        # > - If you set **ReadWriteMode** to **ReadOnly**, you can associate only one node with the endpoint. If this node fails, the endpoint may be unavailable for up to 1 hour. This configuration is not recommended for a production environment. To improve availability, associate at least two nodes with the endpoint.
        # >
        # > - If you set **ReadWriteMode** to **ReadWrite**, you must associate at least two nodes with the endpoint.
        # >   \\* For a PolarDB for MySQL cluster, you can select any two nodes. If both nodes are read-only nodes, write requests are routed to the primary node.
        # >   \\* For a PolarDB for PostgreSQL cluster or a PolarDB for PostgreSQL (compatible with Oracle) cluster, the primary node must be included.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.polar_fs_instance_id = polar_fs_instance_id
        # The policy for handling global consistency read timeouts. Valid values:
        # 
        # - **0**: Send the request to the primary node.
        # 
        # - **2**: Downgrade to a regular request. If a global consistency read times out, the query is automatically downgraded, and the client does not receive an error.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - **ReadWrite**: read/write (automatic read/write splitting).
        # 
        # - **ReadOnly** (default): read-only.
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable global consistency (high-performance mode). Valid values:
        # 
        # - **ON**: Enables the feature.
        # 
        # - **OFF**: Disables the feature.
        self.scc_mode = scc_mode
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

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

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

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

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

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

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

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

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

