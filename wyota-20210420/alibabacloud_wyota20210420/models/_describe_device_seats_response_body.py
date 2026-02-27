# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class DescribeDeviceSeatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeDeviceSeatsResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeDeviceSeatsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeviceSeatsResponseBodyData(DaraModel):
    def __init__(
        self,
        seat_col: int = None,
        seat_name: str = None,
        seat_no: str = None,
        seat_row: int = None,
        serial_no: str = None,
        site_id: str = None,
        site_name: str = None,
    ):
        self.seat_col = seat_col
        self.seat_name = seat_name
        self.seat_no = seat_no
        self.seat_row = seat_row
        self.serial_no = serial_no
        self.site_id = site_id
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.seat_col is not None:
            result['SeatCol'] = self.seat_col

        if self.seat_name is not None:
            result['SeatName'] = self.seat_name

        if self.seat_no is not None:
            result['SeatNo'] = self.seat_no

        if self.seat_row is not None:
            result['SeatRow'] = self.seat_row

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeatCol') is not None:
            self.seat_col = m.get('SeatCol')

        if m.get('SeatName') is not None:
            self.seat_name = m.get('SeatName')

        if m.get('SeatNo') is not None:
            self.seat_no = m.get('SeatNo')

        if m.get('SeatRow') is not None:
            self.seat_row = m.get('SeatRow')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        return self

