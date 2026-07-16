# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServicesShrinkRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        autoscaler_enabled: bool = None,
        caller_uid: str = None,
        cronscaler_enabled: bool = None,
        filter: str = None,
        gateway: str = None,
        group_name: str = None,
        include_no_workspace: bool = None,
        label_shrink: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_service_uid: str = None,
        quota_id: str = None,
        resource_alias_name: str = None,
        resource_burstable: bool = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        role: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        service_uid: str = None,
        sort: str = None,
        traffic_state: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # Specifies whether to enable Auto Scaling for the service.
        self.autoscaler_enabled = autoscaler_enabled
        # The UID of the account that created the service.
        self.caller_uid = caller_uid
        # Specifies whether to enable scheduled auto scaling for the service.
        self.cronscaler_enabled = cronscaler_enabled
        # The keyword for a fuzzy search. This parameter supports fuzzy searches by service name only.
        self.filter = filter
        # The private gateway ID.
        self.gateway = gateway
        # The name of the service group. To learn how to obtain this name, see [ListServices](https://help.aliyun.com/document_detail/412109.html).
        self.group_name = group_name
        # Specifies whether to include services that do not belong to any workspace. The default value is true.
        self.include_no_workspace = include_no_workspace
        # Filters services by label.
        self.label_shrink = label_shrink
        # The sort order. Valid values:
        # 
        # - `desc` (default): descending.
        # 
        # - `asc`: ascending.
        self.order = order
        # The page number of the results to return. The default value is 1.
        self.page_number = page_number
        # The number of services to return per page. The default value is 100.
        self.page_size = page_size
        # The UID of the primary service. This parameter applies to member services in a service group.
        self.parent_service_uid = parent_service_uid
        # The quota ID.
        self.quota_id = quota_id
        # The custom name of the resource group.
        self.resource_alias_name = resource_alias_name
        # Specifies whether to enable a burstable resource pool for the service.
        self.resource_burstable = resource_burstable
        # The ID of the resource group. To learn how to query for this ID, see [ListResources](https://help.aliyun.com/document_detail/412133.html).
        self.resource_id = resource_id
        # The name or ID of the service\\"s resource group.
        self.resource_name = resource_name
        # The type of resource the service uses. Valid values:
        # 
        # - PublicResource
        # 
        # - DedicatedResource
        # 
        # - Lingjun
        # 
        # - SelfManagedLingjun
        self.resource_type = resource_type
        # The service role.
        self.role = role
        # The service name.
        self.service_name = service_name
        # The status of the service.
        self.service_status = service_status
        # The service type. Valid values:
        # 
        # - Async
        # 
        # - Standard
        # 
        # - Queue
        # 
        # - LLM
        # 
        # - RAG
        # 
        # - Serverless
        # 
        # - LLMGatewayService
        # 
        # - OfflineTask
        # 
        # - SDCluster
        # 
        # - ScalableJob
        # 
        # - ScalableJobService
        # 
        # - AssistantJob
        self.service_type = service_type
        # The service UID.
        self.service_uid = service_uid
        # The sort field. By default, results are sorted by timestamp in descending order.
        self.sort = sort
        # Specifies whether the service accepts group traffic. This parameter applies only to services within a service group.
        self.traffic_state = traffic_state
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.autoscaler_enabled is not None:
            result['AutoscalerEnabled'] = self.autoscaler_enabled

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.cronscaler_enabled is not None:
            result['CronscalerEnabled'] = self.cronscaler_enabled

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.include_no_workspace is not None:
            result['IncludeNoWorkspace'] = self.include_no_workspace

        if self.label_shrink is not None:
            result['Label'] = self.label_shrink

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_service_uid is not None:
            result['ParentServiceUid'] = self.parent_service_uid

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.resource_alias_name is not None:
            result['ResourceAliasName'] = self.resource_alias_name

        if self.resource_burstable is not None:
            result['ResourceBurstable'] = self.resource_burstable

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.role is not None:
            result['Role'] = self.role

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_uid is not None:
            result['ServiceUid'] = self.service_uid

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AutoscalerEnabled') is not None:
            self.autoscaler_enabled = m.get('AutoscalerEnabled')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('CronscalerEnabled') is not None:
            self.cronscaler_enabled = m.get('CronscalerEnabled')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IncludeNoWorkspace') is not None:
            self.include_no_workspace = m.get('IncludeNoWorkspace')

        if m.get('Label') is not None:
            self.label_shrink = m.get('Label')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentServiceUid') is not None:
            self.parent_service_uid = m.get('ParentServiceUid')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('ResourceAliasName') is not None:
            self.resource_alias_name = m.get('ResourceAliasName')

        if m.get('ResourceBurstable') is not None:
            self.resource_burstable = m.get('ResourceBurstable')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceUid') is not None:
            self.service_uid = m.get('ServiceUid')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

