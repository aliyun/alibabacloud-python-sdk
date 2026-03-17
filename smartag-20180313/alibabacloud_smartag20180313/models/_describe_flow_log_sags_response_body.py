# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowLogSagsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sags: main_models.DescribeFlowLogSagsResponseBodySags = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.sags = sags
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.sags:
            self.sags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sags is not None:
            result['Sags'] = self.sags.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sags') is not None:
            temp_model = main_models.DescribeFlowLogSagsResponseBodySags()
            self.sags = temp_model.from_map(m.get('Sags'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFlowLogSagsResponseBodySags(DaraModel):
    def __init__(
        self,
        sag: List[main_models.DescribeFlowLogSagsResponseBodySagsSag] = None,
    ):
        self.sag = sag

    def validate(self):
        if self.sag:
            for v1 in self.sag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sag'] = []
        if self.sag is not None:
            for k1 in self.sag:
                result['Sag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sag = []
        if m.get('Sag') is not None:
            for k1 in m.get('Sag'):
                temp_model = main_models.DescribeFlowLogSagsResponseBodySagsSag()
                self.sag.append(temp_model.from_map(k1))

        return self

class DescribeFlowLogSagsResponseBodySagsSag(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        smart_agid: str = None,
    ):
        self.description = description
        self.name = name
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

