# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeWhitelistSettingResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeWhitelistSettingResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Pagination parameter: current page number, default value is 1.
        self.current_page = current_page
        # List of certification details.
        self.items = items
        # Number of items per page for pagination.
        self.page_size = page_size
        # ID of this request.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeWhitelistSettingResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWhitelistSettingResponseBodyItems(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remark: str = None,
        scene_id: int = None,
        status: str = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        # Certificate number.
        self.cert_no = cert_no
        # Certificate ID.
        self.certify_id = certify_id
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Whitelist ID.
        self.id = id
        # Remark.
        self.remark = remark
        # Scene ID.
        self.scene_id = scene_id
        # Whitelist status:
        # - **VALID**: Valid.
        # - **INVALID**: Invalid.
        # - **DELETED**: Deleted.
        self.status = status
        # Effective end date.
        self.valid_end_date = valid_end_date
        # Effective start time.
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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')

        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')

        return self

