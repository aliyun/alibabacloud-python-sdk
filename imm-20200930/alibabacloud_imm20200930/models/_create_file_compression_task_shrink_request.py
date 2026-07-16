# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileCompressionTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        compressed_format: str = None,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        source_manifest_uri: str = None,
        sources_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # The compression format for file packaging.
        # 
        # > Currently, only the zip format is supported.
        self.compressed_format = compressed_format
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The chained authorization configuration. This parameter is not required. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The message notification configuration. For more information, see the Notification data type. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # > IMM API callbacks do not currently support specifying a webhook address. Use MNS instead.
        self.notification_shrink = notification_shrink
        # The name of the project. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The address where the file manifest is stored. The file manifest stores the \\`Sources\\` structure in JSON format on OSS. This is suitable for scenarios with many files to package.
        # 
        # > Specify either this parameter or `Sources`. In the manifest file, the `URI` parameter is required and the `Alias` parameter is optional. \\`SourceManifestURI\\` supports up to 80,000 packaging rules.
        # > >Warning: When you save the content to OSS, specify the OSS address of the file for this parameter.
        # 
        # The following is an example of the file structure:
        # 
        # ```
        # [{"URI":"oss://<bucket>/<object>", "Alias":"/new-dir/new-name"}]
        # ```
        self.source_manifest_uri = source_manifest_uri
        # A list of files to package and their packaging rules.
        # 
        # > Specify either this parameter or \\`SourceManifestURI\\`. \\`Sources\\` supports a maximum of 100 packaging rules.
        # > >Warning: If you have more than 100 packaging rules, use the \\`SourceManifestURI\\` parameter.
        self.sources_shrink = sources_shrink
        # The OSS address of the output file. The compressed file is named after the file name in this path, such as `name.zip`.
        # 
        # The OSS address must be in the \\`oss\\://${Bucket}/${Object}\\` format. \\`${Bucket}\\` is the name of the OSS bucket that is in the same region as the current project. \\`${Object}\\` is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # Custom user data. This data is returned in the asynchronous notification message, which helps you associate the notification with your internal system. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compressed_format is not None:
            result['CompressedFormat'] = self.compressed_format

        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_manifest_uri is not None:
            result['SourceManifestURI'] = self.source_manifest_uri

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressedFormat') is not None:
            self.compressed_format = m.get('CompressedFormat')

        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceManifestURI') is not None:
            self.source_manifest_uri = m.get('SourceManifestURI')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

