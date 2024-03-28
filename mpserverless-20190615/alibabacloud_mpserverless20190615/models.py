# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddCorsDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        space_id: str = None,
    ):
        self.domain = domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AddCorsDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        request_id: str = None,
    ):
        self.domain_id = domain_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCorsDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCorsDomainResponseBody = None,
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
            temp_model = AddCorsDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AddDingtalkOpenPlatformConfigResponseBody(TeaModel):
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


class AddDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDingtalkOpenPlatformConfigResponseBody = None,
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
            temp_model = AddDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachWebHostingCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_type: str = None,
        domain: str = None,
        private_key: str = None,
        server_certificate: str = None,
        space_id: str = None,
    ):
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.domain = domain
        self.private_key = private_key
        self.server_certificate = server_certificate
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AttachWebHostingCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachWebHostingCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachWebHostingCertificateResponseBody = None,
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
            temp_model = AttachWebHostingCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteWebHostingFilesRequest(TeaModel):
    def __init__(
        self,
        file_paths: List[str] = None,
        space_id: str = None,
    ):
        self.file_paths = file_paths
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class BatchDeleteWebHostingFilesResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteWebHostingFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteWebHostingFilesResponseBody = None,
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
            temp_model = BatchDeleteWebHostingFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindWebHostingCustomDomainRequest(TeaModel):
    def __init__(
        self,
        custom_domain: str = None,
        space_id: str = None,
    ):
        self.custom_domain = custom_domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class BindWebHostingCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindWebHostingCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindWebHostingCustomDomainResponseBody = None,
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
            temp_model = BindWebHostingCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMpServerlessRoleExistsRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CheckMpServerlessRoleExistsResponseBody(TeaModel):
    def __init__(
        self,
        exists: bool = None,
        request_id: str = None,
    ):
        self.exists = exists
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exists is not None:
            result['Exists'] = self.exists
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMpServerlessRoleExistsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckMpServerlessRoleExistsResponseBody = None,
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
            temp_model = CheckMpServerlessRoleExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBExportTaskRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        fields: str = None,
        file_type: str = None,
        space_id: str = None,
    ):
        self.collection = collection
        self.fields = fields
        self.file_type = file_type
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateDBExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBExportTaskResponseBody = None,
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
            temp_model = CreateDBExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBImportTaskRequest(TeaModel):
    def __init__(
        self,
        collection: str = None,
        file_type: str = None,
        mode: str = None,
        space_id: str = None,
    ):
        self.collection = collection
        self.file_type = file_type
        self.mode = mode
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateDBImportTaskResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        expire_time: str = None,
        file_key: str = None,
        host: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        task_id: str = None,
    ):
        self.access_key_id = access_key_id
        self.expire_time = expire_time
        self.file_key = file_key
        self.host = host
        self.policy = policy
        self.request_id = request_id
        self.signature = signature
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBImportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBImportTaskResponseBody = None,
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
            temp_model = CreateDBImportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRestoreTaskRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        new_collections: str = None,
        origin_collections: str = None,
        space_id: str = None,
    ):
        self.backup_id = backup_id
        self.new_collections = new_collections
        self.origin_collections = origin_collections
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.new_collections is not None:
            result['NewCollections'] = self.new_collections
        if self.origin_collections is not None:
            result['OriginCollections'] = self.origin_collections
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('NewCollections') is not None:
            self.new_collections = m.get('NewCollections')
        if m.get('OriginCollections') is not None:
            self.origin_collections = m.get('OriginCollections')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateDBRestoreTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBRestoreTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBRestoreTaskResponseBody = None,
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
            temp_model = CreateDBRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        memory: int = None,
        name: str = None,
        runtime: str = None,
        space_id: str = None,
        timeout: int = None,
    ):
        self.desc = desc
        self.memory = memory
        self.name = name
        self.runtime = runtime
        self.space_id = space_id
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateFunctionResponseBodySpec(TeaModel):
    def __init__(
        self,
        instance_concurrency: str = None,
        memory: str = None,
        runtime: str = None,
        timeout: str = None,
    ):
        self.instance_concurrency = instance_concurrency
        self.memory = memory
        self.runtime = runtime
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        desc: str = None,
        modified_at: str = None,
        name: str = None,
        request_id: str = None,
        spec: CreateFunctionResponseBodySpec = None,
    ):
        self.created_at = created_at
        self.desc = desc
        self.modified_at = modified_at
        self.name = name
        self.request_id = request_id
        self.spec = spec

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            temp_model = CreateFunctionResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionResponseBody = None,
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
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionDeploymentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        space_id: str = None,
    ):
        self.name = name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateFunctionDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        request_id: str = None,
        upload_signed_url: str = None,
    ):
        self.deployment_id = deployment_id
        self.request_id = request_id
        self.upload_signed_url = upload_signed_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_signed_url is not None:
            result['UploadSignedUrl'] = self.upload_signed_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadSignedUrl') is not None:
            self.upload_signed_url = m.get('UploadSignedUrl')
        return self


class CreateFunctionDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionDeploymentResponseBody = None,
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
            temp_model = CreateFunctionDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpaceRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        workspace_id: int = None,
    ):
        self.desc = desc
        self.name = name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        space_id: str = None,
    ):
        self.request_id = request_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSpaceResponseBody = None,
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
            temp_model = CreateSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpaceWithOrderRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        package_version: str = None,
        period: int = None,
        subscription_type: str = None,
        use_coupon: bool = None,
    ):
        self.desc = desc
        self.name = name
        self.package_version = package_version
        self.period = period
        self.subscription_type = subscription_type
        self.use_coupon = use_coupon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.period is not None:
            result['Period'] = self.period
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        return self


class CreateSpaceWithOrderResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
        request_id: str = None,
        space_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.request_id = request_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateSpaceWithOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSpaceWithOrderResponseBody = None,
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
            temp_model = CreateSpaceWithOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteAntOpenPlatformConfigResponseBody(TeaModel):
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


class DeleteAntOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAntOpenPlatformConfigResponseBody = None,
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
            temp_model = DeleteAntOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCorsDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        space_id: str = None,
    ):
        self.domain_id = domain_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteCorsDomainResponseBody(TeaModel):
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


class DeleteCorsDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCorsDomainResponseBody = None,
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
            temp_model = DeleteCorsDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBCollectionRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        space_id: str = None,
    ):
        self.body = body
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteDBCollectionResponseBody(TeaModel):
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


class DeleteDBCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBCollectionResponseBody = None,
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
            temp_model = DeleteDBCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteDingtalkOpenPlatformConfigResponseBody(TeaModel):
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


class DeleteDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDingtalkOpenPlatformConfigResponseBody = None,
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
            temp_model = DeleteDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        space_id: str = None,
    ):
        self.id = id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteFileResponseBody(TeaModel):
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


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFileResponseBody = None,
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        space_id: str = None,
    ):
        self.name = name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteFunctionResponseBody(TeaModel):
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


class DeleteFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFunctionResponseBody = None,
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
            temp_model = DeleteFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpaceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteSpaceResponseBody(TeaModel):
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


class DeleteSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSpaceResponseBody = None,
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
            temp_model = DeleteSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebHostingCertificateRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        space_id: str = None,
    ):
        self.domain = domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteWebHostingCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebHostingCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWebHostingCertificateResponseBody = None,
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
            temp_model = DeleteWebHostingCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebHostingFileRequest(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        space_id: str = None,
    ):
        self.file_path = file_path
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteWebHostingFileResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebHostingFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWebHostingFileResponseBody = None,
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
            temp_model = DeleteWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWechatOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteWechatOpenPlatformConfigResponseBody(TeaModel):
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


class DeleteWechatOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWechatOpenPlatformConfigResponseBody = None,
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
            temp_model = DeleteWechatOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployFunctionRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        space_id: str = None,
    ):
        self.deployment_id = deployment_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeployFunctionResponseBody(TeaModel):
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


class DeployFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployFunctionResponseBody = None,
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
            temp_model = DeployFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        self.space_id = space_id
        self.tenant_id = tenant_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainResponseBodyAuthConfig(TeaModel):
    def __init__(
        self,
        auth_delta: int = None,
        auth_key: str = None,
        auth_type: str = None,
        config_id: str = None,
    ):
        self.auth_delta = auth_delta
        self.auth_key = auth_key
        self.auth_type = auth_type
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_delta is not None:
            result['AuthDelta'] = self.auth_delta
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.config_id is not None:
            result['configId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthDelta') is not None:
            self.auth_delta = m.get('AuthDelta')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('configId') is not None:
            self.config_id = m.get('configId')
        return self


class DescribeCdnDomainResponseBodyCorsConfig(TeaModel):
    def __init__(
        self,
        access_origin_control: bool = None,
        allow_origin: str = None,
        config_id: str = None,
    ):
        self.access_origin_control = access_origin_control
        self.allow_origin = allow_origin
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_origin_control is not None:
            result['AccessOriginControl'] = self.access_origin_control
        if self.allow_origin is not None:
            result['AllowOrigin'] = self.allow_origin
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessOriginControl') is not None:
            self.access_origin_control = m.get('AccessOriginControl')
        if m.get('AllowOrigin') is not None:
            self.allow_origin = m.get('AllowOrigin')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DescribeCdnDomainResponseBodyIpConfig(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        ip_list: str = None,
        type: str = None,
    ):
        self.config_id = config_id
        self.ip_list = ip_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainResponseBodyRefererConfig(TeaModel):
    def __init__(
        self,
        allow_empty: str = None,
        config_id: str = None,
        disable_ast: str = None,
        refer_list: str = None,
        type: str = None,
    ):
        self.allow_empty = allow_empty
        self.config_id = config_id
        self.disable_ast = disable_ast
        self.refer_list = refer_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_empty is not None:
            result['AllowEmpty'] = self.allow_empty
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.disable_ast is not None:
            result['DisableAst'] = self.disable_ast
        if self.refer_list is not None:
            result['ReferList'] = self.refer_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowEmpty') is not None:
            self.allow_empty = m.get('AllowEmpty')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DisableAst') is not None:
            self.disable_ast = m.get('DisableAst')
        if m.get('ReferList') is not None:
            self.refer_list = m.get('ReferList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCdnDomainResponseBodyUaConfig(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        type: str = None,
        ua_list: str = None,
    ):
        self.config_id = config_id
        self.type = type
        self.ua_list = ua_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.type is not None:
            result['Type'] = self.type
        if self.ua_list is not None:
            result['UaList'] = self.ua_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UaList') is not None:
            self.ua_list = m.get('UaList')
        return self


