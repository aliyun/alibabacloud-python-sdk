# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNASAvailableResourceInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        nas_available_resource_info: List[main_models.DescribeNASAvailableResourceInfoResponseBodyNasAvailableResourceInfo] = None,
        request_id: str = None,
    ):
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The error message.
        self.message = message
        # The information of available NAS resources.
        self.nas_available_resource_info = nas_available_resource_info
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.nas_available_resource_info:
            for v1 in self.nas_available_resource_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['NasAvailableResourceInfo'] = []
        if self.nas_available_resource_info is not None:
            for k1 in self.nas_available_resource_info:
                result['NasAvailableResourceInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.nas_available_resource_info = []
        if m.get('NasAvailableResourceInfo') is not None:
            for k1 in m.get('NasAvailableResourceInfo'):
                temp_model = main_models.DescribeNASAvailableResourceInfoResponseBodyNasAvailableResourceInfo()
                self.nas_available_resource_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNASAvailableResourceInfoResponseBodyNasAvailableResourceInfo(DaraModel):
    def __init__(
        self,
        ability: List[str] = None,
        area: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        ens_region_name: str = None,
        nas_available_amount: int = None,
        nas_available_storge_type: str = None,
        province: str = None,
    ):
        # The product supported by the edge node.
        self.ability = ability
        # The region to which the ENS node belongs.
        self.area = area
        # The English name.
        self.en_name = en_name
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The name of the ENS node.
        self.ens_region_name = ens_region_name
        # the number of available NAS resources.
        self.nas_available_amount = nas_available_amount
        # The types of available NAS resources.
        self.nas_available_storge_type = nas_available_storge_type
        # The province to which the ENS node belongs.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability is not None:
            result['Ability'] = self.ability

        if self.area is not None:
            result['Area'] = self.area

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_name is not None:
            result['EnsRegionName'] = self.ens_region_name

        if self.nas_available_amount is not None:
            result['NasAvailableAmount'] = self.nas_available_amount

        if self.nas_available_storge_type is not None:
            result['NasAvailableStorgeType'] = self.nas_available_storge_type

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ability') is not None:
            self.ability = m.get('Ability')

        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionName') is not None:
            self.ens_region_name = m.get('EnsRegionName')

        if m.get('NasAvailableAmount') is not None:
            self.nas_available_amount = m.get('NasAvailableAmount')

        if m.get('NasAvailableStorgeType') is not None:
            self.nas_available_storge_type = m.get('NasAvailableStorgeType')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

