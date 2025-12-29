# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebAclConfig(DaraModel):
    def __init__(
        self,
        web_acl_entries: List[main_models.WebAclEntryConfig] = None,
    ):
        # This parameter is required.
        self.web_acl_entries = web_acl_entries

    def validate(self):
        if self.web_acl_entries:
            for v1 in self.web_acl_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WebAclEntries'] = []
        if self.web_acl_entries is not None:
            for k1 in self.web_acl_entries:
                result['WebAclEntries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.web_acl_entries = []
        if m.get('WebAclEntries') is not None:
            for k1 in m.get('WebAclEntries'):
                temp_model = main_models.WebAclEntryConfig()
                self.web_acl_entries.append(temp_model.from_map(k1))

        return self

