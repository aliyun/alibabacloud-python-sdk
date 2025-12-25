# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateConsumerAuthorizationRuleRequest(DaraModel):
    def __init__(
        self,
        authorization_resource_infos: List[main_models.AuthorizationResourceInfo] = None,
        expire_mode: str = None,
        expire_timestamp: int = None,
        parent_resource_type: str = None,
        resource_type: str = None,
    ):
        # The list of resource authorization information.
        self.authorization_resource_infos = authorization_resource_infos
        # The expiry mode. Valid values: LongTerm and ShortTerm.
        self.expire_mode = expire_mode
        # The expiration time.
        self.expire_timestamp = expire_timestamp
        # The type of the parent resource.
        self.parent_resource_type = parent_resource_type
        # The resource type,
        self.resource_type = resource_type

    def validate(self):
        if self.authorization_resource_infos:
            for v1 in self.authorization_resource_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['authorizationResourceInfos'] = []
        if self.authorization_resource_infos is not None:
            for k1 in self.authorization_resource_infos:
                result['authorizationResourceInfos'].append(k1.to_map() if k1 else None)

        if self.expire_mode is not None:
            result['expireMode'] = self.expire_mode

        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp

        if self.parent_resource_type is not None:
            result['parentResourceType'] = self.parent_resource_type

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorization_resource_infos = []
        if m.get('authorizationResourceInfos') is not None:
            for k1 in m.get('authorizationResourceInfos'):
                temp_model = main_models.AuthorizationResourceInfo()
                self.authorization_resource_infos.append(temp_model.from_map(k1))

        if m.get('expireMode') is not None:
            self.expire_mode = m.get('expireMode')

        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')

        if m.get('parentResourceType') is not None:
            self.parent_resource_type = m.get('parentResourceType')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

