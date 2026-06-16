# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ObtainDomainProxyTokenResponseBody(DaraModel):
    def __init__(
        self,
        domain_proxy_token: main_models.ObtainDomainProxyTokenResponseBodyDomainProxyToken = None,
        request_id: str = None,
    ):
        # The information about the proxy token.
        self.domain_proxy_token = domain_proxy_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_proxy_token:
            self.domain_proxy_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_proxy_token is not None:
            result['DomainProxyToken'] = self.domain_proxy_token.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainProxyToken') is not None:
            temp_model = main_models.ObtainDomainProxyTokenResponseBodyDomainProxyToken()
            self.domain_proxy_token = temp_model.from_map(m.get('DomainProxyToken'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ObtainDomainProxyTokenResponseBodyDomainProxyToken(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        domain_id: str = None,
        domain_proxy_token: str = None,
        domain_proxy_token_id: str = None,
        instance_id: str = None,
        last_used_time: int = None,
        status: str = None,
        update_time: int = None,
    ):
        # The time when the domain name proxy token was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The domain ID.
        self.domain_id = domain_id
        # The domain name proxy token.
        self.domain_proxy_token = domain_proxy_token
        # The ID of the domain name proxy token.
        self.domain_proxy_token_id = domain_proxy_token_id
        # The instance ID.
        self.instance_id = instance_id
        # The time when the domain name proxy token was last used. This value is a UNIX timestamp. Unit: milliseconds.
        self.last_used_time = last_used_time
        # The status of the token. Valid values:
        # 
        # - enabled: The token is enabled.
        # 
        # - disabled: The token is disabled.
        self.status = status
        # The time when the domain name proxy token was last updated. This value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_proxy_token is not None:
            result['DomainProxyToken'] = self.domain_proxy_token

        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainProxyToken') is not None:
            self.domain_proxy_token = m.get('DomainProxyToken')

        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

