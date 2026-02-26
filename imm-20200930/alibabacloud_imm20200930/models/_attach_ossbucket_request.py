# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachOSSBucketRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        ossbucket: str = None,
        project_name: str = None,
    ):
        # The description of the binding. The description must be 1 to 128 characters in length. By default, no description is applied.
        self.description = description
        # The name of the OSS bucket in the same region as the project.
        # 
        # This parameter is required.
        self.ossbucket = ossbucket
        # The name of the project. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

