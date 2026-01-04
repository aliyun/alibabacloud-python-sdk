# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStorageVolumeRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        gateway_id: str = None,
        is_enable: int = None,
        page_number: int = None,
        page_size: int = None,
        storage_id: str = None,
        volume_id: str = None,
    ):
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # Specifies whether to enable the volume. Valid values:
        # 
        # *   **1** (default): enables the volume.
        # *   **0**: disables the volume.
        self.is_enable = is_enable
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the storage medium.
        self.storage_id = storage_id
        # The ID of the volume.
        self.volume_id = volume_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.storage_id is not None:
            result['StorageId'] = self.storage_id

        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StorageId') is not None:
            self.storage_id = m.get('StorageId')

        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')

        return self

