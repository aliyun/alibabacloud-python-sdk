# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsAppIcpRecordRequest(DaraModel):
    def __init__(
        self,
        app_approval_date: str = None,
        app_icp_license_number: str = None,
        app_icp_record_pic: str = None,
        app_principal_unit_name: str = None,
        app_runtime_pic: str = None,
        app_service_name: str = None,
        app_store_download_pic: str = None,
        domain: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ICP filing approval date.
        # 
        # This parameter is required.
        self.app_approval_date = app_approval_date
        # The ICP record/license number. The number must not exceed 15 characters.
        # 
        # This parameter is required.
        self.app_icp_license_number = app_icp_license_number
        # The fileKey for the screenshot of your app\\"s ICP filing details.
        # 
        # 1. To look up your ICP filing, go to the [MIIT service platform](https://beian.miit.gov.cn/#/Integrated/recordQuery), search for your filing, and open its details page.
        # 
        # 2. The ICP filing screenshot must be uploaded to OSS and meet the following requirements:
        # 
        # - The filename cannot contain Chinese characters or special characters.
        # 
        # - The file must be an image in `jpg`, `png`, `gif`, or `jpeg` format. The file size cannot exceed 5 MB.
        # 
        # - The screenshot must show the full URL.
        # 
        # - For **Record Type**, select "APP".
        # 
        # - The **principal unit name** must be identical to the company or institution name on the qualification documents associated with the signature.
        # 
        # - The screenshot must clearly show the complete ICP record/license number.
        # 
        # - The **service name** must be identical to the **signature name**.
        # 
        # 3. To obtain the fileKey, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # This parameter is required.
        self.app_icp_record_pic = app_icp_record_pic
        # The principal unit name from your ICP filing. The name must not exceed 50 characters.
        # 
        # This parameter is required.
        self.app_principal_unit_name = app_principal_unit_name
        # APP实际运行截图osskey
        self.app_runtime_pic = app_runtime_pic
        # The service name from your ICP filing. The name must not exceed 15 characters.
        # 
        # This parameter is required.
        self.app_service_name = app_service_name
        # APP应用商店下载截图osskey
        self.app_store_download_pic = app_store_download_pic
        # The app store link.
        # 
        # > - The link must start with `http://` or `https://`.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_approval_date is not None:
            result['AppApprovalDate'] = self.app_approval_date

        if self.app_icp_license_number is not None:
            result['AppIcpLicenseNumber'] = self.app_icp_license_number

        if self.app_icp_record_pic is not None:
            result['AppIcpRecordPic'] = self.app_icp_record_pic

        if self.app_principal_unit_name is not None:
            result['AppPrincipalUnitName'] = self.app_principal_unit_name

        if self.app_runtime_pic is not None:
            result['AppRuntimePic'] = self.app_runtime_pic

        if self.app_service_name is not None:
            result['AppServiceName'] = self.app_service_name

        if self.app_store_download_pic is not None:
            result['AppStoreDownloadPic'] = self.app_store_download_pic

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppApprovalDate') is not None:
            self.app_approval_date = m.get('AppApprovalDate')

        if m.get('AppIcpLicenseNumber') is not None:
            self.app_icp_license_number = m.get('AppIcpLicenseNumber')

        if m.get('AppIcpRecordPic') is not None:
            self.app_icp_record_pic = m.get('AppIcpRecordPic')

        if m.get('AppPrincipalUnitName') is not None:
            self.app_principal_unit_name = m.get('AppPrincipalUnitName')

        if m.get('AppRuntimePic') is not None:
            self.app_runtime_pic = m.get('AppRuntimePic')

        if m.get('AppServiceName') is not None:
            self.app_service_name = m.get('AppServiceName')

        if m.get('AppStoreDownloadPic') is not None:
            self.app_store_download_pic = m.get('AppStoreDownloadPic')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

