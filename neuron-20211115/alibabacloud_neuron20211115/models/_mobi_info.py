# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MobiInfo(DaraModel):
    def __init__(
        self,
        mobi_commit_id: str = None,
        mobi_id: int = None,
        mobi_module_id: str = None,
        store_url: str = None,
    ):
        self.mobi_commit_id = mobi_commit_id
        self.mobi_id = mobi_id
        self.mobi_module_id = mobi_module_id
        self.store_url = store_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobi_commit_id is not None:
            result['mobiCommitId'] = self.mobi_commit_id

        if self.mobi_id is not None:
            result['mobiId'] = self.mobi_id

        if self.mobi_module_id is not None:
            result['mobiModuleId'] = self.mobi_module_id

        if self.store_url is not None:
            result['storeUrl'] = self.store_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobiCommitId') is not None:
            self.mobi_commit_id = m.get('mobiCommitId')

        if m.get('mobiId') is not None:
            self.mobi_id = m.get('mobiId')

        if m.get('mobiModuleId') is not None:
            self.mobi_module_id = m.get('mobiModuleId')

        if m.get('storeUrl') is not None:
            self.store_url = m.get('storeUrl')

        return self

