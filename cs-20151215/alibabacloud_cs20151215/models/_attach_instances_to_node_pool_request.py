# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachInstancesToNodePoolRequest(DaraModel):
    def __init__(
        self,
        format_disk: bool = None,
        instances: List[str] = None,
        keep_instance_name: bool = None,
        password: str = None,
    ):
        # Specifies whether to store container data and images on data disks. Valid values:
        # 
        # *   `true`: stores container data and images on data disks.
        # *   `false`: does not store container data or images on data disks.
        # 
        # Default value: `false`.
        # 
        # How to mount a data disk:
        # 
        # *   If the ECS instances are already mounted with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4 and mounts it to /var/lib/docker and /var/lib/kubelet.
        # *   If no data disk is attached to the ECS instances, the system does not purchase a new data disk.
        # 
        # > If you choose to store container data and images on a data disk and the data disk is already mounted to the ECS instance, the existing data on the data disk will be cleared. You can back up the disk to avoid data loss.
        self.format_disk = format_disk
        # The IDs of the instances to be added.
        self.instances = instances
        # Specifies whether to retain the instance name. Valid values:
        # 
        # *   `true`: retains the instance name.
        # *   `false`: does not retain the instance name.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The SSH password that is used to log on to the instance.
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

        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')

        if m.get('password') is not None:
            self.password = m.get('password')

        return self

