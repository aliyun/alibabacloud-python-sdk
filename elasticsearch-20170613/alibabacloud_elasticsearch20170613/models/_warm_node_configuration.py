# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WarmNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        performance_level: str = None,
        spec: str = None,
    ):
        # The number of cold data nodes.
        self.amount = amount
        # The storage space size of cold data nodes, in GB.
        self.disk = disk
        # Specifies whether to enable cloud disk encryption for cold data nodes. Valid values:
        # 
        # - true: enabled.
        # - false: not enabled.
        self.disk_encryption = disk_encryption
        # The storage type of cold data nodes. Only cloud_efficiency (ultra cloud disk) is supported.
        self.disk_type = disk_type
        # The performance level (PL) of the ESSD cloud disk. This parameter is required when the disk type of cold data nodes is a standard SSD. Valid values: PL1, PL2, and PL3.
        self.performance_level = performance_level
        # The node specifications of cold data nodes. For more information, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
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

        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

