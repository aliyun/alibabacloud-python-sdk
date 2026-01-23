# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSecuritySecretKeyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        security_secret_key_info: main_models.GetSecuritySecretKeyResponseBodySecuritySecretKeyInfo = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.security_secret_key_info = security_secret_key_info
        self.success = success

    def validate(self):
        if self.security_secret_key_info:
            self.security_secret_key_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_secret_key_info is not None:
            result['SecuritySecretKeyInfo'] = self.security_secret_key_info.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecuritySecretKeyInfo') is not None:
            temp_model = main_models.GetSecuritySecretKeyResponseBodySecuritySecretKeyInfo()
            self.security_secret_key_info = temp_model.from_map(m.get('SecuritySecretKeyInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSecuritySecretKeyResponseBodySecuritySecretKeyInfo(DaraModel):
    def __init__(
        self,
        algorithm_type: str = None,
        algorithm_type_alias: str = None,
        description: str = None,
        enable_openapi_query: bool = None,
        generation_type: str = None,
        id: int = None,
        is_owner_manage_only: bool = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        secret_key_list: List[str] = None,
        sub_key_count: int = None,
        type: str = None,
    ):
        self.algorithm_type = algorithm_type
        self.algorithm_type_alias = algorithm_type_alias
        self.description = description
        self.enable_openapi_query = enable_openapi_query
        self.generation_type = generation_type
        self.id = id
        self.is_owner_manage_only = is_owner_manage_only
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.secret_key_list = secret_key_list
        self.sub_key_count = sub_key_count
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type

        if self.algorithm_type_alias is not None:
            result['AlgorithmTypeAlias'] = self.algorithm_type_alias

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_openapi_query is not None:
            result['EnableOpenapiQuery'] = self.enable_openapi_query

        if self.generation_type is not None:
            result['GenerationType'] = self.generation_type

        if self.id is not None:
            result['Id'] = self.id

        if self.is_owner_manage_only is not None:
            result['IsOwnerManageOnly'] = self.is_owner_manage_only

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.secret_key_list is not None:
            result['SecretKeyList'] = self.secret_key_list

        if self.sub_key_count is not None:
            result['SubKeyCount'] = self.sub_key_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')

        if m.get('AlgorithmTypeAlias') is not None:
            self.algorithm_type_alias = m.get('AlgorithmTypeAlias')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableOpenapiQuery') is not None:
            self.enable_openapi_query = m.get('EnableOpenapiQuery')

        if m.get('GenerationType') is not None:
            self.generation_type = m.get('GenerationType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsOwnerManageOnly') is not None:
            self.is_owner_manage_only = m.get('IsOwnerManageOnly')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('SecretKeyList') is not None:
            self.secret_key_list = m.get('SecretKeyList')

        if m.get('SubKeyCount') is not None:
            self.sub_key_count = m.get('SubKeyCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

