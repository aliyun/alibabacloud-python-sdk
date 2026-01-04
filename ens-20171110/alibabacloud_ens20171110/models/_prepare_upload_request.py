# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepareUploadRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        client_ip: str = None,
    ):
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The specified IP address. This parameter is applicable to scenarios where the user IP address is inconsistent with the operation calling IP address, such as the scenario where the server obtains authorization and sends the authorization to the client.
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        return self

