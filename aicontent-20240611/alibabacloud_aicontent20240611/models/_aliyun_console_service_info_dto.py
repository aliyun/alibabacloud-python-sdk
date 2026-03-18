# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AliyunConsoleServiceInfoDTO(DaraModel):
    def __init__(
        self,
        buy_url: str = None,
        document_url: str = None,
        free_concurrency_count: int = None,
        free_count: int = None,
        service_code: str = None,
        service_name: str = None,
    ):
        self.buy_url = buy_url
        self.document_url = document_url
        self.free_concurrency_count = free_concurrency_count
        self.free_count = free_count
        self.service_code = service_code
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url

        if self.document_url is not None:
            result['documentUrl'] = self.document_url

        if self.free_concurrency_count is not None:
            result['freeConcurrencyCount'] = self.free_concurrency_count

        if self.free_count is not None:
            result['freeCount'] = self.free_count

        if self.service_code is not None:
            result['serviceCode'] = self.service_code

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')

        if m.get('documentUrl') is not None:
            self.document_url = m.get('documentUrl')

        if m.get('freeConcurrencyCount') is not None:
            self.free_concurrency_count = m.get('freeConcurrencyCount')

        if m.get('freeCount') is not None:
            self.free_count = m.get('freeCount')

        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

