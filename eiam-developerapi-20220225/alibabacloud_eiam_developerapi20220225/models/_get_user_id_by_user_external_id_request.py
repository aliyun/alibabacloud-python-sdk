# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserIdByUserExternalIdRequest(DaraModel):
    def __init__(
        self,
        user_external_id: str = None,
        user_source_id: str = None,
        user_source_type: str = None,
    ):
        # The external ID of the account.
        # 
        # This parameter is required.
        self.user_external_id = user_external_id
        # The source ID of the account. If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        # 
        # This parameter is required.
        self.user_source_id = user_source_id
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in Identity as a Service (IDaaS).
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        # 
        # This parameter is required.
        self.user_source_type = user_source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id

        if self.user_source_id is not None:
            result['userSourceId'] = self.user_source_id

        if self.user_source_type is not None:
            result['userSourceType'] = self.user_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')

        if m.get('userSourceId') is not None:
            self.user_source_id = m.get('userSourceId')

        if m.get('userSourceType') is not None:
            self.user_source_type = m.get('userSourceType')

        return self

