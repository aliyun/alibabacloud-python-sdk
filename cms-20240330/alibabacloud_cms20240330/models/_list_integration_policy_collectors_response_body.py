# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPolicyCollectorsResponseBody(DaraModel):
    def __init__(
        self,
        collectors: List[main_models.ListIntegrationPolicyCollectorsResponseBodyCollectors] = None,
        request_id: str = None,
    ):
        self.collectors = collectors
        self.request_id = request_id

    def validate(self):
        if self.collectors:
            for v1 in self.collectors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['collectors'] = []
        if self.collectors is not None:
            for k1 in self.collectors:
                result['collectors'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.collectors = []
        if m.get('collectors') is not None:
            for k1 in m.get('collectors'):
                temp_model = main_models.ListIntegrationPolicyCollectorsResponseBodyCollectors()
                self.collectors.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListIntegrationPolicyCollectorsResponseBodyCollectors(DaraModel):
    def __init__(
        self,
        addon_meta: main_models.AddonMeta = None,
        collector_name: str = None,
        collector_type: str = None,
        conditions: List[main_models.ListIntegrationPolicyCollectorsResponseBodyCollectorsConditions] = None,
        managed: bool = None,
        release_name: str = None,
        state: str = None,
        version: str = None,
        workloads: List[main_models.ListIntegrationPolicyCollectorsResponseBodyCollectorsWorkloads] = None,
    ):
        self.addon_meta = addon_meta
        self.collector_name = collector_name
        self.collector_type = collector_type
        self.conditions = conditions
        self.managed = managed
        self.release_name = release_name
        self.state = state
        self.version = version
        self.workloads = workloads

    def validate(self):
        if self.addon_meta:
            self.addon_meta.validate()
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.workloads:
            for v1 in self.workloads:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_meta is not None:
            result['addonMeta'] = self.addon_meta.to_map()

        if self.collector_name is not None:
            result['collectorName'] = self.collector_name

        if self.collector_type is not None:
            result['collectorType'] = self.collector_type

        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.managed is not None:
            result['managed'] = self.managed

        if self.release_name is not None:
            result['releaseName'] = self.release_name

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        result['workloads'] = []
        if self.workloads is not None:
            for k1 in self.workloads:
                result['workloads'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonMeta') is not None:
            temp_model = main_models.AddonMeta()
            self.addon_meta = temp_model.from_map(m.get('addonMeta'))

        if m.get('collectorName') is not None:
            self.collector_name = m.get('collectorName')

        if m.get('collectorType') is not None:
            self.collector_type = m.get('collectorType')

        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.ListIntegrationPolicyCollectorsResponseBodyCollectorsConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('managed') is not None:
            self.managed = m.get('managed')

        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        self.workloads = []
        if m.get('workloads') is not None:
            for k1 in m.get('workloads'):
                temp_model = main_models.ListIntegrationPolicyCollectorsResponseBodyCollectorsWorkloads()
                self.workloads.append(temp_model.from_map(k1))

        return self

class ListIntegrationPolicyCollectorsResponseBodyCollectorsWorkloads(DaraModel):
    def __init__(
        self,
        host_ip: str = None,
        ip: str = None,
        managed: bool = None,
        managed_info: main_models.ListIntegrationPolicyCollectorsResponseBodyCollectorsWorkloadsManagedInfo = None,
        message: str = None,
        name: str = None,
        namespace: str = None,
        owner_reference_kind: str = None,
        owner_reference_name: str = None,
        start_time: str = None,
        status: str = None,
        version: str = None,
    ):
        self.host_ip = host_ip
        self.ip = ip
        self.managed = managed
        self.managed_info = managed_info
        self.message = message
        self.name = name
        self.namespace = namespace
        self.owner_reference_kind = owner_reference_kind
        self.owner_reference_name = owner_reference_name
        self.start_time = start_time
        self.status = status
        self.version = version

    def validate(self):
        if self.managed_info:
            self.managed_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_ip is not None:
            result['hostIp'] = self.host_ip

        if self.ip is not None:
            result['ip'] = self.ip

        if self.managed is not None:
            result['managed'] = self.managed

        if self.managed_info is not None:
            result['managedInfo'] = self.managed_info.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.owner_reference_kind is not None:
            result['ownerReferenceKind'] = self.owner_reference_kind

        if self.owner_reference_name is not None:
            result['ownerReferenceName'] = self.owner_reference_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostIp') is not None:
            self.host_ip = m.get('hostIp')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('managed') is not None:
            self.managed = m.get('managed')

        if m.get('managedInfo') is not None:
            temp_model = main_models.ListIntegrationPolicyCollectorsResponseBodyCollectorsWorkloadsManagedInfo()
            self.managed_info = temp_model.from_map(m.get('managedInfo'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('ownerReferenceKind') is not None:
            self.owner_reference_kind = m.get('ownerReferenceKind')

        if m.get('ownerReferenceName') is not None:
            self.owner_reference_name = m.get('ownerReferenceName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListIntegrationPolicyCollectorsResponseBodyCollectorsWorkloadsManagedInfo(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        vswitch_id: str = None,
    ):
        self.security_group_id = security_group_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        return self

class ListIntegrationPolicyCollectorsResponseBodyCollectorsConditions(DaraModel):
    def __init__(
        self,
        first_transition_time: str = None,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        self.first_transition_time = first_transition_time
        self.last_transition_time = last_transition_time
        self.message = message
        self.reason = reason
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_transition_time is not None:
            result['firstTransitionTime'] = self.first_transition_time

        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time

        if self.message is not None:
            result['message'] = self.message

        if self.reason is not None:
            result['reason'] = self.reason

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstTransitionTime') is not None:
            self.first_transition_time = m.get('firstTransitionTime')

        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

