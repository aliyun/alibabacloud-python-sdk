# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchGetFileMetaRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris: List[str] = None,
        with_fields: List[str] = None,
    ):
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The array of object URIs. You can specify up to 100 object URIs in an array.
        # 
        # This parameter is required.
        self.uris = uris
        # The fields to return. If you specify this parameter, only specified metadata fields are returned. You can use this parameter to control the size of the response.
        # 
        # If you do not specify this parameter or leave this parameter empty, the operation returns all metadata fields.
        self.with_fields = with_fields

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

        if self.uris is not None:
            result['URIs'] = self.uris

        if self.with_fields is not None:
            result['WithFields'] = self.with_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('URIs') is not None:
            self.uris = m.get('URIs')

        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')

        return self

