# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListUserAuthnSourceMappingsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
        user_authn_source_mappings: List[main_models.ListUserAuthnSourceMappingsResponseBodyUserAuthnSourceMappings] = None,
    ):
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        # 本次调用返回的查询凭证（Token）值，用于上一次翻页查询。
        self.previous_token = previous_token
        self.request_id = request_id
        self.total_count = total_count
        self.user_authn_source_mappings = user_authn_source_mappings

    def validate(self):
        if self.user_authn_source_mappings:
            for v1 in self.user_authn_source_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserAuthnSourceMappings'] = []
        if self.user_authn_source_mappings is not None:
            for k1 in self.user_authn_source_mappings:
                result['UserAuthnSourceMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_authn_source_mappings = []
        if m.get('UserAuthnSourceMappings') is not None:
            for k1 in m.get('UserAuthnSourceMappings'):
                temp_model = main_models.ListUserAuthnSourceMappingsResponseBodyUserAuthnSourceMappings()
                self.user_authn_source_mappings.append(temp_model.from_map(k1))

        return self

class ListUserAuthnSourceMappingsResponseBodyUserAuthnSourceMappings(DaraModel):
    def __init__(
        self,
        authn_source_type: str = None,
        create_time: int = None,
        external_data: str = None,
        identity_provider_id: str = None,
        instance_id: str = None,
        update_time: int = None,
        user_external_id: str = None,
        user_id: str = None,
    ):
        # 来源Idp类型
        self.authn_source_type = authn_source_type
        # 创建时间
        self.create_time = create_time
        self.external_data = external_data
        # 来源Idp Id
        self.identity_provider_id = identity_provider_id
        # 实例Id
        self.instance_id = instance_id
        # 最近一次更新时间
        self.update_time = update_time
        # 外部ID
        self.user_external_id = user_external_id
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_source_type is not None:
            result['AuthnSourceType'] = self.authn_source_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.external_data is not None:
            result['ExternalData'] = self.external_data

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnSourceType') is not None:
            self.authn_source_type = m.get('AuthnSourceType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExternalData') is not None:
            self.external_data = m.get('ExternalData')

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

