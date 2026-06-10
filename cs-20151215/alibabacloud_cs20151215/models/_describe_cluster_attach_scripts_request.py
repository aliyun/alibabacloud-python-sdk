# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeClusterAttachScriptsRequest(DaraModel):
    def __init__(
        self,
        arch: str = None,
        expired: int = None,
        format_disk: bool = None,
        keep_instance_name: bool = None,
        nodepool_id: str = None,
        one_time_token: bool = None,
        options: str = None,
        rds_instances: List[str] = None,
    ):
        # The CPU architecture of the node. Supported CPU architectures include `amd64`, `arm`, and `arm64`.
        # 
        # Default value: `amd64`.
        # 
        # > This parameter is required if the cluster is a managed edge cluster.
        self.arch = arch
        # The Unix timestamp that indicates when the generated token expires. For example, the timestamp 1739980800 corresponds to 00:00:00 on February 20, 2025 (UTC).
        self.expired = expired
        # Specifies whether to mount a data disk to the instance and store containers and images on the data disk when you manually add an existing instance to the cluster. Valid values:
        # 
        # - `true`: Mounts the data disk to the instance. The original data on the data disk will be erased. Back up your data before you proceed.
        # 
        # - `false`: Does not mount the data disk to the instance.
        # 
        # Default value: `false`.
        # 
        # Data disk mounting rules:
        # 
        # - If an ECS instance has data disks attached and the last data disk is uninitialized, the system automatically formats that disk to ext4 and uses it to store content for `/var/lib/docker` and `/var/lib/kubelet`.
        # 
        # - If no data disk is attached to the ECS instance, the system does not mount a new data disk.
        self.format_disk = format_disk
        # Specifies whether to retain the instance name when the instance is added to the cluster. If you do not retain the instance name, the system renames the instance to use the `worker-k8s-for-cs-<clusterid>` format. Valid values:
        # 
        # - `true`: Retains the instance name.
        # 
        # - `false`: Does not retain the instance name. The system renames the instance based on a system rule.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The node pool ID. You can add the node to a specific node pool.
        # 
        # > If you do not specify a node pool ID, the node is added to the default node pool.
        self.nodepool_id = nodepool_id
        self.one_time_token = one_time_token
        # The configuration parameters for node attachment.
        # 
        # > This parameter is required if the cluster is a managed edge cluster.
        self.options = options
        # If you specify a list of RDS instances, the system automatically adds the ECS instances of the cluster nodes to the access whitelists of the specified RDS instances.
        self.rds_instances = rds_instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arch is not None:
            result['arch'] = self.arch

        if self.expired is not None:
            result['expired'] = self.expired

        if self.format_disk is not None:
            result['format_disk'] = self.format_disk

        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.one_time_token is not None:
            result['one_time_token'] = self.one_time_token

        if self.options is not None:
            result['options'] = self.options

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arch') is not None:
            self.arch = m.get('arch')

        if m.get('expired') is not None:
            self.expired = m.get('expired')

        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')

        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('one_time_token') is not None:
            self.one_time_token = m.get('one_time_token')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        return self

