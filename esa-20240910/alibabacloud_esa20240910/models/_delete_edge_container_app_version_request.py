# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEdgeContainerAppVersionRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        version_id: str = None,
    ):
        # The application ID, which can be obtained by calling the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the version that you want to delete. To obtain the version ID, call the [ListEdgeContainerAppVersions](~~ListEdgeContainerAppVersions~~) operation.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

