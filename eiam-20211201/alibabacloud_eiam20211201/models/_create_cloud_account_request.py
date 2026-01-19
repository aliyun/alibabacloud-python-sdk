# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudAccountRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cloud_account_external_id: str = None,
        cloud_account_name: str = None,
        cloud_account_provider_name: str = None,
        cloud_account_vendor_type: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # 云账号唯一标识
        # 
        # This parameter is required.
        self.cloud_account_external_id = cloud_account_external_id
        # 云账号名称
        self.cloud_account_name = cloud_account_name
        # 云账号提供商名称
        self.cloud_account_provider_name = cloud_account_provider_name
        # 云账号类型
        # 
        # This parameter is required.
        self.cloud_account_vendor_type = cloud_account_vendor_type
        # 云账号描述
        self.description = description
        # IDaaS EIAM实例的ID。
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cloud_account_external_id is not None:
            result['CloudAccountExternalId'] = self.cloud_account_external_id

        if self.cloud_account_name is not None:
            result['CloudAccountName'] = self.cloud_account_name

        if self.cloud_account_provider_name is not None:
            result['CloudAccountProviderName'] = self.cloud_account_provider_name

        if self.cloud_account_vendor_type is not None:
            result['CloudAccountVendorType'] = self.cloud_account_vendor_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloudAccountExternalId') is not None:
            self.cloud_account_external_id = m.get('CloudAccountExternalId')

        if m.get('CloudAccountName') is not None:
            self.cloud_account_name = m.get('CloudAccountName')

        if m.get('CloudAccountProviderName') is not None:
            self.cloud_account_provider_name = m.get('CloudAccountProviderName')

        if m.get('CloudAccountVendorType') is not None:
            self.cloud_account_vendor_type = m.get('CloudAccountVendorType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

