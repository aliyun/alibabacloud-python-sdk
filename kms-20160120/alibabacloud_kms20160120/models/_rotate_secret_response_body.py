# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RotateSecretResponseBody(DaraModel):
    def __init__(
        self,
        arn: str = None,
        request_id: str = None,
        secret_name: str = None,
        version_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the secret.
        self.arn = arn
        # The request ID.
        self.request_id = request_id
        # The name of the secret.
        self.secret_name = secret_name
        # The version number of the secret after the secret is rotated.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

