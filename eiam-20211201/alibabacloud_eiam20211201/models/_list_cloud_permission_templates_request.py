# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudPermissionTemplatesRequest(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_permission_template_name_prefix: str = None,
        cloud_permission_template_sharing_mode: str = None,
        cloud_permission_template_usage_type: str = None,
        creator_type: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the cloud account.
        # 
        # This parameter is required.
        self.cloud_account_id = cloud_account_id
        # Filters the results by the prefix of the template name.
        self.cloud_permission_template_name_prefix = cloud_permission_template_name_prefix
        # Filters the results by permission template sharing mode. Valid values: shared and exclusive. If you do not specify this parameter, no filtering is applied.
        self.cloud_permission_template_sharing_mode = cloud_permission_template_sharing_mode
        # Filters the results by permission template usage type. Valid values: user (privilege escalation for human users) and application (privilege escalation for machine-to-machine applications).
        self.cloud_permission_template_usage_type = cloud_permission_template_usage_type
        # Filters the results by creator type. Valid values: idaas_admin and idaas_user.
        self.creator_type = creator_type
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of entries to return per page in a paging query. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token. Set the value to the NextToken value returned from the previous call.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_permission_template_name_prefix is not None:
            result['CloudPermissionTemplateNamePrefix'] = self.cloud_permission_template_name_prefix

        if self.cloud_permission_template_sharing_mode is not None:
            result['CloudPermissionTemplateSharingMode'] = self.cloud_permission_template_sharing_mode

        if self.cloud_permission_template_usage_type is not None:
            result['CloudPermissionTemplateUsageType'] = self.cloud_permission_template_usage_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudPermissionTemplateNamePrefix') is not None:
            self.cloud_permission_template_name_prefix = m.get('CloudPermissionTemplateNamePrefix')

        if m.get('CloudPermissionTemplateSharingMode') is not None:
            self.cloud_permission_template_sharing_mode = m.get('CloudPermissionTemplateSharingMode')

        if m.get('CloudPermissionTemplateUsageType') is not None:
            self.cloud_permission_template_usage_type = m.get('CloudPermissionTemplateUsageType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

