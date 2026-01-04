# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateFileSystemResponseBody(DaraModel):
    def __init__(
        self,
        allocation_id: List[str] = None,
        allocation_ids: List[main_models.CreateFileSystemResponseBodyAllocationIds] = None,
        biz_status_code: str = None,
        request_id: str = None,
        un_allocation_id: List[str] = None,
    ):
        # The information about the file system that was created.
        self.allocation_id = allocation_id
        self.allocation_ids = allocation_ids
        # The status code for successful operations. Valid values:
        # 
        # *   PartSuccess: The operation is partially successful.
        # *   AllSuccess: The operation is successful.
        self.biz_status_code = biz_status_code
        # The ID of the request.
        self.request_id = request_id
        # The information about the file system that failed to be created.
        self.un_allocation_id = un_allocation_id

    def validate(self):
        if self.allocation_ids:
            for v1 in self.allocation_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        result['AllocationIds'] = []
        if self.allocation_ids is not None:
            for k1 in self.allocation_ids:
                result['AllocationIds'].append(k1.to_map() if k1 else None)

        if self.biz_status_code is not None:
            result['BizStatusCode'] = self.biz_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.un_allocation_id is not None:
            result['UnAllocationId'] = self.un_allocation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        self.allocation_ids = []
        if m.get('AllocationIds') is not None:
            for k1 in m.get('AllocationIds'):
                temp_model = main_models.CreateFileSystemResponseBodyAllocationIds()
                self.allocation_ids.append(temp_model.from_map(k1))

        if m.get('BizStatusCode') is not None:
            self.biz_status_code = m.get('BizStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UnAllocationId') is not None:
            self.un_allocation_id = m.get('UnAllocationId')

        return self

class CreateFileSystemResponseBodyAllocationIds(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

