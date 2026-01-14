# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CountTextRequest(DaraModel):
    def __init__(
        self,
        generation_source: str = None,
        industry: str = None,
        publish_status: str = None,
        style: str = None,
    ):
        # API
        self.generation_source = generation_source
        self.industry = industry
        self.publish_status = publish_status
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generation_source is not None:
            result['generationSource'] = self.generation_source

        if self.industry is not None:
            result['industry'] = self.industry

        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationSource') is not None:
            self.generation_source = m.get('generationSource')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

