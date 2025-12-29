# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PageQueryWhiteListSettingRequest(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        current_page: int = None,
        page_size: int = None,
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
        # Current page number, default is 1.
        self.current_page = current_page
        # Number of items per page, default is 10
        self.page_size = page_size
        # Authentication scene ID. This ID is automatically generated after creating an authentication scene in the console. For how to create an authentication scene, see Adding an Authentication Scene.
        self.scene_id = scene_id
        # ServiceCode of the real person cloud product, value: **antcloudauth**.
        self.service_code = service_code
        # Status:
        # 
        # - DELETE: Deleted
        # - VALID: Not deleted and within the validity period, valid
        # - INVALID: Not deleted but outside the validity period, invalid
        self.status = status
        # End date of validity (timestamp in milliseconds)
        self.valid_end_date = valid_end_date
        # Start date of validity (timestamp in milliseconds)
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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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

