# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateFileCompressionTaskRequest(DaraModel):
    def __init__(
        self,
        compressed_format: str = None,
        credential_config: main_models.CredentialConfig = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        source_manifest_uri: str = None,
        sources: List[main_models.CreateFileCompressionTaskRequestSources] = None,
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
        self.credential_config = credential_config
        # The message notification configuration. For more information, see the Notification data type. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # > IMM API callbacks do not currently support specifying a webhook address. Use MNS instead.
        self.notification = notification
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
        self.sources = sources
        # The OSS address of the output file. The compressed file is named after the file name in this path, such as `name.zip`.
        # 
        # The OSS address must be in the \\`oss\\://${Bucket}/${Object}\\` format. \\`${Bucket}\\` is the name of the OSS bucket that is in the same region as the current project. \\`${Object}\\` is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # Custom user data. This data is returned in the asynchronous notification message, which helps you associate the notification with your internal system. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compressed_format is not None:
            result['CompressedFormat'] = self.compressed_format

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_manifest_uri is not None:
            result['SourceManifestURI'] = self.source_manifest_uri

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceManifestURI') is not None:
            self.source_manifest_uri = m.get('SourceManifestURI')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.CreateFileCompressionTaskRequestSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateFileCompressionTaskRequestSources(DaraModel):
    def __init__(
        self,
        alias: str = None,
        mode: str = None,
        uri: str = None,
    ):
        # Specifies a new path or name for the source file within the output compressed file.
        # 
        # - If you do not specify this parameter, the source directory structure is preserved. For example, if the source file is at `oss://test-bucket/test-dir/test-object.doc`, the path of the file in the compressed file is `/test-dir/test-object.doc`.
        # 
        # - Rename the file. For example, if the source file is at `oss://test-bucket/test-object.jpg` and you set this parameter to `/test-rename-object.jpg`, the file in the compressed file is named `test-rename-object.jpg`.
        # 
        # - Specify a new path for the source file in the compressed file. For example, if the source directory is `oss://test-bucket/test-dir/` and you set this parameter to `/new-dir/`, all files in the source directory are compressed into the `/new-dir/` path.
        # 
        # - Set the value to `/` to remove the source directory structure. All files are placed directly in the root directory of the compressed file, and the original directory structure is not preserved.
        # 
        # - Specify both a path and a file name. The file is renamed and moved to the specified path. For example, if you set this parameter to `/new-dir/alias.doc`, the file is renamed to `alias.doc` and placed in the `/new-dir/` path of the compressed file.
        # 
        # > * Avoid creating files with duplicate names during the renaming process. If duplicate names exist, you may not be able to decompress the file in the compressed package. This depends on the decompression program you use.
        # >
        # > * Format requirement: The value must start with a forward slash (\\`/\\`), such as `/new-dir/alias.doc`.
        self.alias = alias
        # The pattern matching mode for the packaging rule. Valid values include `prefix` (prefix matching) and `fullname` (exact matching). The default value is `prefix`.
        # 
        # - `prefix`: In this mode, all files that match the prefix are packaged.
        # 
        # - `fullname`: In this mode, only the file that exactly matches the rule is packaged.
        self.mode = mode
        # The OSS address of the directory or file to package.
        # 
        # The OSS address must be in the \\`oss\\://${Bucket}/${Object}\\` format. \\`${Bucket}\\` is the name of the OSS bucket that is in the same region as the current project. \\`${Object}\\` is described as follows:
        # 
        # - To package a directory, \\`${Object}\\` is the directory name.
        # 
        # - To package a file, \\`${Object}\\` is the full path of the file, including the file name extension.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

