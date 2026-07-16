# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CostInstanceType(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        data_disks: List[main_models.DataDisk] = None,
        instance_type: str = None,
        memory: int = None,
        system_disk: main_models.SystemDisk = None,
    ):
        # CPU核数。
        self.cpu = cpu
        # 数据盘列表。
        self.data_disks = data_disks
        # 实例类型列表。
        self.instance_type = instance_type
        # 内存大小。
        self.memory = memory
        # 系统盘信息。
        self.system_disk = system_disk

    def validate(self):
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.DataDisk()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.SystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        return self

