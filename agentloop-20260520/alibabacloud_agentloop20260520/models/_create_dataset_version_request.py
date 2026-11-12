# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetVersionRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        version: str = None,
        client_token: str = None,
    ):
        # The description of the version. This parameter is optional. If this parameter is not specified, an empty string is used.
        self.description = description
        # The name of the version to be created, which is used to identify the version within the current dataset. The name cannot be empty after leading and trailing whitespaces are removed. The length of the UTF-8 encoded name cannot exceed 128 bytes, and the name cannot contain forward slashes (/).
        # 
        # This parameter is required.
        self.version = version
        # The optional client token that is generated and passed by the client. Do not use this token to determine whether the version is created. You can call ListDatasetVersions to query the version.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.version is not None:
            result['version'] = self.version

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