class DescribeCdnDomainResponseBody(TeaModel):
    def __init__(
        self,
        auth_config: DescribeCdnDomainResponseBodyAuthConfig = None,
        cors_config: DescribeCdnDomainResponseBodyCorsConfig = None,
        domain_name: str = None,
        ip_config: DescribeCdnDomainResponseBodyIpConfig = None,
        referer_config: DescribeCdnDomainResponseBodyRefererConfig = None,
        request_id: str = None,
        service_status: str = None,
        space_id: str = None,
        ua_config: DescribeCdnDomainResponseBodyUaConfig = None,
    ):
        self.auth_config = auth_config
        self.cors_config = cors_config
        self.domain_name = domain_name
        self.ip_config = ip_config
        self.referer_config = referer_config
        self.request_id = request_id
        self.service_status = service_status
        self.space_id = space_id
        self.ua_config = ua_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cors_config:
            self.cors_config.validate()
        if self.ip_config:
            self.ip_config.validate()
        if self.referer_config:
            self.referer_config.validate()
        if self.ua_config:
            self.ua_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config.to_map()
        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.ip_config is not None:
            result['IpConfig'] = self.ip_config.to_map()
        if self.referer_config is not None:
            result['RefererConfig'] = self.referer_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.ua_config is not None:
            result['UaConfig'] = self.ua_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyAuthConfig()
            self.auth_config = temp_model.from_map(m['AuthConfig'])
        if m.get('CorsConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyCorsConfig()
            self.cors_config = temp_model.from_map(m['CorsConfig'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IpConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyIpConfig()
            self.ip_config = temp_model.from_map(m['IpConfig'])
        if m.get('RefererConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyRefererConfig()
            self.referer_config = temp_model.from_map(m['RefererConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('UaConfig') is not None:
            temp_model = DescribeCdnDomainResponseBodyUaConfig()
            self.ua_config = temp_model.from_map(m['UaConfig'])
        return self


class DescribeCdnDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnDomainResponseBody = None,
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
            temp_model = DescribeCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFCOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeFCOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFCOpenStatusResponseBody = None,
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
            temp_model = DescribeFCOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileUploadSignedUrlRequest(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        file_id: str = None,
        filename: str = None,
        size: int = None,
        space_id: str = None,
    ):
        self.content_type = content_type
        self.file_id = file_id
        self.filename = filename
        self.size = size
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.size is not None:
            result['Size'] = self.size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeFileUploadSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        oss_callback_url: str = None,
        overwrite: bool = None,
        request_id: str = None,
        sign_url: str = None,
    ):
        self.id = id
        self.oss_callback_url = oss_callback_url
        self.overwrite = overwrite
        self.request_id = request_id
        self.sign_url = sign_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_callback_url is not None:
            result['OssCallbackUrl'] = self.oss_callback_url
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_url is not None:
            result['SignUrl'] = self.sign_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssCallbackUrl') is not None:
            self.oss_callback_url = m.get('OssCallbackUrl')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignUrl') is not None:
            self.sign_url = m.get('SignUrl')
        return self


class DescribeFileUploadSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFileUploadSignedUrlResponseBody = None,
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
            temp_model = DescribeFileUploadSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFunctionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        space_id: str = None,
    ):
        self.name = name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeFunctionResponseBodyDeployment(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        deployment_id: str = None,
        download_signed_url: str = None,
        modified_at: str = None,
        version_no: str = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.download_signed_url = download_signed_url
        self.modified_at = modified_at
        self.version_no = version_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.download_signed_url is not None:
            result['DownloadSignedUrl'] = self.download_signed_url
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.version_no is not None:
            result['VersionNo'] = self.version_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('DownloadSignedUrl') is not None:
            self.download_signed_url = m.get('DownloadSignedUrl')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')
        return self


class DescribeFunctionResponseBodyFunctionSpec(TeaModel):
    def __init__(
        self,
        instance_concurrency: int = None,
        memory: str = None,
        runtime: str = None,
        timeout: str = None,
    ):
        self.instance_concurrency = instance_concurrency
        self.memory = memory
        self.runtime = runtime
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class DescribeFunctionResponseBodyFunction(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        desc: str = None,
        http_trigger_path: str = None,
        modified_at: str = None,
        name: str = None,
        spec: DescribeFunctionResponseBodyFunctionSpec = None,
        timing_trigger_config: str = None,
        timing_trigger_user_payload: str = None,
    ):
        self.created_at = created_at
        self.desc = desc
        self.http_trigger_path = http_trigger_path
        self.modified_at = modified_at
        self.name = name
        self.spec = spec
        self.timing_trigger_config = timing_trigger_config
        self.timing_trigger_user_payload = timing_trigger_user_payload

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.timing_trigger_user_payload is not None:
            result['TimingTriggerUserPayload'] = self.timing_trigger_user_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Spec') is not None:
            temp_model = DescribeFunctionResponseBodyFunctionSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('TimingTriggerUserPayload') is not None:
            self.timing_trigger_user_payload = m.get('TimingTriggerUserPayload')
        return self


class DescribeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        deployment: DescribeFunctionResponseBodyDeployment = None,
        function: DescribeFunctionResponseBodyFunction = None,
        request_id: str = None,
    ):
        self.deployment = deployment
        self.function = function
        self.request_id = request_id

    def validate(self):
        if self.deployment:
            self.deployment.validate()
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment is not None:
            result['Deployment'] = self.deployment.to_map()
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deployment') is not None:
            temp_model = DescribeFunctionResponseBodyDeployment()
            self.deployment = temp_model.from_map(m['Deployment'])
        if m.get('Function') is not None:
            temp_model = DescribeFunctionResponseBodyFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFunctionResponseBody = None,
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
            temp_model = DescribeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHttpTriggerConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeHttpTriggerConfigResponseBody(TeaModel):
    def __init__(
        self,
        custom_domain: str = None,
        custom_domain_certificate_info: str = None,
        custom_domain_cname: str = None,
        default_endpoint: str = None,
        enable_service: bool = None,
        request_id: str = None,
    ):
        self.custom_domain = custom_domain
        self.custom_domain_certificate_info = custom_domain_certificate_info
        self.custom_domain_cname = custom_domain_cname
        self.default_endpoint = default_endpoint
        self.enable_service = enable_service
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate_info is not None:
            result['CustomDomainCertificateInfo'] = self.custom_domain_certificate_info
        if self.custom_domain_cname is not None:
            result['CustomDomainCname'] = self.custom_domain_cname
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificateInfo') is not None:
            self.custom_domain_certificate_info = m.get('CustomDomainCertificateInfo')
        if m.get('CustomDomainCname') is not None:
            self.custom_domain_cname = m.get('CustomDomainCname')
        if m.get('DefaultEndpoint') is not None:
            self.default_endpoint = m.get('DefaultEndpoint')
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHttpTriggerConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHttpTriggerConfigResponseBody = None,
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
            temp_model = DescribeHttpTriggerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceQuotaRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeResourceQuotaResponseBody(TeaModel):
    def __init__(
        self,
        cloud_storage_data_size_quota: float = None,
        request_id: str = None,
        static_web_data_size_quota: float = None,
    ):
        self.cloud_storage_data_size_quota = cloud_storage_data_size_quota
        self.request_id = request_id
        self.static_web_data_size_quota = static_web_data_size_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_storage_data_size_quota is not None:
            result['CloudStorageDataSizeQuota'] = self.cloud_storage_data_size_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.static_web_data_size_quota is not None:
            result['StaticWebDataSizeQuota'] = self.static_web_data_size_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudStorageDataSizeQuota') is not None:
            self.cloud_storage_data_size_quota = m.get('CloudStorageDataSizeQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StaticWebDataSizeQuota') is not None:
            self.static_web_data_size_quota = m.get('StaticWebDataSizeQuota')
        return self


class DescribeResourceQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceQuotaResponseBody = None,
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
            temp_model = DescribeResourceQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceUsageRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        format: str = None,
        page_number: int = None,
        page_size: int = None,
        space_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.format = format
        self.page_number = page_number
        self.page_size = page_size
        self.space_id = space_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.format is not None:
            result['Format'] = self.format
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeResourceUsageResponseBodyDataListCloudDB(TeaModel):
    def __init__(
        self,
        data_size: int = None,
        read: int = None,
        write: int = None,
    ):
        self.data_size = data_size
        self.read = read
        self.write = write

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.read is not None:
            result['Read'] = self.read
        if self.write is not None:
            result['Write'] = self.write
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Read') is not None:
            self.read = m.get('Read')
        if m.get('Write') is not None:
            self.write = m.get('Write')
        return self


class DescribeResourceUsageResponseBodyDataListCloudFunction(TeaModel):
    def __init__(
        self,
        compute: int = None,
        count: int = None,
        traffic: int = None,
    ):
        self.compute = compute
        self.count = count
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute
        if self.count is not None:
            result['Count'] = self.count
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compute') is not None:
            self.compute = m.get('Compute')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeResourceUsageResponseBodyDataListCloudStorage(TeaModel):
    def __init__(
        self,
        data_size: int = None,
        download: int = None,
        traffic: int = None,
        upload: int = None,
    ):
        self.data_size = data_size
        self.download = download
        self.traffic = traffic
        self.upload = upload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.download is not None:
            result['Download'] = self.download
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.upload is not None:
            result['Upload'] = self.upload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Download') is not None:
            self.download = m.get('Download')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('Upload') is not None:
            self.upload = m.get('Upload')
        return self


class DescribeResourceUsageResponseBodyDataListStaticWeb(TeaModel):
    def __init__(
        self,
        data_size: int = None,
        traffic: int = None,
    ):
        self.data_size = data_size
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeResourceUsageResponseBodyDataList(TeaModel):
    def __init__(
        self,
        cloud_db: DescribeResourceUsageResponseBodyDataListCloudDB = None,
        cloud_function: DescribeResourceUsageResponseBodyDataListCloudFunction = None,
        cloud_storage: DescribeResourceUsageResponseBodyDataListCloudStorage = None,
        end_time: str = None,
        start_time: str = None,
        static_web: DescribeResourceUsageResponseBodyDataListStaticWeb = None,
    ):
        self.cloud_db = cloud_db
        self.cloud_function = cloud_function
        self.cloud_storage = cloud_storage
        self.end_time = end_time
        self.start_time = start_time
        self.static_web = static_web

    def validate(self):
        if self.cloud_db:
            self.cloud_db.validate()
        if self.cloud_function:
            self.cloud_function.validate()
        if self.cloud_storage:
            self.cloud_storage.validate()
        if self.static_web:
            self.static_web.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_db is not None:
            result['CloudDB'] = self.cloud_db.to_map()
        if self.cloud_function is not None:
            result['CloudFunction'] = self.cloud_function.to_map()
        if self.cloud_storage is not None:
            result['CloudStorage'] = self.cloud_storage.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.static_web is not None:
            result['StaticWeb'] = self.static_web.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudDB') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListCloudDB()
            self.cloud_db = temp_model.from_map(m['CloudDB'])
        if m.get('CloudFunction') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListCloudFunction()
            self.cloud_function = temp_model.from_map(m['CloudFunction'])
        if m.get('CloudStorage') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListCloudStorage()
            self.cloud_storage = temp_model.from_map(m['CloudStorage'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StaticWeb') is not None:
            temp_model = DescribeResourceUsageResponseBodyDataListStaticWeb()
            self.static_web = temp_model.from_map(m['StaticWeb'])
        return self


class DescribeResourceUsageResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeResourceUsageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_list: List[DescribeResourceUsageResponseBodyDataList] = None,
        http_status_code: str = None,
        message: str = None,
        paginator: DescribeResourceUsageResponseBodyPaginator = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data_list = data_list
        self.http_status_code = http_status_code
        self.message = message
        self.paginator = paginator
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeResourceUsageResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Paginator') is not None:
            temp_model = DescribeResourceUsageResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeResourceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceUsageResponseBody = None,
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
            temp_model = DescribeResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServicePolicyRequest(TeaModel):
    def __init__(
        self,
        collection_name: str = None,
        service_name: str = None,
        space_id: str = None,
    ):
        self.collection_name = collection_name
        self.service_name = service_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeServicePolicyResponseBody(TeaModel):
    def __init__(
        self,
        collection_name: str = None,
        policy: str = None,
        policy_name: str = None,
        request_id: str = None,
        service_name: str = None,
        space_id: str = None,
    ):
        self.collection_name = collection_name
        self.policy = policy
        self.policy_name = policy_name
        self.request_id = request_id
        self.service_name = service_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeServicePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServicePolicyResponseBody = None,
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
            temp_model = DescribeServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpaceClientConfigRequest(TeaModel):
    def __init__(
        self,
        detail: str = None,
        space_id: str = None,
        workspace_id: int = None,
    ):
        self.detail = detail
        self.space_id = space_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DescribeSpaceClientConfigResponseBody(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        endpoint: str = None,
        file_upload_endpoint: str = None,
        name: str = None,
        private_key: str = None,
        request_id: str = None,
        space_id: str = None,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.file_upload_endpoint = file_upload_endpoint
        self.name = name
        self.private_key = private_key
        self.request_id = request_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_upload_endpoint is not None:
            result['FileUploadEndpoint'] = self.file_upload_endpoint
        if self.name is not None:
            result['Name'] = self.name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileUploadEndpoint') is not None:
            self.file_upload_endpoint = m.get('FileUploadEndpoint')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeSpaceClientConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSpaceClientConfigResponseBody = None,
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
            temp_model = DescribeSpaceClientConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpacesRequest(TeaModel):
    def __init__(
        self,
        emas_workspace_id: int = None,
        page_num: int = None,
        page_size: int = None,
        space_ids: List[str] = None,
        spec_code: str = None,
        tenant_id: str = None,
    ):
        self.emas_workspace_id = emas_workspace_id
        self.page_num = page_num
        self.page_size = page_size
        self.space_ids = space_ids
        self.spec_code = spec_code
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids is not None:
            result['SpaceIds'] = self.space_ids
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids = m.get('SpaceIds')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSpacesShrinkRequest(TeaModel):
    def __init__(
        self,
        emas_workspace_id: int = None,
        page_num: int = None,
        page_size: int = None,
        space_ids_shrink: str = None,
        spec_code: str = None,
        tenant_id: str = None,
    ):
        self.emas_workspace_id = emas_workspace_id
        self.page_num = page_num
        self.page_size = page_size
        self.space_ids_shrink = space_ids_shrink
        self.spec_code = spec_code
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids_shrink is not None:
            result['SpaceIds'] = self.space_ids_shrink
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids_shrink = m.get('SpaceIds')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSpacesResponseBodySpaces(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        charge_type: str = None,
        description: str = None,
        emas_workspace_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        name: str = None,
        order_type: str = None,
        package_end_date: str = None,
        package_start_date: str = None,
        package_status: str = None,
        renew_duration: str = None,
        service_status: str = None,
        space_id: str = None,
        spec_code: str = None,
    ):
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.description = description
        self.emas_workspace_id = emas_workspace_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.name = name
        self.order_type = order_type
        self.package_end_date = package_end_date
        self.package_start_date = package_start_date
        self.package_status = package_status
        self.renew_duration = renew_duration
        self.service_status = service_status
        self.space_id = space_id
        self.spec_code = spec_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.description is not None:
            result['Description'] = self.description
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.package_end_date is not None:
            result['PackageEndDate'] = self.package_end_date
        if self.package_start_date is not None:
            result['PackageStartDate'] = self.package_start_date
        if self.package_status is not None:
            result['PackageStatus'] = self.package_status
        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PackageEndDate') is not None:
            self.package_end_date = m.get('PackageEndDate')
        if m.get('PackageStartDate') is not None:
            self.package_start_date = m.get('PackageStartDate')
        if m.get('PackageStatus') is not None:
            self.package_status = m.get('PackageStatus')
        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        return self


class DescribeSpacesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        gmt_create: str = None,
        request_id: str = None,
        spaces: List[DescribeSpacesResponseBodySpaces] = None,
    ):
        self.count = count
        self.gmt_create = gmt_create
        self.request_id = request_id
        self.spaces = spaces

    def validate(self):
        if self.spaces:
            for k in self.spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['Spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spaces = []
        if m.get('Spaces') is not None:
            for k in m.get('Spaces'):
                temp_model = DescribeSpacesResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class DescribeSpacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSpacesResponseBody = None,
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
            temp_model = DescribeSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebHostingFileRequest(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        space_id: str = None,
    ):
        self.file_path = file_path
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeWebHostingFileResponseBodyData(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        etag: str = None,
        exists: bool = None,
        file_path: str = None,
        last_modified_time: int = None,
        signed_url: str = None,
        size: int = None,
    ):
        self.content_type = content_type
        self.etag = etag
        self.exists = exists
        self.file_path = file_path
        self.last_modified_time = last_modified_time
        self.signed_url = signed_url
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.exists is not None:
            result['Exists'] = self.exists
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeWebHostingFileResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeWebHostingFileResponseBodyData = None,
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
            temp_model = DescribeWebHostingFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebHostingFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebHostingFileResponseBody = None,
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
            temp_model = DescribeWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExtensionRequest(TeaModel):
    def __init__(
        self,
        extension_id: str = None,
    ):
        self.extension_id = extension_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')
        return self


class EnableExtensionResponseBody(TeaModel):
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


class EnableExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableExtensionResponseBody = None,
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
            temp_model = EnableExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        custom_domain: str = None,
        space_id: str = None,
    ):
        self.custom_domain = custom_domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingCertificateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expired_time: int = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_type: str = None,
        server_certificate_status: str = None,
    ):
        self.cert_domain_name = cert_domain_name
        self.cert_expired_time = cert_expired_time
        self.cert_life = cert_life
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.server_certificate_status = server_certificate_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expired_time is not None:
            result['CertExpiredTime'] = self.cert_expired_time
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpiredTime') is not None:
            self.cert_expired_time = m.get('CertExpiredTime')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        return self


class GetWebHostingCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWebHostingCertificateDetailResponseBodyData = None,
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
            temp_model = GetWebHostingCertificateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebHostingCertificateDetailResponseBody = None,
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
            temp_model = GetWebHostingCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        allowed_ips: str = None,
        default_domain: str = None,
        error_http_status: str = None,
        error_path: str = None,
        index_path: str = None,
        space_id: str = None,
    ):
        self.allowed_ips = allowed_ips
        self.default_domain = default_domain
        self.error_http_status = error_http_status
        self.error_path = error_path
        self.index_path = index_path
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ips is not None:
            result['AllowedIps'] = self.allowed_ips
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.error_http_status is not None:
            result['ErrorHttpStatus'] = self.error_http_status
        if self.error_path is not None:
            result['ErrorPath'] = self.error_path
        if self.index_path is not None:
            result['IndexPath'] = self.index_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedIps') is not None:
            self.allowed_ips = m.get('AllowedIps')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('ErrorHttpStatus') is not None:
            self.error_http_status = m.get('ErrorHttpStatus')
        if m.get('ErrorPath') is not None:
            self.error_path = m.get('ErrorPath')
        if m.get('IndexPath') is not None:
            self.index_path = m.get('IndexPath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWebHostingConfigResponseBodyData = None,
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
            temp_model = GetWebHostingConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebHostingConfigResponseBody = None,
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
            temp_model = GetWebHostingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingDomainVerificationContentRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        space_id: str = None,
    ):
        self.domain = domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingDomainVerificationContentResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        domain: str = None,
    ):
        self.content = content
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetWebHostingDomainVerificationContentResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWebHostingDomainVerificationContentResponseBodyData = None,
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
            temp_model = GetWebHostingDomainVerificationContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingDomainVerificationContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebHostingDomainVerificationContentResponseBody = None,
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
            temp_model = GetWebHostingDomainVerificationContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        status: str = None,
    ):
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWebHostingStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWebHostingStatusResponseBodyData = None,
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
            temp_model = GetWebHostingStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebHostingStatusResponseBody = None,
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
            temp_model = GetWebHostingStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingUploadCredentialRequest(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        space_id: str = None,
    ):
        self.file_path = file_path
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingUploadCredentialResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        endpoint: str = None,
        expired_time: int = None,
        file_path: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        self.access_key_id = access_key_id
        self.endpoint = endpoint
        self.expired_time = expired_time
        self.file_path = file_path
        self.policy = policy
        self.security_token = security_token
        self.signature = signature

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
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetWebHostingUploadCredentialResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWebHostingUploadCredentialResponseBodyData = None,
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
            temp_model = GetWebHostingUploadCredentialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWebHostingUploadCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebHostingUploadCredentialResponseBody = None,
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
            temp_model = GetWebHostingUploadCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorsDomainsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListCorsDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: str = None,
        domain_id: str = None,
    ):
        self.domain = domain
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class ListCorsDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: List[ListCorsDomainsResponseBodyDomains] = None,
        request_id: str = None,
    ):
        self.domains = domains
        self.request_id = request_id

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListCorsDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCorsDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCorsDomainsResponseBody = None,
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
            temp_model = ListCorsDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDingtalkOpenPlatformConfigsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListDingtalkOpenPlatformConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        create_time: str = None,
        update_time: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.create_time = create_time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDingtalkOpenPlatformConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[ListDingtalkOpenPlatformConfigsResponseBodyConfigs] = None,
        request_id: str = None,
    ):
        self.configs = configs
        self.request_id = request_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = ListDingtalkOpenPlatformConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDingtalkOpenPlatformConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDingtalkOpenPlatformConfigsResponseBody = None,
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
            temp_model = ListDingtalkOpenPlatformConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExtensionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExtensionsResponseBodyExtensions(TeaModel):
    def __init__(
        self,
        enabled: str = None,
        extension_desc: str = None,
        extension_documentation_link: str = None,
        extension_id: str = None,
        extension_name: str = None,
    ):
        self.enabled = enabled
        self.extension_desc = extension_desc
        self.extension_documentation_link = extension_documentation_link
        self.extension_id = extension_id
        self.extension_name = extension_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.extension_desc is not None:
            result['ExtensionDesc'] = self.extension_desc
        if self.extension_documentation_link is not None:
            result['ExtensionDocumentationLink'] = self.extension_documentation_link
        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id
        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExtensionDesc') is not None:
            self.extension_desc = m.get('ExtensionDesc')
        if m.get('ExtensionDocumentationLink') is not None:
            self.extension_documentation_link = m.get('ExtensionDocumentationLink')
        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')
        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')
        return self


