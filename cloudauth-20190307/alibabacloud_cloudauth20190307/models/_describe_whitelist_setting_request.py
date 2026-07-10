# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhitelistSettingRequest(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        scene_id: int = None,
        service_code: str = None,
        source_ip: str = None,
        status: str = None,
        valid_end_date: int = None,
        valid_start_date: int = None,
        whitelist_type: str = None,
    ):
        # The ID card number.
        self.cert_no = cert_no
        # The certification ID.
        self.certify_id = certify_id
        # The current page number. Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The language of the query result. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The number of entries per page in a paged query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The scene ID.
        self.scene_id = scene_id
        # The service code. Valid values:
        # - **cloudauthst**: enhanced financial-grade edition.
        # - **antcloudauth**: financial-grade edition.
        # 
        # This parameter is required.
        self.service_code = service_code
        # The source IP address of the visitor.
        self.source_ip = source_ip
        # The whitelist status. Valid values:
        # - **VALID**: valid.
        # - **INVALID**: invalid.
        # - **DELETED**: deleted.
        self.status = status
        # The end time of the validity period.
        self.valid_end_date = valid_end_date
        # The start time of the validity period. The value is a UNIX timestamp in seconds.
        self.valid_start_date = valid_start_date
        self.whitelist_type = whitelist_type

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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date

        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date

        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')

        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')

        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')

        return self

