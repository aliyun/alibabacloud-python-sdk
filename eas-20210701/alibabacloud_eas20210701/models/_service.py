# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class Service(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        app_config: str = None,
        app_spec_name: str = None,
        app_type: str = None,
        app_version: str = None,
        autoscaler_enabled: bool = None,
        caller_uid: str = None,
        cpu: int = None,
        create_time: str = None,
        cronscaler_enabled: bool = None,
        current_version: int = None,
        extra_data: str = None,
        gpucore_percentage: int = None,
        gpumemory: int = None,
        gateway: str = None,
        gpu: int = None,
        image: str = None,
        instance_count_in_resource: main_models.ServiceInstanceCountInResource = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        labels: List[main_models.ServiceLabels] = None,
        latest_version: int = None,
        memory: int = None,
        message: str = None,
        namespace: str = None,
        parent_uid: str = None,
        pending_instance: int = None,
        quota_id: str = None,
        reason: str = None,
        region: str = None,
        request_id: str = None,
        resource: str = None,
        resource_alias: str = None,
        resource_burstable: bool = None,
        role: str = None,
        role_attrs: str = None,
        running_instance: int = None,
        safety_lock: str = None,
        secondary_internet_endpoint: str = None,
        secondary_intranet_endpoint: str = None,
        service_config: str = None,
        service_group: str = None,
        service_id: str = None,
        service_name: str = None,
        service_uid: str = None,
        source: str = None,
        status: str = None,
        total_instance: int = None,
        traffic_state: str = None,
        update_time: str = None,
        weight: int = None,
        workspace_id: str = None,
    ):
        self.access_token = access_token
        self.app_config = app_config
        self.app_spec_name = app_spec_name
        self.app_type = app_type
        self.app_version = app_version
        self.autoscaler_enabled = autoscaler_enabled
        self.caller_uid = caller_uid
        self.cpu = cpu
        self.create_time = create_time
        self.cronscaler_enabled = cronscaler_enabled
        self.current_version = current_version
        self.extra_data = extra_data
        self.gpucore_percentage = gpucore_percentage
        self.gpumemory = gpumemory
        self.gateway = gateway
        self.gpu = gpu
        self.image = image
        self.instance_count_in_resource = instance_count_in_resource
        self.internet_endpoint = internet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.labels = labels
        self.latest_version = latest_version
        self.memory = memory
        self.message = message
        self.namespace = namespace
        self.parent_uid = parent_uid
        self.pending_instance = pending_instance
        self.quota_id = quota_id
        self.reason = reason
        self.region = region
        self.request_id = request_id
        self.resource = resource
        self.resource_alias = resource_alias
        self.resource_burstable = resource_burstable
        self.role = role
        self.role_attrs = role_attrs
        self.running_instance = running_instance
        self.safety_lock = safety_lock
        self.secondary_internet_endpoint = secondary_internet_endpoint
        self.secondary_intranet_endpoint = secondary_intranet_endpoint
        self.service_config = service_config
        self.service_group = service_group
        self.service_id = service_id
        self.service_name = service_name
        self.service_uid = service_uid
        self.source = source
        self.status = status
        self.total_instance = total_instance
        self.traffic_state = traffic_state
        self.update_time = update_time
        self.weight = weight
        self.workspace_id = workspace_id

    def validate(self):
        if self.instance_count_in_resource:
            self.instance_count_in_resource.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.app_spec_name is not None:
            result['AppSpecName'] = self.app_spec_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.autoscaler_enabled is not None:
            result['AutoscalerEnabled'] = self.autoscaler_enabled

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cronscaler_enabled is not None:
            result['CronscalerEnabled'] = self.cronscaler_enabled

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.gpucore_percentage is not None:
            result['GPUCorePercentage'] = self.gpucore_percentage

        if self.gpumemory is not None:
            result['GPUMemory'] = self.gpumemory

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.image is not None:
            result['Image'] = self.image

        if self.instance_count_in_resource is not None:
            result['InstanceCountInResource'] = self.instance_count_in_resource.to_map()

        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid

        if self.pending_instance is not None:
            result['PendingInstance'] = self.pending_instance

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_alias is not None:
            result['ResourceAlias'] = self.resource_alias

        if self.resource_burstable is not None:
            result['ResourceBurstable'] = self.resource_burstable

        if self.role is not None:
            result['Role'] = self.role

        if self.role_attrs is not None:
            result['RoleAttrs'] = self.role_attrs

        if self.running_instance is not None:
            result['RunningInstance'] = self.running_instance

        if self.safety_lock is not None:
            result['SafetyLock'] = self.safety_lock

        if self.secondary_internet_endpoint is not None:
            result['SecondaryInternetEndpoint'] = self.secondary_internet_endpoint

        if self.secondary_intranet_endpoint is not None:
            result['SecondaryIntranetEndpoint'] = self.secondary_intranet_endpoint

        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config

        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_uid is not None:
            result['ServiceUid'] = self.service_uid

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.total_instance is not None:
            result['TotalInstance'] = self.total_instance

        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AppSpecName') is not None:
            self.app_spec_name = m.get('AppSpecName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AutoscalerEnabled') is not None:
            self.autoscaler_enabled = m.get('AutoscalerEnabled')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CronscalerEnabled') is not None:
            self.cronscaler_enabled = m.get('CronscalerEnabled')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('GPUCorePercentage') is not None:
            self.gpucore_percentage = m.get('GPUCorePercentage')

        if m.get('GPUMemory') is not None:
            self.gpumemory = m.get('GPUMemory')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('InstanceCountInResource') is not None:
            temp_model = main_models.ServiceInstanceCountInResource()
            self.instance_count_in_resource = temp_model.from_map(m.get('InstanceCountInResource'))

        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ServiceLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')

        if m.get('PendingInstance') is not None:
            self.pending_instance = m.get('PendingInstance')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceAlias') is not None:
            self.resource_alias = m.get('ResourceAlias')

        if m.get('ResourceBurstable') is not None:
            self.resource_burstable = m.get('ResourceBurstable')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RoleAttrs') is not None:
            self.role_attrs = m.get('RoleAttrs')

        if m.get('RunningInstance') is not None:
            self.running_instance = m.get('RunningInstance')

        if m.get('SafetyLock') is not None:
            self.safety_lock = m.get('SafetyLock')

        if m.get('SecondaryInternetEndpoint') is not None:
            self.secondary_internet_endpoint = m.get('SecondaryInternetEndpoint')

        if m.get('SecondaryIntranetEndpoint') is not None:
            self.secondary_intranet_endpoint = m.get('SecondaryIntranetEndpoint')

        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')

        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceUid') is not None:
            self.service_uid = m.get('ServiceUid')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalInstance') is not None:
            self.total_instance = m.get('TotalInstance')

        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ServiceLabels(DaraModel):
    def __init__(
        self,
        label_key: str = None,
        label_value: str = None,
    ):
        self.label_key = label_key
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_key is not None:
            result['LabelKey'] = self.label_key

        if self.label_value is not None:
            result['LabelValue'] = self.label_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')

        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')

        return self

class ServiceInstanceCountInResource(DaraModel):
    def __init__(
        self,
        dedicated: int = None,
        public: int = None,
        quota: int = None,
    ):
        self.dedicated = dedicated
        self.public = public
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated is not None:
            result['Dedicated'] = self.dedicated

        if self.public is not None:
            result['Public'] = self.public

        if self.quota is not None:
            result['Quota'] = self.quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dedicated') is not None:
            self.dedicated = m.get('Dedicated')

        if m.get('Public') is not None:
            self.public = m.get('Public')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        return self

