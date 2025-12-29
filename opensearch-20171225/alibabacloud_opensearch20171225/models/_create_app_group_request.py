# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateAppGroupRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        name: str = None,
        quota: main_models.CreateAppGroupRequestQuota = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateAppGroupRequestTags] = None,
        type: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type
        # The name of the application.
        self.name = name
        # The quota.
        self.quota = quota
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The type of the application. Valid values:
        # 
        # *   standard
        # *   enhanced
        self.type = type

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.name is not None:
            result['name'] = self.name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quota') is not None:
            temp_model = main_models.CreateAppGroupRequestQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateAppGroupRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateAppGroupRequestTags(DaraModel):
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
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateAppGroupRequestQuota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The computing resources. Unit: logical computing unit (LCU).
        self.compute_resource = compute_resource
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.doc_size is not None:
            result['docSize'] = self.doc_size

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

