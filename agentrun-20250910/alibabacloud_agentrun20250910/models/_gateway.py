# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Gateway(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        gateway_id: str = None,
        internet_url: str = None,
        intranet_url: str = None,
        name: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.gateway_id = gateway_id
        self.internet_url = internet_url
        self.intranet_url = intranet_url
        self.name = name
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.internet_url is not None:
            result['internetUrl'] = self.internet_url

        if self.intranet_url is not None:
            result['intranetUrl'] = self.intranet_url

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('internetUrl') is not None:
            self.internet_url = m.get('internetUrl')

        if m.get('intranetUrl') is not None:
            self.intranet_url = m.get('intranetUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

