# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyCloudVendorAccountAKRequest(DaraModel):
    def __init__(
        self,
        auth_ids: str = None,
        auth_modules: List[str] = None,
        ctdr_cloud_user_id: str = None,
        domain: str = None,
        extend_info: str = None,
        lang: str = None,
        regions: List[str] = None,
        secret_id: str = None,
        secret_key: str = None,
        status: int = None,
        subscription_ids: List[str] = None,
        tenant_id: str = None,
        vendor_auth_alias: str = None,
    ):
        # The unique ID of the AccessKey pair.
        # 
        # >  You can call the [DescribeCloudVendorAccountAKList](~~DescribeCloudVendorAccountAKList~~) operation to query the unique ID.
        # 
        # This parameter is required.
        self.auth_ids = auth_ids
        # The modules that are associated with the AccessKey pair. Valid values:
        # 
        # *   **HOST**: host.
        # *   **CSPM**: configuration assessment.
        # *   **SIEM**: Cloud Threat Detection and Response (CTDR).
        # *   **TRIAL**: log audit.
        # 
        # >  You can call the [GetSupportedModules](~~GetSupportedModules~~) operation to query the supported modules.
        self.auth_modules = auth_modules
        # Account ID.
        # > The account ID of the connected cloud vendor, required when the permission description includes threat analysis and response.
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # Access account domain. Values: 
        # -  **china**: China
        # -  **global**: Global 
        # -  **europe**: Huawei Europe
        # > This parameter is only valid and required for **Vendor** being **HUAWEICLOUD**, **Azure**, **AWS**, or **VOLCENGINE**.
        self.domain = domain
        # Extended information.
        # 
        # > Used to record extended information from different vendors.
        # > For Google Cloud, which is accessed through a service account, ExtendInfo stores a JSON-formatted service key file, excluding the private_key_id and zprivate_key fields. The file includes the following fields: type, project_id, client_email, client_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_x509_cert_url, universe_domain.
        self.extend_info = extend_info
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The regions that are examined during AccessKey pair authentication.
        self.regions = regions
        # ID of the AK parameter. Values:
        # 
        # 1. When AkType is primary:
        # - **Tencent**: AccessKeyId of the main account
        # - **HUAWEICLOUD**: AccessKeyId of the main account
        # - **Azure**: ClientId
        # - **AWS**: AccessKeyId of the main account
        # - **VOLCENGINE**: AccessKeyId of the main account
        # 
        # 2. When AkType is sub:
        # - **Tencent**: AccessKeyId of the sub-account
        # - **HUAWEICLOUD**: AccessKeyId of the sub-account
        # - **Azure**: ClientId
        # - **AWS**: AccessKeyId of the sub-account
        # - **VOLCENGINE**: AccessKeyId of the sub-account
        # - **google**: private_key_id
        # 
        # > If AkType is **primary**, this value is the SecretID of the main account from another cloud. If AkType is **sub**, this value is the Access Key ID of the sub-account from another cloud. For **Azure**, there is no distinction, and this value is the **appId** of the authentication information. Google Cloud is accessed through a service account, with AkType defaulting to sub, and this value is taken from the private_key_id attribute in the JSON format service key file.
        self.secret_id = secret_id
        # The AccessKey secret.
        # 
        # >  If AkType is set to **primary**, you must set SecretKey to the AccessKey secret of the third-party master account. If AkType is set to **sub**, you must set SecretKey to the AccessKey secret of the third-party sub-account. This parameter value does not change for a **Microsoft Azure account**. For an Azure account, set this parameter to the **password** that is used for authentication.
        self.secret_key = secret_key
        # The status of the AccessKey pair. Valid values:
        # 
        # *   **0**: enabled.
        # *   **1**: disabled.
        self.status = status
        # The IDs of subscriptions.
        # 
        # >  This parameter takes effect only when Vendor is set to Azure.
        self.subscription_ids = subscription_ids
        # The tenant ID.
        # 
        # >  This parameter takes effect only when Vendor is set to Azure.
        self.tenant_id = tenant_id
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
        if self.auth_ids is not None:
            result['AuthIds'] = self.auth_ids

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

        if self.status is not None:
            result['Status'] = self.status

        if self.subscription_ids is not None:
            result['SubscriptionIds'] = self.subscription_ids

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vendor_auth_alias is not None:
            result['VendorAuthAlias'] = self.vendor_auth_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthIds') is not None:
            self.auth_ids = m.get('AuthIds')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubscriptionIds') is not None:
            self.subscription_ids = m.get('SubscriptionIds')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VendorAuthAlias') is not None:
            self.vendor_auth_alias = m.get('VendorAuthAlias')

        return self

