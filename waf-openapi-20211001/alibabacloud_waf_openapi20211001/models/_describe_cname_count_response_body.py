# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeCnameCountResponseBody(DaraModel):
    def __init__(
        self,
        cname_count: main_models.DescribeCnameCountResponseBodyCnameCount = None,
        request_id: str = None,
    ):
        # The information about the number of domain names that are added to WAF in CNAME record mode and hybrid cloud reverse proxy mode.
        self.cname_count = cname_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cname_count:
            self.cname_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname_count is not None:
            result['CnameCount'] = self.cname_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameCount') is not None:
            temp_model = main_models.DescribeCnameCountResponseBodyCnameCount()
            self.cname_count = temp_model.from_map(m.get('CnameCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCnameCountResponseBodyCnameCount(DaraModel):
    def __init__(
        self,
        cname: int = None,
        hybrid_cloud_cname: int = None,
        total: int = None,
    ):
        # The number of domain names that are added to WAF in CNAME record mode.
        self.cname = cname
        # The number of domain names that are added to WAF in hybrid cloud reverse proxy mode.
        self.hybrid_cloud_cname = hybrid_cloud_cname
        # The total number of domain names that are added to WAF in CNAME record mode and hybrid cloud reverse proxy mode.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.hybrid_cloud_cname is not None:
            result['HybridCloudCname'] = self.hybrid_cloud_cname

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('HybridCloudCname') is not None:
            self.hybrid_cloud_cname = m.get('HybridCloudCname')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

