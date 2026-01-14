# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryBusinessLocationsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryBusinessLocationsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result of the request.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryBusinessLocationsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryBusinessLocationsResponseBodyData(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        description: str = None,
        district_cn_name: str = None,
        district_en_name: str = None,
        district_id: str = None,
        district_ordering: int = None,
        district_show_name: str = None,
        en_description: str = None,
        en_name: str = None,
        name: str = None,
        ordering: int = None,
        show_name: str = None,
        type: str = None,
    ):
        # The Chinese name of the region.
        self.cn_name = cn_name
        # The description.
        self.description = description
        # The Chinese name of the district.
        self.district_cn_name = district_cn_name
        # The English name of the district.
        self.district_en_name = district_en_name
        # The ID of the region.
        self.district_id = district_id
        # The ordering information of the district.
        self.district_ordering = district_ordering
        # The display name of the district.
        self.district_show_name = district_show_name
        # The complete description of the region.
        self.en_description = en_description
        # The English name of the region.
        self.en_name = en_name
        # The name.
        self.name = name
        # The ordering information.
        self.ordering = ordering
        # The display name.
        self.show_name = show_name
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_name is not None:
            result['CnName'] = self.cn_name

        if self.description is not None:
            result['Description'] = self.description

        if self.district_cn_name is not None:
            result['DistrictCnName'] = self.district_cn_name

        if self.district_en_name is not None:
            result['DistrictEnName'] = self.district_en_name

        if self.district_id is not None:
            result['DistrictId'] = self.district_id

        if self.district_ordering is not None:
            result['DistrictOrdering'] = self.district_ordering

        if self.district_show_name is not None:
            result['DistrictShowName'] = self.district_show_name

        if self.en_description is not None:
            result['EnDescription'] = self.en_description

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.name is not None:
            result['Name'] = self.name

        if self.ordering is not None:
            result['Ordering'] = self.ordering

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DistrictCnName') is not None:
            self.district_cn_name = m.get('DistrictCnName')

        if m.get('DistrictEnName') is not None:
            self.district_en_name = m.get('DistrictEnName')

        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')

        if m.get('DistrictOrdering') is not None:
            self.district_ordering = m.get('DistrictOrdering')

        if m.get('DistrictShowName') is not None:
            self.district_show_name = m.get('DistrictShowName')

        if m.get('EnDescription') is not None:
            self.en_description = m.get('EnDescription')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Ordering') is not None:
            self.ordering = m.get('Ordering')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

