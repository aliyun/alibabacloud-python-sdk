# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class AclConfig(DaraModel):
    def __init__(
        self,
        acl_entries: List[main_models.AclEntryConfig] = None,
    ):
        # This parameter is required.
        self.acl_entries = acl_entries

    def validate(self):
        if self.acl_entries:
            for v1 in self.acl_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['aclEntries'] = []
        if self.acl_entries is not None:
            for k1 in self.acl_entries:
                result['aclEntries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('aclEntries') is not None:
            for k1 in m.get('aclEntries'):
                temp_model = main_models.AclEntryConfig()
                self.acl_entries.append(temp_model.from_map(k1))

        return self

