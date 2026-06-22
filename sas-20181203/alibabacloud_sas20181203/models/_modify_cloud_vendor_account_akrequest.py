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
        # >Call the [DescribeCloudVendorAccountAKList](~~DescribeCloudVendorAccountAKList~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.auth_ids = auth_ids
        # The list of module codes associated with the AccessKey pair. Valid values:
        # - **HOST**: host
        # - **CSPM**: cloud product configuration check
        # - **SIEM**: Cloud Threat Detection and Response (CTDR)
        # - **TRIAL**: log audit
        # > Call the [GetSupportedModules](~~GetSupportedModules~~) operation to obtain the supported modules.
        self.auth_modules = auth_modules
        # The account ID.
        # >The account ID of the connected cloud vendor. This parameter is required when the permission description includes Cloud Threat Detection and Response (CTDR).
        self.ctdr_cloud_user_id = ctdr_cloud_user_id
        # The domain of the connected account. Valid values:
        # - **china**: China
        # - **global**: global
        # - **europe**: Huawei Cloud Europe
        # 
        # > This parameter is valid only when **Vendor** is set to **HUAWEICLOUD**, **Azure**, **AWS**, or **VOLCENGINE**, and is required.
        self.domain = domain
        # The extended information.
        # 
        # > Used to store extended information for different vendors.
        # >Google Cloud is accessed through a service account. ExtendInfo stores the JSON-formatted service key file, excluding the private_key_id and zprivate_key fields. The file contains the following fields: type, project_id, client_email, client_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_x509_cert_url, and universe_domain.
        self.extend_info = extend_info
        # The language type for the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The list of regions used for AccessKey information verification.
        self.regions = regions
        # The AccessKey parameter ID. Valid values:
        # 
        # 1. If AkType is set to primary:
        # - **Tencent**: AccessKeyId of the primary account
        # - **HUAWEICLOUD**: AccessKeyId of the primary account
        # - **Azure**: ClientId
        # - **AWS**: AccessKeyId of the primary account
        # - **VOLCENGINE**: AccessKeyId of the primary account
        # 
        # 2. If AkType is set to sub:
        # - **Tencent**: AccessKeyId of the RAM user
        # - **HUAWEICLOUD**: AccessKeyId of the RAM user
        # - **Azure**: ClientId
        # - **AWS**: AccessKeyId of the RAM user
        # - **VOLCENGINE**: AccessKeyId of the RAM user
        # - **google**: private_key_id
        # 
        # >If AkType is set to **primary**, this value is the SecretID of the primary account on the third-party cloud. If AkType is set to **sub**, this value is the Access Key ID of the RAM user on the third-party cloud. For **Azure**, no distinction is made, and this value is the **appId** of the authentication information. Google Cloud is accessed through a service account. AkType is set to sub by default, and this value is the private_key_id property value from the JSON-formatted service key file.
        self.secret_id = secret_id
        # The AccessKey parameter secret.
        # > If AkType is set to **primary**, this value is the Secret Access Key of the primary account on the third-party cloud. If AkType is set to **sub**, this value is the Secret Access Key of the RAM user on the third-party cloud. For **Azure**, no distinction is made, and this value is the **password** of the authentication information. Google Cloud is accessed through a service account. AkType is set to sub by default, and this value is the private_key property value from the JSON-formatted service key file.
        self.secret_key = secret_key
        # The usage status of the AccessKey pair. Valid values:
        # - **0**: enabled
        # - **1**: disabled.
        self.status = status
        # The list of subscription IDs.
        # > This parameter is no longer valid.
        self.subscription_ids = subscription_ids
        # The tenant ID.
        # >This parameter is valid only when Vendor is set to Azure.
        self.tenant_id = tenant_id
        # The name of the AccessKey account.
        # >Used to identify the account to which third-party host assets belong.
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

