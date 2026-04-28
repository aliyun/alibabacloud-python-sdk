# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class GetProductListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.GetProductListResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: List[main_models.GetProductListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_message: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_message = user_message

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_message is not None:
            result['UserMessage'] = self.user_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.GetProductListResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetProductListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserMessage') is not None:
            self.user_message = m.get('UserMessage')

        return self

class GetProductListResponseBodyData(DaraModel):
    def __init__(
        self,
        category: str = None,
        product_list: List[main_models.GetProductListResponseBodyDataProductList] = None,
    ):
        self.category = category
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            for v1 in self.product_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        result['ProductList'] = []
        if self.product_list is not None:
            for k1 in self.product_list:
                result['ProductList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        self.product_list = []
        if m.get('ProductList') is not None:
            for k1 in m.get('ProductList'):
                temp_model = main_models.GetProductListResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k1))

        return self

class GetProductListResponseBodyDataProductList(DaraModel):
    def __init__(
        self,
        new_label: str = None,
        product: str = None,
    ):
        self.new_label = new_label
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_label is not None:
            result['NewLabel'] = self.new_label

        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewLabel') is not None:
            self.new_label = m.get('NewLabel')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

class GetProductListResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

