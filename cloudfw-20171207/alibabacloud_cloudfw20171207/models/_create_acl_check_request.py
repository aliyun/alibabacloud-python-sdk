# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAclCheckRequest(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        check_names: List[str] = None,
        lang: str = None,
    ):
        # This parameter is required.
        self.acl_type = acl_type
        self.check_names = check_names
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.check_names is not None:
            result['CheckNames'] = self.check_names

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('CheckNames') is not None:
            self.check_names = m.get('CheckNames')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

