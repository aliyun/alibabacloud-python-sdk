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
        # The format of the output file.
        # 
        # > Only the ZIP format is supported.
        self.compressed_format = compressed_format
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The configurations of authorization chains. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS URI of the inventory object that contains the objects to compress. The inventory object stores the objects to compress by using the same data structure of the Sources parameter in the JSON format. This parameter is suitable for specifying a large number of objects to compress.
        # 
        # >  You must specify this parameter or the `Sources` parameter. The `URI` parameter is required and the `Alias` parameter is optional. You can specify up to 80,000 compression rule by using SourceManifestURI in one single call to the operation. The following line provides an example of the content within an inventory object.
        # 
        #     [{"URI":"oss://<bucket>/<object>", "Alias":"/new-dir/new-name"}]
        self.source_manifest_uri = source_manifest_uri
        # The objects to be packed and packing rules.
        # 
        # >  You must specify this parameter or the SourceManifestURI parameter. The Sources parameter can hold up to 100 packing rules. If you want to include more than 100 packing rules, use the SourceManifestURI parameter.
        self.sources = sources
        # The OSS URI of the package. The object name part in the URI is used as the name of the package. Example: `name.zip`.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum length of the value is 2,048 bytes.
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
        # Specifies the path of the object in the package, or renames the object in the package.
        # 
        # *   Leave this parameter empty to retain the original directory structure of the object in the package. For example, if the object is stored at `oss://test-bucket/test-dir/test-object.doc` and you do not specify this parameter, the path of the object in the package is `/test-dir/test-object.doc`.
        # *   Rename the object. For example, if the object is stored at `oss://test-bucket/test-object.jpg` and you set the **Alias** parameter to `test-rename-object.jpg`, the name of the object in the package is `test-rename-object.jpg`.
        # *   Specify a different path for the object in the package. For example, if the directory to be packed is `oss://test-bucket/test-dir/` and you set the **Alias** parameter to `/new-dir/`, all objects in the directory are placed in the `/new-dir/` path in the package.
        # *   Set the parameter to `/` to remove the original directory structure.
        # 
        # >  Duplicate object names may cause a failure in extracting the objects from the package, depending on the packing tool that you use. We recommend that you avoid using duplicate object names when you rename objects in the packing task.
        self.alias = alias
        # The object matching rule. Valid values: `fullname` and `prefix`. Default value: `prefix`
        # 
        # *   `prefix`: matches objects by object name prefix.
        # *   `fullname`: exactly matches one single object by its full object name.
        self.mode = mode
        # The OSS URI of the object or directory.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is a directory or object:
        # 
        # When you pack a directory, `${Object}` is the path of the directory.
        # 
        # *   When you pack an object, `${Object}` is the path of the object with the extension included.
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

