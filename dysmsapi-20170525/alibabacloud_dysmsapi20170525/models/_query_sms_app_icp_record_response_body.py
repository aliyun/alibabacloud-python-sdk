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
        # The access denial details.
        self.access_denied_detail = access_denied_detail
        # The status code of the request.
        # 
        # - OK indicates a successful request.
        # 
        # - For other error codes, see the [error code list](https://help.aliyun.com/document_detail/101346.htm).
        self.code = code
        # A list of APP-ICP record entity details.
        self.data = data
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Specifies whether the API call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # 
        # - **false**: The call failed.
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
        app_runtime_pic: str = None,
        app_runtime_pic_url: str = None,
        app_service_name: str = None,
        app_store_download_pic: str = None,
        app_store_download_pic_url: str = None,
        domain: str = None,
    ):
        # The approval date.
        self.app_approval_date = app_approval_date
        # The icp filing/license number.
        self.app_icp_license_number = app_icp_license_number
        # The ID of the APP-ICP record material.
        self.app_icp_record_id = app_icp_record_id
        # The OSS fileKey for the APP-ICP record screenshot.
        self.app_icp_record_pic = app_icp_record_pic
        # The URL of the APP-ICP record screenshot.
        self.app_icp_record_pic_url = app_icp_record_pic_url
        # The hosting unit name.
        self.app_principal_unit_name = app_principal_unit_name
        # APP实际运行截图Osskey
        self.app_runtime_pic = app_runtime_pic
        # APP实际运行截图url地址
        self.app_runtime_pic_url = app_runtime_pic_url
        # The app service name.
        self.app_service_name = app_service_name
        # APP应用商店下载截图Osskey
        self.app_store_download_pic = app_store_download_pic
        # APP应用商店下载截图url地址
        self.app_store_download_pic_url = app_store_download_pic_url
        # The app store link.
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

        if self.app_runtime_pic is not None:
            result['AppRuntimePic'] = self.app_runtime_pic

        if self.app_runtime_pic_url is not None:
            result['AppRuntimePicUrl'] = self.app_runtime_pic_url

        if self.app_service_name is not None:
            result['AppServiceName'] = self.app_service_name

        if self.app_store_download_pic is not None:
            result['AppStoreDownloadPic'] = self.app_store_download_pic

        if self.app_store_download_pic_url is not None:
            result['AppStoreDownloadPicUrl'] = self.app_store_download_pic_url

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

        if m.get('AppRuntimePic') is not None:
            self.app_runtime_pic = m.get('AppRuntimePic')

        if m.get('AppRuntimePicUrl') is not None:
            self.app_runtime_pic_url = m.get('AppRuntimePicUrl')

        if m.get('AppServiceName') is not None:
            self.app_service_name = m.get('AppServiceName')

        if m.get('AppStoreDownloadPic') is not None:
            self.app_store_download_pic = m.get('AppStoreDownloadPic')

        if m.get('AppStoreDownloadPicUrl') is not None:
            self.app_store_download_pic_url = m.get('AppStoreDownloadPicUrl')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

