# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvicesFlatPageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAdvicesFlatPageResponseBodyData = None,
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
            temp_model = main_models.DescribeAdvicesFlatPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAdvicesFlatPageResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        result: List[main_models.DescribeAdvicesFlatPageResponseBodyDataResult] = None,
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
                temp_model = main_models.DescribeAdvicesFlatPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAdvicesFlatPageResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        content: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_expired: bool = None,
        product: str = None,
        resource: str = None,
        resource_id: str = None,
        severity: int = None,
    ):
        self.aliyun_id = aliyun_id
        self.check_id = check_id
        self.check_name = check_name
        self.content = content
        self.description = description
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_expired = is_expired
        self.product = product
        self.resource = resource
        self.resource_id = resource_id
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired

        if self.product is not None:
            result['Product'] = self.product

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.severity is not None:
            result['Severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        return self

