# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAICImagesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        image_type: str = None,
        image_url: str = None,
        max_date: str = None,
        min_date: str = None,
        page_number: str = None,
        page_size: str = None,
        status: str = None,
    ):
        # The description of the image.
        self.description = description
        # The ID of the Android in Container (AIC) image.
        self.image_id = image_id
        # The image type. Valid values:
        # 
        # - **public**: public image.
        # 
        # - **private**: custom image.
        self.image_type = image_type
        # The URL of the AIC image repository.
        self.image_url = image_url
        # The end time of the query. Format: "2006-01-02". By default, no time limit is applied.
        self.max_date = max_date
        # The start time of the query. Format: "2006-01-02". By default, no time limit is applied.
        self.min_date = min_date
        # The page number. The value starts from **1**.
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for paging. Maximum value: **100**.
        # Default value: **10**.
        self.page_size = page_size
        # The image status. Valid values:
        # 
        # - **verifying**: pending verification.
        # 
        # - **disable**: unavailable.
        # 
        # - **available**: available.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.max_date is not None:
            result['MaxDate'] = self.max_date

        if self.min_date is not None:
            result['MinDate'] = self.min_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')

        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

