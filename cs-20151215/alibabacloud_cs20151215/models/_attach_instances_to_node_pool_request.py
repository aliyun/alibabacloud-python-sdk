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
        # Specifies whether to store container data and images on data cloud disks. Valid values:
        # 
        # - `true`: Stores container data and images on data cloud disks.
        # 
        # - `false`: Does not store container data and images on data cloud disks.
        # 
        # Default value: `false`.
        # 
        # 
        # Data cloud disk mounting rules:
        # 
        # - If the ECS instance has data cloud disks mounted and the file system of the last data cloud disk is not initialized, the system automatically formats the data cloud disk to EXT4 to store the /var/lib/docker and /var/lib/kubelet directories.
        # - If the ECS instance does not have data cloud disks mounted, no new data cloud disks are mounted.
        # > If you choose to store data on data cloud disks and the ECS instance already has data cloud disks mounted, the existing data on the data cloud disks will be lost. Back up your data in advance.
        self.format_disk = format_disk
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