class ListExtensionsResponseBody(TeaModel):
    def __init__(
        self,
        extensions: List[ListExtensionsResponseBodyExtensions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.extensions = extensions
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.extensions:
            for k in self.extensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Extensions'] = []
        if self.extensions is not None:
            for k in self.extensions:
                result['Extensions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extensions = []
        if m.get('Extensions') is not None:
            for k in m.get('Extensions'):
                temp_model = ListExtensionsResponseBodyExtensions()
                self.extensions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExtensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExtensionsResponseBody = None,
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
            temp_model = ListExtensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileRequest(TeaModel):
    def __init__(
        self,
        auth_delta: int = None,
        file_id: str = None,
        keyword: str = None,
        mode: str = None,
        next_token: str = None,
        page_size: int = None,
        prefix: str = None,
        space_id: str = None,
    ):
        self.auth_delta = auth_delta
        self.file_id = file_id
        self.keyword = keyword
        self.mode = mode
        self.next_token = next_token
        self.page_size = page_size
        self.prefix = prefix
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_delta is not None:
            result['AuthDelta'] = self.auth_delta
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthDelta') is not None:
            self.auth_delta = m.get('AuthDelta')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListFileResponseBodyDataList(TeaModel):
    def __init__(
        self,
        auth_delta: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        name: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.auth_delta = auth_delta
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_delta is not None:
            result['AuthDelta'] = self.auth_delta
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthDelta') is not None:
            self.auth_delta = m.get('AuthDelta')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListFileResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        page_size: int = None,
    ):
        self.next_token = next_token
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFileResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListFileResponseBodyDataList] = None,
        paginator: ListFileResponseBodyPaginator = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.paginator = paginator
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFileResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFileResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFileResponseBody = None,
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
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionRequest(TeaModel):
    def __init__(
        self,
        filter_by: str = None,
        page_num: int = None,
        page_size: int = None,
        space_id: str = None,
    ):
        self.filter_by = filter_by
        self.page_num = page_num
        self.page_size = page_size
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_by is not None:
            result['FilterBy'] = self.filter_by
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterBy') is not None:
            self.filter_by = m.get('FilterBy')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListFunctionResponseBodyDataListSpec(TeaModel):
    def __init__(
        self,
        instance_concurrency: int = None,
        memory: str = None,
        runtime: str = None,
        timeout: str = None,
    ):
        self.instance_concurrency = instance_concurrency
        self.memory = memory
        self.runtime = runtime
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class ListFunctionResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        desc: str = None,
        http_trigger_path: str = None,
        modified_at: str = None,
        name: str = None,
        spec: ListFunctionResponseBodyDataListSpec = None,
        timing_trigger_config: str = None,
    ):
        self.created_at = created_at
        self.desc = desc
        self.http_trigger_path = http_trigger_path
        self.modified_at = modified_at
        self.name = name
        self.spec = spec
        self.timing_trigger_config = timing_trigger_config

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Spec') is not None:
            temp_model = ListFunctionResponseBodyDataListSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        return self


class ListFunctionResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFunctionResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListFunctionResponseBodyDataList] = None,
        paginator: ListFunctionResponseBodyPaginator = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.paginator = paginator
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFunctionResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionResponseBody = None,
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
            temp_model = ListFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionDeploymentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        space_id: str = None,
        status: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionDeploymentResponseBodyDataListStatus(TeaModel):
    def __init__(
        self,
        label: str = None,
        status: str = None,
    ):
        self.label = label
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionDeploymentResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        deployment_id: str = None,
        download_signed_url: str = None,
        modified_at: str = None,
        status: ListFunctionDeploymentResponseBodyDataListStatus = None,
        version_no: str = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.download_signed_url = download_signed_url
        self.modified_at = modified_at
        self.status = status
        self.version_no = version_no

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.download_signed_url is not None:
            result['DownloadSignedUrl'] = self.download_signed_url
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.version_no is not None:
            result['VersionNo'] = self.version_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('DownloadSignedUrl') is not None:
            self.download_signed_url = m.get('DownloadSignedUrl')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Status') is not None:
            temp_model = ListFunctionDeploymentResponseBodyDataListStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')
        return self


class ListFunctionDeploymentResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFunctionDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListFunctionDeploymentResponseBodyDataList] = None,
        paginator: ListFunctionDeploymentResponseBodyPaginator = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.paginator = paginator
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionDeploymentResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFunctionDeploymentResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionDeploymentResponseBody = None,
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
            temp_model = ListFunctionDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionLogRequest(TeaModel):
    def __init__(
        self,
        from_date: int = None,
        log_request_id: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        space_id: str = None,
        status: str = None,
        to_date: int = None,
    ):
        self.from_date = from_date
        self.log_request_id = log_request_id
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.space_id = space_id
        self.status = status
        self.to_date = to_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        return self


class ListFunctionLogResponseBodyDataList(TeaModel):
    def __init__(
        self,
        contents: List[str] = None,
        function_name: str = None,
        levels: List[str] = None,
        request_id: str = None,
        space_id: str = None,
        status: str = None,
        timestamps: List[str] = None,
    ):
        self.contents = contents
        self.function_name = function_name
        self.levels = levels
        self.request_id = request_id
        self.space_id = space_id
        self.status = status
        self.timestamps = timestamps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')
        return self


class ListFunctionLogResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFunctionLogResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[ListFunctionLogResponseBodyDataList] = None,
        paginator: ListFunctionLogResponseBodyPaginator = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.paginator = paginator
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.paginator:
            self.paginator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionLogResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Paginator') is not None:
            temp_model = ListFunctionLogResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionLogResponseBody = None,
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
            temp_model = ListFunctionLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        platform: str = None,
        space_id: str = None,
    ):
        self.platform = platform
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListOpenPlatformConfigResponseBodySecretList(TeaModel):
    def __init__(
        self,
        app_cert: str = None,
        app_id: str = None,
        app_secret: str = None,
        platform: str = None,
        private_key: str = None,
        public_cert: str = None,
        public_key: str = None,
        root_cert: str = None,
        sign_mode: str = None,
        space_id: str = None,
    ):
        self.app_cert = app_cert
        self.app_id = app_id
        self.app_secret = app_secret
        self.platform = platform
        self.private_key = private_key
        self.public_cert = public_cert
        self.public_key = public_key
        self.root_cert = root_cert
        self.sign_mode = sign_mode
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cert is not None:
            result['AppCert'] = self.app_cert
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_cert is not None:
            result['PublicCert'] = self.public_cert
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.root_cert is not None:
            result['RootCert'] = self.root_cert
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCert') is not None:
            self.app_cert = m.get('AppCert')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicCert') is not None:
            self.public_cert = m.get('PublicCert')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RootCert') is not None:
            self.root_cert = m.get('RootCert')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListOpenPlatformConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_list: List[ListOpenPlatformConfigResponseBodySecretList] = None,
    ):
        self.request_id = request_id
        self.secret_list = secret_list

    def validate(self):
        if self.secret_list:
            for k in self.secret_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecretList'] = []
        if self.secret_list is not None:
            for k in self.secret_list:
                result['SecretList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.secret_list = []
        if m.get('SecretList') is not None:
            for k in m.get('SecretList'):
                temp_model = ListOpenPlatformConfigResponseBodySecretList()
                self.secret_list.append(temp_model.from_map(k))
        return self


class ListOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOpenPlatformConfigResponseBody = None,
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
            temp_model = ListOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpaceRequest(TeaModel):
    def __init__(
        self,
        emas_workspace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        space_ids: List[str] = None,
    ):
        self.emas_workspace_id = emas_workspace_id
        self.page_num = page_num
        self.page_size = page_size
        self.space_ids = space_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids is not None:
            result['SpaceIds'] = self.space_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids = m.get('SpaceIds')
        return self


class ListSpaceShrinkRequest(TeaModel):
    def __init__(
        self,
        emas_workspace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        space_ids_shrink: str = None,
    ):
        self.emas_workspace_id = emas_workspace_id
        self.page_num = page_num
        self.page_size = page_size
        self.space_ids_shrink = space_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emas_workspace_id is not None:
            result['EmasWorkspaceId'] = self.emas_workspace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_ids_shrink is not None:
            result['SpaceIds'] = self.space_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmasWorkspaceId') is not None:
            self.emas_workspace_id = m.get('EmasWorkspaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceIds') is not None:
            self.space_ids_shrink = m.get('SpaceIds')
        return self


class ListSpaceResponseBodySpaces(TeaModel):
    def __init__(
        self,
        desc: str = None,
        gmt_create: int = None,
        gmt_last_access: int = None,
        name: str = None,
        space_id: str = None,
        status: str = None,
    ):
        self.desc = desc
        self.gmt_create = gmt_create
        self.gmt_last_access = gmt_last_access
        self.name = name
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_last_access is not None:
            result['GmtLastAccess'] = self.gmt_last_access
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtLastAccess') is not None:
            self.gmt_last_access = m.get('GmtLastAccess')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSpaceResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        gmt_create: str = None,
        request_id: str = None,
        spaces: List[ListSpaceResponseBodySpaces] = None,
    ):
        self.count = count
        self.gmt_create = gmt_create
        self.request_id = request_id
        self.spaces = spaces

    def validate(self):
        if self.spaces:
            for k in self.spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['Spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spaces = []
        if m.get('Spaces') is not None:
            for k in m.get('Spaces'):
                temp_model = ListSpaceResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class ListSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSpaceResponseBody = None,
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
            temp_model = ListSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebHostingCustomDomainsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListWebHostingCustomDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        access_control_allow_origin: str = None,
        access_origin_control: bool = None,
        cname: str = None,
        create_time: int = None,
        description: str = None,
        domain: str = None,
        enable_cors: bool = None,
        force_redirect_type: str = None,
        ssl_protocol: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.access_control_allow_origin = access_control_allow_origin
        self.access_origin_control = access_origin_control
        self.cname = cname
        self.create_time = create_time
        self.description = description
        self.domain = domain
        self.enable_cors = enable_cors
        self.force_redirect_type = force_redirect_type
        self.ssl_protocol = ssl_protocol
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_origin_control is not None:
            result['AccessOriginControl'] = self.access_origin_control
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable_cors is not None:
            result['EnableCors'] = self.enable_cors
        if self.force_redirect_type is not None:
            result['ForceRedirectType'] = self.force_redirect_type
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessOriginControl') is not None:
            self.access_origin_control = m.get('AccessOriginControl')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnableCors') is not None:
            self.enable_cors = m.get('EnableCors')
        if m.get('ForceRedirectType') is not None:
            self.force_redirect_type = m.get('ForceRedirectType')
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListWebHostingCustomDomainsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListWebHostingCustomDomainsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWebHostingCustomDomainsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWebHostingCustomDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWebHostingCustomDomainsResponseBody = None,
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
            temp_model = ListWebHostingCustomDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebHostingFilesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        page_size: int = None,
        prefix: str = None,
        space_id: str = None,
    ):
        self.marker = marker
        self.page_size = page_size
        self.prefix = prefix
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListWebHostingFilesResponseBodyDataWebHostingFiles(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        etag: str = None,
        file_path: str = None,
        last_modified_time: int = None,
        signed_url: str = None,
        size: int = None,
    ):
        self.content_type = content_type
        self.etag = etag
        self.file_path = file_path
        self.last_modified_time = last_modified_time
        self.signed_url = signed_url
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListWebHostingFilesResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        next_marker: str = None,
        web_hosting_files: List[ListWebHostingFilesResponseBodyDataWebHostingFiles] = None,
    ):
        self.count = count
        self.next_marker = next_marker
        self.web_hosting_files = web_hosting_files

    def validate(self):
        if self.web_hosting_files:
            for k in self.web_hosting_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        result['WebHostingFiles'] = []
        if self.web_hosting_files is not None:
            for k in self.web_hosting_files:
                result['WebHostingFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        self.web_hosting_files = []
        if m.get('WebHostingFiles') is not None:
            for k in m.get('WebHostingFiles'):
                temp_model = ListWebHostingFilesResponseBodyDataWebHostingFiles()
                self.web_hosting_files.append(temp_model.from_map(k))
        return self


class ListWebHostingFilesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListWebHostingFilesResponseBodyData = None,
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
            temp_model = ListWebHostingFilesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWebHostingFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWebHostingFilesResponseBody = None,
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
            temp_model = ListWebHostingFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebHostingConfigRequest(TeaModel):
    def __init__(
        self,
        allowed_ips: str = None,
        error_http_status: str = None,
        error_path: str = None,
        index_path: str = None,
        space_id: str = None,
    ):
        self.allowed_ips = allowed_ips
        self.error_http_status = error_http_status
        self.error_path = error_path
        self.index_path = index_path
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_ips is not None:
            result['AllowedIps'] = self.allowed_ips
        if self.error_http_status is not None:
            result['ErrorHttpStatus'] = self.error_http_status
        if self.error_path is not None:
            result['ErrorPath'] = self.error_path
        if self.index_path is not None:
            result['IndexPath'] = self.index_path
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedIps') is not None:
            self.allowed_ips = m.get('AllowedIps')
        if m.get('ErrorHttpStatus') is not None:
            self.error_http_status = m.get('ErrorHttpStatus')
        if m.get('ErrorPath') is not None:
            self.error_path = m.get('ErrorPath')
        if m.get('IndexPath') is not None:
            self.index_path = m.get('IndexPath')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ModifyWebHostingConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebHostingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyWebHostingConfigResponseBody = None,
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
            temp_model = ModifyWebHostingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenServiceRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        space_id: str = None,
    ):
        self.service_name = service_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class OpenServiceResponseBody(TeaModel):
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


class OpenServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenServiceResponseBody = None,
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
            temp_model = OpenServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenWebHostingServiceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class OpenWebHostingServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenWebHostingServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenWebHostingServiceResponseBody = None,
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
            temp_model = OpenWebHostingServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBBackupCollectionsRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        space_id: str = None,
    ):
        self.backup_id = backup_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryDBBackupCollectionsResponseBody(TeaModel):
    def __init__(
        self,
        collections: List[str] = None,
        request_id: str = None,
    ):
        self.collections = collections
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collections is not None:
            result['Collections'] = self.collections
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDBBackupCollectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDBBackupCollectionsResponseBody = None,
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
            temp_model = QueryDBBackupCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBBackupDumpTimesRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryDBBackupDumpTimesResponseBodyBackupDumpTimes(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        dump_time: str = None,
    ):
        self.backup_id = backup_id
        self.dump_time = dump_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dump_time is not None:
            result['DumpTime'] = self.dump_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DumpTime') is not None:
            self.dump_time = m.get('DumpTime')
        return self


class QueryDBBackupDumpTimesResponseBody(TeaModel):
    def __init__(
        self,
        backup_dump_times: List[QueryDBBackupDumpTimesResponseBodyBackupDumpTimes] = None,
        request_id: str = None,
    ):
        self.backup_dump_times = backup_dump_times
        self.request_id = request_id

    def validate(self):
        if self.backup_dump_times:
            for k in self.backup_dump_times:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupDumpTimes'] = []
        if self.backup_dump_times is not None:
            for k in self.backup_dump_times:
                result['BackupDumpTimes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_dump_times = []
        if m.get('BackupDumpTimes') is not None:
            for k in m.get('BackupDumpTimes'):
                temp_model = QueryDBBackupDumpTimesResponseBodyBackupDumpTimes()
                self.backup_dump_times.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDBBackupDumpTimesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDBBackupDumpTimesResponseBody = None,
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
            temp_model = QueryDBBackupDumpTimesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBExportTaskStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        task_id: str = None,
    ):
        self.space_id = space_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBExportTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        detail_message: str = None,
        download_url: str = None,
        exported_count: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.detail_message = detail_message
        self.download_url = download_url
        self.exported_count = exported_count
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.exported_count is not None:
            result['ExportedCount'] = self.exported_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExportedCount') is not None:
            self.exported_count = m.get('ExportedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDBExportTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDBExportTaskStatusResponseBody = None,
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
            temp_model = QueryDBExportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBImportTaskStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        task_id: str = None,
    ):
        self.space_id = space_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBImportTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        detail_message: str = None,
        failed_count: str = None,
        request_id: str = None,
        status: str = None,
        success_count: str = None,
    ):
        self.detail_message = detail_message
        self.failed_count = failed_count
        self.request_id = request_id
        self.status = status
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryDBImportTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDBImportTaskStatusResponseBody = None,
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
            temp_model = QueryDBImportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBRestoreTaskStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        task_id: str = None,
    ):
        self.space_id = space_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBRestoreTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        detail_message: str = None,
        failed_count: int = None,
        request_id: str = None,
        status: str = None,
        success_count: int = None,
    ):
        self.detail_message = detail_message
        self.failed_count = failed_count
        self.request_id = request_id
        self.status = status
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryDBRestoreTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDBRestoreTaskStatusResponseBody = None,
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
            temp_model = QueryDBRestoreTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServiceStatusRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        space_id: str = None,
    ):
        self.service_name = service_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_status: str = None,
    ):
        self.request_id = request_id
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class QueryServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryServiceStatusResponseBody = None,
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
            temp_model = QueryServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySpaceConsumptionRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QuerySpaceConsumptionResponseBodyCsUsage(TeaModel):
    def __init__(
        self,
        cdn_traffic: int = None,
        download_count: int = None,
        storage_size: int = None,
        upload_count: int = None,
    ):
        self.cdn_traffic = cdn_traffic
        self.download_count = download_count
        self.storage_size = storage_size
        self.upload_count = upload_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.download_count is not None:
            result['DownloadCount'] = self.download_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.upload_count is not None:
            result['UploadCount'] = self.upload_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UploadCount') is not None:
            self.upload_count = m.get('UploadCount')
        return self


