# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryRecordMinutesUrlResponseBody(DaraModel):
    def __init__(
        self,
        record_minutes_urls: List[main_models.QueryRecordMinutesUrlResponseBodyRecordMinutesUrls] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.record_minutes_urls = record_minutes_urls
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.record_minutes_urls:
            for v1 in self.record_minutes_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['recordMinutesUrls'] = []
        if self.record_minutes_urls is not None:
            for k1 in self.record_minutes_urls:
                result['recordMinutesUrls'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_minutes_urls = []
        if m.get('recordMinutesUrls') is not None:
            for k1 in m.get('recordMinutesUrls'):
                temp_model = main_models.QueryRecordMinutesUrlResponseBodyRecordMinutesUrls()
                self.record_minutes_urls.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class QueryRecordMinutesUrlResponseBodyRecordMinutesUrls(DaraModel):
    def __init__(
        self,
        record_minutes_url: str = None,
    ):
        self.record_minutes_url = record_minutes_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_minutes_url is not None:
            result['RecordMinutesUrl'] = self.record_minutes_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordMinutesUrl') is not None:
            self.record_minutes_url = m.get('RecordMinutesUrl')

        return self

