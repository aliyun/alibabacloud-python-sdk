# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDomainRequest(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        fields: str = None,
        get_quota_used: bool = None,
    ):
        # The ID of the domain.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        self.fields = fields
        # Specifies whether to return the used quota of the domain. Default value: false. If the quota of the domain is greater than 0 and you set this parameter to true, the used quota of the domain is returned.
        self.get_quota_used = get_quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.fields is not None:
            result['fields'] = self.fields

        if self.get_quota_used is not None:
            result['get_quota_used'] = self.get_quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('get_quota_used') is not None:
            self.get_quota_used = m.get('get_quota_used')

        return self

