# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecordsRequest(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        page_number: int = None,
        page_size: int = None,
        proxied: bool = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        type: str = None,
    ):
        # The business scenario of the record for acceleration. Valid values:
        # 
        # *   **image_video**: video and image.
        # *   **api**: API.
        # *   **web**: web page.
        self.biz_name = biz_name
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **500**.
        self.page_size = page_size
        # Filters by whether the record is proxied. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.proxied = proxied
        # The match mode to search for the record name. Default value: exact. Valid values:
        # 
        # *   **prefix**: match by prefix.
        # *   **suffix**: match by suffix.
        # *   **exact**: exact match.
        # *   **fuzzy**: fuzzy match.
        self.record_match_type = record_match_type
        # The record name. This parameter specifies a filter condition for the query.
        self.record_name = record_name
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The origin type of the record. Only CNAME records can be filtered by using this field. Valid values:
        # 
        # *   **OSS**: OSS bucket.
        # *   **S3**: S3 bucket.
        # *   **LB**: load balancer.
        # *   **OP**: origin pool.
        # *   **Domain**: domain name.
        self.source_type = source_type
        # The DNS record type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_match_type is not None:
            result['RecordMatchType'] = self.record_match_type

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordMatchType') is not None:
            self.record_match_type = m.get('RecordMatchType')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

