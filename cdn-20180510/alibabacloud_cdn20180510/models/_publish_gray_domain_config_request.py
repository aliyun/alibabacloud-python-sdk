# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishGrayDomainConfigRequest(DaraModel):
    def __init__(
        self,
        custom_country_id: int = None,
        custom_percent: int = None,
        custom_province_id: int = None,
        domain_name: str = None,
        publish_mode: str = None,
    ):
        self.custom_country_id = custom_country_id
        self.custom_percent = custom_percent
        self.custom_province_id = custom_province_id
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.publish_mode = publish_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_country_id is not None:
            result['CustomCountryId'] = self.custom_country_id

        if self.custom_percent is not None:
            result['CustomPercent'] = self.custom_percent

        if self.custom_province_id is not None:
            result['CustomProvinceId'] = self.custom_province_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomCountryId') is not None:
            self.custom_country_id = m.get('CustomCountryId')

        if m.get('CustomPercent') is not None:
            self.custom_percent = m.get('CustomPercent')

        if m.get('CustomProvinceId') is not None:
            self.custom_province_id = m.get('CustomProvinceId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        return self

