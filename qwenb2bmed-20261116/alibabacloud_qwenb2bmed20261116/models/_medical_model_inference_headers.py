# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class MedicalModelInferenceHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_gwaccess: str = None,
        x_gwnonce: str = None,
        x_gwprotocol: str = None,
        x_gwsignature: str = None,
        x_gwtimestamp: str = None,
        x_request_id: str = None,
    ):
        self.common_headers = common_headers
        # The business AccessKey ID.
        # 
        # This parameter is required.
        self.x_gwaccess = x_gwaccess
        # The random string for the current request.
        # 
        # This parameter is required.
        self.x_gwnonce = x_gwnonce
        # The format of the request and response fields.
        self.x_gwprotocol = x_gwprotocol
        # The business request signature.
        # 
        # This parameter is required.
        self.x_gwsignature = x_gwsignature
        # The request timestamp in milliseconds.
        # 
        # This parameter is required.
        self.x_gwtimestamp = x_gwtimestamp
        # The business request ID.
        # 
        # This parameter is required.
        self.x_request_id = x_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_gwaccess is not None:
            result['X-GW-Access'] = self.x_gwaccess

        if self.x_gwnonce is not None:
            result['X-GW-Nonce'] = self.x_gwnonce

        if self.x_gwprotocol is not None:
            result['X-GW-Protocol'] = self.x_gwprotocol

        if self.x_gwsignature is not None:
            result['X-GW-Signature'] = self.x_gwsignature

        if self.x_gwtimestamp is not None:
            result['X-GW-Timestamp'] = self.x_gwtimestamp

        if self.x_request_id is not None:
            result['X-Request-Id'] = self.x_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('X-GW-Access') is not None:
            self.x_gwaccess = m.get('X-GW-Access')

        if m.get('X-GW-Nonce') is not None:
            self.x_gwnonce = m.get('X-GW-Nonce')

        if m.get('X-GW-Protocol') is not None:
            self.x_gwprotocol = m.get('X-GW-Protocol')

        if m.get('X-GW-Signature') is not None:
            self.x_gwsignature = m.get('X-GW-Signature')

        if m.get('X-GW-Timestamp') is not None:
            self.x_gwtimestamp = m.get('X-GW-Timestamp')

        if m.get('X-Request-Id') is not None:
            self.x_request_id = m.get('X-Request-Id')

        return self

