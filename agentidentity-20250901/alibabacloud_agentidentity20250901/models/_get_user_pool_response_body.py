# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetUserPoolResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_pool: main_models.GetUserPoolResponseBodyUserPool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The user pool information.
        self.user_pool = user_pool

    def validate(self):
        if self.user_pool:
            self.user_pool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_pool is not None:
            result['UserPool'] = self.user_pool.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserPool') is not None:
            temp_model = main_models.GetUserPoolResponseBodyUserPool()
            self.user_pool = temp_model.from_map(m.get('UserPool'))

        return self

class GetUserPoolResponseBodyUserPool(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        oidcdiscovery_url: str = None,
        signin_base_url: str = None,
        source_platform: str = None,
        update_time: str = None,
        user_pool_id: str = None,
        user_pool_name: str = None,
    ):
        # The creation time in ISO 8601 format (UTC).
        self.create_time = create_time
        # The description of the user pool.
        self.description = description
        # The discovery URL for the OpenID Connect (OIDC) protocol.
        self.oidcdiscovery_url = oidcdiscovery_url
        # The base URL for logon.
        self.signin_base_url = signin_base_url
        # The source platform.
        self.source_platform = source_platform
        # The update time in ISO 8601 format (UTC).
        self.update_time = update_time
        # The ID of the user pool.
        self.user_pool_id = user_pool_id
        # The name of the user pool.
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.oidcdiscovery_url is not None:
            result['OIDCDiscoveryURL'] = self.oidcdiscovery_url

        if self.signin_base_url is not None:
            result['SigninBaseURL'] = self.signin_base_url

        if self.source_platform is not None:
            result['SourcePlatform'] = self.source_platform

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_pool_id is not None:
            result['UserPoolId'] = self.user_pool_id

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OIDCDiscoveryURL') is not None:
            self.oidcdiscovery_url = m.get('OIDCDiscoveryURL')

        if m.get('SigninBaseURL') is not None:
            self.signin_base_url = m.get('SigninBaseURL')

        if m.get('SourcePlatform') is not None:
            self.source_platform = m.get('SourcePlatform')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserPoolId') is not None:
            self.user_pool_id = m.get('UserPoolId')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

