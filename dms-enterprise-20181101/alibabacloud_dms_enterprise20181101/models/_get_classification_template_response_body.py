# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetClassificationTemplateResponseBody(DaraModel):
    def __init__(
        self,
        classification_resource_template_map: main_models.GetClassificationTemplateResponseBodyClassificationResourceTemplateMap = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the classification template that is associated to the instance.
        self.classification_resource_template_map = classification_resource_template_map
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.classification_resource_template_map:
            self.classification_resource_template_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classification_resource_template_map is not None:
            result['ClassificationResourceTemplateMap'] = self.classification_resource_template_map.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationResourceTemplateMap') is not None:
            temp_model = main_models.GetClassificationTemplateResponseBodyClassificationResourceTemplateMap()
            self.classification_resource_template_map = temp_model.from_map(m.get('ClassificationResourceTemplateMap'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetClassificationTemplateResponseBodyClassificationResourceTemplateMap(DaraModel):
    def __init__(
        self,
        resource_id: int = None,
        resource_type: str = None,
        template_id: int = None,
        template_type: str = None,
    ):
        # The ID of the resource. The supported resource type is INSTANCE. The resource ID corresponds to the value of InstanceId. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) operation to obtain the value of InstanceId.
        self.resource_id = resource_id
        # The resource type. The value is fixed as **INSTANCE**.
        self.resource_type = resource_type
        # The ID of the classification and grading template.
        self.template_id = template_id
        # The type of the classification and grading template. Valid values:
        # 
        # *   **INNER**: a built-in template.
        # *   **USER_DEFINE**: a custom template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

