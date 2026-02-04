# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnUserSecDropByMinuteResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        len: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rows: List[main_models.DescribeDcdnUserSecDropByMinuteResponseBodyRows] = None,
        total_count: int = None,
    ):
        # The description of HTTP responses.
        self.description = description
        # The total number of entries returned.
        self.len = len
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # An array.
        self.rows = rows
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.len is not None:
            result['Len'] = self.len

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['Rows'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Len') is not None:
            self.len = m.get('Len')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rows = []
        if m.get('Rows') is not None:
            for k1 in m.get('Rows'):
                temp_model = main_models.DescribeDcdnUserSecDropByMinuteResponseBodyRows()
                self.rows.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnUserSecDropByMinuteResponseBodyRows(DaraModel):
    def __init__(
        self,
        domain: str = None,
        drops: int = None,
        object: str = None,
        rule_name: str = None,
        sec_func: str = None,
        tm_str: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The number of packets blocked within 5 minutes.
        self.drops = drops
        # The object that triggered rate limiting.
        self.object = object
        # The rule that was triggered.
        self.rule_name = rule_name
        # The security feature that blocked the packets.
        self.sec_func = sec_func
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.tm_str = tm_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.drops is not None:
            result['Drops'] = self.drops

        if self.object is not None:
            result['Object'] = self.object

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func

        if self.tm_str is not None:
            result['TmStr'] = self.tm_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Drops') is not None:
            self.drops = m.get('Drops')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')

        if m.get('TmStr') is not None:
            self.tm_str = m.get('TmStr')

        return self

