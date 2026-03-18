# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ListAuthenticationTokensResponseBody(DaraModel):
    def __init__(
        self,
        entities: List[main_models.ListAuthenticationTokensResponseBodyEntities] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # 资源实体列表。
        self.entities = entities
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['entities'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('entities') is not None:
            for k1 in m.get('entities'):
                temp_model = main_models.ListAuthenticationTokensResponseBodyEntities()
                self.entities.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListAuthenticationTokensResponseBodyEntities(DaraModel):
    def __init__(
        self,
        authentication_token_id: str = None,
        authentication_token_type: str = None,
        consumer_id: str = None,
        consumer_type: str = None,
        create_time: int = None,
        creator_id: str = None,
        creator_type: str = None,
        credential_provider_id: str = None,
        expiration_time: int = None,
        instance_id: str = None,
        revoked: bool = None,
        update_time: int = None,
    ):
        self.authentication_token_id = authentication_token_id
        self.authentication_token_type = authentication_token_type
        self.consumer_id = consumer_id
        self.consumer_type = consumer_type
        self.create_time = create_time
        self.creator_id = creator_id
        self.creator_type = creator_type
        self.credential_provider_id = credential_provider_id
        self.expiration_time = expiration_time
        # EIAM实例ID。
        self.instance_id = instance_id
        self.revoked = revoked
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_token_id is not None:
            result['authenticationTokenId'] = self.authentication_token_id

        if self.authentication_token_type is not None:
            result['authenticationTokenType'] = self.authentication_token_type

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_type is not None:
            result['consumerType'] = self.consumer_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_type is not None:
            result['creatorType'] = self.creator_type

        if self.credential_provider_id is not None:
            result['credentialProviderId'] = self.credential_provider_id

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.revoked is not None:
            result['revoked'] = self.revoked

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationTokenId') is not None:
            self.authentication_token_id = m.get('authenticationTokenId')

        if m.get('authenticationTokenType') is not None:
            self.authentication_token_type = m.get('authenticationTokenType')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerType') is not None:
            self.consumer_type = m.get('consumerType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorType') is not None:
            self.creator_type = m.get('creatorType')

        if m.get('credentialProviderId') is not None:
            self.credential_provider_id = m.get('credentialProviderId')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('revoked') is not None:
            self.revoked = m.get('revoked')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

