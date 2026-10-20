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
        # The CPU architecture of the node. Valid values: `amd64`, `arm`, and `arm64`.
        # 
        # Default value: `amd64`.
        # 
        # > This parameter is required when the cluster type is managed edge.
        self.arch = arch
        # The expiration time of the generated token, in UNIX timestamp format. For example, 1739980800 indicates 2025-02-20 00:00:00.
        self.expired = expired
        # Specifies whether to mount data cloud disks to the instance when manually adding existing instances to the cluster, storing containers and images on the data cloud disks. Valid values:
        # 
        # - `true`: Mounts data cloud disks to the instance. Existing data on the data cloud disks will be lost. Back up your data in advance.
        # - `false`: Does not mount data cloud disks to the instance.
        # 
        # Default value: `false`.
        # 
        # Data mounting rules:
        # 
        # - If the ECS instance already has data cloud disks mounted and the file system of the last data cloud disk is not initialized, the system automatically formats the data cloud disk as ext4 to store the content of /var/lib/docker and /var/lib/kubelet.
        # - If the ECS instance does not have data cloud disks mounted, no new data cloud disks are mounted.
        self.format_disk = format_disk
        # Specifies whether to retain the instance name when adding existing instances to the cluster. If the instance name is not retained, the instance name format is `worker-k8s-for-cs-<clusterid>`. Valid values:
        # 
        # - `true`: Retains the instance name.
        # - `false`: Does not retain the instance name. The name is replaced based on system rules.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The node pool ID. When adding a node, you can add the node to the specified node pool.
        # 
        # > If you do not specify a node pool ID, the node is added to the default node pool.
        self.nodepool_id = nodepool_id
        self.one_time_token = one_time_token
        # The access configuration parameters of the node.
        # 
        # > This parameter is required when the cluster type is managed edge.
        self.options = options
        # If you specify a list of RDS instances, the ECS nodes in the cluster are automatically added to the RDS whitelist.
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