class QuerySpaceConsumptionResponseBodyDbUsage(TeaModel):
    def __init__(
        self,
        read_count: int = None,
        storage_size: int = None,
        write_count: int = None,
    ):
        self.read_count = read_count
        self.storage_size = storage_size
        self.write_count = write_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.write_count is not None:
            result['WriteCount'] = self.write_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('WriteCount') is not None:
            self.write_count = m.get('WriteCount')
        return self


class QuerySpaceConsumptionResponseBodyFcUsage(TeaModel):
    def __init__(
        self,
        cost: int = None,
        request_count: int = None,
        tx_traffic: int = None,
    ):
        self.cost = cost
        self.request_count = request_count
        self.tx_traffic = tx_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tx_traffic is not None:
            result['TxTraffic'] = self.tx_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TxTraffic') is not None:
            self.tx_traffic = m.get('TxTraffic')
        return self


class QuerySpaceConsumptionResponseBodyWhUsage(TeaModel):
    def __init__(
        self,
        cdn_traffic: int = None,
        storage_size: int = None,
    ):
        self.cdn_traffic = cdn_traffic
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class QuerySpaceConsumptionResponseBody(TeaModel):
    def __init__(
        self,
        cs_usage: QuerySpaceConsumptionResponseBodyCsUsage = None,
        cycle_end_time: int = None,
        cycle_start_time: int = None,
        db_usage: QuerySpaceConsumptionResponseBodyDbUsage = None,
        fc_usage: QuerySpaceConsumptionResponseBodyFcUsage = None,
        gmt_create: str = None,
        request_id: str = None,
        space_id: str = None,
        spec_code: str = None,
        wh_usage: QuerySpaceConsumptionResponseBodyWhUsage = None,
    ):
        self.cs_usage = cs_usage
        self.cycle_end_time = cycle_end_time
        self.cycle_start_time = cycle_start_time
        self.db_usage = db_usage
        self.fc_usage = fc_usage
        self.gmt_create = gmt_create
        self.request_id = request_id
        self.space_id = space_id
        self.spec_code = spec_code
        self.wh_usage = wh_usage

    def validate(self):
        if self.cs_usage:
            self.cs_usage.validate()
        if self.db_usage:
            self.db_usage.validate()
        if self.fc_usage:
            self.fc_usage.validate()
        if self.wh_usage:
            self.wh_usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs_usage is not None:
            result['CsUsage'] = self.cs_usage.to_map()
        if self.cycle_end_time is not None:
            result['CycleEndTime'] = self.cycle_end_time
        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time
        if self.db_usage is not None:
            result['DbUsage'] = self.db_usage.to_map()
        if self.fc_usage is not None:
            result['FcUsage'] = self.fc_usage.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.wh_usage is not None:
            result['WhUsage'] = self.wh_usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyCsUsage()
            self.cs_usage = temp_model.from_map(m['CsUsage'])
        if m.get('CycleEndTime') is not None:
            self.cycle_end_time = m.get('CycleEndTime')
        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')
        if m.get('DbUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyDbUsage()
            self.db_usage = temp_model.from_map(m['DbUsage'])
        if m.get('FcUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyFcUsage()
            self.fc_usage = temp_model.from_map(m['FcUsage'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('WhUsage') is not None:
            temp_model = QuerySpaceConsumptionResponseBodyWhUsage()
            self.wh_usage = temp_model.from_map(m['WhUsage'])
        return self


class QuerySpaceConsumptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySpaceConsumptionResponseBody = None,
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
            temp_model = QuerySpaceConsumptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySpaceSpecDetailRequest(TeaModel):
    def __init__(
        self,
        spec_code: str = None,
    ):
        self.spec_code = spec_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        return self


class QuerySpaceSpecDetailResponseBody(TeaModel):
    def __init__(
        self,
        cs_cdn_traffic: int = None,
        cs_download_count: int = None,
        cs_storage_size: int = None,
        cs_upload_count: int = None,
        db_read_count: int = None,
        db_storage_size: int = None,
        db_write_count: int = None,
        fc_cost: int = None,
        fc_request_count: int = None,
        fc_tx_traffic: int = None,
        gmt_create: str = None,
        request_id: str = None,
        spec_code: str = None,
        spec_detail_text: str = None,
        wh_cdn_traffic: int = None,
        wh_storage_size: int = None,
    ):
        self.cs_cdn_traffic = cs_cdn_traffic
        self.cs_download_count = cs_download_count
        self.cs_storage_size = cs_storage_size
        self.cs_upload_count = cs_upload_count
        self.db_read_count = db_read_count
        self.db_storage_size = db_storage_size
        self.db_write_count = db_write_count
        self.fc_cost = fc_cost
        self.fc_request_count = fc_request_count
        self.fc_tx_traffic = fc_tx_traffic
        self.gmt_create = gmt_create
        self.request_id = request_id
        self.spec_code = spec_code
        self.spec_detail_text = spec_detail_text
        self.wh_cdn_traffic = wh_cdn_traffic
        self.wh_storage_size = wh_storage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs_cdn_traffic is not None:
            result['CsCdnTraffic'] = self.cs_cdn_traffic
        if self.cs_download_count is not None:
            result['CsDownloadCount'] = self.cs_download_count
        if self.cs_storage_size is not None:
            result['CsStorageSize'] = self.cs_storage_size
        if self.cs_upload_count is not None:
            result['CsUploadCount'] = self.cs_upload_count
        if self.db_read_count is not None:
            result['DbReadCount'] = self.db_read_count
        if self.db_storage_size is not None:
            result['DbStorageSize'] = self.db_storage_size
        if self.db_write_count is not None:
            result['DbWriteCount'] = self.db_write_count
        if self.fc_cost is not None:
            result['FcCost'] = self.fc_cost
        if self.fc_request_count is not None:
            result['FcRequestCount'] = self.fc_request_count
        if self.fc_tx_traffic is not None:
            result['FcTxTraffic'] = self.fc_tx_traffic
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.spec_detail_text is not None:
            result['SpecDetailText'] = self.spec_detail_text
        if self.wh_cdn_traffic is not None:
            result['WhCdnTraffic'] = self.wh_cdn_traffic
        if self.wh_storage_size is not None:
            result['WhStorageSize'] = self.wh_storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsCdnTraffic') is not None:
            self.cs_cdn_traffic = m.get('CsCdnTraffic')
        if m.get('CsDownloadCount') is not None:
            self.cs_download_count = m.get('CsDownloadCount')
        if m.get('CsStorageSize') is not None:
            self.cs_storage_size = m.get('CsStorageSize')
        if m.get('CsUploadCount') is not None:
            self.cs_upload_count = m.get('CsUploadCount')
        if m.get('DbReadCount') is not None:
            self.db_read_count = m.get('DbReadCount')
        if m.get('DbStorageSize') is not None:
            self.db_storage_size = m.get('DbStorageSize')
        if m.get('DbWriteCount') is not None:
            self.db_write_count = m.get('DbWriteCount')
        if m.get('FcCost') is not None:
            self.fc_cost = m.get('FcCost')
        if m.get('FcRequestCount') is not None:
            self.fc_request_count = m.get('FcRequestCount')
        if m.get('FcTxTraffic') is not None:
            self.fc_tx_traffic = m.get('FcTxTraffic')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('SpecDetailText') is not None:
            self.spec_detail_text = m.get('SpecDetailText')
        if m.get('WhCdnTraffic') is not None:
            self.wh_cdn_traffic = m.get('WhCdnTraffic')
        if m.get('WhStorageSize') is not None:
            self.wh_storage_size = m.get('WhStorageSize')
        return self


class QuerySpaceSpecDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySpaceSpecDetailResponseBody = None,
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
            temp_model = QuerySpaceSpecDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySpaceUsageRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        space_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.interval = interval
        self.space_id = space_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage(TeaModel):
    def __init__(
        self,
        cdn_traffic: int = None,
        download_count: int = None,
        storage_size: int = None,
        upload_count: int = None,
    ):
        self.cdn_traffic = cdn_traffic
        self.download_count = download_count
        self.storage_size = storage_size
        self.upload_count = upload_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.download_count is not None:
            result['DownloadCount'] = self.download_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.upload_count is not None:
            result['UploadCount'] = self.upload_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UploadCount') is not None:
            self.upload_count = m.get('UploadCount')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage(TeaModel):
    def __init__(
        self,
        read_count: int = None,
        storage_size: int = None,
        write_count: int = None,
    ):
        self.read_count = read_count
        self.storage_size = storage_size
        self.write_count = write_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.write_count is not None:
            result['WriteCount'] = self.write_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('WriteCount') is not None:
            self.write_count = m.get('WriteCount')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage(TeaModel):
    def __init__(
        self,
        cost: int = None,
        request_count: int = None,
        tx_traffic: int = None,
    ):
        self.cost = cost
        self.request_count = request_count
        self.tx_traffic = tx_traffic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.tx_traffic is not None:
            result['TxTraffic'] = self.tx_traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('TxTraffic') is not None:
            self.tx_traffic = m.get('TxTraffic')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage(TeaModel):
    def __init__(
        self,
        cdn_traffic: int = None,
        storage_size: int = None,
    ):
        self.cdn_traffic = cdn_traffic
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_traffic is not None:
            result['CdnTraffic'] = self.cdn_traffic
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnTraffic') is not None:
            self.cdn_traffic = m.get('CdnTraffic')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class QuerySpaceUsageResponseBodySpaceUsageDataList(TeaModel):
    def __init__(
        self,
        cs_usage: QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage = None,
        db_usage: QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage = None,
        effective_bill_flag: bool = None,
        fc_usage: QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage = None,
        timestamp: str = None,
        wh_usage: QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage = None,
    ):
        self.cs_usage = cs_usage
        self.db_usage = db_usage
        # 标记该数据是否出账。
        # - true：正常出账。
        # - false：不出账，例如在空间停服的情况下，用量数据不用于出账。
        self.effective_bill_flag = effective_bill_flag
        self.fc_usage = fc_usage
        self.timestamp = timestamp
        self.wh_usage = wh_usage

    def validate(self):
        if self.cs_usage:
            self.cs_usage.validate()
        if self.db_usage:
            self.db_usage.validate()
        if self.fc_usage:
            self.fc_usage.validate()
        if self.wh_usage:
            self.wh_usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cs_usage is not None:
            result['CsUsage'] = self.cs_usage.to_map()
        if self.db_usage is not None:
            result['DbUsage'] = self.db_usage.to_map()
        if self.effective_bill_flag is not None:
            result['EffectiveBillFlag'] = self.effective_bill_flag
        if self.fc_usage is not None:
            result['FcUsage'] = self.fc_usage.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.wh_usage is not None:
            result['WhUsage'] = self.wh_usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListCsUsage()
            self.cs_usage = temp_model.from_map(m['CsUsage'])
        if m.get('DbUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListDbUsage()
            self.db_usage = temp_model.from_map(m['DbUsage'])
        if m.get('EffectiveBillFlag') is not None:
            self.effective_bill_flag = m.get('EffectiveBillFlag')
        if m.get('FcUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListFcUsage()
            self.fc_usage = temp_model.from_map(m['FcUsage'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('WhUsage') is not None:
            temp_model = QuerySpaceUsageResponseBodySpaceUsageDataListWhUsage()
            self.wh_usage = temp_model.from_map(m['WhUsage'])
        return self


class QuerySpaceUsageResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        space_id: str = None,
        space_usage_data_list: List[QuerySpaceUsageResponseBodySpaceUsageDataList] = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.space_id = space_id
        self.space_usage_data_list = space_usage_data_list
        self.start_time = start_time

    def validate(self):
        if self.space_usage_data_list:
            for k in self.space_usage_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        result['SpaceUsageDataList'] = []
        if self.space_usage_data_list is not None:
            for k in self.space_usage_data_list:
                result['SpaceUsageDataList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        self.space_usage_data_list = []
        if m.get('SpaceUsageDataList') is not None:
            for k in m.get('SpaceUsageDataList'):
                temp_model = QuerySpaceUsageResponseBodySpaceUsageDataList()
                self.space_usage_data_list.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QuerySpaceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySpaceUsageResponseBody = None,
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
            temp_model = QuerySpaceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebHostingCustomDomainCacheRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        space_id: str = None,
    ):
        self.domain_name = domain_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RefreshWebHostingCustomDomainCacheResponseBody(TeaModel):
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


class RefreshWebHostingCustomDomainCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshWebHostingCustomDomainCacheResponseBody = None,
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
            temp_model = RefreshWebHostingCustomDomainCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        space_id: str = None,
    ):
        self.id = id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RegisterFileResponseBody(TeaModel):
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


class RegisterFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterFileResponseBody = None,
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
            temp_model = RegisterFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDBCollectionRequest(TeaModel):
    def __init__(
        self,
        new_collection: str = None,
        origin_collection: str = None,
        space_id: str = None,
    ):
        self.new_collection = new_collection
        self.origin_collection = origin_collection
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_collection is not None:
            result['NewCollection'] = self.new_collection
        if self.origin_collection is not None:
            result['OriginCollection'] = self.origin_collection
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewCollection') is not None:
            self.new_collection = m.get('NewCollection')
        if m.get('OriginCollection') is not None:
            self.origin_collection = m.get('OriginCollection')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RenameDBCollectionResponseBody(TeaModel):
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


class RenameDBCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameDBCollectionResponseBody = None,
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
            temp_model = RenameDBCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetServerSecretRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ResetServerSecretResponseBody(TeaModel):
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


class ResetServerSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetServerSecretResponseBody = None,
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
            temp_model = ResetServerSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunDBCommandRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        space_id: str = None,
    ):
        self.body = body
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RunDBCommandResponseBody(TeaModel):
    def __init__(
        self,
        affected_docs: int = None,
        request_id: str = None,
        result: str = None,
    ):
        self.affected_docs = affected_docs
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_docs is not None:
            result['AffectedDocs'] = self.affected_docs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedDocs') is not None:
            self.affected_docs = m.get('AffectedDocs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RunDBCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunDBCommandResponseBody = None,
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
            temp_model = RunDBCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunFunctionRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        space_id: str = None,
    ):
        self.body = body
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RunFunctionResponseBodyRuntimeMeta(TeaModel):
    def __init__(
        self,
        billing_duration: int = None,
        invocation_duration: int = None,
        max_memory_usage: int = None,
        request_id: str = None,
    ):
        self.billing_duration = billing_duration
        self.invocation_duration = invocation_duration
        self.max_memory_usage = max_memory_usage
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_duration is not None:
            result['BillingDuration'] = self.billing_duration
        if self.invocation_duration is not None:
            result['InvocationDuration'] = self.invocation_duration
        if self.max_memory_usage is not None:
            result['MaxMemoryUsage'] = self.max_memory_usage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingDuration') is not None:
            self.billing_duration = m.get('BillingDuration')
        if m.get('InvocationDuration') is not None:
            self.invocation_duration = m.get('InvocationDuration')
        if m.get('MaxMemoryUsage') is not None:
            self.max_memory_usage = m.get('MaxMemoryUsage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        runtime_meta: RunFunctionResponseBodyRuntimeMeta = None,
    ):
        self.request_id = request_id
        self.result = result
        self.runtime_meta = runtime_meta

    def validate(self):
        if self.runtime_meta:
            self.runtime_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.runtime_meta is not None:
            result['RuntimeMeta'] = self.runtime_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RuntimeMeta') is not None:
            temp_model = RunFunctionResponseBodyRuntimeMeta()
            self.runtime_meta = temp_model.from_map(m['RuntimeMeta'])
        return self


class RunFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunFunctionResponseBody = None,
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
            temp_model = RunFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAntOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_cert: str = None,
        app_id: str = None,
        private_key: str = None,
        public_cert: str = None,
        public_key: str = None,
        root_cert: str = None,
        sign_mode: str = None,
        space_id: str = None,
    ):
        self.app_cert = app_cert
        self.app_id = app_id
        self.private_key = private_key
        self.public_cert = public_cert
        self.public_key = public_key
        self.root_cert = root_cert
        self.sign_mode = sign_mode
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cert is not None:
            result['AppCert'] = self.app_cert
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_cert is not None:
            result['PublicCert'] = self.public_cert
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.root_cert is not None:
            result['RootCert'] = self.root_cert
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCert') is not None:
            self.app_cert = m.get('AppCert')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicCert') is not None:
            self.public_cert = m.get('PublicCert')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RootCert') is not None:
            self.root_cert = m.get('RootCert')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveAntOpenPlatformConfigResponseBody(TeaModel):
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


class SaveAntOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveAntOpenPlatformConfigResponseBody = None,
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
            temp_model = SaveAntOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAppAuthTokenRequest(TeaModel):
    def __init__(
        self,
        app_auth_token: str = None,
        app_id: str = None,
        isv_app_id: str = None,
        space_id: str = None,
    ):
        self.app_auth_token = app_auth_token
        self.app_id = app_id
        self.isv_app_id = isv_app_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_auth_token is not None:
            result['AppAuthToken'] = self.app_auth_token
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.isv_app_id is not None:
            result['IsvAppId'] = self.isv_app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppAuthToken') is not None:
            self.app_auth_token = m.get('AppAuthToken')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IsvAppId') is not None:
            self.isv_app_id = m.get('IsvAppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveAppAuthTokenResponseBody(TeaModel):
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


class SaveAppAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveAppAuthTokenResponseBody = None,
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
            temp_model = SaveAppAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveCdnDomainConfigRequest(TeaModel):
    def __init__(
        self,
        auth_config: str = None,
        cors_config: str = None,
        ip_config: str = None,
        referer_config: str = None,
        space_id: str = None,
        tenant_id: str = None,
        type: str = None,
        ua_config: str = None,
    ):
        self.auth_config = auth_config
        self.cors_config = cors_config
        self.ip_config = ip_config
        self.referer_config = referer_config
        self.space_id = space_id
        self.tenant_id = tenant_id
        self.type = type
        self.ua_config = ua_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config
        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config
        if self.ip_config is not None:
            result['IpConfig'] = self.ip_config
        if self.referer_config is not None:
            result['RefererConfig'] = self.referer_config
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.ua_config is not None:
            result['UaConfig'] = self.ua_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfig') is not None:
            self.auth_config = m.get('AuthConfig')
        if m.get('CorsConfig') is not None:
            self.cors_config = m.get('CorsConfig')
        if m.get('IpConfig') is not None:
            self.ip_config = m.get('IpConfig')
        if m.get('RefererConfig') is not None:
            self.referer_config = m.get('RefererConfig')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UaConfig') is not None:
            self.ua_config = m.get('UaConfig')
        return self


class SaveCdnDomainConfigResponseBody(TeaModel):
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


class SaveCdnDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveCdnDomainConfigResponseBody = None,
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
            temp_model = SaveCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebHostingCustomDomainConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        force_redirect_type: str = None,
        space_id: str = None,
    ):
        self.domain_name = domain_name
        self.force_redirect_type = force_redirect_type
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_redirect_type is not None:
            result['ForceRedirectType'] = self.force_redirect_type
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceRedirectType') is not None:
            self.force_redirect_type = m.get('ForceRedirectType')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveWebHostingCustomDomainConfigResponseBody(TeaModel):
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


class SaveWebHostingCustomDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveWebHostingCustomDomainConfigResponseBody = None,
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
            temp_model = SaveWebHostingCustomDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebHostingCustomDomainCorsConfigRequest(TeaModel):
    def __init__(
        self,
        access_control_allow_origin: str = None,
        access_origin_control: bool = None,
        domain_name: str = None,
        enable_cors: bool = None,
        space_id: str = None,
    ):
        self.access_control_allow_origin = access_control_allow_origin
        self.access_origin_control = access_origin_control
        self.domain_name = domain_name
        self.enable_cors = enable_cors
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_origin_control is not None:
            result['AccessOriginControl'] = self.access_origin_control
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable_cors is not None:
            result['EnableCors'] = self.enable_cors
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessOriginControl') is not None:
            self.access_origin_control = m.get('AccessOriginControl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EnableCors') is not None:
            self.enable_cors = m.get('EnableCors')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveWebHostingCustomDomainCorsConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveWebHostingCustomDomainCorsConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveWebHostingCustomDomainCorsConfigResponseBody = None,
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
            temp_model = SaveWebHostingCustomDomainCorsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWechatOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class SaveWechatOpenPlatformConfigResponseBody(TeaModel):
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


class SaveWechatOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveWechatOpenPlatformConfigResponseBody = None,
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
            temp_model = SaveWechatOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindWebHostingCustomDomainRequest(TeaModel):
    def __init__(
        self,
        custom_domain: str = None,
        space_id: str = None,
    ):
        self.custom_domain = custom_domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UnbindWebHostingCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindWebHostingCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindWebHostingCustomDomainResponseBody = None,
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
            temp_model = UnbindWebHostingCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateDingtalkOpenPlatformConfigResponseBody(TeaModel):
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


class UpdateDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDingtalkOpenPlatformConfigResponseBody = None,
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
            temp_model = UpdateDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        http_trigger_path: str = None,
        instance_concurrency: int = None,
        memory: int = None,
        name: str = None,
        runtime: str = None,
        space_id: str = None,
        timeout: int = None,
        timing_trigger_config: str = None,
        timing_trigger_user_payload: str = None,
    ):
        self.desc = desc
        self.http_trigger_path = http_trigger_path
        self.instance_concurrency = instance_concurrency
        self.memory = memory
        self.name = name
        self.runtime = runtime
        self.space_id = space_id
        self.timeout = timeout
        self.timing_trigger_config = timing_trigger_config
        self.timing_trigger_user_payload = timing_trigger_user_payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.timing_trigger_user_payload is not None:
            result['TimingTriggerUserPayload'] = self.timing_trigger_user_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('TimingTriggerUserPayload') is not None:
            self.timing_trigger_user_payload = m.get('TimingTriggerUserPayload')
        return self


class UpdateFunctionResponseBodySpec(TeaModel):
    def __init__(
        self,
        instance_concurrency: int = None,
        memory: str = None,
        runtime: str = None,
        timeout: str = None,
    ):
        self.instance_concurrency = instance_concurrency
        self.memory = memory
        self.runtime = runtime
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        desc: str = None,
        http_trigger_path: str = None,
        modified_at: str = None,
        name: str = None,
        request_id: str = None,
        spec: UpdateFunctionResponseBodySpec = None,
        timing_trigger_config: str = None,
        timing_trigger_user_payload: str = None,
    ):
        self.created_at = created_at
        self.desc = desc
        self.http_trigger_path = http_trigger_path
        self.modified_at = modified_at
        self.name = name
        self.request_id = request_id
        self.spec = spec
        self.timing_trigger_config = timing_trigger_config
        self.timing_trigger_user_payload = timing_trigger_user_payload

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.timing_trigger_user_payload is not None:
            result['TimingTriggerUserPayload'] = self.timing_trigger_user_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            temp_model = UpdateFunctionResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('TimingTriggerUserPayload') is not None:
            self.timing_trigger_user_payload = m.get('TimingTriggerUserPayload')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionResponseBody = None,
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
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpTriggerConfigRequest(TeaModel):
    def __init__(
        self,
        custom_domain: str = None,
        custom_domain_certificate: str = None,
        custom_domain_private_key: str = None,
        enable_service: bool = None,
        space_id: str = None,
    ):
        self.custom_domain = custom_domain
        self.custom_domain_certificate = custom_domain_certificate
        self.custom_domain_private_key = custom_domain_private_key
        self.enable_service = enable_service
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate is not None:
            result['CustomDomainCertificate'] = self.custom_domain_certificate
        if self.custom_domain_private_key is not None:
            result['CustomDomainPrivateKey'] = self.custom_domain_private_key
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificate') is not None:
            self.custom_domain_certificate = m.get('CustomDomainCertificate')
        if m.get('CustomDomainPrivateKey') is not None:
            self.custom_domain_private_key = m.get('CustomDomainPrivateKey')
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateHttpTriggerConfigResponseBody(TeaModel):
    def __init__(
        self,
        custom_domain: str = None,
        custom_domain_certificate_info: str = None,
        custom_domain_cname: str = None,
        default_endpoint: str = None,
        enable_service: bool = None,
        request_id: str = None,
    ):
        self.custom_domain = custom_domain
        self.custom_domain_certificate_info = custom_domain_certificate_info
        self.custom_domain_cname = custom_domain_cname
        self.default_endpoint = default_endpoint
        self.enable_service = enable_service
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate_info is not None:
            result['CustomDomainCertificateInfo'] = self.custom_domain_certificate_info
        if self.custom_domain_cname is not None:
            result['CustomDomainCname'] = self.custom_domain_cname
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificateInfo') is not None:
            self.custom_domain_certificate_info = m.get('CustomDomainCertificateInfo')
        if m.get('CustomDomainCname') is not None:
            self.custom_domain_cname = m.get('CustomDomainCname')
        if m.get('DefaultEndpoint') is not None:
            self.default_endpoint = m.get('DefaultEndpoint')
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateHttpTriggerConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHttpTriggerConfigResponseBody = None,
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
            temp_model = UpdateHttpTriggerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServicePolicyRequest(TeaModel):
    def __init__(
        self,
        collection_name: str = None,
        policy: str = None,
        policy_name: str = None,
        service_name: str = None,
        space_id: str = None,
    ):
        self.collection_name = collection_name
        self.policy = policy
        self.policy_name = policy_name
        self.service_name = service_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateServicePolicyResponseBody(TeaModel):
    def __init__(
        self,
        collection_name: str = None,
        policy: str = None,
        policy_name: str = None,
        request_id: str = None,
        service_name: str = None,
        space_id: str = None,
    ):
        self.collection_name = collection_name
        self.policy = policy
        self.policy_name = policy_name
        self.request_id = request_id
        self.service_name = service_name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateServicePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServicePolicyResponseBody = None,
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
            temp_model = UpdateServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSpaceRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        space_id: str = None,
        status: str = None,
    ):
        self.desc = desc
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateSpaceResponseBody(TeaModel):
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


class UpdateSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSpaceResponseBody = None,
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
            temp_model = UpdateSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyWebHostingDomainOwnerRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        space_id: str = None,
        verify_type: str = None,
    ):
        self.domain = domain
        self.space_id = space_id
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyWebHostingDomainOwnerResponseBody(TeaModel):
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


class VerifyWebHostingDomainOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyWebHostingDomainOwnerResponseBody = None,
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
            temp_model = VerifyWebHostingDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


