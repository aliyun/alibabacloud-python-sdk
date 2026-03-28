# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRuntimeRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        auto_update_image: bool = None,
        run_timeout: int = None,
        version: str = None,
        workspace_id: str = None,
    ):
        # Runtime operation. Valid values:
        # 
        # *   Start: Startup runtime
        # *   Stop: Stop runtime
        self.action = action
        self.auto_update_image = auto_update_image
        # Timeout in seconds for a single test executed on the runtime.
        self.run_timeout = run_timeout
        # Runtime image version.
        self.version = version
        # The ID of the DataWorks workspace. To obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.auto_update_image is not None:
            result['AutoUpdateImage'] = self.auto_update_image

        if self.run_timeout is not None:
            result['RunTimeout'] = self.run_timeout

        if self.version is not None:
            result['Version'] = self.version

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('AutoUpdateImage') is not None:
            self.auto_update_image = m.get('AutoUpdateImage')

        if m.get('RunTimeout') is not None:
            self.run_timeout = m.get('RunTimeout')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

