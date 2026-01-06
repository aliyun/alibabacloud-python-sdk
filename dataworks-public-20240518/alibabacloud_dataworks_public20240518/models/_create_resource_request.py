# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        resource_file: str = None,
        spec: str = None,
    ):
        # The ID of the DataWorks workspace. To obtain the workspace ID, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace configuration page.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The specific file stream or OSS download link contained in the resource.
        # 
        # >  This field allows users to provide a file stream or an OSS download link. When providing an OSS download link, ensure that the OSS link is publicly accessible. A presigned URL is recommended.
        self.resource_file = resource_file
        # The ID of the DataWorks workspace. To obtain the workspace ID, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace configuration page.
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_file is not None:
            result['ResourceFile'] = self.resource_file

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceFile') is not None:
            self.resource_file = m.get('ResourceFile')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

