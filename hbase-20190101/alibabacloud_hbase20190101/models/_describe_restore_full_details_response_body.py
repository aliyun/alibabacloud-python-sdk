# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreFullDetailsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        restore_full: main_models.DescribeRestoreFullDetailsResponseBodyRestoreFull = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The full restoration details.
        self.restore_full = restore_full

    def validate(self):
        if self.restore_full:
            self.restore_full.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_full is not None:
            result['RestoreFull'] = self.restore_full.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreFull') is not None:
            temp_model = main_models.DescribeRestoreFullDetailsResponseBodyRestoreFull()
            self.restore_full = temp_model.from_map(m.get('RestoreFull'))

        return self

class DescribeRestoreFullDetailsResponseBodyRestoreFull(DaraModel):
    def __init__(
        self,
        data_size: str = None,
        fail: int = None,
        page_number: int = None,
        page_size: int = None,
        restore_full_details: main_models.DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails = None,
        speed: str = None,
        succeed: int = None,
        total: int = None,
    ):
        # The total data size.
        self.data_size = data_size
        # The number of failed restorations.
        self.fail = fail
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        self.restore_full_details = restore_full_details
        # The total restoration speed.
        self.speed = speed
        # The number of successful restorations.
        self.succeed = succeed
        # The total number of records.
        self.total = total

    def validate(self):
        if self.restore_full_details:
            self.restore_full_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.restore_full_details is not None:
            result['RestoreFullDetails'] = self.restore_full_details.to_map()

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RestoreFullDetails') is not None:
            temp_model = main_models.DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails()
            self.restore_full_details = temp_model.from_map(m.get('RestoreFullDetails'))

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails(DaraModel):
    def __init__(
        self,
        restore_full_detail: List[main_models.DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail] = None,
    ):
        self.restore_full_detail = restore_full_detail

    def validate(self):
        if self.restore_full_detail:
            for v1 in self.restore_full_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RestoreFullDetail'] = []
        if self.restore_full_detail is not None:
            for k1 in self.restore_full_detail:
                result['RestoreFullDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_full_detail = []
        if m.get('RestoreFullDetail') is not None:
            for k1 in m.get('RestoreFullDetail'):
                temp_model = main_models.DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail()
                self.restore_full_detail.append(temp_model.from_map(k1))

        return self

class DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail(DaraModel):
    def __init__(
        self,
        data_size: str = None,
        end_time: str = None,
        message: str = None,
        process: str = None,
        speed: str = None,
        start_time: str = None,
        state: str = None,
        table: str = None,
    ):
        self.data_size = data_size
        self.end_time = end_time
        self.message = message
        self.process = process
        self.speed = speed
        self.start_time = start_time
        self.state = state
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.message is not None:
            result['Message'] = self.message

        if self.process is not None:
            result['Process'] = self.process

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

