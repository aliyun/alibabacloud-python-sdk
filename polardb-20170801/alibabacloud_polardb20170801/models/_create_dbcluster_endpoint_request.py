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
    ):
        # Specifies whether to enable automatic association of newly added nodes with the cluster endpoint. Valid values:
        # 
        # *   **Enable**
        # *   **Disable** (default)
        self.auto_add_new_nodes = auto_add_new_nodes
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. The token is case-sensitive.
        self.client_token = client_token
        # The ID of cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the custom cluster endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The advanced configurations of the cluster endpoint. You must specify the configurations in the JSON format. You can specify the configurations of the following attributes: consistency level, transaction splitting, connection pool, and offload reads from the primary node.
        # 
        # *   Specify the consistency level in the format of `{"ConsistLevel":"Consistency level"}`. Default value: 1. Valid values:
        # 
        #     *   **0**: eventual consistency.
        #     *   **1**: session consistency.
        #     *   **2**: global consistency.
        # 
        # *   Specify the transaction splitting feature in the format of `{"DistributedTransaction":"Transaction splitting"}`. Valid values:
        # 
        #     *   **on**: enables the transaction splitting feature. By default, the feature is enabled.
        #     *   **off**: disables the transaction splitting feature.
        # 
        # *   Specify the offload reads from the primary node feature in the format of `{"MasterAcceptReads":"Offload reads from the primary node"}`. Default value: off. Valid values:
        # 
        #     *   **on**: The primary node accepts read requests.
        #     *   **off**: The primary node does not accept read requests.
        # 
        # *   Specify the connection pool in the format of `{"ConnectionPersist":"Connection pool"}`. Default value: off. Valid values:
        # 
        #     *   **off**: disables the connection pool.
        #     *   **Session**: enables the session-level connection pool.
        #     *   **Transaction**: enables the transaction-level connection pool.
        # 
        # >- You can specify the transaction splitting, connection pool, and offload reads from the primary node features for a PolarDB for MySQL cluster only if ReadWriteMode is set to ReadWrite for the cluster endpoint.
        # >- Only PolarDB for MySQL supports global consistency.
        # >- If the **ReadWriteMode** parameter is set to **ReadOnly**, the consistency level must be **0**.
        # >- You can use one record to specify the consistency level, transaction splitting, connection pool, and offload reads from the primary node features, such as `{"ConsistLevel":"1","DistributedTransaction":"on","ConnectionPersist":"Session","MasterAcceptReads":"on"}`.
        # >- The transaction splitting settings are restricted by the consistency level settings. For example, if you set the consistency level to **0**, transaction splitting cannot be enabled. If you set the consistency level to **1** or **2**, transaction splitting can be enabled.
        self.endpoint_config = endpoint_config
        # The type of the cluster endpoint. Set the value to **Custom**.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The reader nodes that you want to associate with the endpoint. If you want to specify multiple reader nodes, separate the reader nodes with commas (,). If you do not specify this parameter, all nodes are used.
        # 
        # >- You need to specify the node IDs for a PolarDB for MySQL cluster.
        # >- You need to specify the role name of each node for a PolarDB for PostgreSQL cluster or a PolarDB for PostgreSQL (Compatible with Oracle) cluster. Example: `Writer, Reader1, Reader2`.
        # >- If you set **ReadWriteMode** to **ReadOnly**, you can associate only one node with the endpoint. If the only node becomes faulty, the cluster endpoint may be unavailable for up to 1 hour. We recommend that you associate more than one node with the cluster endpoint in production environments. We recommend that you associate at least two nodes with the cluster endpoint to improve service availability.
        # >- If you set **ReadWriteMode** to **ReadWrite**, you need to associate at least two nodes with the cluster endpoint.
        # >- PolarDB for MySQL does not impose a limit on the types of the two nodes. If the nodes are read-only nodes, write requests are forwarded to the primary node. 
        # >- PolarDB for PostgreSQL and PolarDB for PostgreSQL (compatible with Oracle) require a primary node.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.polar_fs_instance_id = polar_fs_instance_id
        # Global consistency timeout strategy. The value range is as follows:
        # - **0**: Send the request to the primary node
        # - **2**: Timeout degradation, when a global consistency read times out, the query operation will automatically degrade to an inconsistent read, and the client will not receive an error message
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # Global consistency timeout
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # *   **ReadWrite**: receives and forwards read and write requests. Automatic read/write splitting is enabled.
        # *   **ReadOnly**: The account has the read-only permissions on the database.
        # 
        # Default value: **ReadOnly**.
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the nodes. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
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

        return self

