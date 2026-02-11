# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWebhookRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        contact_id: int = None,
        contact_name: str = None,
        http_headers: str = None,
        http_params: str = None,
        method: str = None,
        region_id: str = None,
        url: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.http_headers = http_headers
        self.http_params = http_params
        self.method = method
        # This parameter is required.
        self.region_id = region_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers

        if self.http_params is not None:
            result['HttpParams'] = self.http_params

        if self.method is not None:
            result['Method'] = self.method

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')

        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

