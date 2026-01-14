# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClusterRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_alias_name: str = None,
        instance_id: str = None,
        maintenance_end_time: str = None,
        maintenance_start_time: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The alias of the instance.
        self.cluster_alias_name = cluster_alias_name
        # The ID of the instance.
        self.instance_id = instance_id
        # The end time of the O\\&M window.
        self.maintenance_end_time = maintenance_end_time
        # The start time of the O\\&M window.
        self.maintenance_start_time = maintenance_start_time
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.maintenance_end_time is not None:
            result['MaintenanceEndTime'] = self.maintenance_end_time

        if self.maintenance_start_time is not None:
            result['MaintenanceStartTime'] = self.maintenance_start_time

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaintenanceEndTime') is not None:
            self.maintenance_end_time = m.get('MaintenanceEndTime')

        if m.get('MaintenanceStartTime') is not None:
            self.maintenance_start_time = m.get('MaintenanceStartTime')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

