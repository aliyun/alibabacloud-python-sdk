# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListDDoSInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_info: List[main_models.ListDDoSInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.instance_info = instance_info
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.instance_info:
            for v1 in self.instance_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k1 in self.instance_info:
                result['InstanceInfo'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k1 in m.get('InstanceInfo'):
                temp_model = main_models.ListDDoSInstancesResponseBodyInstanceInfo()
                self.instance_info.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListDDoSInstancesResponseBodyInstanceInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        ddo_sburstable_domestic_protection: str = None,
        ddo_sburstable_overseas_protection: str = None,
        instance_id: str = None,
        reserve_release_time: str = None,
        site_instance_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.ddo_sburstable_domestic_protection = ddo_sburstable_domestic_protection
        self.ddo_sburstable_overseas_protection = ddo_sburstable_overseas_protection
        self.instance_id = instance_id
        self.reserve_release_time = reserve_release_time
        self.site_instance_id = site_instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ddo_sburstable_domestic_protection is not None:
            result['DDoSBurstableDomesticProtection'] = self.ddo_sburstable_domestic_protection

        if self.ddo_sburstable_overseas_protection is not None:
            result['DDoSBurstableOverseasProtection'] = self.ddo_sburstable_overseas_protection

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reserve_release_time is not None:
            result['ReserveReleaseTime'] = self.reserve_release_time

        if self.site_instance_id is not None:
            result['SiteInstanceId'] = self.site_instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DDoSBurstableDomesticProtection') is not None:
            self.ddo_sburstable_domestic_protection = m.get('DDoSBurstableDomesticProtection')

        if m.get('DDoSBurstableOverseasProtection') is not None:
            self.ddo_sburstable_overseas_protection = m.get('DDoSBurstableOverseasProtection')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReserveReleaseTime') is not None:
            self.reserve_release_time = m.get('ReserveReleaseTime')

        if m.get('SiteInstanceId') is not None:
            self.site_instance_id = m.get('SiteInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

