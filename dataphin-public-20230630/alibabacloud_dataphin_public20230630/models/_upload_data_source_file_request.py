# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UploadDataSourceFileRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        upload_command: main_models.UploadDataSourceFileRequestUploadCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id
        # The request object for uploading a datasource authentication file.
        # 
        # This parameter is required.
        self.upload_command = upload_command

    def validate(self):
        if self.upload_command:
            self.upload_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.upload_command is not None:
            result['UploadCommand'] = self.upload_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('UploadCommand') is not None:
            temp_model = main_models.UploadDataSourceFileRequestUploadCommand()
            self.upload_command = temp_model.from_map(m.get('UploadCommand'))

        return self

class UploadDataSourceFileRequestUploadCommand(DaraModel):
    def __init__(
        self,
        file_content_base_64: str = None,
        file_name: str = None,
    ):
        # The Base64-encoded file content. The decoded file size must be between 0 and 5 MB.
        # 
        # This parameter is required.
        self.file_content_base_64 = file_content_base_64
        # The file name, including the extension. The extension is validated against a whitelist. Supported extensions: jar, xml, conf, keytab, jks, rsa, pem, yaml, keystore, properties, and key.
        # 
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_content_base_64 is not None:
            result['FileContentBase64'] = self.file_content_base_64

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContentBase64') is not None:
            self.file_content_base_64 = m.get('FileContentBase64')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

