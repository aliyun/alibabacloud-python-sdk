# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnUserVipsByDomainResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        vips: main_models.DescribeDcdnUserVipsByDomainResponseBodyVips = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The request ID.
        self.request_id = request_id
        # The list of VIPs.
        self.vips = vips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vips is not None:
            result['Vips'] = self.vips.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Vips') is not None:
            temp_model = main_models.DescribeDcdnUserVipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m.get('Vips'))

        return self

class DescribeDcdnUserVipsByDomainResponseBodyVips(DaraModel):
    def __init__(
        self,
        vip: List[str] = None,
    ):
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vip is not None:
            result['Vip'] = self.vip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        return self

