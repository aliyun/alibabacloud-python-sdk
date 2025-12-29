# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class PageQueryWhiteListSettingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.PageQueryWhiteListSettingResponseBodyResultObject] = None,
        success: bool = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Return code, **200** indicates a successful API response.
        self.code = code
        # Current page number.
        self.current_page = current_page
        # Return message.
        self.message = message
        # Number of items per page.
        self.page_size = page_size
        # ID of the request
        self.request_id = request_id
        # Request result
        self.result_object = result_object
        # Whether the response was successful.
        self.success = success
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.PageQueryWhiteListSettingResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class PageQueryWhiteListSettingResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remark: str = None,
        scene_id: int = None,
        service_code: str = None,
        status: str = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        # ID number.
        self.cert_no = cert_no
        # Unique identifier for real person authentication.
        self.certify_id = certify_id
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Whitelist ID.
        self.id = id
        # Remark information.
        self.remark = remark
        # Authentication scene ID.
        self.scene_id = scene_id
        # ServiceCode of the real person cloud product
        self.service_code = service_code
        # Status:
        # 
        # - DELETE: Deleted
        # - VALID: Not deleted and within the validity period, valid
        # - INVALID: Not deleted but outside the validity period, invalid
        self.status = status
        # End date of validity
        self.valid_end_date = valid_end_date
        # Start date of validity
        self.valid_start_date = valid_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.status is not None:
            result['Status'] = self.status

        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date

        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')

        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')

        return self

