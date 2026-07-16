# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeApiMeteringResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        fatal: bool = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[main_models.DescribeApiMeteringResponseBodyResult] = None,
        success: bool = None,
        version: str = None,
    ):
        self.code = code
        self.count = count
        # fatal
        self.fatal = fatal
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result = result
        self.success = success
        self.version = version

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
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.fatal is not None:
            result['Fatal'] = self.fatal

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Fatal') is not None:
            self.fatal = m.get('Fatal')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeApiMeteringResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeApiMeteringResponseBodyResult(DaraModel):
    def __init__(
        self,
        aliyun_pk: int = None,
        product_code: str = None,
        product_name: str = None,
        total_capacity: int = None,
        total_quota: int = None,
        total_usage: int = None,
        unit: str = None,
    ):
        self.aliyun_pk = aliyun_pk
        self.product_code = product_code
        self.product_name = product_name
        self.total_capacity = total_capacity
        self.total_quota = total_quota
        self.total_usage = total_usage
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

