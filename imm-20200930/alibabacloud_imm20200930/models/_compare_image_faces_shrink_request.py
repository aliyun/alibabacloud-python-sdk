# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareImageFacesShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_shrink: str = None,
    ):
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The URLs of the two images for compression.
        self.source_shrink = source_shrink

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

        if self.source_shrink is not None:
            result['Source'] = self.source_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')

        return self

