# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListVersionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListVersionsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
                temp_model = main_models.ListVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        concurrent_count: int = None,
        end_time: str = None,
        instance_count: int = None,
        instance_id: str = None,
        order_id: int = None,
        product_type: str = None,
        quota: int = None,
        start_time: str = None,
        use_quota: int = None,
        version_detail: str = None,
        version_name: str = None,
        version_status: int = None,
    ):
        self.concurrent_count = concurrent_count
        self.end_time = end_time
        self.instance_count = instance_count
        self.instance_id = instance_id
        self.order_id = order_id
        self.product_type = product_type
        self.quota = quota
        self.start_time = start_time
        self.use_quota = use_quota
        self.version_detail = version_detail
        self.version_name = version_name
        self.version_status = version_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrent_count is not None:
            result['ConcurrentCount'] = self.concurrent_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.use_quota is not None:
            result['UseQuota'] = self.use_quota

        if self.version_detail is not None:
            result['VersionDetail'] = self.version_detail

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.version_status is not None:
            result['VersionStatus'] = self.version_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentCount') is not None:
            self.concurrent_count = m.get('ConcurrentCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UseQuota') is not None:
            self.use_quota = m.get('UseQuota')

        if m.get('VersionDetail') is not None:
            self.version_detail = m.get('VersionDetail')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')

        return self

