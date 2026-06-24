# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MasterNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The number of dedicated master nodes.
        # 
        # This parameter is required.
        self.amount = amount
        # The storage space of dedicated master nodes. Unit: GB.
        # 
        # This parameter is required.
        self.disk = disk
        # The storage type of dedicated master nodes. Valid values:
        # - cloud_ssd: standard SSD
        # - cloud_essd (default): Enterprise SSD (ESSD).
        # 
        # This parameter is required.
        self.disk_type = disk_type
        # The node specifications of dedicated master nodes. For more information, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

