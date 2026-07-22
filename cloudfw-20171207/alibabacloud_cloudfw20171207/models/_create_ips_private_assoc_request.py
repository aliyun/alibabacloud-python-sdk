# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpsPrivateAssocRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        resource_id: str = None,
    ):
        # The language type for the request and response messages. Valid values:
        # - en: English.
        # - zh: Chinese.
        self.lang = lang
        # The instance ID. This parameter is required. If this parameter is not specified, the API returns error code -103201. Only NAT gateway instance IDs (in the format ngw-*) that are protected by Cloud Firewall are accepted. Other resource types such as vpc-* or eip-* are rejected.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

