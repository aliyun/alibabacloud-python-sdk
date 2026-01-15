# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class SearchImageByTextResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.SearchImageByTextResponseBodyAccessDeniedDetail = None,
        auctions: List[main_models.SearchImageByTextResponseBodyAuctions] = None,
        code: int = None,
        head: main_models.SearchImageByTextResponseBodyHead = None,
        msg: str = None,
        pic_info: main_models.SearchImageByTextResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.auctions = auctions
        self.code = code
        self.head = head
        self.msg = msg
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.auctions:
            for v1 in self.auctions:
                 if v1:
                    v1.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        result['Auctions'] = []
        if self.auctions is not None:
            for k1 in self.auctions:
                result['Auctions'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.head is not None:
            result['Head'] = self.head.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.SearchImageByTextResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        self.auctions = []
        if m.get('Auctions') is not None:
            for k1 in m.get('Auctions'):
                temp_model = main_models.SearchImageByTextResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Head') is not None:
            temp_model = main_models.SearchImageByTextResponseBodyHead()
            self.head = temp_model.from_map(m.get('Head'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PicInfo') is not None:
            temp_model = main_models.SearchImageByTextResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m.get('PicInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchImageByTextResponseBodyPicInfo(DaraModel):
    def __init__(
        self,
        all_categories: List[main_models.SearchImageByTextResponseBodyPicInfoAllCategories] = None,
    ):
        self.all_categories = all_categories

    def validate(self):
        if self.all_categories:
            for v1 in self.all_categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k1 in self.all_categories:
                result['AllCategories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k1 in m.get('AllCategories'):
                temp_model = main_models.SearchImageByTextResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k1))

        return self

class SearchImageByTextResponseBodyPicInfoAllCategories(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class SearchImageByTextResponseBodyHead(DaraModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        self.docs_found = docs_found
        self.docs_return = docs_return
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found

        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return

        if self.search_time is not None:
            result['SearchTime'] = self.search_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')

        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')

        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')

        return self

class SearchImageByTextResponseBodyAuctions(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        self.category_id = category_id
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        self.pic_name = pic_name
        self.product_id = product_id
        self.score = score
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr

        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2

        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3

        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.score is not None:
            result['Score'] = self.score

        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr

        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2

        if self.str_attr_3 is not None:
            result['StrAttr3'] = self.str_attr_3

        if self.str_attr_4 is not None:
            result['StrAttr4'] = self.str_attr_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')

        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')

        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')

        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')

        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')

        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')

        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')

        return self

class SearchImageByTextResponseBodyAccessDeniedDetail(DaraModel):
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

