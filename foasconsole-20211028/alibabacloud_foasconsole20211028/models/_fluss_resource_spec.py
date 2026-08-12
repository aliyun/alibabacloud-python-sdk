# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlussResourceSpec(DaraModel):
    def __init__(
        self,
        disk_size_in_gb: int = None,
        slave_model: str = None,
        slave_num: int = None,
        tiering_post_cu: int = None,
        tiering_pre_cu: int = None,
    ):
        # Disk size per node, in GB.
        self.disk_size_in_gb = disk_size_in_gb
        # Instance type of the slave nodes.
        self.slave_model = slave_model
        # Number of slave nodes.
        self.slave_num = slave_num
        # Number of CUs for the post-tiering stage.
        self.tiering_post_cu = tiering_post_cu
        # Number of compute units (CUs) for the pre-tiering stage.
        self.tiering_pre_cu = tiering_pre_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_size_in_gb is not None:
            result['DiskSizeInGB'] = self.disk_size_in_gb

        if self.slave_model is not None:
            result['SlaveModel'] = self.slave_model

        if self.slave_num is not None:
            result['SlaveNum'] = self.slave_num

        if self.tiering_post_cu is not None:
            result['TieringPostCu'] = self.tiering_post_cu

        if self.tiering_pre_cu is not None:
            result['TieringPreCu'] = self.tiering_pre_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSizeInGB') is not None:
            self.disk_size_in_gb = m.get('DiskSizeInGB')

        if m.get('SlaveModel') is not None:
            self.slave_model = m.get('SlaveModel')

        if m.get('SlaveNum') is not None:
            self.slave_num = m.get('SlaveNum')

        if m.get('TieringPostCu') is not None:
            self.tiering_post_cu = m.get('TieringPostCu')

        if m.get('TieringPreCu') is not None:
            self.tiering_pre_cu = m.get('TieringPreCu')

        return self

