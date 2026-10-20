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
        # The AccessKey type. Valid values:
        # 
        # - **primary**: Primary account
        # - **sub**: Sub-account
        # - **ctdr**: Agentic SOC
        # >Warning: When the vendor is **CHAITIN**, **FORTINET**, **THREATBOOK**, or **WIZ**, set this parameter to **ctdr**. When the vendor is **OracleCloud**, **google**, **BaiduCloud**, or **StateCloud**, set this parameter to **sub**.
        # 
        # This parameter is required.
        self.ak_type = ak_type
        # The list of modules associated with the AccessKey.
        # 
        # When AkType is set to ctdr, this parameter is required and at least one module must be provided, such as SIEM, HOST, or CSPM. If this parameter is not provided, the API returns HTTP 400 with the error code -101.
        self.auth_modules = auth_modules
        # The account ID.
        # 
        # > The account ID of the connected cloud vendor. This parameter is required when the permission description includes Cloud Threat Detection and Response.
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The domain to which the connected account belongs. Valid values:
        # - **china**: China
        # - **global**: Global
        # - **europe**: Huawei Cloud Europe
        # 
        # > This parameter is valid and required only when **Vendor** is set to **HUAWEICLOUD**, **Azure**, **AWS**, **VOLCENGINE**, **KingsoftCloud**, **UCloud**, **BaiduCloud**, or **OracleCloud**. For **KingsoftCloud** and **BaiduCloud**, set this parameter to **china**. For **OracleCloud**, set this parameter to **global**.
        self.domain = domain
        # The extension information.
        # 
        # > This parameter is used to record the extension information of different vendors.
        # Google Cloud is accessed through a service account. ExtendInfo stores the JSON-formatted service key file, excluding the private_key_id and zprivate_key fields. The file contains the following fields: type, project_id, client_email, client_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_x509_cert_url, and universe_domain. When the vendor is **OracleCloud**, this parameter contains the **fingerprint** key, which indicates the fingerprint.
        self.extend_info = extend_info
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The list of regions used to verify the AccessKey information. This parameter is valid only when **Vendor** is set to **AWS** or **OracleCloud**.
        # >You can call the [ListCloudVendorRegions](~~ListCloudVendorRegions~~) operation to query the regions.
        self.regions = regions
        # The AccessKey ID. Valid values:
        # 
        # - If AkType is set to primary:
        #   - **Tencent**: AccessKey ID of the primary account
        #   - **HUAWEICLOUD**: AccessKey ID of the primary account
        #   - **Azure**: Client ID
        #   - **AWS**: AccessKey ID of the primary account
        #   - **VOLCENGINE**: AccessKey ID of the primary account
        #   - **KingsoftCloud**: AccessKey ID of the primary account
        #   - **UCloud**: AccessKey ID of the primary account
        # - If AkType is set to sub:
        #   - **Tencent**: AccessKey ID of the sub-account
        #   - **HUAWEICLOUD**: AccessKey ID of the sub-account
        #   - **Azure**: Client ID
        #   - **AWS**: AccessKey ID of the sub-account
        #   - **VOLCENGINE**: AccessKey ID of the sub-account
        #   - **google**: private_key_id
        #   - **OracleCloud**: OCID of the sub-user
        #   - **BaiduCloud**: AccessKey ID of the sub-account
        #   - **KingsoftCloud**: AccessKey ID of the sub-account
        #   - **UCloud**: AccessKey ID of the sub-account
        #   - **StateCloud**: AccessKey ID of the sub-account
        # 
        # >If AkType is set to **primary**, this value is the AccessKey ID of the primary account in the third-party cloud. If AkType is set to **sub**, this value is the AccessKey ID of the sub-account in the third-party cloud. For **Azure**, this parameter is not differentiated and the value is the **appId** of the authentication information. Google Cloud is accessed through a service account, and AkType defaults to **sub**. The value is obtained from the private_key_id property in the JSON-formatted service key file. If the vendor is **OracleCloud**, this value is the OCID of the sub-user.
        # 
        # This parameter is required.
        self.secret_id = secret_id
        # The AccessKey secret. Valid values:
        # - If AkType is set to primary:
        #   - **Tencent**: AccessKey secret of the primary account
        #   - **HUAWEICLOUD**: AccessKey secret of the primary account
        #   - **Azure**: Client secret
        #   - **AWS**: AccessKey secret of the primary account
        #   - **VOLCENGINE**: AccessKey secret of the primary account
        #   - **KingsoftCloud**: AccessKey secret of the primary account
        #   - **UCloud**: AccessKey secret of the primary account
        # - If AkType is set to sub:
        #   - **Tencent**: AccessKey secret of the sub-account
        #   - **HUAWEICLOUD**: AccessKey secret of the sub-account
        #   - **Azure**: Client secret
        #   - **AWS**: AccessKey secret of the sub-account
        #   - **google**: private_key
        #   - **OracleCloud**: private_key of the sub-user
        #   - **BaiduCloud**: AccessKey secret of the sub-account
        #   - **KingsoftCloud**: AccessKey secret of the sub-account
        #   - **UCloud**: AccessKey secret of the sub-account
        #   - **StateCloud**: AccessKey secret of the sub-account
        # >If AkType is set to **primary**, this value is the AccessKey secret of the primary account in the third-party cloud. If AkType is set to **sub**, this value is the AccessKey secret of the sub-account in the third-party cloud. For **Azure**, this parameter is not differentiated and the value is the **password** of the authentication information. Google Cloud is accessed through a service account, and AkType defaults to **sub**. The value is obtained from the private_key property in the JSON-formatted service key file. For **OracleCloud**, this value is obtained from the content of the corresponding private key file.
        # 
        # This parameter is required.
        self.secret_key = secret_key
        # The list of subscription IDs.
        # 
        # > This parameter is deprecated.
        self.subscription_ids = subscription_ids
        # The tenant ID.
        # > This parameter is valid only when Vendor is set to **Azure** or **OracleCloud**.
        self.tenant_id = tenant_id
        # The cloud asset vendor. Valid values:
        # - **Tencent**: Tencent Cloud
        # - **HUAWEICLOUD**: Huawei Cloud
        # - **Azure**: Azure
        # - **AWS**: AWS
        # - **VOLCENGINE**: Volcengine
        # - **google**: Google Cloud
        # - **CHAITIN**: Chaitin Tech
        # - **FORTINET**: Fortinet
        # - **THREATBOOK**: ThreatBook
        # - **KingsoftCloud**: Kingsoft Cloud
        # - **UCloud**: UCloud
        # - **BaiduCloud**: Baidu AI Cloud
        # - **WIZ**: Wiz
        # - **OracleCloud**: Oracle Cloud
        # - **StateCloud**: China Telecom Cloud
        # 
        # This parameter is required.
        self.vendor = vendor
        # The name of the AccessKey account.
        # > This parameter is used to identify the account to which the third-party host assets belong.
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

