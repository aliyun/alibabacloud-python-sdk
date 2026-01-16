# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryReceiverDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_schema: str = None,
        next_start: str = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryReceiverDetailResponseBodyData = None,
    ):
        # Field name for the Data of recipients
        self.data_schema = data_schema
        # Used for pagination. If there are more results, set this returned value to the NextStart in the next request.
        self.next_start = next_start
        # Request ID
        self.request_id = request_id
        # Total count (deprecated field, kept for historical compatibility)
        self.total_count = total_count
        # Detailed information
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_schema is not None:
            result['DataSchema'] = self.data_schema

        if self.next_start is not None:
            result['NextStart'] = self.next_start

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSchema') is not None:
            self.data_schema = m.get('DataSchema')

        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryReceiverDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryReceiverDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        detail: List[main_models.QueryReceiverDetailResponseBodyDataDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['detail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k1 in m.get('detail'):
                temp_model = main_models.QueryReceiverDetailResponseBodyDataDetail()
                self.detail.append(temp_model.from_map(k1))

        return self

class QueryReceiverDetailResponseBodyDataDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data: str = None,
        email: str = None,
        utc_create_time: int = None,
    ):
        # Creation Time
        self.create_time = create_time
        # Content
        self.data = data
        # Recipient address
        self.email = email
        # Creation time in UTC format
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data is not None:
            result['Data'] = self.data

        if self.email is not None:
            result['Email'] = self.email

        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')

        return self

