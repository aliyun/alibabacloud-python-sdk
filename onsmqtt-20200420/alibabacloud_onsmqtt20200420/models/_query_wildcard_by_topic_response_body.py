# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class QueryWildcardByTopicResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryWildcardByTopicResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The dataset of parent topic information.
        self.data = data
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryWildcardByTopicResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryWildcardByTopicResponseBodyData(DaraModel):
    def __init__(
        self,
        limit: str = None,
        total: str = None,
        wildcard_list: List[str] = None,
    ):
        # The maximum number of results returned.
        self.limit = limit
        # The total number of query results.
        self.total = total
        # The wildcard list.
        self.wildcard_list = wildcard_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.total is not None:
            result['Total'] = self.total

        if self.wildcard_list is not None:
            result['WildcardList'] = self.wildcard_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('WildcardList') is not None:
            self.wildcard_list = m.get('WildcardList')

        return self

