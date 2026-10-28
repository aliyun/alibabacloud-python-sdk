# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaTemplateServiceStatusRequest(DaraModel):
    def __init__(
        self,
        resource_directory_id: str = None,
    ):
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        return self

