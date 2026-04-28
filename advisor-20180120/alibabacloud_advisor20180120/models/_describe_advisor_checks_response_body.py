# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvisorChecksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeAdvisorChecksResponseBodyData = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeAdvisorChecksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAdvisorChecksResponseBodyData(DaraModel):
    def __init__(
        self,
        advisor_check: List[main_models.DescribeAdvisorChecksResponseBodyDataAdvisorCheck] = None,
    ):
        self.advisor_check = advisor_check

    def validate(self):
        if self.advisor_check:
            for v1 in self.advisor_check:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvisorCheck'] = []
        if self.advisor_check is not None:
            for k1 in self.advisor_check:
                result['AdvisorCheck'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advisor_check = []
        if m.get('AdvisorCheck') is not None:
            for k1 in m.get('AdvisorCheck'):
                temp_model = main_models.DescribeAdvisorChecksResponseBodyDataAdvisorCheck()
                self.advisor_check.append(temp_model.from_map(k1))

        return self

class DescribeAdvisorChecksResponseBodyDataAdvisorCheck(DaraModel):
    def __init__(
        self,
        category: str = None,
        code: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        name: str = None,
        operate_column: str = None,
        product: str = None,
        status: str = None,
        tips: str = None,
        view_column: str = None,
    ):
        self.category = category
        self.code = code
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.name = name
        self.operate_column = operate_column
        self.product = product
        self.status = status
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

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.operate_column is not None:
            result['OperateColumn'] = self.operate_column

        if self.product is not None:
            result['Product'] = self.product

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperateColumn') is not None:
            self.operate_column = m.get('OperateColumn')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('ViewColumn') is not None:
            self.view_column = m.get('ViewColumn')

        return self

