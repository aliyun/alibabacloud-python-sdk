# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeUsedServiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        records: List[main_models.DescribeUsedServiceResponseBodyRecords] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Record details
        self.records = records

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.DescribeUsedServiceResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class DescribeUsedServiceResponseBodyRecords(DaraModel):
    def __init__(
        self,
        en_name: str = None,
        name: str = None,
        service_code: str = None,
    ):
        # English name
        self.en_name = en_name
        # Service name
        self.name = name
        # Service code
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.en_name is not None:
            result['enName'] = self.en_name

        if self.name is not None:
            result['name'] = self.name

        if self.service_code is not None:
            result['serviceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enName') is not None:
            self.en_name = m.get('enName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')

        return self

