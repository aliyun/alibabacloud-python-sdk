# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvisorChecksFoPagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeAdvisorChecksFoPagesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAdvisorChecksFoPagesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAdvisorChecksFoPagesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        result: List[main_models.DescribeAdvisorChecksFoPagesResponseBodyDataResult] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.result = result
        self.total = total

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeAdvisorChecksFoPagesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAdvisorChecksFoPagesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        category: str = None,
        code: str = None,
        config_support: str = None,
        description: str = None,
        inspection_scope: str = None,
        name: str = None,
        operate_column: str = None,
        product: str = None,
        risk_level: int = None,
        source: str = None,
        status: str = None,
        sub_category: List[int] = None,
        tips: str = None,
        view_column: str = None,
    ):
        self.category = category
        self.code = code
        self.config_support = config_support
        self.description = description
        self.inspection_scope = inspection_scope
        self.name = name
        self.operate_column = operate_column
        self.product = product
        self.risk_level = risk_level
        self.source = source
        self.status = status
        self.sub_category = sub_category
        self.tips = tips
        self.view_column = view_column

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.code is not None:
            result['Code'] = self.code

        if self.config_support is not None:
            result['ConfigSupport'] = self.config_support

        if self.description is not None:
            result['Description'] = self.description

        if self.inspection_scope is not None:
            result['InspectionScope'] = self.inspection_scope

        if self.name is not None:
            result['Name'] = self.name

        if self.operate_column is not None:
            result['OperateColumn'] = self.operate_column

        if self.product is not None:
            result['Product'] = self.product

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_category is not None:
            result['SubCategory'] = self.sub_category

        if self.tips is not None:
            result['Tips'] = self.tips

        if self.view_column is not None:
            result['ViewColumn'] = self.view_column

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConfigSupport') is not None:
            self.config_support = m.get('ConfigSupport')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InspectionScope') is not None:
            self.inspection_scope = m.get('InspectionScope')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperateColumn') is not None:
            self.operate_column = m.get('OperateColumn')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubCategory') is not None:
            self.sub_category = m.get('SubCategory')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('ViewColumn') is not None:
            self.view_column = m.get('ViewColumn')

        return self

