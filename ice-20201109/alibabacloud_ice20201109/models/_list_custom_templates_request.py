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
        # The template name.
        self.name = name
        # The order in which the entries are sorted. Valid values:
        # 
        # *   CreateTimeDesc: sorted by creation time in descending order.
        # *   CreateTimeAsc: sorted by creation time in ascending order.
        self.order_by = order_by
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The subtype ID of the template.
        # 
        # *   Valid values for transcoding templates:
        # 
        #     *   1 (Normal): regular template.
        #     *   2 (AudioTranscode): audio transcoding template.
        #     *   3 (Remux): container format conversion template.
        #     *   4 (NarrowBandV1): Narrowband HD 1.0 template.
        #     *   5 (NarrowBandV2): Narrowband HD 2.0 template.
        # 
        # *   Valid values for snapshot templates:
        # 
        #     *   1 (Normal): regular template.
        #     *   2 (Sprite): sprite template.
        #     *   3 (WebVtt): WebVTT template.
        # 
        # *   Valid values for AI-assisted content moderation templates:
        # 
        #     *   1 (Video): video moderation template.
        #     *   2 (Audio): audio moderation template.
        #     *   3 (Image): image moderation template.
        # 
        # *   Valid values for AI-assisted intelligent erasure templates:
        # 
        #     *   1 (VideoDelogo): logo erasure template.
        #     *   2 (VideoDetext): subtitle erasure template.
        self.subtype = subtype
        # The template ID.
        self.template_id = template_id
        # The template type. Valid values:
        # 
        # *   1: transcoding template.
        # *   2: snapshot template.
        # *   3: animated image template.
        # *   4\\. image watermark template.
        # *   5: text watermark template.
        # *   6: subtitle template.
        # *   7: AI-assisted content moderation template.
        # *   8: AI-assisted intelligent thumbnail template.
        # *   9: AI-assisted intelligent erasure template.
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

