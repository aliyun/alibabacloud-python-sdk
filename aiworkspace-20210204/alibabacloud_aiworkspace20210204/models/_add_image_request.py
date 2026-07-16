# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class AddImageRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        image_id: str = None,
        image_uri: str = None,
        labels: List[main_models.AddImageRequestLabels] = None,
        name: str = None,
        size: int = None,
        source_id: str = None,
        source_type: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the image. Valid values:
        # 
        # - PUBLIC: All members of the workspace can perform operations on the image.
        # 
        # - PRIVATE: Only the creator can perform operations on the image.
        self.accessibility = accessibility
        # The description of the image.
        self.description = description
        # The ID of the image. If you leave this parameter empty, the system automatically generates an ID.
        # The format is \\`image-\\` followed by 18 uppercase letters, lowercase letters, or digits.
        self.image_id = image_id
        # The URI of the image. The URI can be reused. For more information, see [ListImage](https://help.aliyun.com/document_detail/449118.html).
        # 
        # This parameter is required.
        self.image_uri = image_uri
        # The labels of the image. This is an array where each item contains a key and a value.
        # Official images have the following label: system.official=true
        # The following keys are supported:
        # 
        # - system.chipType
        # 
        # - system.dsw\\.cudaVersion
        # 
        # - system.dsw\\.fromImageId
        # 
        # - system.dsw\\.fromInstanceId
        # 
        # - system.dsw\\.id
        # 
        # - system.dsw\\.os
        # 
        # - system.dsw\\.osVersion
        # 
        # - system.dsw\\.resourceType
        # 
        # - system.dsw\\.rootImageId
        # 
        # - system.dsw\\.stage
        # 
        # - system.dsw\\.tag
        # 
        # - system.dsw\\.type
        # 
        # - system.framework
        # 
        # - system.origin
        # 
        # - system.pythonVersion
        # 
        # - system.source
        # 
        # - system.supported.dlc
        # 
        # - system.supported.dsw
        self.labels = labels
        # The image name. The naming convention is as follows:
        # 
        # - The name must be 1 to 50 characters long.
        # 
        # - The name can contain lowercase letters, digits, and hyphens (-). It must start with a letter.
        # 
        # - The name must be unique within the workspace.
        # 
        # This parameter is required.
        self.name = name
        # The size of the image, in GB.
        self.size = size
        # The source ID of the image. If the source type is Build, this ID corresponds to the image build ID.
        self.source_id = source_id
        # The source type of the image. Valid values:
        # Import
        # Build
        self.source_type = source_type
        # The ID of the workspace to which the image belongs. For more information, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.AddImageRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AddImageRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the label.
        self.key = key
        # The value of the label.
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

