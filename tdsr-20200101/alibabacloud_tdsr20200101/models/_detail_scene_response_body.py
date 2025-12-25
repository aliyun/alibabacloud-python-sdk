# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tdsr20200101 import models as main_models
from darabonba.model import DaraModel

class DetailSceneResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DetailSceneResponseBodyAccessDeniedDetail = None,
        captures: List[main_models.DetailSceneResponseBodyCaptures] = None,
        code: int = None,
        cover_url: str = None,
        floor_plans: List[main_models.DetailSceneResponseBodyFloorPlans] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        preview_token: str = None,
        published: bool = None,
        request_id: str = None,
        source_num: int = None,
        status: str = None,
        status_name: str = None,
        sub_scene_num: int = None,
        success: bool = None,
        type: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.captures = captures
        self.code = code
        self.cover_url = cover_url
        self.floor_plans = floor_plans
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.message = message
        self.name = name
        self.preview_token = preview_token
        self.published = published
        self.request_id = request_id
        self.source_num = source_num
        self.status = status
        self.status_name = status_name
        self.sub_scene_num = sub_scene_num
        self.success = success
        self.type = type

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.captures:
            for v1 in self.captures:
                 if v1:
                    v1.validate()
        if self.floor_plans:
            for v1 in self.floor_plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        result['Captures'] = []
        if self.captures is not None:
            for k1 in self.captures:
                result['Captures'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        result['FloorPlans'] = []
        if self.floor_plans is not None:
            for k1 in self.floor_plans:
                result['FloorPlans'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token

        if self.published is not None:
            result['Published'] = self.published

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_num is not None:
            result['SourceNum'] = self.source_num

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.sub_scene_num is not None:
            result['SubSceneNum'] = self.sub_scene_num

        if self.success is not None:
            result['Success'] = self.success

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DetailSceneResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        self.captures = []
        if m.get('Captures') is not None:
            for k1 in m.get('Captures'):
                temp_model = main_models.DetailSceneResponseBodyCaptures()
                self.captures.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        self.floor_plans = []
        if m.get('FloorPlans') is not None:
            for k1 in m.get('FloorPlans'):
                temp_model = main_models.DetailSceneResponseBodyFloorPlans()
                self.floor_plans.append(temp_model.from_map(k1))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceNum') is not None:
            self.source_num = m.get('SourceNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('SubSceneNum') is not None:
            self.sub_scene_num = m.get('SubSceneNum')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DetailSceneResponseBodyFloorPlans(DaraModel):
    def __init__(
        self,
        color_map_url: str = None,
        floor_label: str = None,
        floor_name: str = None,
        mini_map_url: str = None,
    ):
        self.color_map_url = color_map_url
        self.floor_label = floor_label
        self.floor_name = floor_name
        self.mini_map_url = mini_map_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color_map_url is not None:
            result['ColorMapUrl'] = self.color_map_url

        if self.floor_label is not None:
            result['FloorLabel'] = self.floor_label

        if self.floor_name is not None:
            result['FloorName'] = self.floor_name

        if self.mini_map_url is not None:
            result['MiniMapUrl'] = self.mini_map_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorMapUrl') is not None:
            self.color_map_url = m.get('ColorMapUrl')

        if m.get('FloorLabel') is not None:
            self.floor_label = m.get('FloorLabel')

        if m.get('FloorName') is not None:
            self.floor_name = m.get('FloorName')

        if m.get('MiniMapUrl') is not None:
            self.mini_map_url = m.get('MiniMapUrl')

        return self

class DetailSceneResponseBodyCaptures(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DetailSceneResponseBodyAccessDeniedDetail(DaraModel):
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

