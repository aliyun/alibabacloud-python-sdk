# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateArchiveFileInspectionTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        password: str = None,
        project_name: str = None,
        source_uri: str = None,
        user_data: str = None,
    ):
        # **Leave this parameter empty if you do not have special requirements.**
        # 
        # The configuration for chained authorization. This parameter is not required. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The notification configuration. For more information, see Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # > Currently, API callbacks in IMM do not support custom webhook addresses. Use MNS instead.
        self.notification_shrink = notification_shrink
        # The password of the compressed file. If the file is encrypted, provide the password to inspect its contents.
        self.password = password
        # The project name. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The location of the compressed file.
        # 
        # The Object Storage Service (OSS) URI must be in the oss\\://${Bucket}/${Object} format. In this format, `${Bucket}` is the name of the OSS bucket that is in the same region as the current project, and `${Object}` is the full path of the file, including the file name extension.
        self.source_uri = source_uri
        # Custom information that is returned in the asynchronous notification message. You can use this information to associate the notification message with your services. The maximum length is 2,048 bytes.
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

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

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

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

