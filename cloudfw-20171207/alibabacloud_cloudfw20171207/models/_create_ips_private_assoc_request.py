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
        # The language of the request and response messages.
        self.lang = lang
        # The ID of the Internet NAT gateway instance to associate. This parameter is required. If this parameter is not specified, ErrorParamsNotEnough is returned (HTTP 400, Parameters are insufficient.).
        # 
        # > The backend does not validate the ID format. Instead, it queries the instance in the Cloud Firewall private network asset table for the current account. If the instance is not found, ErrorParamsInvalid is returned (HTTP 400, Invalid Params). Common scenarios include the resource type not being a NAT gateway, the resource not being managed by Cloud Firewall, or a newly created NAT gateway for which asynchronous asset synchronization has not yet completed.
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

