# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListComponentInstancesResponseBody(DaraModel):
    def __init__(
        self,
        component_instances: List[main_models.ListComponentInstancesResponseBodyComponentInstances] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of instance component installation information.
        self.component_instances = component_instances
        # The maximum number of entries returned.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.component_instances:
            for v1 in self.component_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentInstances'] = []
        if self.component_instances is not None:
            for k1 in self.component_instances:
                result['ComponentInstances'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_instances = []
        if m.get('ComponentInstances') is not None:
            for k1 in m.get('ComponentInstances'):
                temp_model = main_models.ListComponentInstancesResponseBodyComponentInstances()
                self.component_instances.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListComponentInstancesResponseBodyComponentInstances(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        biz_state: str = None,
        commission_state: str = None,
        component_instance_state: str = None,
        component_name: str = None,
        create_time: int = None,
        desired_state: str = None,
        node_id: str = None,
        node_name: str = None,
        zone_id: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The status of the component service. Valid values:
        # 
        # *   active: the primary service.
        # *   standby: the standby service.
        self.biz_state = biz_state
        # The status of the Commission. Valid values:
        # 
        # *   COMMISSIONED
        # *   COMMISSIONING
        # *   DECOMMISSIONED
        # *   DECOMMISSIONINPROGRESS
        # *   DECOMMISSIONFAILED
        # *   INSERVICE
        # *   UNKNOWN
        self.commission_state = commission_state
        # The status of the component. Valid values:
        # 
        # *   WAITING
        # *   INSTALLING
        # *   INSTALLED
        # *   INSTALL_FAILED
        # *   STARTING
        # *   STARTED
        # *   START_FAILED
        # *   STOPPING
        # *   STOPPED
        # *   STOP_FAILED
        self.component_instance_state = component_instance_state
        # The component name.
        self.component_name = component_name
        # The timestamp of the installation.
        self.create_time = create_time
        # Valid values:
        # 
        # *   WAITING
        # *   INSTALLING
        # *   INSTALLED
        # *   INSTALL_FAILED
        # *   STARTING
        # *   STARTED
        # *   START_FAILED
        # *   STOPPING
        # *   STOPPED
        # *   STOP_FAILED
        self.desired_state = desired_state
        # The instance ID.
        self.node_id = node_id
        # The instance name.
        self.node_name = node_name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.biz_state is not None:
            result['BizState'] = self.biz_state

        if self.commission_state is not None:
            result['CommissionState'] = self.commission_state

        if self.component_instance_state is not None:
            result['ComponentInstanceState'] = self.component_instance_state

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.desired_state is not None:
            result['DesiredState'] = self.desired_state

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('BizState') is not None:
            self.biz_state = m.get('BizState')

        if m.get('CommissionState') is not None:
            self.commission_state = m.get('CommissionState')

        if m.get('ComponentInstanceState') is not None:
            self.component_instance_state = m.get('ComponentInstanceState')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DesiredState') is not None:
            self.desired_state = m.get('DesiredState')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

