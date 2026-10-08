# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContactTemplatesRequest(DaraModel):
    def __init__(
        self,
        registrant_profile_ids: str = None,
        user_client_ip: str = None,
    ):
        # The IDs of the contact templates to delete. Separate multiple values with commas (,).
        # 
        # The system automatically generates an ID upon successful creation of a contact template. You can invoke the [QueryRegistrantProfiles](https://help.aliyun.com/document_detail/67701.html) API to query the template IDs.
        # 
        # This parameter is required.
        self.registrant_profile_ids = registrant_profile_ids
        # User IP address. You can set this parameter to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registrant_profile_ids is not None:
            result['RegistrantProfileIds'] = self.registrant_profile_ids

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrantProfileIds') is not None:
            self.registrant_profile_ids = m.get('RegistrantProfileIds')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

