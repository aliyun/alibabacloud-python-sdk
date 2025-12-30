# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteZoneRecordRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
        record_id: int = None,
        user_client_ip: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

