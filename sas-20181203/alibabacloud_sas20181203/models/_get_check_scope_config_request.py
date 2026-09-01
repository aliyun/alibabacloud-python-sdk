# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCheckScopeConfigRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        resource_directory_account_id: int = None,
    ):
        # The ID of the configuration. This parameter is optional. If you do not specify this parameter, a default ID is generated.
        self.config_id = config_id
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self

