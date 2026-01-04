# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateStorageGatewayResponseBody(DaraModel):
    def __init__(
        self,
        allocation_id: List[main_models.CreateStorageGatewayResponseBodyAllocationId] = None,
        biz_status_code: str = None,
        request_id: str = None,
        un_allocation_id: List[main_models.CreateStorageGatewayResponseBodyUnAllocationId] = None,
    ):
        # The list of created nodes.
        self.allocation_id = allocation_id
        # The success status code.
        # 
        # *   **PartSuccess**: partially succeeded.
        # *   **AllSuccess**: all succeeded.
        self.biz_status_code = biz_status_code
        # The request ID.
        self.request_id = request_id
        # The list of nodes that are not created.
        self.un_allocation_id = un_allocation_id

    def validate(self):
        if self.allocation_id:
            for v1 in self.allocation_id:
                 if v1:
                    v1.validate()
        if self.un_allocation_id:
            for v1 in self.un_allocation_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllocationId'] = []
        if self.allocation_id is not None:
            for k1 in self.allocation_id:
                result['AllocationId'].append(k1.to_map() if k1 else None)

        if self.biz_status_code is not None:
            result['BizStatusCode'] = self.biz_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UnAllocationId'] = []
        if self.un_allocation_id is not None:
            for k1 in self.un_allocation_id:
                result['UnAllocationId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allocation_id = []
        if m.get('AllocationId') is not None:
            for k1 in m.get('AllocationId'):
                temp_model = main_models.CreateStorageGatewayResponseBodyAllocationId()
                self.allocation_id.append(temp_model.from_map(k1))

        if m.get('BizStatusCode') is not None:
            self.biz_status_code = m.get('BizStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.un_allocation_id = []
        if m.get('UnAllocationId') is not None:
            for k1 in m.get('UnAllocationId'):
                temp_model = main_models.CreateStorageGatewayResponseBodyUnAllocationId()
                self.un_allocation_id.append(temp_model.from_map(k1))

        return self

class CreateStorageGatewayResponseBodyUnAllocationId(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The ID of the instance.
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

class CreateStorageGatewayResponseBodyAllocationId(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The ID of the instance.
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

