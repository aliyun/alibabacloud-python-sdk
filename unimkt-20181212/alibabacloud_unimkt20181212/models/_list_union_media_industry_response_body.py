# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_unimkt20181212 import models as main_models
from darabonba.model import DaraModel

class ListUnionMediaIndustryResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListUnionMediaIndustryResponseBodyData] = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUnionMediaIndustryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class ListUnionMediaIndustryResponseBodyData(DaraModel):
    def __init__(
        self,
        industry_code: str = None,
        industry_name: str = None,
        level: str = None,
        parent_industry_code: str = None,
        used_flag: bool = None,
    ):
        self.industry_code = industry_code
        self.industry_name = industry_name
        self.level = level
        self.parent_industry_code = parent_industry_code
        self.used_flag = used_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.industry_code is not None:
            result['IndustryCode'] = self.industry_code

        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_industry_code is not None:
            result['ParentIndustryCode'] = self.parent_industry_code

        if self.used_flag is not None:
            result['UsedFlag'] = self.used_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndustryCode') is not None:
            self.industry_code = m.get('IndustryCode')

        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentIndustryCode') is not None:
            self.parent_industry_code = m.get('ParentIndustryCode')

        if m.get('UsedFlag') is not None:
            self.used_flag = m.get('UsedFlag')

        return self

