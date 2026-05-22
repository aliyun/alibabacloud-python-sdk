# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListEdgeContainerAppRecordsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListEdgeContainerAppRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The details about the associated domain names.
        self.records = records
        # The request ID.
        self.request_id = request_id
        # The number of domain names that are associated with the specified application.
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListEdgeContainerAppRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEdgeContainerAppRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cname: str = None,
        config_id: int = None,
        create_time: str = None,
        record_id: int = None,
        record_name: str = None,
        schemd_id: int = None,
        site_id: int = None,
        update_time: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The CNAME of the associated domain name.
        self.cname = cname
        # The configuration ID of the associated domain name.
        self.config_id = config_id
        # The time when the domain name was added. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The record ID of the associated domain name.
        self.record_id = record_id
        # The associated domain name.
        self.record_name = record_name
        # The scheduling domain ID of the associated domain name.
        self.schemd_id = schemd_id
        # The website ID.
        self.site_id = site_id
        # The time when the scheduling domain ID or CNAME was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.schemd_id is not None:
            result['SchemdId'] = self.schemd_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SchemdId') is not None:
            self.schemd_id = m.get('SchemdId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

