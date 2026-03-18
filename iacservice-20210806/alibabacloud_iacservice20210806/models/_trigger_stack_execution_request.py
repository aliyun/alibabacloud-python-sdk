# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TriggerStackExecutionRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        changed_folders: List[str] = None,
        client_token: str = None,
        code_package_path: str = None,
        code_version_id: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.changed_folders = changed_folders
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.code_package_path = code_package_path
        self.code_version_id = code_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.changed_folders is not None:
            result['changedFolders'] = self.changed_folders

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.code_package_path is not None:
            result['codePackagePath'] = self.code_package_path

        if self.code_version_id is not None:
            result['codeVersionId'] = self.code_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('changedFolders') is not None:
            self.changed_folders = m.get('changedFolders')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('codePackagePath') is not None:
            self.code_package_path = m.get('codePackagePath')

        if m.get('codeVersionId') is not None:
            self.code_version_id = m.get('codeVersionId')

        return self

