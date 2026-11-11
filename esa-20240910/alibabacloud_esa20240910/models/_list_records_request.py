# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecordsRequest(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        custom_port: str = None,
        page_number: int = None,
        page_size: int = None,
        proxied: bool = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        type: str = None,
    ):
        # The business scenario for record acceleration. This parameter is used as a filter condition for the query. Valid values:
        # - **image_video**: images and videos
        # - **api**: APIs
        # - **web**: web pages
        self.biz_name = biz_name
        # Specifies whether a custom port is enabled for the record. Valid values:
        # 
        # - on: enabled
        # - off: disabled
        self.custom_port = custom_port
        # The page number for paging. The value must be greater than or equal to 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for paging. Valid values: 1 to 500. Default value: **500**.
        self.page_size = page_size
        # Specifies whether proxy acceleration is enabled for the record. This parameter is used as a filter condition for the query. Valid values:
        # 
        # - **true**: Proxy acceleration is enabled.
        # - **false**: Proxy acceleration is disabled.
        self.proxied = proxied
        # The search match mode for the record name. Default value: exact. Valid values:
        # 
        # - **prefix**: prefix match
        # - **suffix**: suffix match
        # - **exact**: exact match
        # - **fuzzy**: fuzzy match
        self.record_match_type = record_match_type
        # The record name. This parameter is used as a filter condition for the query.
        self.record_name = record_name
        # The site ID. You can obtain the site ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The origin server type of the record. This parameter is used as a filter condition for the query. Only CNAME records can be filtered by this field. Valid values:
        # - **OSS**: OSS origin server
        # - **S3**: S3 origin server
        # - **LB**: load balancing origin server
        # - **OP**: IPAM pool origin server
        # - **Domain**: regular domain name origin server
        self.source_type = source_type
        # The DNS record type of the record. This parameter is used as a filter condition for the query.
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

        if self.custom_port is not None:
            result['CustomPort'] = self.custom_port

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

        if m.get('CustomPort') is not None:
            self.custom_port = m.get('CustomPort')

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

