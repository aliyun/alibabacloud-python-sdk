# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizationResourcesResponseBody(DaraModel):
    def __init__(
        self,
        authorization_resources: List[main_models.ListAuthorizationResourcesResponseBodyAuthorizationResources] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorization_resources = authorization_resources
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorization_resources:
            for v1 in self.authorization_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizationResources'] = []
        if self.authorization_resources is not None:
            for k1 in self.authorization_resources:
                result['AuthorizationResources'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorization_resources = []
        if m.get('AuthorizationResources') is not None:
            for k1 in m.get('AuthorizationResources'):
                temp_model = main_models.ListAuthorizationResourcesResponseBodyAuthorizationResources()
                self.authorization_resources.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorizationResourcesResponseBodyAuthorizationResources(DaraModel):
    def __init__(
        self,
        authorization_resource_entity_id: str = None,
        authorization_resource_entity_type: str = None,
        authorization_resource_id: str = None,
        authorization_rule_id: str = None,
        cloud_account_id: str = None,
        instance_id: str = None,
    ):
        # 资源实体标识
        self.authorization_resource_entity_id = authorization_resource_entity_id
        # 资源实体类型，枚举类型：asset（资产）、credential（凭据）、cloud_identity_role（云账号角色）
        self.authorization_resource_entity_type = authorization_resource_entity_type
        # 授权资源标识
        self.authorization_resource_id = authorization_resource_id
        # 授权规则标识
        self.authorization_rule_id = authorization_rule_id
        # 云账号ID。
        self.cloud_account_id = cloud_account_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_resource_entity_id is not None:
            result['AuthorizationResourceEntityId'] = self.authorization_resource_entity_id

        if self.authorization_resource_entity_type is not None:
            result['AuthorizationResourceEntityType'] = self.authorization_resource_entity_type

        if self.authorization_resource_id is not None:
            result['AuthorizationResourceId'] = self.authorization_resource_id

        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceEntityId') is not None:
            self.authorization_resource_entity_id = m.get('AuthorizationResourceEntityId')

        if m.get('AuthorizationResourceEntityType') is not None:
            self.authorization_resource_entity_type = m.get('AuthorizationResourceEntityType')

        if m.get('AuthorizationResourceId') is not None:
            self.authorization_resource_id = m.get('AuthorizationResourceId')

        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

