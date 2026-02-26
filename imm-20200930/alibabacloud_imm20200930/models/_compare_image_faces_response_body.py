# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareImageFacesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        similarity: float = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The face similarity. A larger value indicates a higher face similarity. Valid values: 0 to 1.
        self.similarity = similarity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

