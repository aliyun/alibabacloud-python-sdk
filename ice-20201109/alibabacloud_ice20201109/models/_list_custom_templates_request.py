# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomTemplatesRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        subtype: str = None,
        template_id: str = None,
        type: str = None,
    ):
        # The name of the template.
        self.name = name
        # The sort order of the results. Valid values:
        # 
        # - `CreationTime:Desc`: Sorts the results by Creation Time in descending order.
        # 
        # - `CreationTime:Asc`: Sorts the results by Creation Time in ascending order.
        self.order_by = order_by
        # The page number of the results to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The subtype of the template. This parameter applies only when `Type` is set to 1, 2, 7, or 9.
        # 
        # - Transcoding Template subtypes:
        # 
        #   - 1: Normal (`Normal`)
        # 
        #   - 2: Audio-only (`AudioTranscode`)
        # 
        #   - 3: Remuxing (`Remux`)
        # 
        #   - 4: Narrowband HD 1.0 (`NarrowBandV1`)
        # 
        #   - 5: Narrowband HD 2.0 (`NarrowBandV2`)
        # 
        # - Screenshot Template subtypes:
        # 
        #   - 1: Normal (`Normal`)
        # 
        #   - 2: Sprite Image (`Sprite`)
        # 
        #   - 3: WebVTT (`WebVtt`)
        # 
        # - AI Content Moderation subtypes:
        # 
        #   - 1: Video moderation (`Video`)
        # 
        #   - 2: Audio moderation (`Audio`)
        # 
        #   - 3: Image moderation (`Image`)
        # 
        # - AI-powered Object Removal subtypes:
        # 
        #   - 1: Logo Removal (`VideoDelogo`)
        # 
        #   - 2: Text Removal (`VideoDetext`)
        self.subtype = subtype
        # The ID of the template.
        self.template_id = template_id
        # The type of the template. Valid values:
        # 
        # - 1: Transcoding Template
        # 
        # - 2: Screenshot Template
        # 
        # - 3: Animated GIF Template
        # 
        # - 4: Image Watermark Template
        # 
        # - 5: Text Watermark Template
        # 
        # - 6: Subtitle Template
        # 
        # - 7: AI Content Moderation
        # 
        # - 8: AI-powered Smart Cover
        # 
        # - 9: AI-powered Object Removal
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

