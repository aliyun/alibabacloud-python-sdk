# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class GetResolveCountSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resolve_summary: main_models.GetResolveCountSummaryResponseBodyResolveSummary = None,
    ):
        self.request_id = request_id
        self.resolve_summary = resolve_summary

    def validate(self):
        if self.resolve_summary:
            self.resolve_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resolve_summary is not None:
            result['ResolveSummary'] = self.resolve_summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResolveSummary') is not None:
            temp_model = main_models.GetResolveCountSummaryResponseBodyResolveSummary()
            self.resolve_summary = temp_model.from_map(m.get('ResolveSummary'))

        return self

class GetResolveCountSummaryResponseBodyResolveSummary(DaraModel):
    def __init__(
        self,
        doh: int = None,
        http: int = None,
        http_6: int = None,
        http_aes: str = None,
        https: int = None,
        https_6: int = None,
        https_aes: str = None,
    ):
        self.doh = doh
        self.http = http
        self.http_6 = http_6
        self.http_aes = http_aes
        self.https = https
        self.https_6 = https_6
        self.https_aes = https_aes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doh is not None:
            result['Doh'] = self.doh

        if self.http is not None:
            result['Http'] = self.http

        if self.http_6 is not None:
            result['Http6'] = self.http_6

        if self.http_aes is not None:
            result['HttpAes'] = self.http_aes

        if self.https is not None:
            result['Https'] = self.https

        if self.https_6 is not None:
            result['Https6'] = self.https_6

        if self.https_aes is not None:
            result['HttpsAes'] = self.https_aes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Doh') is not None:
            self.doh = m.get('Doh')

        if m.get('Http') is not None:
            self.http = m.get('Http')

        if m.get('Http6') is not None:
            self.http_6 = m.get('Http6')

        if m.get('HttpAes') is not None:
            self.http_aes = m.get('HttpAes')

        if m.get('Https') is not None:
            self.https = m.get('Https')

        if m.get('Https6') is not None:
            self.https_6 = m.get('Https6')

        if m.get('HttpsAes') is not None:
            self.https_aes = m.get('HttpsAes')

        return self

