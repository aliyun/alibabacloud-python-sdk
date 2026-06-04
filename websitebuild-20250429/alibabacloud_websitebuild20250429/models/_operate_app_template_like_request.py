# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateAppTemplateLikeRequest(DaraModel):
    def __init__(
        self,
        liked: bool = None,
        template_id: str = None,
    ):
        self.liked = liked
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.liked is not None:
            result['Liked'] = self.liked

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

