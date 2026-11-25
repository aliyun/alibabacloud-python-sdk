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
        format_disk_option: str = None,
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
        # > Required when the cluster type is ACK Edge.
        self.arch = arch
        # The expiration time of the generated token. The time is in the UNIX timestamp format. For example, 1739980800 indicates 2025-02-20 00:00:00.
        self.expired = expired
        # **[Deprecated]** Use `format_disk_option` instead.
        # - `true`: Equivalent to setting `format_disk_option` to `DataDisk`.
        # - `false`: Equivalent to setting `format_disk_option` to `SystemDisk`.
        self.format_disk = format_disk
        # The disk formatting method. This parameter is mutually exclusive with `format_disk` when `format_disk` is set to `true`. Valid values:
        # 
        # - `SystemDisk`: No additional initialization is performed. Container runtime data is stored on the system cloud disk or any disk that is already mounted to the relevant directory during import.
        # - `DataDisk`: If a data cloud disk or local disk is mounted, the last disk is formatted and mounted to store container runtime data.
        # - `NodePoolDiskConfig`: Initializes data cloud disks based on the configurations of the imported node pool. Cloud disks and elastic ephemeral disks are matched based on the `disk_name` field of the node pool and the `DiskName` field of the block storage. Local disks are matched sequentially based on the PCI address order. Node pool configurations that do not match any disk are ignored.
        # 
        # >Warning: The `DataDisk` option is retained only for historical compatibility and is strongly discouraged.
        # This option uses the last disk in lexicographical order of device names under `/dev` (NVMe is preferred). Note that nvme9 takes precedence over nvme10. Operating systems with newer kernels such as Alinux 4 cannot guarantee a stable device order.
        # 
        # 
        # Disks with a recognizable file system during import skip the formatting step and are directly mounted.
        self.format_disk_option = format_disk_option
        # Specifies whether to retain the instance name when adding an existing instance to the cluster. If you do not retain the instance name, the instance name format is `worker-k8s-for-cs-<clusterid>`. Valid values:
        # 
        # - `true`: Retains the instance name.
        # - `false`: Does not retain the instance name. The instance name is replaced based on system rules.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The ID of the node pool. Specifies the node pool to which the node is added.
        # 
        # > If you do not specify a node pool ID, the node is added to the default node pool by default.
        self.nodepool_id = nodepool_id
        self.one_time_token = one_time_token
        # The access configuration parameters for the node.
        # 
        # > Required when the cluster type is ACK Edge.
        self.options = options
        # If an ApsaraDB RDS instance list is specified, the ECS instances of the cluster nodes are automatically added to the RDS access whitelist.
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

        if self.format_disk_option is not None:
            result['format_disk_option'] = self.format_disk_option

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

        if m.get('format_disk_option') is not None:
            self.format_disk_option = m.get('format_disk_option')

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

