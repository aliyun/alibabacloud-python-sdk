# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAnchorRequest(DaraModel):
    def __init__(
        self,
        anchor_category: str = None,
        anchor_id: str = None,
        anchor_type: str = None,
        cover_rate: str = None,
        digital_human_type: str = None,
        page_number: int = None,
        page_size: int = None,
        res_spec_type: str = None,
        use_scene: str = None,
    ):
        self.anchor_category = anchor_category
        self.anchor_id = anchor_id
        self.anchor_type = anchor_type
        self.cover_rate = cover_rate
        self.digital_human_type = digital_human_type
        self.page_number = page_number
        self.page_size = page_size
        self.res_spec_type = res_spec_type
        self.use_scene = use_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_category is not None:
            result['anchorCategory'] = self.anchor_category

        if self.anchor_id is not None:
            result['anchorId'] = self.anchor_id

        if self.anchor_type is not None:
            result['anchorType'] = self.anchor_type

        if self.cover_rate is not None:
            result['coverRate'] = self.cover_rate

        if self.digital_human_type is not None:
            result['digitalHumanType'] = self.digital_human_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorCategory') is not None:
            self.anchor_category = m.get('anchorCategory')

        if m.get('anchorId') is not None:
            self.anchor_id = m.get('anchorId')

        if m.get('anchorType') is not None:
            self.anchor_type = m.get('anchorType')

        if m.get('coverRate') is not None:
            self.cover_rate = m.get('coverRate')

        if m.get('digitalHumanType') is not None:
            self.digital_human_type = m.get('digitalHumanType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        return self

