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
        recover_body: str = None,
        region_id: str = None,
        url: str = None,
    ):
        # The notification template that is sent when an alert is triggered. This parameter is required if the **Method** parameter is set to **Post**. You can use the $content placeholder to specify the notification content. The content cannot exceed 500 characters in length.
        # 
        # This parameter is required.
        self.body = body
        # The ID of the webhook alert contact. You can call the **SearchAlertContact** operation to obtain the ID.
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # The name of the webhook alert contact.
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # The HTTP request headers.
        self.http_headers = http_headers
        # The parameters in the HTTP request.
        self.http_params = http_params
        # The HTTP request method. Valid values:
        # 
        # *   `Get`
        # *   `Post`
        # 
        # This parameter is required.
        self.method = method
        # The notification template that is sent when an alert is resolved. This parameter is required if the **Method** parameter is set to **Post**. You can use the $content placeholder to specify the notification content. The content cannot exceed 500 characters in length.
        self.recover_body = recover_body
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The URL of the HTTP request method.
        # 
        # This parameter is required.
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

        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body

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

        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

