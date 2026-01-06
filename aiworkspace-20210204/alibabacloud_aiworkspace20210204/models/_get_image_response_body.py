# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetImageResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_uri: str = None,
        labels: List[main_models.GetImageResponseBodyLabels] = None,
        name: str = None,
        parent_user_id: str = None,
        request_id: str = None,
        size: int = None,
        source_id: str = None,
        source_type: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The accessibility of the image. Valid values:
        # 
        # *   PUBLIC: All members can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The image description.
        self.description = description
        # The time when the image is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the image is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The image address, which contains the version number.
        self.image_uri = image_uri
        # The image tags, which are of the array data type. Each element in the array contains a key-value pair. The key of official tags is system.official and the tag value is true.
        self.labels = labels
        # The image name.
        self.name = name
        # The Alibaba Cloud account of the creator.
        self.parent_user_id = parent_user_id
        # The request ID.
        self.request_id = request_id
        # The size of the image. Unit: GB.
        self.size = size
        # 镜像来源 ID
        self.source_id = source_id
        # 镜像来源类型
        self.source_type = source_type
        # The user ID of the image.
        self.user_id = user_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetImageResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetImageResponseBodyLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

