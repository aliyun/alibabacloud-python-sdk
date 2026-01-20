# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDeviceCodeResponseBody(DaraModel):
    def __init__(
        self,
        device_code: str = None,
        expires_at: int = None,
        expires_in: int = None,
        interval: int = None,
        user_code: str = None,
        verification_uri: str = None,
        verification_uri_complete: str = None,
    ):
        # The device code.
        self.device_code = device_code
        # The time when the token expires. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expires_at = expires_at
        # The remaining validity period of the device code. Unit: seconds.
        self.expires_in = expires_in
        # The timeout period of the request token. Unit: seconds.
        self.interval = interval
        # The user authorization code.
        self.user_code = user_code
        # The verification URI.
        self.verification_uri = verification_uri
        # The complete verification URI.
        self.verification_uri_complete = verification_uri_complete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_code is not None:
            result['device_code'] = self.device_code

        if self.expires_at is not None:
            result['expires_at'] = self.expires_at

        if self.expires_in is not None:
            result['expires_in'] = self.expires_in

        if self.interval is not None:
            result['interval'] = self.interval

        if self.user_code is not None:
            result['user_code'] = self.user_code

        if self.verification_uri is not None:
            result['verification_uri'] = self.verification_uri

        if self.verification_uri_complete is not None:
            result['verification_uri_complete'] = self.verification_uri_complete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('device_code') is not None:
            self.device_code = m.get('device_code')

        if m.get('expires_at') is not None:
            self.expires_at = m.get('expires_at')

        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('user_code') is not None:
            self.user_code = m.get('user_code')

        if m.get('verification_uri') is not None:
            self.verification_uri = m.get('verification_uri')

        if m.get('verification_uri_complete') is not None:
            self.verification_uri_complete = m.get('verification_uri_complete')

        return self

