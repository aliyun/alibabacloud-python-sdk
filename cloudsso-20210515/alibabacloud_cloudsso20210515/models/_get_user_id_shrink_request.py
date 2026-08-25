# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserIdShrinkRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        external_id_shrink: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The identifier information about the user that is synchronized from an external identity provider (IdP).
        self.external_id_shrink = external_id_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.external_id_shrink is not None:
            result['ExternalId'] = self.external_id_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ExternalId') is not None:
            self.external_id_shrink = m.get('ExternalId')

        return self

