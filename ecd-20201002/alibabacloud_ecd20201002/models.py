# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class OssUploadCredential(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        endpoint: str = None,
        file_path: str = None,
        oss_policy: str = None,
        oss_signature: str = None,
        sts_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.endpoint = endpoint
        self.file_path = file_path
        self.oss_policy = oss_policy
        self.oss_signature = oss_signature
        self.sts_token = sts_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.oss_policy is not None:
            result['OssPolicy'] = self.oss_policy
        if self.oss_signature is not None:
            result['OssSignature'] = self.oss_signature
        if self.sts_token is not None:
            result['StsToken'] = self.sts_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('OssPolicy') is not None:
            self.oss_policy = m.get('OssPolicy')
        if m.get('OssSignature') is not None:
            self.oss_signature = m.get('OssSignature')
        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')
        return self


class ApproveFotaUpdateRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        client_id: str = None,
        desktop_id: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        target_status: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.app_version = app_version
        # This parameter is required.
        self.client_id = client_id
        self.desktop_id = desktop_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.region_id = region_id
        self.session_id = session_id
        self.target_status = target_status
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.target_status is not None:
            result['TargetStatus'] = self.target_status
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TargetStatus') is not None:
            self.target_status = m.get('TargetStatus')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApproveFotaUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveFotaUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveFotaUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApproveFotaUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        end_user_id: str = None,
        login_token: str = None,
        new_password: str = None,
        office_site_id: str = None,
        old_password: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The user ID.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The new password.
        # 
        # This parameter is required.
        self.new_password = new_password
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The current password.
        # 
        # This parameter is required.
        self.old_password = old_password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ChangePasswordResponseBody(TeaModel):
    def __init__(
        self,
        login_token: str = None,
        request_id: str = None,
    ):
        # The logon token.
        self.login_token = login_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangePasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangePasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFingerPrintTemplateRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        index: int = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_token = client_token
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.index is not None:
            result['Index'] = self.index
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DeleteFingerPrintTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFingerPrintTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFingerPrintTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFingerPrintTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        directory_id: List[str] = None,
        region_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The directory IDs.
        self.directory_id = directory_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        directory_id: str = None,
        directory_type: str = None,
        provider_id: str = None,
        sso_service_url: str = None,
    ):
        # The connection method.
        # 
        # Valid values:
        # 
        # *   VPC: End users connect to cloud computers over an enterprise virtual private cloud (VPC).
        # *   INTERNET: End users connect to cloud computers over the Internet.
        # *   ANY: End users connect to cloud computers over the Internet or an enterprise VPC.
        self.desktop_access_type = desktop_access_type
        # The directory ID.
        self.directory_id = directory_id
        # The directory type.
        self.directory_type = directory_type
        # The provider ID.
        self.provider_id = provider_id
        # The URL of the SSO service.
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        directories: List[DescribeDirectoriesResponseBodyDirectories] = None,
        request_id: str = None,
    ):
        # The directories.
        self.directories = directories
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDirectoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFingerPrintTemplatesRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        creation_time: str = None,
        description: str = None,
        end_user_id: str = None,
        index: int = None,
        login_time: str = None,
        office_site_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        self.client_id = client_id
        # The time when the template was created.
        self.creation_time = creation_time
        # The description of the template.
        self.description = description
        # The user ID.
        self.end_user_id = end_user_id
        # The index.
        self.index = index
        # The logon time.
        self.login_time = login_time
        # The office network ID.
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.index is not None:
            result['Index'] = self.index
        if self.login_time is not None:
            result['LoginTime'] = self.login_time
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DescribeFingerPrintTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        finger_print_templates: List[DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates] = None,
        request_id: str = None,
    ):
        # The fingerprint templates.
        self.finger_print_templates = finger_print_templates
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.finger_print_templates:
            for k in self.finger_print_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FingerPrintTemplates'] = []
        if self.finger_print_templates is not None:
            for k in self.finger_print_templates:
                result['FingerPrintTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.finger_print_templates = []
        if m.get('FingerPrintTemplates') is not None:
            for k in m.get('FingerPrintTemplates'):
                temp_model = DescribeFingerPrintTemplatesResponseBodyFingerPrintTemplates()
                self.finger_print_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFingerPrintTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFingerPrintTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFingerPrintTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalDesktopsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        desktop_access_type: str = None,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        desktop_status: str = None,
        directory_id: str = None,
        keyword: str = None,
        language: str = None,
        login_region_id: str = None,
        login_token: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        order_by: str = None,
        query_fota_update: bool = None,
        region_id: str = None,
        search_region_id: str = None,
        session_id: str = None,
        sort_type: str = None,
        without_latency: bool = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.desktop_access_type = desktop_access_type
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.directory_id = directory_id
        # 关键字。支持模糊搜索桌面ID、云桌面名称和终端用户自定义的桌面名称。
        self.keyword = keyword
        self.language = language
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.order_by = order_by
        self.query_fota_update = query_fota_update
        self.region_id = region_id
        self.search_region_id = search_region_id
        self.session_id = session_id
        self.sort_type = sort_type
        self.without_latency = without_latency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.language is not None:
            result['Language'] = self.language
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.query_fota_update is not None:
            result['QueryFotaUpdate'] = self.query_fota_update
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.without_latency is not None:
            result['WithoutLatency'] = self.without_latency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('QueryFotaUpdate') is not None:
            self.query_fota_update = m.get('QueryFotaUpdate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('WithoutLatency') is not None:
            self.without_latency = m.get('WithoutLatency')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsClients(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # 客户端类型，取值：
        # 
        # - macos：Mac客户端
        # - ios：IOS客户端
        # - android：Android客户端
        # - html5：Web客户端
        # - windows：Windows客户端
        # - linux：Linux客户端
        self.client_type = client_type
        # 客户端状态，取值：
        # 
        # - ON：允许登录
        # - OFF：不允许登录
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers(TeaModel):
    def __init__(
        self,
        allow_client_setting: bool = None,
        cron_expression: str = None,
        enforce: bool = None,
        execution_time: str = None,
        interval: int = None,
        operation_type: str = None,
        reset_type: str = None,
        timer_type: str = None,
    ):
        self.allow_client_setting = allow_client_setting
        self.cron_expression = cron_expression
        self.enforce = enforce
        self.execution_time = execution_time
        self.interval = interval
        self.operation_type = operation_type
        self.reset_type = reset_type
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.enforce is not None:
            result['Enforce'] = self.enforce
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.timer_type is not None:
            result['TimerType'] = self.timer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsDisks(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        disk_type: str = None,
    ):
        self.disk_id = disk_id
        self.disk_size = disk_size
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate(TeaModel):
    def __init__(
        self,
        channel: str = None,
        current_app_version: str = None,
        force: bool = None,
        new_app_version: str = None,
        new_dcd_version: str = None,
        project: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_note_jp: str = None,
        size: str = None,
    ):
        self.channel = channel
        self.current_app_version = current_app_version
        self.force = force
        self.new_app_version = new_app_version
        self.new_dcd_version = new_dcd_version
        self.project = project
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.release_note_jp = release_note_jp
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version
        if self.force is not None:
            result['Force'] = self.force
        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version
        if self.new_dcd_version is not None:
            result['NewDcdVersion'] = self.new_dcd_version
        if self.project is not None:
            result['Project'] = self.project
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.release_note_jp is not None:
            result['ReleaseNoteJp'] = self.release_note_jp
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')
        if m.get('NewDcdVersion') is not None:
            self.new_dcd_version = m.get('NewDcdVersion')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeGlobalDesktopsResponseBodyDesktopsSessions(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
    ):
        self.end_user_id = end_user_id
        self.establishment_time = establishment_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')
        return self


class DescribeGlobalDesktopsResponseBodyDesktops(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        clients: List[DescribeGlobalDesktopsResponseBodyDesktopsClients] = None,
        connection_status: str = None,
        cpu: int = None,
        creation_time: str = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_timers: List[DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers] = None,
        desktop_type: str = None,
        directory_id: str = None,
        disks: List[DescribeGlobalDesktopsResponseBodyDesktopsDisks] = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        expired_time: str = None,
        fota_update: DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate = None,
        gpu_memory: int = None,
        hibernation_beta: bool = None,
        host_name: str = None,
        image_id: str = None,
        last_start_time: str = None,
        local_name: str = None,
        management_flags: List[str] = None,
        memory: int = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        os: str = None,
        os_description: str = None,
        os_type: str = None,
        platform: str = None,
        policy_group_id: str = None,
        protocol_type: str = None,
        real_desktop_id: str = None,
        region_id: str = None,
        region_location: str = None,
        session_type: str = None,
        sessions: List[DescribeGlobalDesktopsResponseBodyDesktopsSessions] = None,
        support_hibernation: bool = None,
        user_custom_name: str = None,
    ):
        self.charge_type = charge_type
        # 支持的客户端信息
        self.clients = clients
        self.connection_status = connection_status
        self.cpu = cpu
        self.creation_time = creation_time
        self.desktop_group_id = desktop_group_id
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.desktop_timers = desktop_timers
        self.desktop_type = desktop_type
        self.directory_id = directory_id
        self.disks = disks
        self.end_user_id = end_user_id
        self.end_user_ids = end_user_ids
        self.expired_time = expired_time
        self.fota_update = fota_update
        self.gpu_memory = gpu_memory
        self.hibernation_beta = hibernation_beta
        self.host_name = host_name
        self.image_id = image_id
        self.last_start_time = last_start_time
        self.local_name = local_name
        self.management_flags = management_flags
        self.memory = memory
        self.network_interface_ip = network_interface_ip
        self.office_site_id = office_site_id
        self.os = os
        self.os_description = os_description
        self.os_type = os_type
        self.platform = platform
        self.policy_group_id = policy_group_id
        self.protocol_type = protocol_type
        self.real_desktop_id = real_desktop_id
        self.region_id = region_id
        self.region_location = region_location
        self.session_type = session_type
        self.sessions = sessions
        self.support_hibernation = support_hibernation
        self.user_custom_name = user_custom_name

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()
        if self.desktop_timers:
            for k in self.desktop_timers:
                if k:
                    k.validate()
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k in self.desktop_timers:
                result['DesktopTimers'].append(k.to_map() if k else None)
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.hibernation_beta is not None:
            result['HibernationBeta'] = self.hibernation_beta
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.os is not None:
            result['Os'] = self.os
        if self.os_description is not None:
            result['OsDescription'] = self.os_description
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.real_desktop_id is not None:
            result['RealDesktopId'] = self.real_desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_location is not None:
            result['RegionLocation'] = self.region_location
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        if self.support_hibernation is not None:
            result['SupportHibernation'] = self.support_hibernation
        if self.user_custom_name is not None:
            result['UserCustomName'] = self.user_custom_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k in m.get('DesktopTimers'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k))
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FotaUpdate') is not None:
            temp_model = DescribeGlobalDesktopsResponseBodyDesktopsFotaUpdate()
            self.fota_update = temp_model.from_map(m['FotaUpdate'])
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('HibernationBeta') is not None:
            self.hibernation_beta = m.get('HibernationBeta')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsDescription') is not None:
            self.os_description = m.get('OsDescription')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RealDesktopId') is not None:
            self.real_desktop_id = m.get('RealDesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionLocation') is not None:
            self.region_location = m.get('RegionLocation')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('SupportHibernation') is not None:
            self.support_hibernation = m.get('SupportHibernation')
        if m.get('UserCustomName') is not None:
            self.user_custom_name = m.get('UserCustomName')
        return self


class DescribeGlobalDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        desktops: List[DescribeGlobalDesktopsResponseBodyDesktops] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.desktops = desktops
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = DescribeGlobalDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGlobalDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGlobalDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGlobalDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOfficeSitesRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        office_site_id: List[str] = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.office_site_id = office_site_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSites(TeaModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        desktop_vpc_endpoint: str = None,
        office_site_id: str = None,
        office_site_type: str = None,
        provider_id: str = None,
        sso_service_url: str = None,
    ):
        self.desktop_access_type = desktop_access_type
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.office_site_id = office_site_id
        self.office_site_type = office_site_type
        self.provider_id = provider_id
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')
        return self


class DescribeOfficeSitesResponseBody(TeaModel):
    def __init__(
        self,
        office_sites: List[DescribeOfficeSitesResponseBodyOfficeSites] = None,
        request_id: str = None,
    ):
        self.office_sites = office_sites
        self.request_id = request_id

    def validate(self):
        if self.office_sites:
            for k in self.office_sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k in self.office_sites:
                result['OfficeSites'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k in m.get('OfficeSites'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOfficeSitesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOfficeSitesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        region_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The region endpoint.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        desktop_id: str = None,
        login_token: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        session_id: str = None,
        snapshot_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.desktop_id = desktop_id
        # This parameter is required.
        self.login_token = login_token
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.session_id = session_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        desktop_id: str = None,
        progress: str = None,
        remain_time: int = None,
        restore_point_id: str = None,
        restore_point_name: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        status: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.desktop_id = desktop_id
        self.progress = progress
        self.remain_time = remain_time
        self.restore_point_id = restore_point_id
        self.restore_point_name = restore_point_name
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.snapshot_type = snapshot_type
        self.source_disk_size = source_disk_size
        self.source_disk_type = source_disk_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.restore_point_id is not None:
            result['RestorePointId'] = self.restore_point_id
        if self.restore_point_name is not None:
            result['RestorePointName'] = self.restore_point_name
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('RestorePointId') is not None:
            self.restore_point_id = m.get('RestorePointId')
        if m.get('RestorePointName') is not None:
            self.restore_point_name = m.get('RestorePointName')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[DescribeSnapshotsResponseBodySnapshots] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.snapshots = snapshots

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserResourcesRequest(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        auto_refresh: bool = None,
        category_id: int = None,
        category_type: int = None,
        client_id: str = None,
        client_type: str = None,
        client_version: str = None,
        dual_center_forward: bool = None,
        language: str = None,
        login_region_id: str = None,
        login_token: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_ids: List[str] = None,
        order_by: str = None,
        product_types: List[str] = None,
        protocol_type: str = None,
        query_fota_update: bool = None,
        refresh_fota_update: bool = None,
        resource_ids: List[str] = None,
        resource_name: str = None,
        resource_types: List[str] = None,
        scene: str = None,
        search_region_id: str = None,
        session_id: str = None,
        sort_type: str = None,
    ):
        self.access_type = access_type
        self.auto_refresh = auto_refresh
        self.category_id = category_id
        self.category_type = category_type
        # This parameter is required.
        self.client_id = client_id
        self.client_type = client_type
        self.client_version = client_version
        self.dual_center_forward = dual_center_forward
        self.language = language
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_ids = office_site_ids
        self.order_by = order_by
        self.product_types = product_types
        self.protocol_type = protocol_type
        self.query_fota_update = query_fota_update
        self.refresh_fota_update = refresh_fota_update
        self.resource_ids = resource_ids
        self.resource_name = resource_name
        self.resource_types = resource_types
        self.scene = scene
        self.search_region_id = search_region_id
        self.session_id = session_id
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.auto_refresh is not None:
            result['AutoRefresh'] = self.auto_refresh
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.dual_center_forward is not None:
            result['DualCenterForward'] = self.dual_center_forward
        if self.language is not None:
            result['Language'] = self.language
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_ids is not None:
            result['OfficeSiteIds'] = self.office_site_ids
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.product_types is not None:
            result['ProductTypes'] = self.product_types
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.query_fota_update is not None:
            result['QueryFotaUpdate'] = self.query_fota_update
        if self.refresh_fota_update is not None:
            result['RefreshFotaUpdate'] = self.refresh_fota_update
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('AutoRefresh') is not None:
            self.auto_refresh = m.get('AutoRefresh')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DualCenterForward') is not None:
            self.dual_center_forward = m.get('DualCenterForward')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteIds') is not None:
            self.office_site_ids = m.get('OfficeSiteIds')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('ProductTypes') is not None:
            self.product_types = m.get('ProductTypes')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('QueryFotaUpdate') is not None:
            self.query_fota_update = m.get('QueryFotaUpdate')
        if m.get('RefreshFotaUpdate') is not None:
            self.refresh_fota_update = m.get('RefreshFotaUpdate')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class DescribeUserResourcesResponseBodyResourcesClients(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        self.client_type = client_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUserResourcesResponseBodyResourcesDesktopDurationList(TeaModel):
    def __init__(
        self,
        order_instance_id: str = None,
        package_creation_time: str = None,
        package_expired_time: str = None,
        package_id: str = None,
        package_status: str = None,
        package_type: str = None,
        package_used_up_strategy: str = None,
        period_end_time: str = None,
        period_start_time: str = None,
        post_paid_limit_fee: float = None,
        total_duration: int = None,
        used_duration: int = None,
    ):
        self.order_instance_id = order_instance_id
        self.package_creation_time = package_creation_time
        self.package_expired_time = package_expired_time
        self.package_id = package_id
        self.package_status = package_status
        self.package_type = package_type
        self.package_used_up_strategy = package_used_up_strategy
        self.period_end_time = period_end_time
        self.period_start_time = period_start_time
        self.post_paid_limit_fee = post_paid_limit_fee
        self.total_duration = total_duration
        self.used_duration = used_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.package_creation_time is not None:
            result['PackageCreationTime'] = self.package_creation_time
        if self.package_expired_time is not None:
            result['PackageExpiredTime'] = self.package_expired_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.package_status is not None:
            result['PackageStatus'] = self.package_status
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_used_up_strategy is not None:
            result['PackageUsedUpStrategy'] = self.package_used_up_strategy
        if self.period_end_time is not None:
            result['PeriodEndTime'] = self.period_end_time
        if self.period_start_time is not None:
            result['PeriodStartTime'] = self.period_start_time
        if self.post_paid_limit_fee is not None:
            result['PostPaidLimitFee'] = self.post_paid_limit_fee
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        if self.used_duration is not None:
            result['UsedDuration'] = self.used_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PackageCreationTime') is not None:
            self.package_creation_time = m.get('PackageCreationTime')
        if m.get('PackageExpiredTime') is not None:
            self.package_expired_time = m.get('PackageExpiredTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PackageStatus') is not None:
            self.package_status = m.get('PackageStatus')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUsedUpStrategy') is not None:
            self.package_used_up_strategy = m.get('PackageUsedUpStrategy')
        if m.get('PeriodEndTime') is not None:
            self.period_end_time = m.get('PeriodEndTime')
        if m.get('PeriodStartTime') is not None:
            self.period_start_time = m.get('PeriodStartTime')
        if m.get('PostPaidLimitFee') is not None:
            self.post_paid_limit_fee = m.get('PostPaidLimitFee')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        if m.get('UsedDuration') is not None:
            self.used_duration = m.get('UsedDuration')
        return self


class DescribeUserResourcesResponseBodyResourcesDesktopTimers(TeaModel):
    def __init__(
        self,
        allow_client_setting: str = None,
        cron_expression: str = None,
        enforce: bool = None,
        execution_time: str = None,
        interval: int = None,
        operation_type: str = None,
        reset_type: str = None,
        timer_type: str = None,
    ):
        self.allow_client_setting = allow_client_setting
        self.cron_expression = cron_expression
        self.enforce = enforce
        self.execution_time = execution_time
        self.interval = interval
        self.operation_type = operation_type
        self.reset_type = reset_type
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.enforce is not None:
            result['Enforce'] = self.enforce
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.timer_type is not None:
            result['TimerType'] = self.timer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')
        return self


class DescribeUserResourcesResponseBodyResourcesFotaUpdate(TeaModel):
    def __init__(
        self,
        channel: str = None,
        current_app_version: str = None,
        force: bool = None,
        new_app_version: str = None,
        new_dcd_version: str = None,
        project: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_note_jp: str = None,
        size: str = None,
    ):
        self.channel = channel
        self.current_app_version = current_app_version
        self.force = force
        self.new_app_version = new_app_version
        self.new_dcd_version = new_dcd_version
        self.project = project
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.release_note_jp = release_note_jp
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version
        if self.force is not None:
            result['Force'] = self.force
        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version
        if self.new_dcd_version is not None:
            result['NewDcdVersion'] = self.new_dcd_version
        if self.project is not None:
            result['Project'] = self.project
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en
        if self.release_note_jp is not None:
            result['ReleaseNoteJp'] = self.release_note_jp
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')
        if m.get('NewDcdVersion') is not None:
            self.new_dcd_version = m.get('NewDcdVersion')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')
        if m.get('ReleaseNoteJp') is not None:
            self.release_note_jp = m.get('ReleaseNoteJp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeUserResourcesResponseBodyResourcesOsUpdatePackages(TeaModel):
    def __init__(
        self,
        description: str = None,
        kb: str = None,
        title: str = None,
    ):
        self.description = description
        self.kb = kb
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.kb is not None:
            result['Kb'] = self.kb
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Kb') is not None:
            self.kb = m.get('Kb')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeUserResourcesResponseBodyResourcesOsUpdate(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        kb_list_string: str = None,
        package_count: int = None,
        packages: List[DescribeUserResourcesResponseBodyResourcesOsUpdatePackages] = None,
        update_catalog_url: str = None,
    ):
        self.check_id = check_id
        self.kb_list_string = kb_list_string
        self.package_count = package_count
        self.packages = packages
        self.update_catalog_url = update_catalog_url

    def validate(self):
        if self.packages:
            for k in self.packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.kb_list_string is not None:
            result['KbListString'] = self.kb_list_string
        if self.package_count is not None:
            result['PackageCount'] = self.package_count
        result['Packages'] = []
        if self.packages is not None:
            for k in self.packages:
                result['Packages'].append(k.to_map() if k else None)
        if self.update_catalog_url is not None:
            result['UpdateCatalogUrl'] = self.update_catalog_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('KbListString') is not None:
            self.kb_list_string = m.get('KbListString')
        if m.get('PackageCount') is not None:
            self.package_count = m.get('PackageCount')
        self.packages = []
        if m.get('Packages') is not None:
            for k in m.get('Packages'):
                temp_model = DescribeUserResourcesResponseBodyResourcesOsUpdatePackages()
                self.packages.append(temp_model.from_map(k))
        if m.get('UpdateCatalogUrl') is not None:
            self.update_catalog_url = m.get('UpdateCatalogUrl')
        return self


class DescribeUserResourcesResponseBodyResourcesSessions(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        resource_session_start_time: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        self.nick_name = nick_name
        self.resource_session_start_time = resource_session_start_time
        self.user_id = user_id
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.resource_session_start_time is not None:
            result['ResourceSessionStartTime'] = self.resource_session_start_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ResourceSessionStartTime') is not None:
            self.resource_session_start_time = m.get('ResourceSessionStartTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DescribeUserResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        ali_uid: int = None,
        app_id: str = None,
        auth_mode: str = None,
        category_id: int = None,
        category_type: int = None,
        cds_name: str = None,
        center_resource_id: str = None,
        charge_type: str = None,
        clients: List[DescribeUserResourcesResponseBodyResourcesClients] = None,
        connection_properties: str = None,
        create_time: str = None,
        desktop_duration_list: List[DescribeUserResourcesResponseBodyResourcesDesktopDurationList] = None,
        desktop_timers: List[DescribeUserResourcesResponseBodyResourcesDesktopTimers] = None,
        expired_time: str = None,
        external_domain_id: str = None,
        external_user_id: str = None,
        fota_update: DescribeUserResourcesResponseBodyResourcesFotaUpdate = None,
        global_status: bool = None,
        has_upgrade: bool = None,
        hibernation_beta: bool = None,
        icon: str = None,
        last_start_time: str = None,
        local_name: str = None,
        management_statuses: List[str] = None,
        office_site_id: str = None,
        order_status: str = None,
        os: str = None,
        os_description: str = None,
        os_type: str = None,
        os_update: DescribeUserResourcesResponseBodyResourcesOsUpdate = None,
        product_type: str = None,
        protocol_type: str = None,
        real_desktop_id: str = None,
        region_id: str = None,
        region_location: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_level: str = None,
        resource_name: str = None,
        resource_session_status: str = None,
        resource_status: str = None,
        resource_type: str = None,
        session_type: str = None,
        sessions: List[DescribeUserResourcesResponseBodyResourcesSessions] = None,
        sub_pay_type: str = None,
        support_hibernation: bool = None,
        supported_actions: List[str] = None,
        theme_color: str = None,
        user_custom_name: str = None,
        version: str = None,
    ):
        self.access_type = access_type
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.auth_mode = auth_mode
        self.category_id = category_id
        self.category_type = category_type
        self.cds_name = cds_name
        self.center_resource_id = center_resource_id
        self.charge_type = charge_type
        self.clients = clients
        self.connection_properties = connection_properties
        self.create_time = create_time
        self.desktop_duration_list = desktop_duration_list
        self.desktop_timers = desktop_timers
        self.expired_time = expired_time
        self.external_domain_id = external_domain_id
        self.external_user_id = external_user_id
        self.fota_update = fota_update
        self.global_status = global_status
        self.has_upgrade = has_upgrade
        self.hibernation_beta = hibernation_beta
        self.icon = icon
        self.last_start_time = last_start_time
        self.local_name = local_name
        self.management_statuses = management_statuses
        self.office_site_id = office_site_id
        self.order_status = order_status
        self.os = os
        self.os_description = os_description
        self.os_type = os_type
        self.os_update = os_update
        self.product_type = product_type
        self.protocol_type = protocol_type
        self.real_desktop_id = real_desktop_id
        self.region_id = region_id
        self.region_location = region_location
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_level = resource_level
        self.resource_name = resource_name
        self.resource_session_status = resource_session_status
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.session_type = session_type
        self.sessions = sessions
        self.sub_pay_type = sub_pay_type
        self.support_hibernation = support_hibernation
        self.supported_actions = supported_actions
        self.theme_color = theme_color
        self.user_custom_name = user_custom_name
        self.version = version

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()
        if self.desktop_duration_list:
            for k in self.desktop_duration_list:
                if k:
                    k.validate()
        if self.desktop_timers:
            for k in self.desktop_timers:
                if k:
                    k.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.os_update:
            self.os_update.validate()
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.cds_name is not None:
            result['CdsName'] = self.cds_name
        if self.center_resource_id is not None:
            result['CenterResourceId'] = self.center_resource_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DesktopDurationList'] = []
        if self.desktop_duration_list is not None:
            for k in self.desktop_duration_list:
                result['DesktopDurationList'].append(k.to_map() if k else None)
        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k in self.desktop_timers:
                result['DesktopTimers'].append(k.to_map() if k else None)
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.external_domain_id is not None:
            result['ExternalDomainId'] = self.external_domain_id
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()
        if self.global_status is not None:
            result['GlobalStatus'] = self.global_status
        if self.has_upgrade is not None:
            result['HasUpgrade'] = self.has_upgrade
        if self.hibernation_beta is not None:
            result['HibernationBeta'] = self.hibernation_beta
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.management_statuses is not None:
            result['ManagementStatuses'] = self.management_statuses
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.os is not None:
            result['Os'] = self.os
        if self.os_description is not None:
            result['OsDescription'] = self.os_description
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.os_update is not None:
            result['OsUpdate'] = self.os_update.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.real_desktop_id is not None:
            result['RealDesktopId'] = self.real_desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_location is not None:
            result['RegionLocation'] = self.region_location
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_session_status is not None:
            result['ResourceSessionStatus'] = self.resource_session_status
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type
        if self.support_hibernation is not None:
            result['SupportHibernation'] = self.support_hibernation
        if self.supported_actions is not None:
            result['SupportedActions'] = self.supported_actions
        if self.theme_color is not None:
            result['ThemeColor'] = self.theme_color
        if self.user_custom_name is not None:
            result['UserCustomName'] = self.user_custom_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('CdsName') is not None:
            self.cds_name = m.get('CdsName')
        if m.get('CenterResourceId') is not None:
            self.center_resource_id = m.get('CenterResourceId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeUserResourcesResponseBodyResourcesClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.desktop_duration_list = []
        if m.get('DesktopDurationList') is not None:
            for k in m.get('DesktopDurationList'):
                temp_model = DescribeUserResourcesResponseBodyResourcesDesktopDurationList()
                self.desktop_duration_list.append(temp_model.from_map(k))
        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k in m.get('DesktopTimers'):
                temp_model = DescribeUserResourcesResponseBodyResourcesDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k))
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ExternalDomainId') is not None:
            self.external_domain_id = m.get('ExternalDomainId')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('FotaUpdate') is not None:
            temp_model = DescribeUserResourcesResponseBodyResourcesFotaUpdate()
            self.fota_update = temp_model.from_map(m['FotaUpdate'])
        if m.get('GlobalStatus') is not None:
            self.global_status = m.get('GlobalStatus')
        if m.get('HasUpgrade') is not None:
            self.has_upgrade = m.get('HasUpgrade')
        if m.get('HibernationBeta') is not None:
            self.hibernation_beta = m.get('HibernationBeta')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ManagementStatuses') is not None:
            self.management_statuses = m.get('ManagementStatuses')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsDescription') is not None:
            self.os_description = m.get('OsDescription')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OsUpdate') is not None:
            temp_model = DescribeUserResourcesResponseBodyResourcesOsUpdate()
            self.os_update = temp_model.from_map(m['OsUpdate'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RealDesktopId') is not None:
            self.real_desktop_id = m.get('RealDesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionLocation') is not None:
            self.region_location = m.get('RegionLocation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceSessionStatus') is not None:
            self.resource_session_status = m.get('ResourceSessionStatus')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeUserResourcesResponseBodyResourcesSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')
        if m.get('SupportHibernation') is not None:
            self.support_hibernation = m.get('SupportHibernation')
        if m.get('SupportedActions') is not None:
            self.supported_actions = m.get('SupportedActions')
        if m.get('ThemeColor') is not None:
            self.theme_color = m.get('ThemeColor')
        if m.get('UserCustomName') is not None:
            self.user_custom_name = m.get('UserCustomName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUserResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        query_failed_resource_types: List[str] = None,
        rank_version: int = None,
        request_id: str = None,
        resources: List[DescribeUserResourcesResponseBodyResources] = None,
    ):
        self.next_token = next_token
        self.query_failed_resource_types = query_failed_resource_types
        self.rank_version = rank_version
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.query_failed_resource_types is not None:
            result['QueryFailedResourceTypes'] = self.query_failed_resource_types
        if self.rank_version is not None:
            result['RankVersion'] = self.rank_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueryFailedResourceTypes') is not None:
            self.query_failed_resource_types = m.get('QueryFailedResourceTypes')
        if m.get('RankVersion') is not None:
            self.rank_version = m.get('RankVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DescribeUserResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class DescribeUserResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptPasswordRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        directory_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        password: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The ID of the client. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The directory ID.
        self.directory_id = directory_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The office network ID.
        self.office_site_id = office_site_id
        # The password that you want to encrypt.
        # 
        # This parameter is required.
        self.password = password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class EncryptPasswordResponseBody(TeaModel):
    def __init__(
        self,
        encrypted_password: str = None,
        request_id: str = None,
    ):
        # The encrypted password.
        self.encrypted_password = encrypted_password
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EncryptPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EncryptPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EncryptPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCloudDriveServiceMountTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        self.client_id = client_id
        self.login_token = login_token
        self.office_site_id = office_site_id
        self.region_id = region_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetCloudDriveServiceMountTokenResponseBodyToken(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        expired_after: str = None,
        status: str = None,
        token: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        self.domain_id = domain_id
        self.expired_after = expired_after
        self.status = status
        self.token = token
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.expired_after is not None:
            result['ExpiredAfter'] = self.expired_after
        if self.status is not None:
            result['Status'] = self.status
        if self.token is not None:
            result['Token'] = self.token
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.used_size is not None:
            result['UsedSize'] = self.used_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('ExpiredAfter') is not None:
            self.expired_after = m.get('ExpiredAfter')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')
        return self


class GetCloudDriveServiceMountTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: GetCloudDriveServiceMountTokenResponseBodyToken = None,
    ):
        self.request_id = request_id
        self.token = token

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            temp_model = GetCloudDriveServiceMountTokenResponseBodyToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class GetCloudDriveServiceMountTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCloudDriveServiceMountTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCloudDriveServiceMountTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        command_content: str = None,
        desktop_id: str = None,
        login_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_id: str = None,
        tag: List[GetConnectionTicketRequestTag] = None,
        task_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_os = client_os
        self.client_type = client_type
        self.client_version = client_version
        self.command_content = command_content
        self.desktop_id = desktop_id
        # This parameter is required.
        self.login_token = login_token
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.session_id = session_id
        self.tag = tag
        self.task_id = task_id
        self.uuid = uuid

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetConnectionTicketRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_code: str = None,
        task_id: str = None,
        task_message: str = None,
        task_status: str = None,
        ticket: str = None,
    ):
        self.request_id = request_id
        self.task_code = task_code
        self.task_id = task_id
        self.task_message = task_message
        self.task_status = task_status
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_message is not None:
            result['TaskMessage'] = self.task_message
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(
        self,
        authentication_code: str = None,
        client_id: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        current_stage: str = None,
        directory_id: str = None,
        end_user_id: str = None,
        keep_alive: bool = None,
        keep_alive_token: str = None,
        new_password: str = None,
        office_site_id: str = None,
        old_password: str = None,
        password: str = None,
        region_id: str = None,
        session_id: str = None,
        token_code: str = None,
        uuid: str = None,
    ):
        # The verification code that is generated by the virtual MFA device. This parameter is required if you set `CurrentStage` to `MFAVerify`.
        self.authentication_code = authentication_code
        # The ID of the Alibaba Cloud Workspace client. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system (OS) of the device that runs an Alibaba Cloud Workspace client.
        self.client_os = client_os
        # The type of Alibaba Cloud Workspace clients.
        # 
        # Valid values:
        # 
        # *   HTML5: web client.
        # 
        # *   WINDOWS: Windows client.
        # 
        # *   MACOS: macOS client.
        # 
        # *   IOS: iOS client.
        # 
        # *   ANDROID: Android client.
        self.client_type = client_type
        # The version of the client. When you use an Alibaba Cloud Workspace client, you can view the client version in the **About** dialog box on the client logon page.
        self.client_version = client_version
        # The logon authentication stage. Valid values:
        # 
        # *   `ADPassword`: the stage to verify the identity of the Active Directory (AD) user. You must specify the value when the system verifies the identity of a convenience account or an AD account.
        # *   `MFABind: the stage to bind a virtual multi-factor authentication (MFA) device.`
        # *   `MFAVerify: the stage to verify the verification code that is generated by the virtual MFA device.`
        # *   `TokenVerify`: the stage to perform two-factor authentication on an Alibaba Cloud Workspace client (hereinafter referred to as the client).
        # *   `ChangePassword`: the stage to change the password of the user.
        # *   `KeepAliveVerify`: the stage to obtain LoginToken if KeepAliveToken is valid.
        self.current_stage = current_stage
        # The office network ID. This parameter has the same meaning as `OfficeSiteId`. We recommend that you replace `DirectoryId` with `OfficeSiteId`. You can specify a value for `DirectoryId` or `OfficeSiteId`.
        self.directory_id = directory_id
        # The name of the convenience user or the AD user. This parameter is required if you set `CurrentStage` to `ADPassword`.
        self.end_user_id = end_user_id
        # Specifies whether to keep the user logged on to the client. 
        # Valid values:
        # * null: Default value. Do not keep the user logged on to the client.
        # * true: Keep the user logged on to the client.
        # * false:  Do not keep the user logged on to the client.
        self.keep_alive = keep_alive
        # The token to keep logging on to an Alibaba Cloud Workspace client. When an end user logs on to the Alibaba Cloud Workspace client and select Auto Sign-in, `KeepAliveToken` is returned after you call this operation. Within the valid period of the returned token``, you can call the `GetLoginToken` operation and set `CurrentStage` to `KeepAliveVerify`. Then, you can obtain LoginToken. If you set `CurrentStage` to `KeepAliveVerify`, `KeepAliveToken` is required.
        self.keep_alive_token = keep_alive_token
        # The new password. This parameter is required if you set `CurrentStage` to `ChangePassword`.
        self.new_password = new_password
        # The office network ID.
        self.office_site_id = office_site_id
        # The current password. This parameter is required if you set `CurrentStage` to `ChangePassword`.
        self.old_password = old_password
        # The password of the convenience user or the AD user. This parameter is required if you set `CurrentStage` to `ADPassword`.
        self.password = password
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by EDS.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the session.
        # 
        # *   If the virtual multi-factor authentication (MFA) device is not bound or two-factor authentication is not enabled for the client, you do not need to specify a value for `SessionId`.
        # *   If the virtual MFA device is not bound or two-factor authentication is enabled for the client, you must specify a value for `SessionId` to verify the user identity after you specify a value for `ADPassword`. The value of the `SessionId` parameter is returned only if the CurrentStage parameter is set to `ADPassword` when you call the `GetLoginToken` operation.
        self.session_id = session_id
        # If two-factor authentication is enabled for Alibaba Cloud Workspace terminals in the EDS console and the system detects that the current logon user is exposed to risks, the system sends a verification code to the email address of the user. This parameter is required if you set `CurrentStage` to `TokenVerify`.
        self.token_code = token_code
        # The unique identifier of the client. When you use an Alibaba Cloud Workspace client, you can view the client version in the **About** dialog box on the client logon page.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_code is not None:
            result['AuthenticationCode'] = self.authentication_code
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token_code is not None:
            result['TokenCode'] = self.token_code
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationCode') is not None:
            self.authentication_code = m.get('AuthenticationCode')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetLoginTokenResponseBodyPasswordStrategy(TeaModel):
    def __init__(
        self,
        tenant_alternative_chars: List[str] = None,
        tenant_password_length: str = None,
    ):
        # > This is a parameter only for internal use.
        self.tenant_alternative_chars = tenant_alternative_chars
        # > This is a parameter only for internal use.
        self.tenant_password_length = tenant_password_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_alternative_chars is not None:
            result['TenantAlternativeChars'] = self.tenant_alternative_chars
        if self.tenant_password_length is not None:
            result['TenantPasswordLength'] = self.tenant_password_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantAlternativeChars') is not None:
            self.tenant_alternative_chars = m.get('TenantAlternativeChars')
        if m.get('TenantPasswordLength') is not None:
            self.tenant_password_length = m.get('TenantPasswordLength')
        return self


class GetLoginTokenResponseBodyRiskVerifyInfo(TeaModel):
    def __init__(
        self,
        email: str = None,
        last_lock_duration: int = None,
        locked: str = None,
        phone: str = None,
    ):
        # The email used for authentication.
        self.email = email
        # The duration of the lock.
        self.last_lock_duration = last_lock_duration
        # Whether the account is locked or not.
        self.locked = locked
        # The mobile number used for authentication.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.last_lock_duration is not None:
            result['LastLockDuration'] = self.last_lock_duration
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLockDuration') is not None:
            self.last_lock_duration = m.get('LastLockDuration')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        industry: str = None,
        keep_alive_token: str = None,
        label: str = None,
        login_token: str = None,
        next_stage: str = None,
        password_strategy: GetLoginTokenResponseBodyPasswordStrategy = None,
        phone: str = None,
        props: Dict[str, str] = None,
        qr_code_png: str = None,
        reason: str = None,
        request_id: str = None,
        risk_verify_info: GetLoginTokenResponseBodyRiskVerifyInfo = None,
        secret: str = None,
        session_id: str = None,
        tenant_id: int = None,
        window_display_mode: str = None,
    ):
        # The email address of the user. The system returns the email address in the return value of the LoginToken parameter after the user logs on to the client.
        # 
        # *   For a convenience user, the return value is the email address specified when the administrator creates the convenience user.
        # *   For an AD user, the return value is in the following format: `Username@Name of the AD domain`.
        self.email = email
        # The account of the convenience user or the AD user.
        self.end_user_id = end_user_id
        # > This is a parameter only for internal use.
        self.industry = industry
        # The token used to keep the user logged on. After the user logs on to the client and select the Keep Logon option, `KeepAliveToken` is returned when you call the operation. If the user does not select the Keep Logon option, null is returned.
        self.keep_alive_token = keep_alive_token
        # The attribute of the convenience user. For an AD user, null is returned.
        self.label = label
        # The logon token.
        self.login_token = login_token
        # The next stage that is expected to enter. For example, an administrator enables MFA in the EDS console. When an end user enters the password, that is, the end user completes the `ADPassword` stage, this parameter returns `MFAVerify`. This indicates that MFA is required.
        # 
        # >  For more information about the authentication stages, see the `CurrentStage` parameter.
        self.next_stage = next_stage
        # > This is a parameter only for internal use.
        self.password_strategy = password_strategy
        # Enter the mobile number of the convenience user. For an AD user, null is returned.
        self.phone = phone
        # > This is a parameter only for internal use.
        self.props = props
        # The QR code that is generated when the virtual MFA device is bound. The value is encoded in Base64. This parameter can be empty. This parameter is required only when the CurrentStage parameter is set to `MFABind`.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.qr_code_png = qr_code_png
        # > This is a parameter only for internal use.
        self.reason = reason
        # The ID of the request.
        self.request_id = request_id
        # Risk identification information regarding the signin process.
        self.risk_verify_info = risk_verify_info
        # The key that is generated when you bind the virtual MFA device. This parameter is required when the CurrentStage parameter is set to `MFABind`.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.secret = secret
        # The ID of the session. The ID is returned the first time you call the `GetLoginToken` operation in the session. If MFA is required, you must specify this parameter in subsequent stages.
        # 
        # > For more information about each authentication stage, see the parameter description of the request parameter `CurrentStage`.
        self.session_id = session_id
        # The ID of the Alibaba Cloud account. The ID is used for hardware client authentication.
        self.tenant_id = tenant_id
        # > This is a parameter only for internal use.
        self.window_display_mode = window_display_mode

    def validate(self):
        if self.password_strategy:
            self.password_strategy.validate()
        if self.risk_verify_info:
            self.risk_verify_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.label is not None:
            result['Label'] = self.label
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.next_stage is not None:
            result['NextStage'] = self.next_stage
        if self.password_strategy is not None:
            result['PasswordStrategy'] = self.password_strategy.to_map()
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.props is not None:
            result['Props'] = self.props
        if self.qr_code_png is not None:
            result['QrCodePng'] = self.qr_code_png
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_verify_info is not None:
            result['RiskVerifyInfo'] = self.risk_verify_info.to_map()
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.window_display_mode is not None:
            result['WindowDisplayMode'] = self.window_display_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('NextStage') is not None:
            self.next_stage = m.get('NextStage')
        if m.get('PasswordStrategy') is not None:
            temp_model = GetLoginTokenResponseBodyPasswordStrategy()
            self.password_strategy = temp_model.from_map(m['PasswordStrategy'])
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('QrCodePng') is not None:
            self.qr_code_png = m.get('QrCodePng')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskVerifyInfo') is not None:
            temp_model = GetLoginTokenResponseBodyRiskVerifyInfo()
            self.risk_verify_info = temp_model.from_map(m['RiskVerifyInfo'])
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WindowDisplayMode') is not None:
            self.window_display_mode = m.get('WindowDisplayMode')
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLoginTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsKeepAliveRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class IsKeepAliveResponseBody(TeaModel):
    def __init__(
        self,
        is_keep_alive: bool = None,
        office_site_id: str = None,
        request_id: str = None,
        tenant_id: str = None,
    ):
        self.is_keep_alive = is_keep_alive
        self.office_site_id = office_site_id
        self.request_id = request_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_keep_alive is not None:
            result['IsKeepAlive'] = self.is_keep_alive
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsKeepAlive') is not None:
            self.is_keep_alive = m.get('IsKeepAlive')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class IsKeepAliveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IsKeepAliveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IsKeepAliveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEdsAgentReportConfigRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        desktop_id: str = None,
        ecs_instance_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.desktop_id = desktop_id
        self.ecs_instance_id = ecs_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        return self


class QueryEdsAgentReportConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        config: str = None,
    ):
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class QueryEdsAgentReportConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryEdsAgentReportConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryEdsAgentReportConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryEdsAgentReportConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEdsAgentReportConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEdsAgentReportConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_token: str = None,
        client_version: str = None,
        desktop_id: List[str] = None,
        login_token: str = None,
        os_update: bool = None,
        region_id: str = None,
        session_id: str = None,
        session_token: str = None,
        uuid: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system (OS) of the device that runs the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client).
        self.client_os = client_os
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence of a request?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The client version. If you use a WUYING client, you can view the client version in the **About** dialog box on the client logon page.
        self.client_version = client_version
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The logon token.
        self.login_token = login_token
        self.os_update = os_update
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The logon token.
        self.session_token = session_token
        # The UUID of the client.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.os_update is not None:
            result['OsUpdate'] = self.os_update
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_token is not None:
            result['SessionToken'] = self.session_token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OsUpdate') is not None:
            self.os_update = m.get('OsUpdate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RebootDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebootDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshLoginTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        directory_id: str = None,
        end_user_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.directory_id = directory_id
        # This parameter is required.
        self.end_user_id = end_user_id
        # This parameter is required.
        self.login_token = login_token
        self.office_site_id = office_site_id
        # This parameter is required.
        self.region_id = region_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class RefreshLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        login_token: str = None,
        request_id: str = None,
    ):
        self.login_token = login_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshLoginTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportEdsAgentInfoRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        desktop_id: str = None,
        ecs_instance_id: str = None,
        eds_agent_info: str = None,
    ):
        self.ali_uid = ali_uid
        self.desktop_id = desktop_id
        self.ecs_instance_id = ecs_instance_id
        self.eds_agent_info = eds_agent_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.eds_agent_info is not None:
            result['EdsAgentInfo'] = self.eds_agent_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EdsAgentInfo') is not None:
            self.eds_agent_info = m.get('EdsAgentInfo')
        return self


class ReportEdsAgentInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportEdsAgentInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportEdsAgentInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReportEdsAgentInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportSessionStatusRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        session_change_time: int = None,
        session_id: str = None,
        session_status: str = None,
    ):
        self.end_user_id = end_user_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_change_time = session_change_time
        # This parameter is required.
        self.session_id = session_id
        # This parameter is required.
        self.session_status = session_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_change_time is not None:
            result['SessionChangeTime'] = self.session_change_time
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionChangeTime') is not None:
            self.session_change_time = m.get('SessionChangeTime')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        return self


class ReportSessionStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportSessionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportSessionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReportSessionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetPasswordRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        email: str = None,
        end_user_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
        phone: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The email address of the user.
        self.email = email
        # The user ID.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The phone number of the user.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.phone is not None:
            result['phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        return self


class ResetPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSnapshotRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        desktop_id: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        snapshot_id: str = None,
        stop_desktop: bool = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # Specifies whether to stop the cloud computer.
        self.stop_desktop = stop_desktop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.stop_desktop is not None:
            result['StopDesktop'] = self.stop_desktop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('StopDesktop') is not None:
            self.stop_desktop = m.get('StopDesktop')
        return self


class ResetSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTokenCodeRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        session_id: str = None,
        token_code: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system on which the client runs.
        self.client_os = client_os
        # The client version. If you use an Alibaba Cloud Workspace client, you can view the client version in the "About" dialog box on the client logon page.
        self.client_version = client_version
        # The username of the account.
        self.end_user_id = end_user_id
        # The logon token.
        self.login_token = login_token
        # The office network ID.
        self.office_site_id = office_site_id
        # The session ID.
        self.session_id = session_id
        # If two-factor authentication is enabled for clients in the Elastic Desktop Service (EDS) Enterprise console, the system will send a verification code to the user\\"s email address if it detects that the current logged-on user is at risk. This parameter is required if you set `CurrentStage` to `TokenVerify`.
        self.token_code = token_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token_code is not None:
            result['TokenCode'] = self.token_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')
        return self


class SendTokenCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendTokenCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendTokenCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendTokenCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFingerPrintTemplateRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        description: str = None,
        encrypted_finger_print_template: str = None,
        encrypted_key: str = None,
        finger_print_template: str = None,
        login_token: str = None,
        password: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_token = client_token
        self.description = description
        self.encrypted_finger_print_template = encrypted_finger_print_template
        self.encrypted_key = encrypted_key
        self.finger_print_template = finger_print_template
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypted_finger_print_template is not None:
            result['EncryptedFingerPrintTemplate'] = self.encrypted_finger_print_template
        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key
        if self.finger_print_template is not None:
            result['FingerPrintTemplate'] = self.finger_print_template
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptedFingerPrintTemplate') is not None:
            self.encrypted_finger_print_template = m.get('EncryptedFingerPrintTemplate')
        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')
        if m.get('FingerPrintTemplate') is not None:
            self.finger_print_template = m.get('FingerPrintTemplate')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SetFingerPrintTemplateResponseBody(TeaModel):
    def __init__(
        self,
        encrypted_password: str = None,
        index: int = None,
        request_id: str = None,
    ):
        self.encrypted_password = encrypted_password
        self.index = index
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password
        if self.index is not None:
            result['Index'] = self.index
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFingerPrintTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFingerPrintTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetFingerPrintTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFingerPrintTemplateDescriptionRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        description: str = None,
        index: int = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_token = client_token
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.index is not None:
            result['Index'] = self.index
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SetFingerPrintTemplateDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFingerPrintTemplateDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFingerPrintTemplateDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetFingerPrintTemplateDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_token: str = None,
        client_version: str = None,
        desktop_id: List[str] = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # The ID of the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client). The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system (OS) of the device that run the client.
        self.client_os = client_os
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The client version. If you use a WUYING client, you can click **About** on the client logon page to view the version of the client.
        self.client_version = client_version
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The UUID of the client.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class StartDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRecordContentRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_version: str = None,
        desktop_id: str = None,
        file_path: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_os = client_os
        self.client_version = client_version
        # This parameter is required.
        self.desktop_id = desktop_id
        self.file_path = file_path
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StartRecordContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartRecordContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartRecordContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartRecordContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_token: str = None,
        client_version: str = None,
        desktop_id: List[str] = None,
        login_token: str = None,
        os_update: bool = None,
        region_id: str = None,
        session_id: str = None,
        session_token: str = None,
        uuid: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system (OS) of the device that runs the Alibaba Cloud Workspace client (hereinafter referred to as WUYING client).
        self.client_os = client_os
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence of a request?](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The client version. If you use a WUYING client, you can view the client version in the **About** dialog box on the client logon page.
        self.client_version = client_version
        # The IDs of the cloud computers. You can specify the IDs of 1 to 20 cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The logon token.
        self.login_token = login_token
        self.os_update = os_update
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The logon token.
        self.session_token = session_token
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.os_update is not None:
            result['OsUpdate'] = self.os_update
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_token is not None:
            result['SessionToken'] = self.session_token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OsUpdate') is not None:
            self.os_update = m.get('OsUpdate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class StopDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordContentRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_version: str = None,
        desktop_id: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_os = client_os
        self.client_version = client_version
        # This parameter is required.
        self.desktop_id = desktop_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StopRecordContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopRecordContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopRecordContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopRecordContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindUserDesktopRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_type: str = None,
        force: bool = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        user_desktop_id: str = None,
    ):
        # The client ID.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client type.
        self.client_type = client_type
        # Specifies whether to enable forced unbinding.
        # 
        # Valid values:
        # 
        # *   true: Even when end users connect to cloud computers, the forced unbinding is still enforced.
        # *   false: Forced unbinding is only enforced when end users are disconnected from cloud computers.
        self.force = force
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The cloud computer ID.
        # 
        # This parameter is required.
        self.user_desktop_id = user_desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.force is not None:
            result['Force'] = self.force
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')
        return self


class UnbindUserDesktopResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindUserDesktopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindUserDesktopResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindUserDesktopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyCredentialRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        credential: str = None,
        credential_type: str = None,
        encrypted_key: str = None,
        login_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        # This parameter is required.
        self.credential = credential
        self.credential_type = credential_type
        self.encrypted_key = encrypted_key
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.office_site_id = office_site_id
        # This parameter is required.
        self.region_id = region_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.credential is not None:
            result['Credential'] = self.credential
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Credential') is not None:
            self.credential = m.get('Credential')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class VerifyCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyCredentialResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


