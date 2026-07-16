# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetDoctorComputeSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        component_info: main_models.GetDoctorComputeSummaryRequestComponentInfo = None,
        date_time: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The resource information, which is used to filter the results.
        self.component_info = component_info
        # Specify the date in the ISO 8601 standard. For example, 2023-01-01 represents January 1, 2023.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.component_info:
            self.component_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_info is not None:
            result['ComponentInfo'] = self.component_info.to_map()

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentInfo') is not None:
            temp_model = main_models.GetDoctorComputeSummaryRequestComponentInfo()
            self.component_info = temp_model.from_map(m.get('ComponentInfo'))

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetDoctorComputeSummaryRequestComponentInfo(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        component_type: str = None,
    ):
        # Set the filter condition name based on the value of ComponentType. For example, if you set ComponentType to queue, you can specify a specific queue name to obtain the resource usage of a specific queue.
        self.component_name = component_name
        # The resource type for filtering. Valid values:
        # 
        # *   engine: filters results by engine.
        # *   queue: filters results by queue.
        # *   cluster: displays the results at the cluster level.
        # 
        # If you do not specify this parameter, the information at the cluster level is displayed by default.
        self.component_type = component_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        return self

