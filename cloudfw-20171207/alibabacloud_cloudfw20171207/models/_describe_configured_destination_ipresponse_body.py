# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeConfiguredDestinationIPResponseBody(DaraModel):
    def __init__(
        self,
        destinations: List[main_models.DescribeConfiguredDestinationIPResponseBodyDestinations] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.destinations = destinations
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.destinations:
            for v1 in self.destinations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Destinations'] = []
        if self.destinations is not None:
            for k1 in self.destinations:
                result['Destinations'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.destinations = []
        if m.get('Destinations') is not None:
            for k1 in m.get('Destinations'):
                temp_model = main_models.DescribeConfiguredDestinationIPResponseBodyDestinations()
                self.destinations.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeConfiguredDestinationIPResponseBodyDestinations(DaraModel):
    def __init__(
        self,
        comment: str = None,
        destination_ip: str = None,
        destination_isp: str = None,
        destination_region: str = None,
        operation_time: int = None,
    ):
        self.comment = comment
        self.destination_ip = destination_ip
        self.destination_isp = destination_isp
        self.destination_region = destination_region
        self.operation_time = operation_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.destination_ip is not None:
            result['DestinationIP'] = self.destination_ip

        if self.destination_isp is not None:
            result['DestinationISP'] = self.destination_isp

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DestinationIP') is not None:
            self.destination_ip = m.get('DestinationIP')

        if m.get('DestinationISP') is not None:
            self.destination_isp = m.get('DestinationISP')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        return self

