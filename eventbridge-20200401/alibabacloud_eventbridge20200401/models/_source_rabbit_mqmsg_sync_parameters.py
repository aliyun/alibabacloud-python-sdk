# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceRabbitMQMsgSyncParameters(DaraModel):
    def __init__(
        self,
        body_data_type: str = None,
        cloud_migration_task_id: str = None,
        dst_cluster_host: str = None,
        dst_cluster_type: str = None,
        endpoint: str = None,
        instance_id: str = None,
        instance_type: str = None,
        network_type: str = None,
        order_consume: str = None,
        password: str = None,
        prefetch_count: str = None,
        regex: str = None,
        security_group_id: str = None,
        src_cluster_host: str = None,
        src_cluster_type: str = None,
        sync_meta_type: str = None,
        username: str = None,
        v_switch_ids: str = None,
        virtual_host_name: str = None,
        vpc_id: str = None,
    ):
        # The data type of the message body.
        self.body_data_type = body_data_type
        # The ID of the RabbitMQ cloud migration task.
        self.cloud_migration_task_id = cloud_migration_task_id
        # The address of the destination cluster.
        self.dst_cluster_host = dst_cluster_host
        # The type of the destination RabbitMQ cluster.
        self.dst_cluster_type = dst_cluster_type
        # The endpoint of the RabbitMQ cluster.
        self.endpoint = endpoint
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id
        # The type of the source RabbitMQ instance.
        self.instance_type = instance_type
        # The network type used to connect to the source RabbitMQ instance.
        self.network_type = network_type
        # Specifies whether SAC is enabled. Do not specify this parameter.
        self.order_consume = order_consume
        # The password used to connect to the RabbitMQ cluster.
        self.password = password
        # The prefetch count.
        self.prefetch_count = prefetch_count
        # The regular expression for matching. Do not specify this parameter.
        self.regex = regex
        # The ID of the security group to which the machines of the RabbitMQ cluster belong.
        self.security_group_id = security_group_id
        # The address of the source cluster.
        self.src_cluster_host = src_cluster_host
        # The type of the source RabbitMQ cluster.
        self.src_cluster_type = src_cluster_type
        # The type of metadata to synchronize. Do not specify this parameter.
        self.sync_meta_type = sync_meta_type
        # The username used to connect to the RabbitMQ cluster.
        self.username = username
        # The IDs of the vSwitches in the VPC where the RabbitMQ cluster is deployed.
        self.v_switch_ids = v_switch_ids
        # The name of the virtual host (vhost) in the RabbitMQ cluster.
        self.virtual_host_name = virtual_host_name
        # The ID of the VPC where the RabbitMQ cluster is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_data_type is not None:
            result['BodyDataType'] = self.body_data_type

        if self.cloud_migration_task_id is not None:
            result['CloudMigrationTaskId'] = self.cloud_migration_task_id

        if self.dst_cluster_host is not None:
            result['DstClusterHost'] = self.dst_cluster_host

        if self.dst_cluster_type is not None:
            result['DstClusterType'] = self.dst_cluster_type

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.order_consume is not None:
            result['OrderConsume'] = self.order_consume

        if self.password is not None:
            result['Password'] = self.password

        if self.prefetch_count is not None:
            result['PrefetchCount'] = self.prefetch_count

        if self.regex is not None:
            result['Regex'] = self.regex

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.src_cluster_host is not None:
            result['SrcClusterHost'] = self.src_cluster_host

        if self.src_cluster_type is not None:
            result['SrcClusterType'] = self.src_cluster_type

        if self.sync_meta_type is not None:
            result['SyncMetaType'] = self.sync_meta_type

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyDataType') is not None:
            self.body_data_type = m.get('BodyDataType')

        if m.get('CloudMigrationTaskId') is not None:
            self.cloud_migration_task_id = m.get('CloudMigrationTaskId')

        if m.get('DstClusterHost') is not None:
            self.dst_cluster_host = m.get('DstClusterHost')

        if m.get('DstClusterType') is not None:
            self.dst_cluster_type = m.get('DstClusterType')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OrderConsume') is not None:
            self.order_consume = m.get('OrderConsume')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrefetchCount') is not None:
            self.prefetch_count = m.get('PrefetchCount')

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SrcClusterHost') is not None:
            self.src_cluster_host = m.get('SrcClusterHost')

        if m.get('SrcClusterType') is not None:
            self.src_cluster_type = m.get('SrcClusterType')

        if m.get('SyncMetaType') is not None:
            self.sync_meta_type = m.get('SyncMetaType')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

