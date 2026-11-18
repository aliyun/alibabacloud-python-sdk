# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeWuyingServerDiskShrinkRequest(DaraModel):
    def __init__(
        self,
        data_disk_list_shrink: str = None,
        product_type: str = None,
        system_disk_new_size: int = None,
        wuying_server_id: str = None,
    ):
        # The size and specifications of the data cloud disks.
        self.data_disk_list_shrink = data_disk_list_shrink
        # The product type.
        self.product_type = product_type
        # The new size of the system cloud disk, in GB.
        self.system_disk_new_size = system_disk_new_size
        # The ID of the WUYING Workspace.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_list_shrink is not None:
            result['DataDiskList'] = self.data_disk_list_shrink

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.system_disk_new_size is not None:
            result['SystemDiskNewSize'] = self.system_disk_new_size

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskList') is not None:
            self.data_disk_list_shrink = m.get('DataDiskList')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SystemDiskNewSize') is not None:
            self.system_disk_new_size = m.get('SystemDiskNewSize')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

