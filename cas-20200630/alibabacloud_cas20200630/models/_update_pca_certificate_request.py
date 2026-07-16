# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class UpdatePcaCertificateRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        client_token: str = None,
        identifier: str = None,
        resource_group_id: str = None,
        tags: List[main_models.UpdatePcaCertificateRequestTags] = None,
    ):
        # The alias of the certificate.
        self.alias_name = alias_name
        # A client token used to ensure the idempotence of the request. The client generates this value to make sure that it is unique among different requests. The token can be a maximum of 64 ASCII characters and cannot contain non-ASCII characters.
        self.client_token = client_token
        # The unique identifier of the CA certificate.
        # 
        # > Call [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) to query the unique identifiers of all CA certificates.
        self.identifier = identifier
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # A list of tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdatePcaCertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UpdatePcaCertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

