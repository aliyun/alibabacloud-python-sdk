# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateModelRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        labels: List[main_models.Label] = None,
        model_description: str = None,
        model_doc: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        parameter_size: int = None,
        tag: List[main_models.Label] = None,
        task: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the model in the workspace. Valid values:
        # 
        # - PRIVATE (default): The model is visible only to you and administrators in the workspace.
        # 
        # - PUBLIC: The model is visible to everyone in the workspace.
        self.accessibility = accessibility
        # The domain. This describes the field that the model is designed for, such as nlp (Natural Language Processing) or cv (computer vision).
        self.domain = domain
        # Other information about the model.
        self.extra_info = extra_info
        # A list of labels. This parameter is deprecated and is replaced by the Tag parameter.
        self.labels = labels
        # The description of the model. Use this to distinguish different models.
        self.model_description = model_description
        # The model documentation.
        self.model_doc = model_doc
        # The name of the model. The name must be 1 to 127 characters in length.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The model type, such as Checkpoint or LoRA.
        self.model_type = model_type
        # The ordinal number of the model. You can use this for custom sorting.
        self.order_number = order_number
        # The source of the model. This specifies the community or organization that the source model belongs to, such as ModelScope and HuggingFace.
        self.origin = origin
        # The number of parameters, in millions.
        self.parameter_size = parameter_size
        # A list of tags.
        self.tag = tag
        # The task. This describes the specific problem that the model solves, such as text-classification (text classification).
        self.task = task
        # The ID of the workspace. For more information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.model_description is not None:
            result['ModelDescription'] = self.model_description

        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.task is not None:
            result['Task'] = self.task

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')

        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.Label()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

