# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.ListImagesResponseBodyImages] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The image details.
        self.images = images
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_version: str = None,
        node_count: int = None,
        platform: str = None,
        release_file_md_5: str = None,
        release_file_size: str = None,
        type: str = None,
    ):
        # The architecture.
        self.architecture = architecture
        # The description.
        self.description = description
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image version.
        self.image_version = image_version
        # The number of nodes.
        self.node_count = node_count
        # The platform.
        self.platform = platform
        # The MD5 hash value of the file.
        self.release_file_md_5 = release_file_md_5
        # The image size.
        self.release_file_size = release_file_size
        # The image type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.release_file_md_5 is not None:
            result['ReleaseFileMd5'] = self.release_file_md_5

        if self.release_file_size is not None:
            result['ReleaseFileSize'] = self.release_file_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ReleaseFileMd5') is not None:
            self.release_file_md_5 = m.get('ReleaseFileMd5')

        if m.get('ReleaseFileSize') is not None:
            self.release_file_size = m.get('ReleaseFileSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

