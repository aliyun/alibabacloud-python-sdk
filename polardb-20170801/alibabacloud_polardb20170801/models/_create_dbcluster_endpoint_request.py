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
        # * **Enable**: New nodes are automatically added to the endpoint.
        # * **Disable** (default): New nodes are not automatically added to the endpoint.
        self.auto_add_new_nodes = auto_add_new_nodes
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value of this parameter on the client side. The value must be unique across different requests and is case-sensitive. The value can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the custom cluster endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The advanced settings of the cluster endpoint. The value must be in JSON format. You can set the consistency level, transaction splitting, offload reads from primary node, and connection pool.
        # * Set the load balancing policy. Format: `{"LoadBalancePolicy":"load balancing policy"}`. Valid values:
        #    * **0**: load balancing based on the number of connections (default).
        #    * **1**: load balancing based on the number of active requests.
        # * Set the consistency level. Format: `{"ConsistLevel":"consistency level"}`. Valid values:
        #     * **0**: eventual consistency.
        #     * **1**: session consistency (default).
        #     * **2**: global consistency.
        # * Set transaction splitting. Format: `{"DistributedTransaction":"transaction splitting"}`. Valid values:
        #     * **on**: enables transaction splitting (default).
        #     * **off**: shutdown transaction splitting.
        # * Set whether the primary node accepts read requests. Format: `{"MasterAcceptReads":"offload reads from primary node"}`. Valid values:
        #     * **on**: The primary node accepts read requests.
        #     * **off**: The primary node does not accept read requests (default).
        # * Set the connection pool. Format: `{"ConnectionPersist":"connection pool"}`. Valid values:
        #     * **off**: shutdown the connection pool (default).
        #     * **Session**: enables the session-level connection pool.
        #     * **Transaction**: enables transaction-level connection pooling.
        # * Set parallel query. Format: `{"MaxParallelDegree":"parallel query"}`. Valid values:
        #     * A specific concurrent count. Example: `"MaxParallelDegree":"2"`.
        #     * **off**: shutdown parallel query (default).
        # * Set automatic request distribution among row store and column store nodes. Format: `{"EnableHtapImci":"automatic request distribution"}`. Valid values:
        #     * **on**: enables the automatic request distribution feature among row store and column store nodes.
        #     * **off**: shutdown the automatic request distribution feature among row store and column store nodes (default).
        # * Set whether to enable overload protection. Format: `{"EnableOverloadThrottle":"whether to enable overload protection"}`. Valid values:
        #    * **on**: enables overload protection.
        #    * **off**: shutdown overload protection (default).
        # 
        # > * Transaction splitting, offloading reads from the primary node, connection pool, and overload protection can be set only when the read/write pattern of the PolarDB for MySQL cluster endpoint is set to **read and write (automatic read/write splitting)**.
        # >* When the read/write pattern of the PolarDB for MySQL cluster endpoint is set to **read-only**, both **load balancing based on the number of connections** and **load balancing based on the number of active requests** are supported. For cluster endpoints in the **read and write (automatic read/write splitting) pattern**, only **load balancing based on the number of active requests** is supported.
        # >* Automatic request distribution among row store and column store nodes can be set when the read/write pattern of the PolarDB for MySQL cluster endpoint is set to **read and write (automatic read/write splitting)**, or when the read/write pattern is set to **read-only** and the load balancing policy is set to **load balancing based on the number of active requests**.
        # >* Only PolarDB for MySQL supports setting the consistency level to global consistency.
        # >* If the parameter **ReadWriteMode** is set to **ReadOnly**, the consistency level can only be set to **0**.
        # >* You can set the consistency level, transaction splitting, offloading reads from the primary node, and connection pool at the same time. Example: `{"ConsistLevel":"1","DistributedTransaction":"on","ConnectionPersist":"Session","MasterAcceptReads":"on"}`.
        # >* The transaction splitting settings are constrained by the consistency level settings. For example, if the consistency level is set to **0**, transaction splitting cannot be enabled. If the consistency level is set to **1** or **2**, transaction splitting can be enabled.
        # 
        # > Note: Clusters with DeployUnit=Advanced (hot standby/multi-master) may not support some advanced endpoint settings. If the OperationDenied.InstanceType error occurs, remove EndpointConfig and retry, or confirm the compatibility of the target cluster deployment type with the selected settings.
        self.endpoint_config = endpoint_config
        # The type of the custom cluster endpoint. Valid values:
        # 
        # - **Custom**: custom cluster endpoint.
        # 
        # - **DynamoDB**: DynamoDB endpoint.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The read-only nodes to be added to the endpoint. Separate multiple nodes with commas (,). Default value: all nodes. 
        # 
        # > * For PolarDB for MySQL, specify node IDs.
        # >* For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle), specify node role names, such as `Writer,Reader1,Reader2`.
        # >* If **ReadWriteMode** is set to **ReadOnly**, you can add only one node. However, if this node fails, the endpoint may be unavailable for up to 1 hour. Do not use this configuration in production environments. Select at least two nodes to improve availability.
        # >* If **ReadWriteMode** is set to **ReadWrite**, select at least two nodes.
        #     * For PolarDB for MySQL, you can select any two nodes. If both nodes are read-only nodes, write requests are forwarded to the primary node.
        #     * For PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle), the primary node must be included.
        self.nodes = nodes
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The PolarFS instance ID.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The timeout policy for global consistency. Valid values:
        # 
        # - **0**: sends the request to the primary node.
        # 
        # - **2**: degrades the request upon timeout. If a global consistency read times out, the query is automatically downgraded to regular requests, and the client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values: 
        # 
        # - **ReadWrite**: read and write (automatic read/write splitting). 
        # - **ReadOnly** (default): read-only.
        self.read_write_mode = read_write_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the global consistency (high-performance mode) feature for the node. Valid values:
        # 
        # - **ON**: Enabled.
        # 
        # - **OFF**: shutdown
        self.scc_mode = scc_mode
        # vpc-2zehr7ghqovft******
        # Virtual private cloud identifier.
        self.vpcid = vpcid
        # The vSwitch ID.
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

