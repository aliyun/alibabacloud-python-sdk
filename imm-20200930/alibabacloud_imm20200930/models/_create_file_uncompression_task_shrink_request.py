# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileUncompressionTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        password: str = None,
        project_name: str = None,
        selected_files_shrink: str = None,
        source_uri: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # **Leave this parameter empty unless you have specific requirements.**
        # 
        # The chained authorization configuration. This parameter is optional. For more information, see [Use chained authorization to access other entity resources](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The message notification configuration. For details, click Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # > Intelligent Media Management API callbacks do not support custom webhook addresses. Use MNS instead.
        self.notification_shrink = notification_shrink
        # The password for the encrypted compressed package.
        self.password = password
        # The name of the project. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The list of files to decompress. If this parameter is empty, the entire compressed package is decompressed. The default value is empty.
        self.selected_files_shrink = selected_files_shrink
        # The Object Storage Service (OSS) address where the compressed file is stored.
        # 
        # The OSS address must be in the \\`oss\\://${Bucket}/${Object}\\` format. \\`${Bucket}\\` is the name of the OSS bucket in the same region as the current project. \\`${Object}\\` is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The destination OSS address for the decompressed files. The selected files or the entire compressed package are decompressed to this address.
        # 
        # The OSS address must be in the \\`oss\\://${Bucket}/${Object}\\` format. \\`${Bucket}\\` is the name of the OSS bucket in the same region as the current project. \\`${Object}\\` is the full path of the file, including the file name extension.
        self.target_uri = target_uri
        # Custom user information. It is returned in the asynchronous notification message to help you associate the notification with your system. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.password is not None:
            result['Password'] = self.password

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.selected_files_shrink is not None:
            result['SelectedFiles'] = self.selected_files_shrink

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
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SelectedFiles') is not None:
            self.selected_files_shrink = m.get('SelectedFiles')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

