# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateSecurityIPModeResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        request_id: str = None,
        security_ipmode: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The ID of the request.
        self.request_id = request_id
        # The whitelist mode after the change, which is the enhanced whitelist mode.
        # 
        # Valid values:
        # 
        # *   safety
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     enhanced whitelist mode
        # 
        #     <!-- -->
        self.security_ipmode = security_ipmode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_ipmode is not None:
            result['SecurityIPMode'] = self.security_ipmode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIPMode') is not None:
            self.security_ipmode = m.get('SecurityIPMode')

        return self

