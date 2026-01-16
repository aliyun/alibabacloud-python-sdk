# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ValidateTransferableNodesRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.ValidateTransferableNodesRequestBody] = None,
        node_type: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.ValidateTransferableNodesRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        return self

class ValidateTransferableNodesRequestBody(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['host'] = self.host

        if self.port is not None:
            result['port'] = self.port

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

