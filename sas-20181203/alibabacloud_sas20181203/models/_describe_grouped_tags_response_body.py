# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupedTagsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        grouped_fileds: List[main_models.DescribeGroupedTagsResponseBodyGroupedFileds] = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is deprecated.
        self.count = count
        # An array that consists of the statistics of the asset tags.
        self.grouped_fileds = grouped_fileds
        # The HTTP status code of the request.
        self.http_status_code = http_status_code
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.grouped_fileds:
            for v1 in self.grouped_fileds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['GroupedFileds'] = []
        if self.grouped_fileds is not None:
            for k1 in self.grouped_fileds:
                result['GroupedFileds'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.grouped_fileds = []
        if m.get('GroupedFileds') is not None:
            for k1 in m.get('GroupedFileds'):
                temp_model = main_models.DescribeGroupedTagsResponseBodyGroupedFileds()
                self.grouped_fileds.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeGroupedTagsResponseBodyGroupedFileds(DaraModel):
    def __init__(
        self,
        count: str = None,
        name: str = None,
        tag_id: int = None,
    ):
        # The number of assets to which the tag is added.
        self.count = count
        # The name of the tag.
        self.name = name
        # The ID of the tag.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

