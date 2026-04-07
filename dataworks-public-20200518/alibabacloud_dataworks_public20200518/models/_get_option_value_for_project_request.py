# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOptionValueForProjectRequest(DaraModel):
    def __init__(
        self,
        extension_code: str = None,
        project_id: str = None,
    ):
        # The unique code of the extension.
        self.extension_code = extension_code
        # The workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

