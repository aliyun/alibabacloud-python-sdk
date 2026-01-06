# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetSparkTemplateFileContentResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSparkTemplateFileContentResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSparkTemplateFileContentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSparkTemplateFileContentResponseBodyData(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        content: str = None,
        id: int = None,
        resource_group_name: str = None,
        type: str = None,
    ):
        # The application type. Valid values:
        # 
        # *   **SQL**
        # *   **STREAMING**
        # *   **BATCH**
        self.app_type = app_type
        # The content of the application template.
        self.content = content
        # The application template ID.
        self.id = id
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The file type. Valid values:
        # 
        # *   **folder**
        # *   **file**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

