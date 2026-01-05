# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListResourcesForTagOptionResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resource_details: List[main_models.ListResourcesForTagOptionResponseBodyResourceDetails] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page.
        # 
        # Valid values: 1 to 100 Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the associated resources.
        self.resource_details = resource_details
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resource_details:
            for v1 in self.resource_details:
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

        result['ResourceDetails'] = []
        if self.resource_details is not None:
            for k1 in self.resource_details:
                result['ResourceDetails'].append(k1.to_map() if k1 else None)

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

        self.resource_details = []
        if m.get('ResourceDetails') is not None:
            for k1 in m.get('ResourceDetails'):
                temp_model = main_models.ListResourcesForTagOptionResponseBodyResourceDetails()
                self.resource_details.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourcesForTagOptionResponseBodyResourceDetails(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        # The time when the resource was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the resource.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        self.resource_arn = resource_arn
        # The ID of the resource with which the tag option is associated.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

