# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeColdDataBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeColdDataBasicInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeColdDataBasicInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeColdDataBasicInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        backup_set_count: int = None,
        backup_set_space_size: float = None,
        cloud_product: str = None,
        current_space_size: float = None,
        data_redundancy_type: str = None,
        enable_status: bool = None,
        read_access_num: int = None,
        region_id: str = None,
        volume_name: str = None,
        write_access_num: float = None,
    ):
        self.backup_set_count = backup_set_count
        self.backup_set_space_size = backup_set_space_size
        self.cloud_product = cloud_product
        self.current_space_size = current_space_size
        self.data_redundancy_type = data_redundancy_type
        self.enable_status = enable_status
        self.read_access_num = read_access_num
        self.region_id = region_id
        self.volume_name = volume_name
        self.write_access_num = write_access_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_count is not None:
            result['BackupSetCount'] = self.backup_set_count

        if self.backup_set_space_size is not None:
            result['BackupSetSpaceSize'] = self.backup_set_space_size

        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.current_space_size is not None:
            result['CurrentSpaceSize'] = self.current_space_size

        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.read_access_num is not None:
            result['ReadAccessNum'] = self.read_access_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name

        if self.write_access_num is not None:
            result['WriteAccessNum'] = self.write_access_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetCount') is not None:
            self.backup_set_count = m.get('BackupSetCount')

        if m.get('BackupSetSpaceSize') is not None:
            self.backup_set_space_size = m.get('BackupSetSpaceSize')

        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('CurrentSpaceSize') is not None:
            self.current_space_size = m.get('CurrentSpaceSize')

        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('ReadAccessNum') is not None:
            self.read_access_num = m.get('ReadAccessNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')

        if m.get('WriteAccessNum') is not None:
            self.write_access_num = m.get('WriteAccessNum')

        return self

