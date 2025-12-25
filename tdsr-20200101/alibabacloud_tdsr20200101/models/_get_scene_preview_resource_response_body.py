# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tdsr20200101 import models as main_models
from darabonba.model import DaraModel

class GetScenePreviewResourceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.GetScenePreviewResourceResponseBodyAccessDeniedDetail = None,
        code: int = None,
        data: main_models.GetScenePreviewResourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.GetScenePreviewResourceResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetScenePreviewResourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetScenePreviewResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_directory: main_models.GetScenePreviewResourceResponseBodyDataResourceDirectory = None,
        version: str = None,
    ):
        self.name = name
        self.resource_directory = resource_directory
        self.version = version

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceDirectory') is not None:
            temp_model = main_models.GetScenePreviewResourceResponseBodyDataResourceDirectory()
            self.resource_directory = temp_model.from_map(m.get('ResourceDirectory'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetScenePreviewResourceResponseBodyDataResourceDirectory(DaraModel):
    def __init__(
        self,
        hotspot_tag_config: str = None,
        model_config: str = None,
        orthomap_config: str = None,
        root_path: str = None,
    ):
        self.hotspot_tag_config = hotspot_tag_config
        self.model_config = model_config
        self.orthomap_config = orthomap_config
        self.root_path = root_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotspot_tag_config is not None:
            result['HotspotTagConfig'] = self.hotspot_tag_config

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config

        if self.orthomap_config is not None:
            result['OrthomapConfig'] = self.orthomap_config

        if self.root_path is not None:
            result['RootPath'] = self.root_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotspotTagConfig') is not None:
            self.hotspot_tag_config = m.get('HotspotTagConfig')

        if m.get('ModelConfig') is not None:
            self.model_config = m.get('ModelConfig')

        if m.get('OrthomapConfig') is not None:
            self.orthomap_config = m.get('OrthomapConfig')

        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')

        return self

class GetScenePreviewResourceResponseBodyAccessDeniedDetail(DaraModel):
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

