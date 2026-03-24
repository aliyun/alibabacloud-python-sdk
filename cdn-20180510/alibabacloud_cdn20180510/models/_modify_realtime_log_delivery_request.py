# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRealtimeLogDeliveryRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The accelerated domain name for which you want to modify the configurations of real-time log delivery. Only one domain name is supported.
        # 
        # This parameter is required.
        self.domain = domain
        # The name of the Logstore where log entries are stored.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        # 
        # This parameter is required.
        self.project = project
        # The ID of the region where the Log Service project is deployed. For more information, see [Regions that support real-time log delivery](https://help.aliyun.com/document_detail/144883.html).
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

