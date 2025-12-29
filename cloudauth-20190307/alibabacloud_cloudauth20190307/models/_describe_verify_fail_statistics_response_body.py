# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyFailStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyFailStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Authentication result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyFailStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyFailStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        column: main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectColumn = None,
        line: main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectLine = None,
    ):
        # Line chart of failure reasons.
        self.column = column
        # Bar chart of failure reasons.
        self.line = line

    def validate(self):
        if self.column:
            self.column.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column.to_map()

        if self.line is not None:
            result['Line'] = self.line.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            temp_model = main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectColumn()
            self.column = temp_model.from_map(m.get('Column'))

        if m.get('Line') is not None:
            temp_model = main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectLine()
            self.line = temp_model.from_map(m.get('Line'))

        return self

class DescribeVerifyFailStatisticsResponseBodyResultObjectLine(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectLineItems] = None,
        total_count: int = None,
    ):
        # Column information.
        self.items = items
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectLineItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVerifyFailStatisticsResponseBodyResultObjectLineItems(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectLineItemsData] = None,
    ):
        # Error code.
        self.code = code
        # Returned quantity data.
        self.data = data

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectLineItemsData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeVerifyFailStatisticsResponseBodyResultObjectLineItemsData(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        date: str = None,
    ):
        # Error code.
        self.code = code
        # Count.
        self.count = count
        # Date.
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.date is not None:
            result['Date'] = self.date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        return self

class DescribeVerifyFailStatisticsResponseBodyResultObjectColumn(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectColumnItems] = None,
        total_count: int = None,
    ):
        # Column information.
        self.items = items
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifyFailStatisticsResponseBodyResultObjectColumnItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVerifyFailStatisticsResponseBodyResultObjectColumnItems(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        rate: str = None,
    ):
        # Error code.
        self.code = code
        # Failure count.
        self.count = count
        # Date: Date
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.rate is not None:
            result['Rate'] = self.rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        return self

