# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListObjectScanEventRequest(DaraModel):
    def __init__(
        self,
        batch_type: str = None,
        bucket_name: str = None,
        current_page: int = None,
        event_id: int = None,
        event_name: str = None,
        lang: str = None,
        md_5: str = None,
        oss_key: str = None,
        page_size: int = None,
        parent_event_id: int = None,
        risk_level: str = None,
        source: str = None,
        status: int = None,
        time_end: int = None,
        time_start: int = None,
    ):
        self.batch_type = batch_type
        self.bucket_name = bucket_name
        # This parameter is required.
        self.current_page = current_page
        self.event_id = event_id
        self.event_name = event_name
        self.lang = lang
        self.md_5 = md_5
        self.oss_key = oss_key
        # This parameter is required.
        self.page_size = page_size
        self.parent_event_id = parent_event_id
        self.risk_level = risk_level
        self.source = source
        self.status = status
        self.time_end = time_end
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_event_id is not None:
            result['ParentEventId'] = self.parent_event_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.time_end is not None:
            result['TimeEnd'] = self.time_end

        if self.time_start is not None:
            result['TimeStart'] = self.time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentEventId') is not None:
            self.parent_event_id = m.get('ParentEventId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')

        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')

        return self

