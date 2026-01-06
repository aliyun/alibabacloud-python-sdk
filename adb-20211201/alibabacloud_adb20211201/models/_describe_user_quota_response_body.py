# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserQuotaResponseBody(DaraModel):
    def __init__(
        self,
        elastic_acu: str = None,
        request_id: str = None,
        reserverd_compte_acu: str = None,
        reserverd_storage_acu: str = None,
        resource_group_count: str = None,
    ):
        # The available elastic AnalyticDB compute units (ACUs).
        self.elastic_acu = elastic_acu
        # The request ID.
        self.request_id = request_id
        # The available reserved computing resources.
        self.reserverd_compte_acu = reserverd_compte_acu
        # The available reserved storage resources.
        self.reserverd_storage_acu = reserverd_storage_acu
        # The number of available resource groups.
        self.resource_group_count = resource_group_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_acu is not None:
            result['ElasticACU'] = self.elastic_acu

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserverd_compte_acu is not None:
            result['ReserverdCompteACU'] = self.reserverd_compte_acu

        if self.reserverd_storage_acu is not None:
            result['ReserverdStorageACU'] = self.reserverd_storage_acu

        if self.resource_group_count is not None:
            result['ResourceGroupCount'] = self.resource_group_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticACU') is not None:
            self.elastic_acu = m.get('ElasticACU')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReserverdCompteACU') is not None:
            self.reserverd_compte_acu = m.get('ReserverdCompteACU')

        if m.get('ReserverdStorageACU') is not None:
            self.reserverd_storage_acu = m.get('ReserverdStorageACU')

        if m.get('ResourceGroupCount') is not None:
            self.resource_group_count = m.get('ResourceGroupCount')

        return self

