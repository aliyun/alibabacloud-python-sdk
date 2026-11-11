# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableCloudPermissionTemplateRequest(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_permission_template_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the cloud account.
        # 
        # This parameter is required.
        self.cloud_account_id = cloud_account_id
        # The ID of the permission template.
        # 
        # This parameter is required.
        self.cloud_permission_template_id = cloud_permission_template_id
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_permission_template_id is not None:
            result['CloudPermissionTemplateId'] = self.cloud_permission_template_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudPermissionTemplateId') is not None:
            self.cloud_permission_template_id = m.get('CloudPermissionTemplateId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

