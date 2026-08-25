# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeVSwitchesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeVSwitchesResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The result list.
        self.items = items
        # The number of entries per page for a paged query.
        self.max_results = max_results
        # The token for the next query. An empty value of NextToken indicates that no more results exist.
        self.next_token = next_token
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVSwitchesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeVSwitchesResponseBodyItems(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        v_switch_name: str = None,
        zone_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The vSwitch name.
        self.v_switch_name = v_switch_name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

