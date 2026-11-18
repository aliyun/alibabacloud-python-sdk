# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ResizeWuyingServerDiskRequest(DaraModel):
    def __init__(
        self,
        data_disk_list: List[main_models.ResizeWuyingServerDiskRequestDataDiskList] = None,
        product_type: str = None,
        system_disk_new_size: int = None,
        wuying_server_id: str = None,
    ):
        # The size and specifications of the data cloud disks.
        self.data_disk_list = data_disk_list
        # The product type.
        self.product_type = product_type
        # The new size of the system cloud disk, in GB.
        self.system_disk_new_size = system_disk_new_size
        # The ID of the WUYING Workspace.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        if self.data_disk_list:
            for v1 in self.data_disk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDiskList'] = []
        if self.data_disk_list is not None:
            for k1 in self.data_disk_list:
                result['DataDiskList'].append(k1.to_map() if k1 else None)

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.system_disk_new_size is not None:
            result['SystemDiskNewSize'] = self.system_disk_new_size

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk_list = []
        if m.get('DataDiskList') is not None:
            for k1 in m.get('DataDiskList'):
                temp_model = main_models.ResizeWuyingServerDiskRequestDataDiskList()
                self.data_disk_list.append(temp_model.from_map(k1))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SystemDiskNewSize') is not None:
            self.system_disk_new_size = m.get('SystemDiskNewSize')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

class ResizeWuyingServerDiskRequestDataDiskList(DaraModel):
    def __init__(
        self,
        disk_no: str = None,
        disk_sub_type: str = None,
        disk_type: str = None,
        new_size: int = None,
    ):
        # The disk number.
        self.disk_no = disk_no
        # The disk subtype.
        self.disk_sub_type = disk_sub_type
        # The type of disk data included in the image. By default, the system cloud disk and data cloud disks of the instance are included.
        self.disk_type = disk_type
        # The new size.
        self.new_size = new_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_no is not None:
            result['DiskNo'] = self.disk_no

        if self.disk_sub_type is not None:
            result['DiskSubType'] = self.disk_sub_type

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.new_size is not None:
            result['NewSize'] = self.new_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskNo') is not None:
            self.disk_no = m.get('DiskNo')

        if m.get('DiskSubType') is not None:
            self.disk_sub_type = m.get('DiskSubType')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')

        return self

