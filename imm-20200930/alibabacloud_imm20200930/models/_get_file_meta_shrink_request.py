# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFileMetaShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
        with_fields_shrink: str = None,
    ):
        # The name of the dataset. For more information about how to obtain the dataset name, refer to [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The name of the project. For more information about how to obtain the project name, refer to [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The URI of the file. Make sure that the file has been **indexed**.
        # 
        # The OSS URI format is oss://${Bucket}/${Object}, where `${Bucket}` is the name of the OSS bucket that resides in the same region as the current project, and `${Object}` is the full path of the file including the file name extension.
        # 
        # The PDS URI format is pds://domains/${domain}/drives/${drive}/files/${file}/revisions/${revision}.
        # 
        # This parameter is required.
        self.uri = uri
        # Specifies the specific fields to return, instead of all existing metadata fields. You can use this parameter to reduce the size of the returned struct.
        # 
        # If you do not specify this parameter or leave it empty, all fields are returned.
        self.with_fields_shrink = with_fields_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.uri is not None:
            result['URI'] = self.uri

        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')

        return self

