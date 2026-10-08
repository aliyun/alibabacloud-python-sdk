# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetFileMetaShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris_shrink: str = None,
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
        # The list of file URIs. A maximum of 100 URIs are supported.
        # 
        # This parameter is required.
        self.uris_shrink = uris_shrink
        # The list of fields to be returned. If you specify this parameter, only the values of the specified fields are returned, instead of all existing metadata fields. This parameter can be used to reduce the size of the returned struct.
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

        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink

        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')

        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')

        return self

