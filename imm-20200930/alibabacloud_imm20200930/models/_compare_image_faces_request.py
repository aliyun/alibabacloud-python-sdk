# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CompareImageFacesRequest(DaraModel):
    def __init__(
        self,
        credential_config: main_models.CredentialConfig = None,
        project_name: str = None,
        source: main_models.CompareImageFacesRequestSource = None,
    ):
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The URLs of the two images for compression.
        self.source = source

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source is not None:
            result['Source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Source') is not None:
            temp_model = main_models.CompareImageFacesRequestSource()
            self.source = temp_model.from_map(m.get('Source'))

        return self

class CompareImageFacesRequestSource(DaraModel):
    def __init__(
        self,
        uri1: str = None,
        uri2: str = None,
    ):
        # The OSS URL of the image file.
        # 
        # Specify the URL in the `oss://<bucket>/<object>` format. `<bucket>` specifies the name of the OSS bucket that is in the same region as the current project. `<object>` specifies path of the object with the extension included.
        self.uri1 = uri1
        # The OSS URL of the image file.
        # 
        # Specify the URL in the `oss://<bucket>/<object>` format. `<bucket>` specifies the name of the OSS bucket that is in the same region as the current project, and `<object>` specifies the path of the object with the extension included.
        self.uri2 = uri2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uri1 is not None:
            result['URI1'] = self.uri1

        if self.uri2 is not None:
            result['URI2'] = self.uri2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI1') is not None:
            self.uri1 = m.get('URI1')

        if m.get('URI2') is not None:
            self.uri2 = m.get('URI2')

        return self

