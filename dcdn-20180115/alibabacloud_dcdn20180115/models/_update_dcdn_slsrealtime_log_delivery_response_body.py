# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class UpdateDcdnSLSRealtimeLogDeliveryResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent = None,
        request_id: str = None,
    ):
        # The configuration results of the domain name.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContent(DaraModel):
    def __init__(
        self,
        domains: List[main_models.UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains] = None,
    ):
        self.domains = domains

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains()
                self.domains.append(temp_model.from_map(k1))

        return self

class UpdateDcdnSLSRealtimeLogDeliveryResponseBodyContentDomains(DaraModel):
    def __init__(
        self,
        desc: str = None,
        domain_name: str = None,
        region: str = None,
        status: str = None,
    ):
        # The description of the returned result.
        self.desc = desc
        # The domain name.
        self.domain_name = domain_name
        # The name of the region.
        self.region = region
        # Indicates whether the real-time log delivery project was successfully updated. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.region is not None:
            result['Region'] = self.region

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

