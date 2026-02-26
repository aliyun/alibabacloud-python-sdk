# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateFileUncompressionTaskRequest(DaraModel):
    def __init__(
        self,
        credential_config: main_models.CredentialConfig = None,
        notification: main_models.Notification = None,
        password: str = None,
        project_name: str = None,
        selected_files: List[str] = None,
        source_uri: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # >  The IMM operation does not support a callback URL. We recommend that you use Simple Message Queue (SMQ) to receive notifications.
        self.notification = notification
        # The password that protects the package.
        self.password = password
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The files to extract. If you do not specify this parameter, the entire package is decompressed.
        self.selected_files = selected_files
        # The OSS URI of the package.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The OSS URI to which you want to extract files from the package or decompress the entire package.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        self.target_uri = target_uri
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum length of the value is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.password is not None:
            result['Password'] = self.password

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.selected_files is not None:
            result['SelectedFiles'] = self.selected_files

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SelectedFiles') is not None:
            self.selected_files = m.get('SelectedFiles')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

