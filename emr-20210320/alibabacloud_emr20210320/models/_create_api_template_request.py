# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiTemplateRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        content: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        template_name: str = None,
    ):
        # The name of the API operation. You can create only a cluster API operation template. Set the value to CreateCluster.
        # 
        # This parameter is required.
        self.api_name = api_name
        # The content of the cluster API operation template. Set the value to JSON strings of the request parameters of the [CreateCluster](https://help.aliyun.com/document_detail/454393.html) API operation for creating a cluster.
        # 
        # This parameter is required.
        self.content = content
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Cluster template name.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.content is not None:
            result['Content'] = self.content

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

