# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSuspEventUserSettingRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        levels_on: str = None,
        resource_directory_account_id: int = None,
    ):
        # The data source of the exception. Set the value to sas.
        self.from_ = from_
        # The severities of alert notifications. Valid values:
        # 
        # *   **remind**
        # *   **suspicious**
        # *   **serious**
        self.levels_on = levels_on
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self

