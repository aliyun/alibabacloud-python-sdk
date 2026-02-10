# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAgentlessRegionResponseBody(DaraModel):
    def __init__(
        self,
        region_list: List[str] = None,
        request_id: str = None,
        vendor_region_list: List[main_models.ListAgentlessRegionResponseBodyVendorRegionList] = None,
    ):
        # The information about the regions.
        self.region_list = region_list
        # The request ID.
        self.request_id = request_id
        # The information about the regions.
        self.vendor_region_list = vendor_region_list

    def validate(self):
        if self.vendor_region_list:
            for v1 in self.vendor_region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_list is not None:
            result['RegionList'] = self.region_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VendorRegionList'] = []
        if self.vendor_region_list is not None:
            for k1 in self.vendor_region_list:
                result['VendorRegionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vendor_region_list = []
        if m.get('VendorRegionList') is not None:
            for k1 in m.get('VendorRegionList'):
                temp_model = main_models.ListAgentlessRegionResponseBodyVendorRegionList()
                self.vendor_region_list.append(temp_model.from_map(k1))

        return self

class ListAgentlessRegionResponseBodyVendorRegionList(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vendor: int = None,
    ):
        # The region ID of the instance.
        self.region_id = region_id
        # The type of the server. Valid values:
        # 
        # - **0**: Alibaba Cloud
        # - **3**: Tencent Cloud
        # - **4**: Huawei Cloud
        # - **5**: Azure
        # - **7**: AWS
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

