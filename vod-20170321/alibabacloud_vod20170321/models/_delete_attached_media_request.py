# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAttachedMediaRequest(DaraModel):
    def __init__(
        self,
        media_ids: str = None,
    ):
        # The ID of the auxiliary media asset that you want to delete.
        # 
        # *   Separate multiple IDs with commas (,). You can specify up to 20 IDs.
        # *   You can obtain the ID from the response to the [CreateUploadAttachedMedia](~~CreateUploadAttachedMedia~~) operation that you call to obtain the upload URL and credential.
        # 
        # This parameter is required.
        self.media_ids = media_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        return self

