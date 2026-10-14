# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SignUserImageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        image_url: str = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The URL of the image to be signed. HTTP/HTTPS URLs are supported. Specify either `ImageUrl` or `ObjectKey`. At least one of them is required.
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

