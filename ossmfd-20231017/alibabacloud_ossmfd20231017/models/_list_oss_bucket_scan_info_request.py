# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOssBucketScanInfoRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        current_page: int = None,
        fuzz_bucket_name: str = None,
        has_risk: int = None,
        lang: str = None,
        page_size: int = None,
        status: int = None,
    ):
        self.bucket_name = bucket_name
        # This parameter is required.
        self.current_page = current_page
        self.fuzz_bucket_name = fuzz_bucket_name
        self.has_risk = has_risk
        self.lang = lang
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.fuzz_bucket_name is not None:
            result['FuzzBucketName'] = self.fuzz_bucket_name

        if self.has_risk is not None:
            result['HasRisk'] = self.has_risk

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FuzzBucketName') is not None:
            self.fuzz_bucket_name = m.get('FuzzBucketName')

        if m.get('HasRisk') is not None:
            self.has_risk = m.get('HasRisk')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

