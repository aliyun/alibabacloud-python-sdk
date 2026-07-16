# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecretRequest(DaraModel):
    def __init__(
        self,
        fetch_tags: str = None,
        secret_name: str = None,
    ):
        # Specifies whether to return the resource tags of the secret. Valid values:
        # 
        # *   true: The resource tags are returned.
        # *   false: The resource tags are not returned. This is the default value.
        self.fetch_tags = fetch_tags
        # The name of the secret.
        # 
        # This parameter is required.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

