# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeMOTokenUsageDetailResponseBody(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        records: List[main_models.DescribeMOTokenUsageDetailResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.records = records
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeMOTokenUsageDetailResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMOTokenUsageDetailResponseBodyRecords(DaraModel):
    def __init__(
        self,
        consumer_name: str = None,
        instance_id: str = None,
        model: str = None,
        region: str = None,
        request_time: str = None,
        total_tokens: float = None,
    ):
        self.consumer_name = consumer_name
        self.instance_id = instance_id
        self.model = model
        self.region = region
        self.request_time = request_time
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_name is not None:
            result['ConsumerName'] = self.consumer_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.region is not None:
            result['Region'] = self.region

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerName') is not None:
            self.consumer_name = m.get('ConsumerName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

