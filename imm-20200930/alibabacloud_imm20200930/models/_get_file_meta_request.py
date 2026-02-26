# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetFileMetaRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
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
        # The URI of the file. Make sure that the file is indexed****.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # Specify the URI of the file in Photo and Drive Service in the pds://domains/${domain}/drives/${drive}/files/${file}/revisions/${revision} format.
        # 
        # This parameter is required.
        self.uri = uri
        # The metadata fields that you want to include in the response. You can use this parameter to reduce the size of the response.
        # 
        # If you do not specify this parameter or leave this parameter empty, the operation returns all metadata fields of the file.
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

        if self.uri is not None:
            result['URI'] = self.uri

        if self.with_fields is not None:
            result['WithFields'] = self.with_fields

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
            self.with_fields = m.get('WithFields')

        return self

