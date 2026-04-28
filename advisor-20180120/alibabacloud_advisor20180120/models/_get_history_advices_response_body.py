# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class GetHistoryAdvicesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetHistoryAdvicesResponseBodyData = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetHistoryAdvicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHistoryAdvicesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        result: List[main_models.GetHistoryAdvicesResponseBodyDataResult] = None,
        total: int = None,
    ):
        self.page_no = page_no
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

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetHistoryAdvicesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetHistoryAdvicesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        check_name: str = None,
        description: str = None,
        gmt_created: str = None,
        product: str = None,
        resource_id: str = None,
        severity: int = None,
        url: str = None,
    ):
        self.check_id = check_id
        self.check_name = check_name
        self.description = description
        self.gmt_created = gmt_created
        self.product = product
        self.resource_id = resource_id
        self.severity = severity
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.product is not None:
            result['Product'] = self.product

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

