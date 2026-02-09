# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeUserSpnSummaryInfoResponseBody(DaraModel):
    def __init__(
        self,
        instance_family_list: List[str] = None,
        region_list: List[main_models.DescribeUserSpnSummaryInfoResponseBodyRegionList] = None,
        request_id: str = None,
        spn_code_and_type_list: List[main_models.DescribeUserSpnSummaryInfoResponseBodySpnCodeAndTypeList] = None,
    ):
        self.instance_family_list = instance_family_list
        self.region_list = region_list
        self.request_id = request_id
        self.spn_code_and_type_list = spn_code_and_type_list

    def validate(self):
        if self.region_list:
            for v1 in self.region_list:
                 if v1:
                    v1.validate()
        if self.spn_code_and_type_list:
            for v1 in self.spn_code_and_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_family_list is not None:
            result['InstanceFamilyList'] = self.instance_family_list

        result['RegionList'] = []
        if self.region_list is not None:
            for k1 in self.region_list:
                result['RegionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpnCodeAndTypeList'] = []
        if self.spn_code_and_type_list is not None:
            for k1 in self.spn_code_and_type_list:
                result['SpnCodeAndTypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceFamilyList') is not None:
            self.instance_family_list = m.get('InstanceFamilyList')

        self.region_list = []
        if m.get('RegionList') is not None:
            for k1 in m.get('RegionList'):
                temp_model = main_models.DescribeUserSpnSummaryInfoResponseBodyRegionList()
                self.region_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spn_code_and_type_list = []
        if m.get('SpnCodeAndTypeList') is not None:
            for k1 in m.get('SpnCodeAndTypeList'):
                temp_model = main_models.DescribeUserSpnSummaryInfoResponseBodySpnCodeAndTypeList()
                self.spn_code_and_type_list.append(temp_model.from_map(k1))

        return self

class DescribeUserSpnSummaryInfoResponseBodySpnCodeAndTypeList(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        spn_commodity_code: str = None,
        spn_type: str = None,
        spn_type_name: str = None,
    ):
        self.product_code = product_code
        self.spn_commodity_code = spn_commodity_code
        self.spn_type = spn_type
        self.spn_type_name = spn_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.spn_commodity_code is not None:
            result['SpnCommodityCode'] = self.spn_commodity_code

        if self.spn_type is not None:
            result['SpnType'] = self.spn_type

        if self.spn_type_name is not None:
            result['SpnTypeName'] = self.spn_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SpnCommodityCode') is not None:
            self.spn_commodity_code = m.get('SpnCommodityCode')

        if m.get('SpnType') is not None:
            self.spn_type = m.get('SpnType')

        if m.get('SpnTypeName') is not None:
            self.spn_type_name = m.get('SpnTypeName')

        return self

class DescribeUserSpnSummaryInfoResponseBodyRegionList(DaraModel):
    def __init__(
        self,
        region_code: str = None,
        region_name: str = None,
    ):
        self.region_code = region_code
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        return self

