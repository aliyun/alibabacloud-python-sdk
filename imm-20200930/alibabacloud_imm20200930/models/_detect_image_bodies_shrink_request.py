# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectImageBodiesShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        sensitivity: float = None,
        source_uri: str = None,
    ):
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The accuracy level of detecting and recognizing specific content in the image. Valid values: 0 to 1. Default value: 0.6. A higher sensitivity specifies that more image details can be detected.
        self.sensitivity = sensitivity
        # The URI of the Object Storage Service (OSS) bucket in which the image file is stored.
        # 
        # Specify the value in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that resides in the same region as the current project. `${Object}` specifies the complete path to the file that has an extension.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        return self

