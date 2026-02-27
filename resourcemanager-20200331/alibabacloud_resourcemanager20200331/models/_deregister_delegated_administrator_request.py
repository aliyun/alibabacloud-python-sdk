# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeregisterDelegatedAdministratorRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        service_principal: str = None,
    ):
        # The ID of the member in the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The identifier of the trusted service.
        # 
        # For more information, see the `Trusted service identifier` column in [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        # 
        # This parameter is required.
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')

        return self

