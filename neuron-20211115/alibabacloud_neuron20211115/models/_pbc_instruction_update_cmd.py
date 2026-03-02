# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcInstructionUpdateCmd(DaraModel):
    def __init__(
        self,
        document: str = None,
        pbc_version_id: int = None,
    ):
        self.document = document
        self.pbc_version_id = pbc_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document

        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        return self

