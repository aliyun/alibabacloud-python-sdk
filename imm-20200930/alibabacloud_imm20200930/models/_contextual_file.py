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
        # The dataset name.
        self.dataset_name = dataset_name
        # Elements.
        self.elements = elements
        # The media type of the file.
        self.media_type = media_type
        # The URI path of the OSS file. This parameter is used only when the URI is a PDS address.
        self.ossuri = ossuri
        # The identifier of the file in the dataset.
        self.object_id = object_id
        # The user ID.
        self.owner_id = owner_id
        # The project name.
        self.project_name = project_name
        # The URI of the file.
        # The format of an OSS URI is oss\\://${bucketname}/${objectname}. ${bucketname} is the name of an OSS bucket in the same region as the current project. ${objectname} is the file path.
        # The format of a PDS URI is pds\\://domains/${domain}/drives/${drive}/files/${file}/revisions/${revision}.
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

