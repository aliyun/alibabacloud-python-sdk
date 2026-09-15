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
        # The AccessKey (AK) type. Valid values:
        # 
        # - **primary**: Primary account.
        # - **sub**: Sub-account.
        # - **ctdr**: Agentic SOC.
        # >Warning: When the vendor is **CHAITIN**, **FORTINET**, **THREATBOOK**, or **WIZ**, set this parameter to ctdr.</warning>
        # 
        # This parameter is required.
        self.ak_type = ak_type
        # The list of AK-associated modules.
        self.auth_modules = auth_modules
        # The account ID.
        # 
        # > The account ID of the connected cloud vendor. This parameter is required when the permission description includes Cloud Threat Detection and Response (CTDR).
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The account domain for access. Valid values:
        # - **china**: China
        # - **global**: Global
        # - **europe**: Huawei Cloud Europe
        # 
        # > This parameter is valid only when **Vendor** is set to **HUAWEICLOUD**, **Azure**, **AWS**, **VOLCENGINE**, **KingsoftCloud**, **UCloud**, or **BaiduCloud**, and is required. Set this parameter to **china** for KingsoftCloud and BaiduCloud, and to **global** for UCloud.
        self.domain = domain
        # The extended information.
        # 
        # > Used to record extended information for different vendors.
        # >Google Cloud is accessed through a service account. ExtendInfo stores the JSON-formatted service key file, excluding the private_key_id and private_key fields. The file contains the following fields: type, project_id, client_email, client_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_x509_cert_url, and universe_domain.
        self.extend_info = extend_info
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The list of regions used for AK information verification. This parameter is valid only when Vendor is set to AWS.
        # >Call the [ListCloudVendorRegions](~~ListCloudVendorRegions~~) operation to obtain this parameter.
        self.regions = regions
        # The AK parameter ID. Valid values:
        # 
        # 1. When AkType is set to primary:
        # - **Tencent**: AccessKeyId of the primary account
        # - **HUAWEICLOUD**: AccessKeyId of the primary account
        # - **Azure**: ClientId
        # - **AWS**: AccessKeyId of the primary account
        # - **VOLCENGINE**: AccessKeyId of the primary account
        # 
        # 2. When AkType is set to sub:
        # - **Tencent**: AccessKeyId of the sub-account
        # - **HUAWEICLOUD**: AccessKeyId of the sub-account
        # - **Azure**: ClientId
        # - **AWS**: AccessKeyId of the sub-account
        # - **VOLCENGINE**: AccessKeyId of the sub-account
        # - **google**: private_key_id
        # 
        # >If AkType is set to **primary**, this value is the SecretID of the primary account on the third-party cloud. If AkType is set to **sub**, this value is the Access Key ID of the sub-account on the third-party cloud. For **Azure**, no distinction is made, and this value is the **appId** in the authentication information. Google Cloud is accessed through a service account. AkType defaults to sub, and this value is the private_key_id property value from the JSON-formatted service key file.
        # 
        # This parameter is required.
        self.secret_id = secret_id
        # The AK parameter secret. Valid values:
        # 
        # 1. When AkType is set to primary:
        # - **Tencent**: SecretAccessKey of the primary account
        # - **HUAWEICLOUD**: SecretAccessKey of the primary account
        # - **Azure**: ClientSecret
        # - **AWS**: SecretAccessKey of the primary account
        # 
        # 2. When AkType is set to sub:
        # - **Tencent**: SecretAccessKey of the sub-account
        # - **HUAWEICLOUD**: SecretAccessKey of the sub-account
        # - **Azure**: ClientSecret
        # - **AWS**: SecretAccessKey of the sub-account
        # - **google**: private_key
        # >If AkType is set to **primary**, this value is the Secret Access Key of the primary account on the third-party cloud. If AkType is set to **sub**, this value is the Secret Access Key of the sub-account on the third-party cloud. For **Azure**, no distinction is made, and this value is the **password** in the authentication information. Google Cloud is accessed through a service account. AkType defaults to sub, and this value is the private_key property value from the JSON-formatted service key file.
        # 
        # This parameter is required.
        self.secret_key = secret_key
        # The list of subscription IDs.
        # 
        # > This parameter is no longer valid.
        self.subscription_ids = subscription_ids
        # The tenant ID. This parameter is valid only when Vendor is set to Azure.
        self.tenant_id = tenant_id
        # The cloud asset vendor. Valid values:
        # - **Tencent**: Tencent Cloud
        # - **HUAWEICLOUD**: Huawei Cloud
        # - **Azure**: Azure
        # - **AWS**: AWS
        # - **VOLCENGINE**: Volcengine
        # - **google**: Google Cloud
        # - **CHAITIN**: Chaitin Technology
        # - **FORTINET**: Fortinet
        # - **THREATBOOK**: ThreatBook
        # - **KingsoftCloud**: Kingsoft Cloud
        # - **UCloud**: UCloud
        # - **BaiduCloud**: Baidu AI Cloud
        # - **WIZ**: Wiz Security
        # 
        # This parameter is required.
        self.vendor = vendor
        # The AK account name.
        # >Used to identify the account to which third-party host assets belong.
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

