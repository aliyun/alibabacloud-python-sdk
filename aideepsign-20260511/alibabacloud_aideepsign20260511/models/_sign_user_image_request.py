# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SignUserImageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        image_url: str = None,
        object_key: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. The client generates this value. Make sure the value is unique across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The URL of the image to be signed. HTTP and HTTPS URLs are supported. Specify at least one of `ImageUrl` and `ObjectKey`.
        self.image_url = image_url
        # The ObjectKey of the image to be signed in OSS. When you use `ObjectKey`, make sure the key belongs to the namespace of the current caller. Specify at least one of `ImageUrl` and `ObjectKey`.
        self.object_key = object_key

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

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        return self

