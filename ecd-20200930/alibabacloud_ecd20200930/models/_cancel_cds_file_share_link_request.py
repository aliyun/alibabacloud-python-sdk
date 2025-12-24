# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelCdsFileShareLinkRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        share_id: str = None,
    ):
        # The ID of the cloud disk.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the file sharing task.
        # 
        # This parameter is required.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.share_id is not None:
            result['ShareId'] = self.share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('ShareId') is not None:
            self.share_id = m.get('ShareId')

        return self

