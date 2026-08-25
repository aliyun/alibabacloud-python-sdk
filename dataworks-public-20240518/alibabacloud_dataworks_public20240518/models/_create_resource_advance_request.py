# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CreateResourceAdvanceRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        resource_file_object: BinaryIO = None,
        spec: str = None,
    ):
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The file stream or Object Storage Service (OSS) download URL of the resource file.
        # >Notice: This field allows you to specify a file stream or an OSS download URL. If you specify an OSS download URL, make sure that the URL is publicly accessible. A pre-signed URL is recommended.
        self.resource_file_object = resource_file_object
        # The FlowSpec information that describes the resource file. For more information about the specification, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
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

        if self.resource_file_object is not None:
            result['ResourceFile'] = self.resource_file_object

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceFile') is not None:
            self.resource_file_object = m.get('ResourceFile')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

