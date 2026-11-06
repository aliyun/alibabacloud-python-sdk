# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataProcessJobTemplatesRequest(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30.
        self.page_size = page_size
        # The ID of the region where the template resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The task template ID used for filtering.
        self.template_id = template_id
        # The node templatetype used for filtering. Valid value: image.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

