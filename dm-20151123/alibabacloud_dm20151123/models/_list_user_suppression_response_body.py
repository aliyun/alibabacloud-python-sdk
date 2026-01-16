# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class ListUserSuppressionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListUserSuppressionResponseBodyData = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Returned results.
        self.data = data
        # Page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Data') is not None:
            temp_model = main_models.ListUserSuppressionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserSuppressionResponseBodyData(DaraModel):
    def __init__(
        self,
        user_suppressions: List[main_models.ListUserSuppressionResponseBodyDataUserSuppressions] = None,
    ):
        self.user_suppressions = user_suppressions

    def validate(self):
        if self.user_suppressions:
            for v1 in self.user_suppressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserSuppressions'] = []
        if self.user_suppressions is not None:
            for k1 in self.user_suppressions:
                result['UserSuppressions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_suppressions = []
        if m.get('UserSuppressions') is not None:
            for k1 in m.get('UserSuppressions'):
                temp_model = main_models.ListUserSuppressionResponseBodyDataUserSuppressions()
                self.user_suppressions.append(temp_model.from_map(k1))

        return self

class ListUserSuppressionResponseBodyDataUserSuppressions(DaraModel):
    def __init__(
        self,
        address: str = None,
        create_time: int = None,
        last_bounce_time: int = None,
        suppression_id: int = None,
        type: str = None,
    ):
        # Email address or domain name
        self.address = address
        # Creation time, timestamp, accurate to the second.
        self.create_time = create_time
        # Last bounce hit time, timestamp, accurate to the second.
        self.last_bounce_time = last_bounce_time
        # Invalid address ID
        self.suppression_id = suppression_id
        # Source of entry, invalid address type
        # - system
        # - user
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_bounce_time is not None:
            result['LastBounceTime'] = self.last_bounce_time

        if self.suppression_id is not None:
            result['SuppressionId'] = self.suppression_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastBounceTime') is not None:
            self.last_bounce_time = m.get('LastBounceTime')

        if m.get('SuppressionId') is not None:
            self.suppression_id = m.get('SuppressionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

