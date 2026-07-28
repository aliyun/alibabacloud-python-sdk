# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProviderDocumentRequest(DaraModel):
    def __init__(
        self,
        provider_version: str = None,
        terraform_resource_type: str = None,
    ):
        self.provider_version = provider_version
        # This parameter is required.
        self.terraform_resource_type = terraform_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provider_version is not None:
            result['providerVersion'] = self.provider_version

        if self.terraform_resource_type is not None:
            result['terraformResourceType'] = self.terraform_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('providerVersion') is not None:
            self.provider_version = m.get('providerVersion')

        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')

        return self

