# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTransportLayerApplicationsRequest(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        page_number: int = None,
        page_size: int = None,
        record_name: str = None,
        site_id: int = None,
    ):
        # Query type for the transport layer application host record, supporting the following 4 types, with exact query as the default.
        # 
        # - fuzzy: Fuzzy query.
        # - exact: Exact query.
        # - prefix: Prefix match query.
        # - suffix: Suffix match query.
        self.match_type = match_type
        # Page number set for pagination. Starting value: 1. Default value: 1.
        self.page_number = page_number
        # Page size. The maximum value is 500.
        self.page_size = page_size
        # Host record of the transport layer application.
        self.record_name = record_name
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

