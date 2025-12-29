# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchStopApplicationsRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        namespace_id: str = None,
        version: str = None,
    ):
        # The ID of the application that you want to stop.
        # 
        # > If you want to stop multiple applications at the same time, separate the IDs with commas (,).
        self.app_ids = app_ids
        # ebf491f0-c1a5-45e2-b2c4-710dbe2a\\*\\*\\*\\*,ebf491f0-c1a5-45e2-b2c4-71025e2a\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The application version.
        self.version = version

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

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

