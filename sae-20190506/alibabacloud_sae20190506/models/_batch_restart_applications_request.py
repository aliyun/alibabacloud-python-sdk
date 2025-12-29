# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchRestartApplicationsRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        namespace_id: str = None,
    ):
        # The application IDs. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.app_ids = app_ids
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

