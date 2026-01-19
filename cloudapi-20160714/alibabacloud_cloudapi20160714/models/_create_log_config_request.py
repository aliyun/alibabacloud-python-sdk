# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLogConfigRequest(DaraModel):
    def __init__(
        self,
        create_slr: bool = None,
        log_type: str = None,
        security_token: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
    ):
        # Specifies to create a service-linked role.
        self.create_slr = create_slr
        # The log type.
        # 
        # Valid values:
        # 
        # *   PROVIDER
        self.log_type = log_type
        self.security_token = security_token
        # slslogstore
        # 
        # This parameter is required.
        self.sls_log_store = sls_log_store
        # The name of the Log Service project.
        # 
        # This parameter is required.
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_slr is not None:
            result['CreateSlr'] = self.create_slr

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSlr') is not None:
            self.create_slr = m.get('CreateSlr')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        return self

