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
        # >  This parameter is required if you want to add a node to an ACK Edge cluster.
        self.arch = arch
        # The expiration time of the token that is generated. The value is a UNIX timestamp. For example, a value of 1739980800 indicates 00:00:00 (UTC+8) on February 20, 2025.
        self.expired = expired
        # Specifies whether to mount data disks to an existing instance when you manually add this instance to the cluster. You can use data disks to store container data and images. Valid values:
        # 
        # *   `true`: mounts data disks to the instance that you want to add. After a data disk is mounted, the original data on the disk is erased. Back up data before you mount a data disk.
        # *   `false`: does not mount data disks to the instance.
        # 
        # Default value: `false`.
        # 
        # How a data disk is mounted:
        # 
        # *   If the Elastic Compute Service (ECS) instances are already mounted with data disks and the file system of the last data disk is uninitialized, the system automatically formats this data disk to ext4 and uses the disk to store the data in the /var/lib/docker and /var/lib/kubelet directories.
        # *   If no data disk is mounted to the ECS instance, the system does not purchase a new data disk.
        self.format_disk = format_disk
        # Specifies whether to retain the name of an existing instance when it is added to the cluster. If you do not retain the instance name, the instance is renamed in the `worker-k8s-for-cs-<clusterid>` format. Valid values:
        # 
        # *   `true`: retains the instance name.
        # *   `false`: does not retain the instance name.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The ID of the node pool to which you want to add an existing node.
        # 
        # >  If you do not specify a node pool ID, the node is added to the default node pool.
        self.nodepool_id = nodepool_id
        self.one_time_token = one_time_token
        # The node configurations for the node that you want to add.
        # 
        # >  This parameter is required if you want to add a node to an ACK Edge cluster.
        self.options = options
        # A list of ApsaraDB RDS instances. ECS instances in the cluster are automatically added to the whitelist of the ApsaraDB RDS instances.
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

