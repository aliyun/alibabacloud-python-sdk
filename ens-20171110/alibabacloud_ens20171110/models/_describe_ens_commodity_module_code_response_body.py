# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsCommodityModuleCodeResponseBody(DaraModel):
    def __init__(
        self,
        commodity_codes_info: List[main_models.DescribeEnsCommodityModuleCodeResponseBodyCommodityCodesInfo] = None,
        request_id: str = None,
    ):
        self.commodity_codes_info = commodity_codes_info
        self.request_id = request_id

    def validate(self):
        if self.commodity_codes_info:
            for v1 in self.commodity_codes_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommodityCodesInfo'] = []
        if self.commodity_codes_info is not None:
            for k1 in self.commodity_codes_info:
                result['CommodityCodesInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity_codes_info = []
        if m.get('CommodityCodesInfo') is not None:
            for k1 in m.get('CommodityCodesInfo'):
                temp_model = main_models.DescribeEnsCommodityModuleCodeResponseBodyCommodityCodesInfo()
                self.commodity_codes_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnsCommodityModuleCodeResponseBodyCommodityCodesInfo(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        module_codes_info: List[main_models.DescribeEnsCommodityModuleCodeResponseBodyCommodityCodesInfoModuleCodesInfo] = None,
    ):
        self.commodity_code = commodity_code
        self.module_codes_info = module_codes_info

    def validate(self):
        if self.module_codes_info:
            for v1 in self.module_codes_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        result['ModuleCodesInfo'] = []
        if self.module_codes_info is not None:
            for k1 in self.module_codes_info:
                result['ModuleCodesInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        self.module_codes_info = []
        if m.get('ModuleCodesInfo') is not None:
            for k1 in m.get('ModuleCodesInfo'):
                temp_model = main_models.DescribeEnsCommodityModuleCodeResponseBodyCommodityCodesInfoModuleCodesInfo()
                self.module_codes_info.append(temp_model.from_map(k1))

        return self

class DescribeEnsCommodityModuleCodeResponseBodyCommodityCodesInfoModuleCodesInfo(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        module_name: str = None,
    ):
        self.module_code = module_code
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

