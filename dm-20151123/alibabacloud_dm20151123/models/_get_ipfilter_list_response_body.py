# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class GetIpfilterListResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.GetIpfilterListResponseBodyData = None,
    ):
        # Current page number
        self.page_number = page_number
        # Number of items per page
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Data records
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.GetIpfilterListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class GetIpfilterListResponseBodyData(DaraModel):
    def __init__(
        self,
        ipfilters: List[main_models.GetIpfilterListResponseBodyDataIpfilters] = None,
    ):
        self.ipfilters = ipfilters

    def validate(self):
        if self.ipfilters:
            for v1 in self.ipfilters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ipfilters'] = []
        if self.ipfilters is not None:
            for k1 in self.ipfilters:
                result['ipfilters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipfilters = []
        if m.get('ipfilters') is not None:
            for k1 in m.get('ipfilters'):
                temp_model = main_models.GetIpfilterListResponseBodyDataIpfilters()
                self.ipfilters.append(temp_model.from_map(k1))

        return self

class GetIpfilterListResponseBodyDataIpfilters(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        ip_address: str = None,
    ):
        # timestamp
        self.create_time = create_time
        # Record ID
        self.id = id
        # IP address/IP range/IP segment
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

