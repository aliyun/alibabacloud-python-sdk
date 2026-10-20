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
        # The unique ID of the AccessKey (AK).
        # >You can call the [DescribeCloudVendorAccountAKList](~~DescribeCloudVendorAccountAKList~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.auth_ids = auth_ids
        # The list of codes for the modules associated with the AK. Valid values:
        # - **HOST**: host
        # - **CSPM**: cloud product configuration check
        # - **SIEM**: threat analysis and response
        # - **TRIAL**: log audit
        # >You can call the [GetSupportedModules](~~GetSupportedModules~~) operation to obtain the supported modules.
        self.auth_modules = auth_modules
        # The account ID.
        # >The account ID of the connected cloud vendor. This parameter is required when the permission description includes threat analysis and response.
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The domain to which the connected account belongs. Valid values:
        # - **china**: China
        # - **global**: global
        # - **europe**: Huawei Cloud Europe site
        # 
        # >This parameter is valid and required only when **Vendor** is set to **HUAWEICLOUD**, **Azure**, **AWS**, **VOLCENGINE**, **KingsoftCloud**, **UCloud**, **BaiduCloud**, or **OracleCloud**. For **KingsoftCloud** and **BaiduCloud**, this parameter is fixed to **china**. For **OracleCloud**, this parameter is fixed to **global**.
        self.domain = domain
        # The extended information.
        # >This parameter is used to record the extended information of different vendors.
        # Google Cloud is accessed through a service account. ExtendInfo stores the JSON-formatted service key file, excluding the private_key_id and zprivate_key fields. The file contains the following fields: type, project_id, client_email, client_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_x509_cert_url, and universe_domain. If the vendor is **OracleCloud**, this parameter contains the **fingerprint** key, which indicates the fingerprint.
        self.extend_info = extend_info
        # The language type of the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The list of regions used for AK information verification. This parameter is valid only when **Vendor** is set to **AWS** or **OracleCloud**.
        # >You can call the [ListCloudVendorRegions](~~ListCloudVendorRegions~~) operation to obtain this parameter.
        self.regions = regions
        # The ID of the AK parameter. Valid values:
        # - If AkType is set to primary:
        # - - **Tencent**: the AccessKey ID of the primary account
        # - - **HUAWEICLOUD**: the AccessKey ID of the primary account
        # - - **Azure**: the client ID
        # - - **AWS**: the AccessKey ID of the primary account
        # - - **VOLCENGINE**: the AccessKey ID of the primary account
        # - - **KingsoftCloud**: the AccessKey ID of the primary account
        # - - **UCloud**: the AccessKey ID of the primary account
        # - If AkType is set to sub:
        # - - **Tencent**: the AccessKey ID of the sub-account
        # - - **HUAWEICLOUD**: the AccessKey ID of the sub-account
        # - - **Azure**: the client ID
        # - - **AWS**: the AccessKey ID of the sub-account
        # - - **VOLCENGINE**: the AccessKey ID of the sub-account
        # - - **google**: the private key ID
        # - - **OracleCloud**: the Oracle Cloud Identifier (OCID) of the sub-user
        # - - **BaiduCloud**: the AccessKey ID of the sub-account
        # - - **KingsoftCloud**: the AccessKey ID of the sub-account
        # - - **UCloud**: the AccessKey ID of the sub-account
        # - - **StateCloud**: the AccessKey ID of the sub-account
        # >If AkType is set to **primary**, this value is the SecretID of the primary account of the third-party cloud. If AkType is set to **sub**, this value is the AccessKey ID of the sub-account of the third-party cloud. For **Azure**, no distinction is made, and this value is the **appId** of the authentication information. Google Cloud is accessed through a service account. By default, AkType is set to sub, and this value is obtained from the private_key_id property of the JSON-formatted service key file. If the vendor is **OracleCloud**, this value is the OCID of the sub-user.
        self.secret_id = secret_id
        # The secret of the AK parameter. Valid values:
        # - If AkType is set to primary:
        # - - **Tencent**: the SecretAccessKey of the primary account
        # - - **HUAWEICLOUD**: the SecretAccessKey of the primary account
        # - - **Azure**: the client secret
        # - - **AWS**: the SecretAccessKey of the primary account
        # - - **VOLCENGINE**: the SecretAccessKey of the primary account
        # - - **KingsoftCloud**: the SecretAccessKey of the primary account
        # - - **UCloud**: the SecretAccessKey of the primary account
        # - If AkType is set to sub:
        # - - **Tencent**: the SecretAccessKey of the sub-account
        # - - **HUAWEICLOUD**: the SecretAccessKey of the sub-account
        # - - **Azure**: the client secret
        # - - **AWS**: the SecretAccessKey of the sub-account
        # - - **google**: the private key
        # - - **OracleCloud**: the private key of the sub-user
        # - - **BaiduCloud**: the SecretAccessKey of the sub-account
        # - - **KingsoftCloud**: the SecretAccessKey of the sub-account
        # - - **UCloud**: the SecretAccessKey of the sub-account
        # - - **StateCloud**: the SecretAccessKey of the sub-account
        # >If AkType is set to **primary**, this value is the Secret Access Key of the primary account of the third-party cloud. If AkType is set to **sub**, this value is the Secret Access Key of the sub-account of the third-party cloud. For **Azure**, no distinction is made, and this value is the **password** of the authentication information. Google Cloud is accessed through a service account. By default, AkType is set to sub, and this value is obtained from the private_key property of the JSON-formatted service key file. For **OracleCloud**, this value is obtained from the content of the corresponding private key file.
        self.secret_key = secret_key
        # The usage status of the AK. Valid values:
        # - **0**: enabled
        # - **1**: disabled
        self.status = status
        # The list of subscription IDs.
        # > **[Deprecated]** This parameter is no longer valid.
        self.subscription_ids = subscription_ids
        # The tenant ID.
        # >This parameter is valid only when Vendor is set to **Azure** or **OracleCloud**.
        self.tenant_id = tenant_id
        # The name of the AK account.
        # >This parameter is used to identify the account information to which the third-party host assets belong.
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

