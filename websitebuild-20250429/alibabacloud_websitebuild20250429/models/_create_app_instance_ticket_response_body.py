# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class CreateAppInstanceTicketResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.CreateAppInstanceTicketResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.CreateAppInstanceTicketResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class CreateAppInstanceTicketResponseBodyModule(DaraModel):
    def __init__(
        self,
        access_token_expires_at: str = None,
        access_token_issued_at: str = None,
        access_token_value: str = None,
        aliyun_pk: str = None,
        attributes: str = None,
        authorization_grant_type: str = None,
        bid: str = None,
        parent_pk: str = None,
        refresh_token_expires_at: str = None,
        refresh_token_issued_at: str = None,
        refresh_token_value: str = None,
        uuid: str = None,
    ):
        self.access_token_expires_at = access_token_expires_at
        self.access_token_issued_at = access_token_issued_at
        self.access_token_value = access_token_value
        self.aliyun_pk = aliyun_pk
        self.attributes = attributes
        self.authorization_grant_type = authorization_grant_type
        # bid
        self.bid = bid
        self.parent_pk = parent_pk
        self.refresh_token_expires_at = refresh_token_expires_at
        self.refresh_token_issued_at = refresh_token_issued_at
        self.refresh_token_value = refresh_token_value
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_expires_at is not None:
            result['AccessTokenExpiresAt'] = self.access_token_expires_at

        if self.access_token_issued_at is not None:
            result['AccessTokenIssuedAt'] = self.access_token_issued_at

        if self.access_token_value is not None:
            result['AccessTokenValue'] = self.access_token_value

        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.authorization_grant_type is not None:
            result['AuthorizationGrantType'] = self.authorization_grant_type

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.parent_pk is not None:
            result['ParentPk'] = self.parent_pk

        if self.refresh_token_expires_at is not None:
            result['RefreshTokenExpiresAt'] = self.refresh_token_expires_at

        if self.refresh_token_issued_at is not None:
            result['RefreshTokenIssuedAt'] = self.refresh_token_issued_at

        if self.refresh_token_value is not None:
            result['RefreshTokenValue'] = self.refresh_token_value

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenExpiresAt') is not None:
            self.access_token_expires_at = m.get('AccessTokenExpiresAt')

        if m.get('AccessTokenIssuedAt') is not None:
            self.access_token_issued_at = m.get('AccessTokenIssuedAt')

        if m.get('AccessTokenValue') is not None:
            self.access_token_value = m.get('AccessTokenValue')

        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('AuthorizationGrantType') is not None:
            self.authorization_grant_type = m.get('AuthorizationGrantType')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('ParentPk') is not None:
            self.parent_pk = m.get('ParentPk')

        if m.get('RefreshTokenExpiresAt') is not None:
            self.refresh_token_expires_at = m.get('RefreshTokenExpiresAt')

        if m.get('RefreshTokenIssuedAt') is not None:
            self.refresh_token_issued_at = m.get('RefreshTokenIssuedAt')

        if m.get('RefreshTokenValue') is not None:
            self.refresh_token_value = m.get('RefreshTokenValue')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

