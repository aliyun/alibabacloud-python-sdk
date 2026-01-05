# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListTagOptionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_option_details: List[main_models.ListTagOptionsResponseBodyTagOptionDetails] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the details of the tag option.
        self.tag_option_details = tag_option_details
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tag_option_details:
            for v1 in self.tag_option_details:
                 if v1:
                    v1.validate()

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

        result['TagOptionDetails'] = []
        if self.tag_option_details is not None:
            for k1 in self.tag_option_details:
                result['TagOptionDetails'].append(k1.to_map() if k1 else None)

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

        self.tag_option_details = []
        if m.get('TagOptionDetails') is not None:
            for k1 in m.get('TagOptionDetails'):
                temp_model = main_models.ListTagOptionsResponseBodyTagOptionDetails()
                self.tag_option_details.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTagOptionsResponseBodyTagOptionDetails(DaraModel):
    def __init__(
        self,
        active: bool = None,
        key: str = None,
        owner: str = None,
        tag_option_id: str = None,
        value: str = None,
    ):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.active = active
        # The key of the tag option.
        self.key = key
        # The ID of the Alibaba Cloud account to which the tag option belongs.
        self.owner = owner
        # The ID of the tag option.
        self.tag_option_id = tag_option_id
        # The value of the tag option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.key is not None:
            result['Key'] = self.key

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

