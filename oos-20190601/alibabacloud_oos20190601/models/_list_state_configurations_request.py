# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListStateConfigurationsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state_configuration_ids: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the desired-state configuration.
        self.state_configuration_ids = state_configuration_ids
        # The tags to be added to the configuration.
        self.tags = tags
        # The name of the template. The name must be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.template_name = template_name
        # The version number of the template. If you do not specify this parameter, the latest version of the template is used.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

