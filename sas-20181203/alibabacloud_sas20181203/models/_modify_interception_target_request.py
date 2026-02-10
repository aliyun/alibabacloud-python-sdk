# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInterceptionTargetRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        image_list: List[str] = None,
        namespace: str = None,
        tag_list: List[str] = None,
        target_id: int = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The name of the application.
        # 
        # > You can call the [DescribeContainerTags](~~DescribeContainerTags~~) operation to obtain the value of this parameter.
        self.app_name = app_name
        # An array that consists of images.
        # 
        # > You can call the [DescribeContainerTags](~~DescribeContainerTags~~) operation to obtain the value of this parameter.
        self.image_list = image_list
        # The namespace.
        # 
        # > You can call the [DescribeContainerTags](~~DescribeContainerTags~~) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.namespace = namespace
        # An array that consists of tags.
        # 
        # > You can call the [DescribeContainerTags](~~DescribeContainerTags~~) operation to obtain the value of this parameter.
        self.tag_list = tag_list
        # The ID of the network object.
        # 
        # > You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.target_id = target_id
        # The name.
        # 
        # This parameter is required.
        self.target_name = target_name
        # The object type. Valid values:
        # 
        # *   **IMAGE**
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

