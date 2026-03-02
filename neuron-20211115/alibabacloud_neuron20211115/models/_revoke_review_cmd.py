# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeReviewCmd(DaraModel):
    def __init__(
        self,
        pbc_version_id: int = None,
    ):
        self.pbc_version_id = pbc_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        return self

