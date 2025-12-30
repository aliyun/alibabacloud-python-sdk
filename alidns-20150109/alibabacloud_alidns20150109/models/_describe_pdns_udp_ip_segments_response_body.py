# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsUdpIpSegmentsResponseBody(DaraModel):
    def __init__(
        self,
        ip_segments: List[main_models.DescribePdnsUdpIpSegmentsResponseBodyIpSegments] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_pages: str = None,
    ):
        self.ip_segments = ip_segments
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_pages = total_pages

    def validate(self):
        if self.ip_segments:
            for v1 in self.ip_segments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpSegments'] = []
        if self.ip_segments is not None:
            for k1 in self.ip_segments:
                result['IpSegments'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_segments = []
        if m.get('IpSegments') is not None:
            for k1 in m.get('IpSegments'):
                temp_model = main_models.DescribePdnsUdpIpSegmentsResponseBodyIpSegments()
                self.ip_segments.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribePdnsUdpIpSegmentsResponseBodyIpSegments(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        create_timestamp: int = None,
        id: str = None,
        ip: str = None,
        mask: int = None,
        name: str = None,
        secret_key: str = None,
        state: str = None,
        update_date: str = None,
    ):
        self.create_date = create_date
        self.create_timestamp = create_timestamp
        self.id = id
        self.ip = ip
        self.mask = mask
        self.name = name
        self.secret_key = secret_key
        self.state = state
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.name is not None:
            result['Name'] = self.name

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.state is not None:
            result['State'] = self.state

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

