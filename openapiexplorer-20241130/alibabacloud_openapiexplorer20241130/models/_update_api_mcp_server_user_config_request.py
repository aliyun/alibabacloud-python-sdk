# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateApiMcpServerUserConfigRequest(DaraModel):
    def __init__(
        self,
        enable_public_access: bool = None,
        vpc_whitelists: List[str] = None,
    ):
        self.enable_public_access = enable_public_access
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_public_access is not None:
            result['enablePublicAccess'] = self.enable_public_access

        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enablePublicAccess') is not None:
            self.enable_public_access = m.get('enablePublicAccess')

        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')

        return self

