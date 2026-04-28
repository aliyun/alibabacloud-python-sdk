# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvicesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAdvicesResponseBodyData = None,
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
            temp_model = main_models.DescribeAdvicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAdvicesResponseBodyData(DaraModel):
    def __init__(
        self,
        advice: List[main_models.DescribeAdvicesResponseBodyDataAdvice] = None,
    ):
        self.advice = advice

    def validate(self):
        if self.advice:
            for v1 in self.advice:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Advice'] = []
        if self.advice is not None:
            for k1 in self.advice:
                result['Advice'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advice = []
        if m.get('Advice') is not None:
            for k1 in m.get('Advice'):
                temp_model = main_models.DescribeAdvicesResponseBodyDataAdvice()
                self.advice.append(temp_model.from_map(k1))

        return self

class DescribeAdvicesResponseBodyDataAdvice(DaraModel):
    def __init__(
        self,
        aliyun_id: int = None,
        check_id: str = None,
        check_name: str = None,
        check_plan_id: int = None,
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
        self.check_plan_id = check_plan_id
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

        if self.check_plan_id is not None:
            result['CheckPlanId'] = self.check_plan_id

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

        if m.get('CheckPlanId') is not None:
            self.check_plan_id = m.get('CheckPlanId')

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

