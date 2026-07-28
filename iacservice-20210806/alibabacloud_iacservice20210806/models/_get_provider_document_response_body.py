# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProviderDocumentResponseBody(DaraModel):
    def __init__(
        self,
        document: str = None,
        provider_version: str = None,
        request_id: str = None,
        terraform_resource_type: str = None,
    ):
        self.document = document
        self.provider_version = provider_version
        # Id of the request
        self.request_id = request_id
        self.terraform_resource_type = terraform_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document

        if self.provider_version is not None:
            result['providerVersion'] = self.provider_version

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.terraform_resource_type is not None:
            result['terraformResourceType'] = self.terraform_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('providerVersion') is not None:
            self.provider_version = m.get('providerVersion')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')

        return self

