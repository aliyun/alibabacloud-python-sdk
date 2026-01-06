# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateModelRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        model_description: str = None,
        model_doc: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        parameter_size: int = None,
        task: str = None,
    ):
        # The visibility of the model in the workspace. Valid values:
        # 
        # *   PRIVATE: The model is visible only to you and the administrator of the workspace.
        # *   PUBLIC: The model is visible to all users in the workspace.
        self.accessibility = accessibility
        # The domain. This parameter describes the domain in which the model is applied. Valid values: nlp (natural language processing) and cv (computer vision).
        self.domain = domain
        # Other information about the model.
        self.extra_info = extra_info
        # The model description.
        self.model_description = model_description
        # The documentation of the model.
        self.model_doc = model_doc
        # The model name, which must be 1 to 127 characters in length.
        self.model_name = model_name
        # The model type. Valid values: Checkpoint and LoRA.
        self.model_type = model_type
        # The sequence number of the model. This parameter can be used for custom sorting.
        self.order_number = order_number
        # The source of the model. This parameter describes the community or organization to which the source model belongs. Valid values: ModelScope and HuggingFace.
        self.origin = origin
        self.parameter_size = parameter_size
        # The task. This parameter specifies the specific issue that the model resolves. Example: text-classification.
        self.task = task

    def validate(self):
        pass

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

        if self.task is not None:
            result['Task'] = self.task

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

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

        if m.get('Task') is not None:
            self.task = m.get('Task')

        return self

