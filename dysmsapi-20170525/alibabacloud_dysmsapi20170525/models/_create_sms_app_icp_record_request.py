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
        app_service_name: str = None,
        domain: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 审核通过日期，示例2025-09-01
        # 
        # This parameter is required.
        self.app_approval_date = app_approval_date
        # ICP备案/许可证号
        # 
        # This parameter is required.
        self.app_icp_license_number = app_icp_license_number
        # app-icp备案详情截图osskey
        # 
        # This parameter is required.
        self.app_icp_record_pic = app_icp_record_pic
        # 主办单位名称
        # 
        # This parameter is required.
        self.app_principal_unit_name = app_principal_unit_name
        # app服务名称
        # 
        # This parameter is required.
        self.app_service_name = app_service_name
        # APP应用商店链接
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

        if self.app_service_name is not None:
            result['AppServiceName'] = self.app_service_name

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

        if m.get('AppServiceName') is not None:
            self.app_service_name = m.get('AppServiceName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

