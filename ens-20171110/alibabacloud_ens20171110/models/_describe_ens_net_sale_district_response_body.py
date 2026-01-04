# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsNetSaleDistrictResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ens_net_districts: main_models.DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts = None,
        request_id: str = None,
    ):
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The information about the ISPs in the area.
        self.ens_net_districts = ens_net_districts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnsNetDistricts') is not None:
            temp_model = main_models.DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(m.get('EnsNetDistricts'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts(DaraModel):
    def __init__(
        self,
        ens_net_district: List[main_models.DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict] = None,
    ):
        self.ens_net_district = ens_net_district

    def validate(self):
        if self.ens_net_district:
            for v1 in self.ens_net_district:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k1 in self.ens_net_district:
                result['EnsNetDistrict'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_district = []
        if m.get('EnsNetDistrict') is not None:
            for k1 in m.get('EnsNetDistrict'):
                temp_model = main_models.DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k1))

        return self

class DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict(DaraModel):
    def __init__(
        self,
        ens_region_id_count: str = None,
        instance_count: str = None,
        net_district_code: str = None,
        net_district_en_name: str = None,
        net_district_father_code: str = None,
        net_district_level: str = None,
        net_district_name: str = None,
    ):
        # The information about the ISP.
        self.ens_region_id_count = ens_region_id_count
        # The information about the instance.
        self.instance_count = instance_count
        # The region code.
        self.net_district_code = net_district_code
        # The name of the region.
        self.net_district_en_name = net_district_en_name
        # The parent code of the region.
        self.net_district_father_code = net_district_father_code
        # The region level. Valid values:
        # 
        # *   **Big**: area
        # *   **Middle**: province
        # *   **Small**: city
        self.net_district_level = net_district_level
        # The Chinese name of the region.
        self.net_district_name = net_district_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id_count is not None:
            result['EnsRegionIdCount'] = self.ens_region_id_count

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code

        if self.net_district_en_name is not None:
            result['NetDistrictEnName'] = self.net_district_en_name

        if self.net_district_father_code is not None:
            result['NetDistrictFatherCode'] = self.net_district_father_code

        if self.net_district_level is not None:
            result['NetDistrictLevel'] = self.net_district_level

        if self.net_district_name is not None:
            result['NetDistrictName'] = self.net_district_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdCount') is not None:
            self.ens_region_id_count = m.get('EnsRegionIdCount')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')

        if m.get('NetDistrictEnName') is not None:
            self.net_district_en_name = m.get('NetDistrictEnName')

        if m.get('NetDistrictFatherCode') is not None:
            self.net_district_father_code = m.get('NetDistrictFatherCode')

        if m.get('NetDistrictLevel') is not None:
            self.net_district_level = m.get('NetDistrictLevel')

        if m.get('NetDistrictName') is not None:
            self.net_district_name = m.get('NetDistrictName')

        return self

