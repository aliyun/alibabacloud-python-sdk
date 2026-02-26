# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ContextualFile(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        dataset_name: str = None,
        elements: List[main_models.Element] = None,
        media_type: str = None,
        ossuri: str = None,
        object_id: str = None,
        owner_id: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        # The Multipurpose Internet Mail Extensions (MIME) type of the file.
        self.content_type = content_type
        # Name of the dataset
        self.dataset_name = dataset_name
        # Elements
        self.elements = elements
        # Media type of the current file
        # 
        # Valid values:
        # 
        # *   image
        # *   other
        # *   document
        # *   archive
        # *   audio
        # *   video
        self.media_type = media_type
        # The URI of the OSS object. This parameter is available only if the value of the URI parameter is the URI of a file in Photo and Drive Service.
        self.ossuri = ossuri
        # The identifier of the corresponding file that exists in the dataset.
        self.object_id = object_id
        # User ID
        self.owner_id = owner_id
        # Name of the project
        self.project_name = project_name
        # URI of the file. Specify the OSS URI in the oss://${bucketname}/${objectname} format, where ${bucketname} is the name of the bucket in the same region as the current project and ${objectname} is the path of the object. The URI of a file in Photo and Drive Service follows the pds://domains/${domain}/drives/${drive}/files/${file}/revisions/${revision} format.
        self.uri = uri

    def validate(self):
        if self.elements:
            for v1 in self.elements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        result['Elements'] = []
        if self.elements is not None:
            for k1 in self.elements:
                result['Elements'].append(k1.to_map() if k1 else None)

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        self.elements = []
        if m.get('Elements') is not None:
            for k1 in m.get('Elements'):
                temp_model = main_models.Element()
                self.elements.append(temp_model.from_map(k1))

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

