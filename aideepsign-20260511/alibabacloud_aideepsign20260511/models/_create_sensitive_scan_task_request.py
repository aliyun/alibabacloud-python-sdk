# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSensitiveScanTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        image_url: str = None,
        object_key: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The URL of the image to scan. Only HTTP and HTTPS protocols are supported. The image size cannot exceed 10 MB. You must specify at least one of ImageUrl and ObjectKey.
        self.image_url = image_url
        # The ObjectKey of the image to scan in OSS. When you use ObjectKey, make sure that the key belongs to the namespace of the current caller. You must specify at least one of ImageUrl and ObjectKey.
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

