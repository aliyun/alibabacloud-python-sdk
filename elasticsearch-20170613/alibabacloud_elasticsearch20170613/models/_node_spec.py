# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_preference: str = None,
        disk_type: str = None,
        performance_level: str = None,
        spec: str = None,
    ):
        # The disk size of the data node, in GB.
        self.disk = disk
        # Specifies whether to enable cloud disk encryption for the data node. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.disk_encryption = disk_encryption
        # The storage preference.
        self.disk_preference = disk_preference
        # The storage type of the data node. Valid values:
        # 
        # - cloud_ssd: standard SSD
        # - cloud_essd: ESSD
        # - cloud_efficiency: ultra disk
        self.disk_type = disk_type
        # The performance level (PL) of the ESSD. This parameter is required when the disk type of the data node is ESSD. Valid values: PL1, PL2, and PL3.
        self.performance_level = performance_level
        # The specifications of the data node. For more information, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
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
        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_preference is not None:
            result['diskPreference'] = self.disk_preference

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskPreference') is not None:
            self.disk_preference = m.get('diskPreference')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

