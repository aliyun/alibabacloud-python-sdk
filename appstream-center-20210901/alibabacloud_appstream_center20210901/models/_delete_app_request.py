# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
    ):
        # The ID of the application to be deleted. **This parameter is required**, and the application must belong to the current account. You must dissociate image references from the target application or version before deletion.
        self.app_id = app_id
        # The ID of the application version to be deleted. If specified, only the adapters corresponding to this application version are deleted. If omitted, the entire application and its adapters are deleted. If the application has no other adapters after the version is deleted, the application record is also deleted.
        self.app_version_id = app_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        return self

