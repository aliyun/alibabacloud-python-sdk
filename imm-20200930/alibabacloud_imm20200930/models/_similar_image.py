# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SimilarImage(DaraModel):
    def __init__(
        self,
        image_score: float = None,
        uri: str = None,
    ):
        # The aesthetic score.
        self.image_score = image_score
        # The URI of the image.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_score is not None:
            result['ImageScore'] = self.image_score

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            self.image_score = m.get('ImageScore')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

