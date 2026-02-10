# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCloudVendorAccountAKRequest(DaraModel):
    def __init__(
        self,
        ak_type: str = None,
        auth_modules: List[str] = None,
        ctdr_cloud_user_id: str = None,
        domain: str = None,
        extend_info: str = None,
        lang: str = None,
        regions: List[str] = None,
        secret_id: str = None,
        secret_key: str = None,
        subscription_ids: List[str] = None,
        tenant_id: str = None,
        vendor: str = None,
        vendor_auth_alias: str = None,
    ):
        # The type of the account to which the AccessKey pair belongs. Valid values:
        # 
        # *   **primary**: a primary account
        # *   **sub**: a sub-account
        # 
        # This parameter is required.
        self.ak_type = ak_type
        # The modules that are associated with the AccessKey pair.
        self.auth_modules = auth_modules
        # Account ID. > The account ID of the cloud provider, required when permissions include threat analysis and response.
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The Active Directory (AD) domain. This parameter takes effect only when Vendor is set to Azure. Valid values:
        # 
        # *   **china**
        # *   **global**
        self.domain = domain
        # Extended information.
        # > Used to record extended information from different vendors. > For Google Cloud, which is accessed via a service account, ExtendInfo stores the service key file in JSON format, excluding the private_key_id and zprivate_key fields. The file includes the following fields: type, project_id, client_email, client_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_x509_cert_url, universe_domain.
        self.extend_info = extend_info
        # The language of the content in the request and response messages. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The regions that are examined during AccessKey pair authentication. This parameter takes effect only when Vendor is set to AWS.
        # 
        # >  You can call the [ListCloudVendorRegions](~~ListCloudVendorRegions~~) operation to query regions.
        self.regions = regions
        # The AccessKey ID. Valid values:
        # 
        # 1\\. If AkType is set to primary, specify this parameter based on the following description:
        # 
        # *   **Tencent**: Enter the AccessKey ID of a primary account on Tencent Cloud.
        # *   **HUAWEICLOUD**: Enter the AccessKey ID of a primary account on Huawei Cloud.
        # *   **Azure**: Enter the AccessKey ID of a primary account on Microsoft Azure.
        # *   **AWS**: Enter the AccessKey ID of a primary account on AWS.
        # 
        # 2\\. If AkType is set to sub, specify this parameter based on the following description:
        # 
        # *   **Tencent**: Enter the AccessKey ID of a sub-account on Tencent Cloud.
        # *   **HUAWEICLOUD**: Enter the AccessKey ID of a sub-account on Huawei Cloud.
        # *   **Azure**: Enter the AccessKey ID of a sub-account on Microsoft Azure.
        # *   **AWS**: Enter the AccessKey ID of a sub-account on AWS.
        # 
        # This parameter is required.
        self.secret_id = secret_id
        # The AccessKey secret. Valid values:
        # 
        # 1\\. If AkType is set to primary, specify this parameter based on the following description:
        # 
        # *   **Tencent**: Enter the AccessKey secret of a primary account on Tencent Cloud.
        # *   **HUAWEICLOUD**: Enter the AccessKey secret of a primary account on Huawei Cloud.
        # *   **Azure**: Enter the AccessKey secret of a primary account on Microsoft Azure.
        # *   **AWS**: Enter the AccessKey secret of a primary account on AWS.
        # 
        # 2\\. If AkType is set to sub, specify this parameter based on the following description:
        # 
        # *   **Tencent**: Enter the AccessKey secret of a sub-account on Tencent Cloud.
        # *   **HUAWEICLOUD**: Enter the AccessKey secret of a sub-account on Huawei Cloud.
        # *   **Azure**: Enter the AccessKey secret of a sub-account on Microsoft Azure.
        # *   **AWS**: Enter the AccessKey secret of a sub-account on AWS.
        # 
        # This parameter is required.
        self.secret_key = secret_key
        # The subscription IDs. This parameter takes effect only when Vendor is set to Azure.
        self.subscription_ids = subscription_ids
        # The tenant ID. This parameter takes effect only when Vendor is set to Azure.
        self.tenant_id = tenant_id
        # The cloud service provider. Valid values:
        # 
        # *   **Tencent**: Tencent Cloud
        # *   **HUAWEICLOUD**: Huawei Cloud
        # *   **Azure**: Microsoft Azure
        # *   **AWS**: Amazon Web Services (AWS)
        # 
        # This parameter is required.
        self.vendor = vendor
        # The name of the AccessKey pair.
        # 
        # >  The account information of the third-party cloud servers.
        self.vendor_auth_alias = vendor_auth_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak_type is not None:
            result['AkType'] = self.ak_type

        if self.auth_modules is not None:
            result['AuthModules'] = self.auth_modules

        if self.ctdr_cloud_user_id is not None:
            result['CtdrCloudUserId'] = self.ctdr_cloud_user_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.regions is not None:
            result['Regions'] = self.regions

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.subscription_ids is not None:
            result['SubscriptionIds'] = self.subscription_ids

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_auth_alias is not None:
            result['VendorAuthAlias'] = self.vendor_auth_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkType') is not None:
            self.ak_type = m.get('AkType')

        if m.get('AuthModules') is not None:
            self.auth_modules = m.get('AuthModules')

        if m.get('CtdrCloudUserId') is not None:
            self.ctdr_cloud_user_id = m.get('CtdrCloudUserId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Regions') is not None:
            self.regions = m.get('Regions')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('SubscriptionIds') is not None:
            self.subscription_ids = m.get('SubscriptionIds')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorAuthAlias') is not None:
            self.vendor_auth_alias = m.get('VendorAuthAlias')

        return self

