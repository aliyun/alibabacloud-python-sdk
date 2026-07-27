# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class UploadMaterialFileForAdminResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.UploadMaterialFileForAdminResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason why access is denied.
        self.access_denied_detail = access_denied_detail
        # Indicates whether a retry is allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message.
        self.dynamic_message = dynamic_message
        # The error parameters returned.
        self.error_args = error_args
        # The file object.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The error message.
        self.root_error_msg = root_error_msg
        # Indicates whether the request is processed synchronously.
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
            temp_model = main_models.UploadMaterialFileForAdminResponseBodyModule()
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

class UploadMaterialFileForAdminResponseBodyModule(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        content_type: str = None,
        create_time: str = None,
        deleted_time: str = None,
        directory_id: str = None,
        file_id: str = None,
        file_url: str = None,
        height: int = None,
        name: str = None,
        status: str = None,
        storage_size: str = None,
        suffix: str = None,
        type: str = None,
        width: int = None,
    ):
        # The business instance ID.
        self.biz_id = biz_id
        # The file content type.
        self.content_type = content_type
        # The creation time.
        self.create_time = create_time
        # The time when the file was moved to the recycle bin or deleted.
        self.deleted_time = deleted_time
        # The directory ID.
        self.directory_id = directory_id
        # The unique ID of the file.
        self.file_id = file_id
        # The file path.
        self.file_url = file_url
        # The height.
        self.height = height
        # The file name.
        self.name = name
        # The file status.
        self.status = status
        # The file size.
        self.storage_size = storage_size
        # The file suffix.
        self.suffix = suffix
        # The file type.
        self.type = type
        # The width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.height is not None:
            result['Height'] = self.height

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        if self.type is not None:
            result['Type'] = self.type

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

