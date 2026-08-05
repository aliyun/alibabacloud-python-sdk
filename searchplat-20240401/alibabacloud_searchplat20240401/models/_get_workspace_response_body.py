# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetWorkspaceResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GetWorkspaceResponseBodyResult(DaraModel):
    def __init__(
        self,
        api_token: str = None,
        charge_type: str = None,
        commodity_code: str = None,
        description: str = None,
        domain_name: str = None,
        engine_type: str = None,
        id: str = None,
        instance_id: str = None,
        name: str = None,
        quota: main_models.GetWorkspaceResponseBodyResultQuota = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetWorkspaceResponseBodyResultTags] = None,
        type: str = None,
    ):
        # apiToken
        self.api_token = api_token
        # The billing type. Valid values:
        # - POSTPAY: pay-as-you-go.
        self.charge_type = charge_type
        # The commodity code.
        self.commodity_code = commodity_code
        # The description.
        self.description = description
        # The custom domain name prefix.
        self.domain_name = domain_name
        # The engine type.
        self.engine_type = engine_type
        # The workspace ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The workspace name.
        self.name = name
        # The quota.
        self.quota = quota
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status.
        self.status = status
        # The tags.
        self.tags = tags
        # The type.
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
        if self.api_token is not None:
            result['apiToken'] = self.api_token

        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.description is not None:
            result['description'] = self.description

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.id is not None:
            result['id'] = self.id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.name is not None:
            result['name'] = self.name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiToken') is not None:
            self.api_token = m.get('apiToken')

        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quota') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyResultQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetWorkspaceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetWorkspaceResponseBodyResultTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class GetWorkspaceResponseBodyResultQuota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The compute resource.
        self.compute_resource = compute_resource
        # The storage capacity.
        self.doc_size = doc_size
        # The specifications.
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

