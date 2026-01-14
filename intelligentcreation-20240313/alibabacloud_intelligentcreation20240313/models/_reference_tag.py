# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReferenceTag(DaraModel):
    def __init__(
        self,
        reference_content: str = None,
        reference_title: str = None,
    ):
        self.reference_content = reference_content
        self.reference_title = reference_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference_content is not None:
            result['referenceContent'] = self.reference_content

        if self.reference_title is not None:
            result['referenceTitle'] = self.reference_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referenceContent') is not None:
            self.reference_content = m.get('referenceContent')

        if m.get('referenceTitle') is not None:
            self.reference_title = m.get('referenceTitle')

        return self

