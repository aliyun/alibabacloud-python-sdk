# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupAgentModelSettingsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetResourceGroupAgentModelSettingsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of model settings for resource groups. One record is returned for each resource group ID specified in the request. If a resource group is not associated with a model group under the specified agent platform and provider, ModelTemplateId and ModelTemplateName are empty.
        self.data = data
        # The request ID, which uniquely identifies the request.
        self.request_id = request_id
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetResourceGroupAgentModelSettingsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetResourceGroupAgentModelSettingsResponseBodyData(DaraModel):
    def __init__(
        self,
        model_template_id: str = None,
        model_template_name: str = None,
        resource_group_id: str = None,
    ):
        # The model group ID.
        self.model_template_id = model_template_id
        # The model group name.
        self.model_template_name = model_template_name
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.model_template_name is not None:
            result['ModelTemplateName'] = self.model_template_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('ModelTemplateName') is not None:
            self.model_template_name = m.get('ModelTemplateName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

