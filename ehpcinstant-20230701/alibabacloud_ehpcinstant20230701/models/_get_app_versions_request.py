# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppVersionsRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        image_category: str = None,
        image_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The source of the image. Valid values:
        # 
        # Public: public images provided by Alibaba Cloud.
        # 
        # Custom: the custom image that you added.
        self.image_category = image_category
        # The type of the images. Valid values:
        # 
        # VM: Virtual Machine Image
        # 
        # Container: container image
        self.image_type = image_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.image_category is not None:
            result['ImageCategory'] = self.image_category

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

