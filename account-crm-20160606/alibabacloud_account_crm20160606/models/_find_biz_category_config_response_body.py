# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class FindBizCategoryConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.FindBizCategoryConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.FindBizCategoryConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindBizCategoryConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_category: List[main_models.FindBizCategoryConfigResponseBodyDataBizCategory] = None,
    ):
        self.biz_category = biz_category

    def validate(self):
        if self.biz_category:
            for v1 in self.biz_category:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizCategory'] = []
        if self.biz_category is not None:
            for k1 in self.biz_category:
                result['BizCategory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_category = []
        if m.get('BizCategory') is not None:
            for k1 in m.get('BizCategory'):
                temp_model = main_models.FindBizCategoryConfigResponseBodyDataBizCategory()
                self.biz_category.append(temp_model.from_map(k1))

        return self

class FindBizCategoryConfigResponseBodyDataBizCategory(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_check: bool = None,
        main_biz: bool = None,
        name: str = None,
        other: str = None,
        sub_configs: main_models.FindBizCategoryConfigResponseBodyDataBizCategorySubConfigs = None,
    ):
        self.code = code
        self.is_check = is_check
        self.main_biz = main_biz
        self.name = name
        self.other = other
        self.sub_configs = sub_configs

    def validate(self):
        if self.sub_configs:
            self.sub_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_check is not None:
            result['IsCheck'] = self.is_check

        if self.main_biz is not None:
            result['MainBiz'] = self.main_biz

        if self.name is not None:
            result['Name'] = self.name

        if self.other is not None:
            result['Other'] = self.other

        if self.sub_configs is not None:
            result['SubConfigs'] = self.sub_configs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')

        if m.get('MainBiz') is not None:
            self.main_biz = m.get('MainBiz')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Other') is not None:
            self.other = m.get('Other')

        if m.get('SubConfigs') is not None:
            temp_model = main_models.FindBizCategoryConfigResponseBodyDataBizCategorySubConfigs()
            self.sub_configs = temp_model.from_map(m.get('SubConfigs'))

        return self

class FindBizCategoryConfigResponseBodyDataBizCategorySubConfigs(DaraModel):
    def __init__(
        self,
        biz_sub_category: List[main_models.FindBizCategoryConfigResponseBodyDataBizCategorySubConfigsBizSubCategory] = None,
    ):
        self.biz_sub_category = biz_sub_category

    def validate(self):
        if self.biz_sub_category:
            for v1 in self.biz_sub_category:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizSubCategory'] = []
        if self.biz_sub_category is not None:
            for k1 in self.biz_sub_category:
                result['BizSubCategory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_sub_category = []
        if m.get('BizSubCategory') is not None:
            for k1 in m.get('BizSubCategory'):
                temp_model = main_models.FindBizCategoryConfigResponseBodyDataBizCategorySubConfigsBizSubCategory()
                self.biz_sub_category.append(temp_model.from_map(k1))

        return self

class FindBizCategoryConfigResponseBodyDataBizCategorySubConfigsBizSubCategory(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_check: bool = None,
        main_biz: bool = None,
        name: str = None,
        other: str = None,
    ):
        self.code = code
        self.is_check = is_check
        self.main_biz = main_biz
        self.name = name
        self.other = other

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_check is not None:
            result['IsCheck'] = self.is_check

        if self.main_biz is not None:
            result['MainBiz'] = self.main_biz

        if self.name is not None:
            result['Name'] = self.name

        if self.other is not None:
            result['Other'] = self.other

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')

        if m.get('MainBiz') is not None:
            self.main_biz = m.get('MainBiz')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Other') is not None:
            self.other = m.get('Other')

        return self

