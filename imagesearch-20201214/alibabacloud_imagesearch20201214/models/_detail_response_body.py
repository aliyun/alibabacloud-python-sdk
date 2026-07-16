# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class DetailResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.DetailResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The instance information.
        self.instance = instance
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.DetailResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DetailResponseBodyInstance(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        name: str = None,
        qps: int = None,
        region: str = None,
        service_type: int = None,
        total_count: int = None,
        utc_create: str = None,
        utc_expire_time: str = None,
    ):
        # The maximum image capacity of the plan. Unit: 10,000.
        self.capacity = capacity
        # The instance name.
        self.name = name
        # The QPS of the plan.
        self.qps = qps
        # The region information.
        self.region = region
        # The Image Search model.
        # 
        # <props="intl">Valid values: 0: product image search. 1: generic image search.
        # <props="china">Valid values: 0: product image search. 1: generic image search. 2: fabric search. 3 and 7: trademark search. 4: copyright search. 5: furniture search. 6: hardware search..
        self.service_type = service_type
        # The number of images.
        self.total_count = total_count
        # The creation time of the instance. Unit: milliseconds.
        self.utc_create = utc_create
        # The time when the instance expires. Unit: milliseconds.
        self.utc_expire_time = utc_expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.name is not None:
            result['Name'] = self.name

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.region is not None:
            result['Region'] = self.region

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create

        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')

        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')

        return self

