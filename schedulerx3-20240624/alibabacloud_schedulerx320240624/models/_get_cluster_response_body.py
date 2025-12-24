# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetClusterResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetClusterResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetClusterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetClusterResponseBodyData(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        create_time: str = None,
        end_time: str = None,
        engine_type: str = None,
        engine_version: str = None,
        internet_domain: str = None,
        intranet_domain: str = None,
        job_num: int = None,
        kube_config: str = None,
        max_job_num: int = None,
        max_workflow_num: int = None,
        product_type: int = None,
        spm: int = None,
        status: int = None,
        tags: Dict[str, Any] = None,
        v_switches: List[main_models.GetClusterResponseBodyDataVSwitches] = None,
        version_lifecycle: str = None,
        vpc_id: str = None,
        worker_num: int = None,
        workflow_num: int = None,
        zones: List[str] = None,
    ):
        self.charge_type = charge_type
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_spec = cluster_spec
        self.create_time = create_time
        self.end_time = end_time
        self.engine_type = engine_type
        self.engine_version = engine_version
        self.internet_domain = internet_domain
        self.intranet_domain = intranet_domain
        self.job_num = job_num
        self.kube_config = kube_config
        self.max_job_num = max_job_num
        self.max_workflow_num = max_workflow_num
        self.product_type = product_type
        self.spm = spm
        self.status = status
        self.tags = tags
        self.v_switches = v_switches
        self.version_lifecycle = version_lifecycle
        # VPC ID
        self.vpc_id = vpc_id
        self.worker_num = worker_num
        self.workflow_num = workflow_num
        self.zones = zones

    def validate(self):
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain

        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        if self.job_num is not None:
            result['JobNum'] = self.job_num

        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config

        if self.max_job_num is not None:
            result['MaxJobNum'] = self.max_job_num

        if self.max_workflow_num is not None:
            result['MaxWorkflowNum'] = self.max_workflow_num

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.spm is not None:
            result['Spm'] = self.spm

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        if self.version_lifecycle is not None:
            result['VersionLifecycle'] = self.version_lifecycle

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num

        if self.workflow_num is not None:
            result['WorkflowNum'] = self.workflow_num

        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')

        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        if m.get('JobNum') is not None:
            self.job_num = m.get('JobNum')

        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')

        if m.get('MaxJobNum') is not None:
            self.max_job_num = m.get('MaxJobNum')

        if m.get('MaxWorkflowNum') is not None:
            self.max_workflow_num = m.get('MaxWorkflowNum')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Spm') is not None:
            self.spm = m.get('Spm')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.GetClusterResponseBodyDataVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('VersionLifecycle') is not None:
            self.version_lifecycle = m.get('VersionLifecycle')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')

        if m.get('WorkflowNum') is not None:
            self.workflow_num = m.get('WorkflowNum')

        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

class GetClusterResponseBodyDataVSwitches(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

