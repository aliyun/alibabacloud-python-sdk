# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySmsAppIcpRecordResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.QuerySmsAppIcpRecordResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySmsAppIcpRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySmsAppIcpRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        app_approval_date: str = None,
        app_icp_license_number: str = None,
        app_icp_record_id: int = None,
        app_icp_record_pic: str = None,
        app_icp_record_pic_url: str = None,
        app_principal_unit_name: str = None,
        app_service_name: str = None,
        domain: str = None,
    ):
        # 审核通过日期，示例2025-09-01
        self.app_approval_date = app_approval_date
        # ICP备案/许可证号
        self.app_icp_license_number = app_icp_license_number
        # app-icp备案材料id
        self.app_icp_record_id = app_icp_record_id
        # app-icp备案截图图片Osskey（给签名传工单用）
        self.app_icp_record_pic = app_icp_record_pic
        # app-icp备案截图url地址
        self.app_icp_record_pic_url = app_icp_record_pic_url
        # 主办单位名称
        self.app_principal_unit_name = app_principal_unit_name
        # app服务名称
        self.app_service_name = app_service_name
        # APP应用商店链接
        self.domain = domain

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

        if self.app_icp_record_id is not None:
            result['AppIcpRecordId'] = self.app_icp_record_id

        if self.app_icp_record_pic is not None:
            result['AppIcpRecordPic'] = self.app_icp_record_pic

        if self.app_icp_record_pic_url is not None:
            result['AppIcpRecordPicUrl'] = self.app_icp_record_pic_url

        if self.app_principal_unit_name is not None:
            result['AppPrincipalUnitName'] = self.app_principal_unit_name

        if self.app_service_name is not None:
            result['AppServiceName'] = self.app_service_name

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppApprovalDate') is not None:
            self.app_approval_date = m.get('AppApprovalDate')

        if m.get('AppIcpLicenseNumber') is not None:
            self.app_icp_license_number = m.get('AppIcpLicenseNumber')

        if m.get('AppIcpRecordId') is not None:
            self.app_icp_record_id = m.get('AppIcpRecordId')

        if m.get('AppIcpRecordPic') is not None:
            self.app_icp_record_pic = m.get('AppIcpRecordPic')

        if m.get('AppIcpRecordPicUrl') is not None:
            self.app_icp_record_pic_url = m.get('AppIcpRecordPicUrl')

        if m.get('AppPrincipalUnitName') is not None:
            self.app_principal_unit_name = m.get('AppPrincipalUnitName')

        if m.get('AppServiceName') is not None:
            self.app_service_name = m.get('AppServiceName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

