# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachInstancesToNodePoolRequest(DaraModel):
    def __init__(
        self,
        format_disk: bool = None,
        format_disk_option: str = None,
        instances: List[str] = None,
        keep_instance_name: bool = None,
        password: str = None,
    ):
        # **[Deprecated]** Use `format_disk_option` instead. Valid values:
        # 
        # - `true`: equivalent to setting `format_disk_option` to `DataDisk`.
        # - `false`: equivalent to setting `format_disk_option` to `SystemDisk`.
        self.format_disk = format_disk
        # The disk formatting method. This parameter is mutually exclusive with `format_disk` set to `true`. Valid values:
        # 
        # - `SystemDisk`: No additional initialization is performed. Container runtime data is stored on the system cloud disk or any disk that is already mounted to the relevant directory during import.
        # - `DataDisk`: If a data cloud disk or local disk is mounted, the last disk is formatted and mounted to store container runtime data.
        # - `NodePoolDiskConfig`: Initializes data cloud disks based on the configuration of the imported node pool. Cloud disks and elastic ephemeral disks are matched based on the `disk_name` field of the node pool and the `DiskName` field of the block storage. Local disks are matched sequentially based on the PCI address order. Node pool configurations that do not match any disk are ignored.
        # 
        # >Warning: The `DataDisk` option is retained only for historical compatibility and is strongly discouraged.
        # This option uses the last disk in lexicographical order of device names under `/dev` (NVMe is preferred). Note that nvme9 takes precedence over nvme10. Operating systems with newer kernels such as Alinux 4 cannot guarantee a stable device order.
        # 
        # 
        # Disks with recognizable file systems during import skip the formatting step and are mounted directly.
        self.format_disk_option = format_disk_option
        # The list of ECS instances to be added.
        self.instances = instances
        # Specifies whether to retain the original instance name. Valid values:
        # 
        # - `true`: Retains the instance name.
        # 
        # - `false`: Does not retain the instance name.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The SSH logon password for the instances to be added.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk

        if self.format_disk_option is not None:
            result['format_disk_option'] = self.format_disk_option

        if self.instances is not None:
            result['instances'] = self.instances

        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name

        if self.password is not None:
            result['password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')

        if m.get('format_disk_option') is not None:
            self.format_disk_option = m.get('format_disk_option')

        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')

        if m.get('password') is not None:
            self.password = m.get('password')

        return self

