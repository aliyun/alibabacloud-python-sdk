# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDcdnSLSRealtimeLogDeliveryRequest(DaraModel):
    def __init__(
        self,
        data_center: str = None,
        domain_name: str = None,
        project_name: str = None,
        slslog_store: str = None,
        slsproject: str = None,
        slsregion: str = None,
        sampling_rate: str = None,
    ):
        # The region from which logs are collected.
        # 
        # *   **cn**: Chinese mainland
        # *   **sg**: Singapore
        # *   **in**: India
        # *   **eu**: Europe
        # *   **us**: United States
        # 
        # This parameter is required.
        self.data_center = data_center
        # The domain names from which logs were collected. You can specify one or more domain names. Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.slslog_store = slslog_store
        # The name of the log file.
        # 
        # This parameter is required.
        self.slsproject = slsproject
        # The region to which logs were delivered.
        # 
        # This parameter is required.
        self.slsregion = slsregion
        # The sampling rate.
        self.sampling_rate = sampling_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        return self

