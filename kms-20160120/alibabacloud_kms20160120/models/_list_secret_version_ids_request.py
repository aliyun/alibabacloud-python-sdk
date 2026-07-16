# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSecretVersionIdsRequest(DaraModel):
    def __init__(
        self,
        include_deprecated: str = None,
        page_number: int = None,
        page_size: int = None,
        secret_name: str = None,
    ):
        # Specifies whether to include credential versions that have no version stages in the response.
        # 
        # Valid values:
        # 
        # - false (default): No
        # 
        # - true: Yes
        self.include_deprecated = include_deprecated
        # The number of the page to return for a paged query. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. Default value: 20.
        self.page_size = page_size
        # The name or Alibaba Cloud Resource Name (ARN) of the credential.
        # 
        # > When you access a credential that belongs to another Alibaba Cloud account, you must specify the ARN of the credential. The ARN of a credential is in the format of `acs:kms:${region}:${account}:secret/${secret-name}`.
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
        if self.include_deprecated is not None:
            result['IncludeDeprecated'] = self.include_deprecated

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeDeprecated') is not None:
            self.include_deprecated = m.get('IncludeDeprecated')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

