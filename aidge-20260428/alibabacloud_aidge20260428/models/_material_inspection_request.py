# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MaterialInspectionRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        image_refer: str = None,
        image_url: str = None,
        req_id: str = None,
        rules: str = None,
    ):
        self.api_id = api_id
        self.image_refer = image_refer
        # This parameter is required.
        self.image_url = image_url
        self.req_id = req_id
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.image_refer is not None:
            result['ImageRefer'] = self.image_refer

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ImageRefer') is not None:
            self.image_refer = m.get('ImageRefer')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

