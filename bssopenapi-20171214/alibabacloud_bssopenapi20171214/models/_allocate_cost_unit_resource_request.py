# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class AllocateCostUnitResourceRequest(DaraModel):
    def __init__(
        self,
        from_unit_id: int = None,
        from_unit_user_id: int = None,
        resource_instance_list: List[main_models.AllocateCostUnitResourceRequestResourceInstanceList] = None,
        to_unit_id: int = None,
        to_unit_user_id: int = None,
    ):
        # The ID of the source cost center.
        # 
        # *   A value of 0 indicates that the resources to be transferred have not been allocated to a cost center.
        # *   A value greater than 0 indicates the ID of an existing cost center.
        # 
        # This parameter is required.
        self.from_unit_id = from_unit_id
        # The user ID of the owner of the source cost center.
        # 
        # This parameter is required.
        self.from_unit_user_id = from_unit_user_id
        # The resource instances to be transferred.
        # 
        # This parameter is required.
        self.resource_instance_list = resource_instance_list
        # The ID of the destination cost center.
        # 
        # *   A value of -1 indicates that the allocated resources are changed to unallocated.
        # *   A value greater than 0 indicates the ID of an existing cost center.
        # 
        # This parameter is required.
        self.to_unit_id = to_unit_id
        # The user ID of the owner of the destination cost center.
        # 
        # This parameter is required.
        self.to_unit_user_id = to_unit_user_id

    def validate(self):
        if self.resource_instance_list:
            for v1 in self.resource_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_unit_id is not None:
            result['FromUnitId'] = self.from_unit_id

        if self.from_unit_user_id is not None:
            result['FromUnitUserId'] = self.from_unit_user_id

        result['ResourceInstanceList'] = []
        if self.resource_instance_list is not None:
            for k1 in self.resource_instance_list:
                result['ResourceInstanceList'].append(k1.to_map() if k1 else None)

        if self.to_unit_id is not None:
            result['ToUnitId'] = self.to_unit_id

        if self.to_unit_user_id is not None:
            result['ToUnitUserId'] = self.to_unit_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromUnitId') is not None:
            self.from_unit_id = m.get('FromUnitId')

        if m.get('FromUnitUserId') is not None:
            self.from_unit_user_id = m.get('FromUnitUserId')

        self.resource_instance_list = []
        if m.get('ResourceInstanceList') is not None:
            for k1 in m.get('ResourceInstanceList'):
                temp_model = main_models.AllocateCostUnitResourceRequestResourceInstanceList()
                self.resource_instance_list.append(temp_model.from_map(k1))

        if m.get('ToUnitId') is not None:
            self.to_unit_id = m.get('ToUnitId')

        if m.get('ToUnitUserId') is not None:
            self.to_unit_user_id = m.get('ToUnitUserId')

        return self

class AllocateCostUnitResourceRequestResourceInstanceList(DaraModel):
    def __init__(
        self,
        apportion_code: str = None,
        commodity_code: str = None,
        resource_id: str = None,
        resource_user_id: int = None,
    ):
        # The split item of the shared instance. This parameter is required only for shared instances.
        # 
        # *   Eight cloud services support bill splitting. The commodity codes of the eight services are oss, dcdn, snapshot, vod, cdn, live, and cbwp.
        # *   You can obtain the split item of a shared instance by calling QueryCostUnitResource operation to obtain all resource instances within a cost center.
        self.apportion_code = apportion_code
        # The commodity code of the resource instance.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The ID of the resource instance.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The user ID of the resource instance owner.
        # 
        # This parameter is required.
        self.resource_user_id = resource_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')

        return self

