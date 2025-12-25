# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tdsr20200101 import models as main_models
from darabonba.model import DaraModel

class ListSubSceneResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ListSubSceneResponseBodyAccessDeniedDetail = None,
        code: int = None,
        count: int = None,
        current_page: int = None,
        has_next: bool = None,
        list: List[main_models.ListSubSceneResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_page: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.count = count
        self.current_page = current_page
        self.has_next = has_next
        self.list = list
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total_page = total_page

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.list:
            for v1 in self.list:
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

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ListSubSceneResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListSubSceneResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListSubSceneResponseBodyList(DaraModel):
    def __init__(
        self,
        base_image_url: str = None,
        cover_url: str = None,
        cubemap_path: str = None,
        deleted: bool = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        layout_data: str = None,
        name: str = None,
        origin_url: str = None,
        resource_id: str = None,
        resource_name: str = None,
        status: int = None,
        type: str = None,
        url: str = None,
    ):
        self.base_image_url = base_image_url
        self.cover_url = cover_url
        self.cubemap_path = cubemap_path
        self.deleted = deleted
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.layout_data = layout_data
        self.name = name
        self.origin_url = origin_url
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.status = status
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_image_url is not None:
            result['BaseImageUrl'] = self.base_image_url

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.cubemap_path is not None:
            result['CubemapPath'] = self.cubemap_path

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data

        if self.name is not None:
            result['Name'] = self.name

        if self.origin_url is not None:
            result['OriginUrl'] = self.origin_url

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseImageUrl') is not None:
            self.base_image_url = m.get('BaseImageUrl')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CubemapPath') is not None:
            self.cubemap_path = m.get('CubemapPath')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OriginUrl') is not None:
            self.origin_url = m.get('OriginUrl')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListSubSceneResponseBodyAccessDeniedDetail(DaraModel):
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

