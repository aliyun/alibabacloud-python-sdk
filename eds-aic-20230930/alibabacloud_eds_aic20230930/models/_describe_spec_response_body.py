# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeSpecResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        spec_info_model: List[main_models.DescribeSpecResponseBodySpecInfoModel] = None,
        total_count: int = None,
    ):
        # The token to use for the next request to retrieve a new page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The specification information.
        self.spec_info_model = spec_info_model
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.spec_info_model:
            for v1 in self.spec_info_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpecInfoModel'] = []
        if self.spec_info_model is not None:
            for k1 in self.spec_info_model:
                result['SpecInfoModel'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spec_info_model = []
        if m.get('SpecInfoModel') is not None:
            for k1 in m.get('SpecInfoModel'):
                temp_model = main_models.DescribeSpecResponseBodySpecInfoModel()
                self.spec_info_model.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSpecResponseBodySpecInfoModel(DaraModel):
    def __init__(
        self,
        core: int = None,
        max_phone_count: str = None,
        memory: int = None,
        min_phone_count: str = None,
        phone_count: str = None,
        resolution: str = None,
        spec_id: str = None,
        spec_status: str = None,
        spec_type: str = None,
        system_disk_size: int = None,
    ):
        # The number of CPU cores.
        self.core = core
        # The maximum number of instances.
        self.max_phone_count = max_phone_count
        # The memory size in GB.
        self.memory = memory
        # The minimum number of instances.
        self.min_phone_count = min_phone_count
        # The number of instances.
        self.phone_count = phone_count
        # The resolution of the cloud phone instance.
        self.resolution = resolution
        # The specification ID.
        self.spec_id = spec_id
        # The specification status.
        self.spec_status = spec_status
        # The specification type.
        self.spec_type = spec_type
        # The size of the system disk, in GB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core is not None:
            result['Core'] = self.core

        if self.max_phone_count is not None:
            result['MaxPhoneCount'] = self.max_phone_count

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.min_phone_count is not None:
            result['MinPhoneCount'] = self.min_phone_count

        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.spec_status is not None:
            result['SpecStatus'] = self.spec_status

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('MaxPhoneCount') is not None:
            self.max_phone_count = m.get('MaxPhoneCount')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MinPhoneCount') is not None:
            self.min_phone_count = m.get('MinPhoneCount')

        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('SpecStatus') is not None:
            self.spec_status = m.get('SpecStatus')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

