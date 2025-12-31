# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateExternalCACertificateShrinkRequest(DaraModel):
    def __init__(
        self,
        api_passthrough_shrink: str = None,
        csr: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateExternalCACertificateShrinkRequestTags] = None,
        validity: str = None,
    ):
        self.api_passthrough_shrink = api_passthrough_shrink
        self.csr = csr
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.validity = validity

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
        if self.api_passthrough_shrink is not None:
            result['ApiPassthrough'] = self.api_passthrough_shrink

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.validity is not None:
            result['Validity'] = self.validity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiPassthrough') is not None:
            self.api_passthrough_shrink = m.get('ApiPassthrough')

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateExternalCACertificateShrinkRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Validity') is not None:
            self.validity = m.get('Validity')

        return self

class CreateExternalCACertificateShrinkRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

