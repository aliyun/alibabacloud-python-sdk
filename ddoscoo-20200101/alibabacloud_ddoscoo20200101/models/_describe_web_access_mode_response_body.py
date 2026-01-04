# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebAccessModeResponseBody(DaraModel):
    def __init__(
        self,
        domain_modes: List[main_models.DescribeWebAccessModeResponseBodyDomainModes] = None,
        request_id: str = None,
    ):
        # An array consisting of the modes in which the website service is added.
        self.domain_modes = domain_modes
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_modes:
            for v1 in self.domain_modes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainModes'] = []
        if self.domain_modes is not None:
            for k1 in self.domain_modes:
                result['DomainModes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_modes = []
        if m.get('DomainModes') is not None:
            for k1 in m.get('DomainModes'):
                temp_model = main_models.DescribeWebAccessModeResponseBodyDomainModes()
                self.domain_modes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWebAccessModeResponseBodyDomainModes(DaraModel):
    def __init__(
        self,
        access_mode: int = None,
        domain: str = None,
    ):
        # The mode in which the website service is added. Valid values:
        # 
        # *   **0**: A record
        # *   **1**: anti-DDoS mode
        # *   **2**: origin redundancy mode
        self.access_mode = access_mode
        # The domain name of the website.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

