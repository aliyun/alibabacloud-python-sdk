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
        # The format of the output file.
        # 
        # > Only the ZIP format is supported.
        self.compressed_format = compressed_format
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The configurations of authorization chains. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
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
        self.sources_shrink = sources_shrink
        # The OSS URI of the package. The object name part in the URI is used as the name of the package. Example: `name.zip`.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum length of the value is 2,048 bytes.
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

