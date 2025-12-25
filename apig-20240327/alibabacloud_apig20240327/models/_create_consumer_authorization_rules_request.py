# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateConsumerAuthorizationRulesRequest(DaraModel):
    def __init__(
        self,
        authorization_rules: List[main_models.CreateConsumerAuthorizationRulesRequestAuthorizationRules] = None,
    ):
        # The consumer authentication rules to be created.
        self.authorization_rules = authorization_rules

    def validate(self):
        if self.authorization_rules:
            for v1 in self.authorization_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['authorizationRules'] = []
        if self.authorization_rules is not None:
            for k1 in self.authorization_rules:
                result['authorizationRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorization_rules = []
        if m.get('authorizationRules') is not None:
            for k1 in m.get('authorizationRules'):
                temp_model = main_models.CreateConsumerAuthorizationRulesRequestAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k1))

        return self

class CreateConsumerAuthorizationRulesRequestAuthorizationRules(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        expire_mode: str = None,
        expire_timestamp: int = None,
        resource_identifier: main_models.CreateConsumerAuthorizationRulesRequestAuthorizationRulesResourceIdentifier = None,
        resource_type: str = None,
    ):
        # The consumer ID.
        self.consumer_id = consumer_id
        # The expiration mode. Valid values: LongTerm and ShortTerm.
        self.expire_mode = expire_mode
        # The expiration timestamp.
        self.expire_timestamp = expire_timestamp
        # The resource identifier, which is provided to non-standard code sources for space reuse.
        self.resource_identifier = resource_identifier
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_identifier:
            self.resource_identifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.expire_mode is not None:
            result['expireMode'] = self.expire_mode

        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp

        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier.to_map()

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('expireMode') is not None:
            self.expire_mode = m.get('expireMode')

        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')

        if m.get('resourceIdentifier') is not None:
            temp_model = main_models.CreateConsumerAuthorizationRulesRequestAuthorizationRulesResourceIdentifier()
            self.resource_identifier = temp_model.from_map(m.get('resourceIdentifier'))

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class CreateConsumerAuthorizationRulesRequestAuthorizationRulesResourceIdentifier(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        parent_resource_id: str = None,
        resource_id: str = None,
        resources: List[str] = None,
    ):
        # The environment ID.
        self.environment_id = environment_id
        self.parent_resource_id = parent_resource_id
        # The resource ID.
        self.resource_id = resource_id
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.parent_resource_id is not None:
            result['parentResourceId'] = self.parent_resource_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resources is not None:
            result['resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('parentResourceId') is not None:
            self.parent_resource_id = m.get('parentResourceId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resources') is not None:
            self.resources = m.get('resources')

        return self

