# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tdsr20200101 import models as main_models
from darabonba.model import DaraModel

class ListSceneResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ListSceneResponseBodyAccessDeniedDetail = None,
        code: int = None,
        count: int = None,
        current_page: int = None,
        has_next: bool = None,
        list: List[main_models.ListSceneResponseBodyList] = None,
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
            temp_model = main_models.ListSceneResponseBodyAccessDeniedDetail()
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
                temp_model = main_models.ListSceneResponseBodyList()
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

class ListSceneResponseBodyList(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        name: str = None,
        preview_token: str = None,
        published: bool = None,
        source_num: int = None,
        status: str = None,
        status_name: str = None,
        sub_scene_num: int = None,
        type: str = None,
    ):
        self.cover_url = cover_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.preview_token = preview_token
        self.published = published
        self.source_num = source_num
        self.status = status
        self.status_name = status_name
        self.sub_scene_num = sub_scene_num
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token

        if self.published is not None:
            result['Published'] = self.published

        if self.source_num is not None:
            result['SourceNum'] = self.source_num

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.sub_scene_num is not None:
            result['SubSceneNum'] = self.sub_scene_num

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('SourceNum') is not None:
            self.source_num = m.get('SourceNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('SubSceneNum') is not None:
            self.sub_scene_num = m.get('SubSceneNum')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListSceneResponseBodyAccessDeniedDetail(DaraModel):
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

