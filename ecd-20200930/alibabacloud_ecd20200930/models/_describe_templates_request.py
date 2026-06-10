# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeTemplatesRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        biz_type: str = None,
        image_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        template_ids: List[str] = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # Region filter for template queries.
        # 
        # > If you set this parameter, results exclude configurations for other regions.
        self.biz_region_id = biz_region_id
        # > This parameter is not available for public use.
        self.biz_type = biz_type
        # Cloud Desktop image ID. You can find this ID on the Image Management page. Supported image types include OS images and custom images.
        self.image_id = image_id
        # Keyword for fuzzy search. Searches template IDs and template names.
        self.keyword = keyword
        # Page number for paged queries.
        self.page_number = page_number
        # Maximum number of entries per page for paged queries.
        self.page_size = page_size
        # Product type. Set this parameter to `CloudDesktop`.
        self.product_type = product_type
        # List of template IDs to query.
        self.template_ids = template_ids
        # Query by template name.
        self.template_name = template_name
        # Template type to query. If you omit this parameter, the system returns all template types.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

