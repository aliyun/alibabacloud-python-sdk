# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreSchemaDetailsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        restore_schema: main_models.DescribeRestoreSchemaDetailsResponseBodyRestoreSchema = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The schema restoration details.
        self.restore_schema = restore_schema

    def validate(self):
        if self.restore_schema:
            self.restore_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_schema is not None:
            result['RestoreSchema'] = self.restore_schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreSchema') is not None:
            temp_model = main_models.DescribeRestoreSchemaDetailsResponseBodyRestoreSchema()
            self.restore_schema = temp_model.from_map(m.get('RestoreSchema'))

        return self

class DescribeRestoreSchemaDetailsResponseBodyRestoreSchema(DaraModel):
    def __init__(
        self,
        fail: int = None,
        page_number: int = None,
        page_size: int = None,
        restore_schema_details: main_models.DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails = None,
        succeed: int = None,
        total: int = None,
    ):
        # The number of failed restorations.
        self.fail = fail
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        self.restore_schema_details = restore_schema_details
        # The number of successful restorations.
        self.succeed = succeed
        # The total number of records.
        self.total = total

    def validate(self):
        if self.restore_schema_details:
            self.restore_schema_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail is not None:
            result['Fail'] = self.fail

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.restore_schema_details is not None:
            result['RestoreSchemaDetails'] = self.restore_schema_details.to_map()

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RestoreSchemaDetails') is not None:
            temp_model = main_models.DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails()
            self.restore_schema_details = temp_model.from_map(m.get('RestoreSchemaDetails'))

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails(DaraModel):
    def __init__(
        self,
        restore_schema_detail: List[main_models.DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail] = None,
    ):
        self.restore_schema_detail = restore_schema_detail

    def validate(self):
        if self.restore_schema_detail:
            for v1 in self.restore_schema_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RestoreSchemaDetail'] = []
        if self.restore_schema_detail is not None:
            for k1 in self.restore_schema_detail:
                result['RestoreSchemaDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_schema_detail = []
        if m.get('RestoreSchemaDetail') is not None:
            for k1 in m.get('RestoreSchemaDetail'):
                temp_model = main_models.DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail()
                self.restore_schema_detail.append(temp_model.from_map(k1))

        return self

class DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        message: str = None,
        start_time: str = None,
        state: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.message = message
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.message is not None:
            result['Message'] = self.message

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

