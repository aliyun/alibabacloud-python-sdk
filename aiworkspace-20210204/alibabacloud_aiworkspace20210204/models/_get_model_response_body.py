# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetModelResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_latest_version_modified_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.Label] = None,
        latest_version: main_models.ModelVersion = None,
        model_description: str = None,
        model_doc: str = None,
        model_id: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        owner_id: str = None,
        parameter_size: int = None,
        provider: str = None,
        request_id: str = None,
        task: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the workspace.
        # 
        # *   PRIVATE: The workspace is visible only to you and the administrator of the workspace.
        # *   PUBLIC: The workspace is visible to all users.
        self.accessibility = accessibility
        # The domain. This parameter specifies the domain for which the model is developed. Valid values: nlp and cv. nlp indicates natural language processing and cv indicates computer vision.
        self.domain = domain
        # Other information about the model.
        self.extra_info = extra_info
        # The time when the model is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        self.gmt_latest_version_modified_time = gmt_latest_version_modified_time
        # The time when the model is last modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The model tags.
        self.labels = labels
        # The latest version of the model.
        self.latest_version = latest_version
        # The model description.
        self.model_description = model_description
        # The documentation of the model.
        self.model_doc = model_doc
        # The model ID.
        self.model_id = model_id
        # The model name.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The sequence number of the model.
        self.order_number = order_number
        # The source of the model. The community or organization to which the model belongs, such as ModelScope or HuggingFace.
        self.origin = origin
        # The ID of the Alibaba Cloud account.
        self.owner_id = owner_id
        self.parameter_size = parameter_size
        # The provider.
        self.provider = provider
        # The request ID.
        self.request_id = request_id
        # The task of the model. This parameter describes specific issues that the model solves, such as text-classification.
        self.task = task
        # The user ID.
        self.user_id = user_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.latest_version:
            self.latest_version.validate()

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

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_latest_version_modified_time is not None:
            result['GmtLatestVersionModifiedTime'] = self.gmt_latest_version_modified_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()

        if self.model_description is not None:
            result['ModelDescription'] = self.model_description

        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.order_number is not None:
            result['OrderNumber'] = self.order_number

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task is not None:
            result['Task'] = self.task

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtLatestVersionModifiedTime') is not None:
            self.gmt_latest_version_modified_time = m.get('GmtLatestVersionModifiedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestVersion') is not None:
            temp_model = main_models.ModelVersion()
            self.latest_version = temp_model.from_map(m.get('LatestVersion'))

        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')

        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

