# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportSuspEventsRequest(DaraModel):
    def __init__(
        self,
        assets_type_list: List[str] = None,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: str = None,
        dealed: str = None,
        from_: str = None,
        group_id: int = None,
        id: int = None,
        lang: str = None,
        levels: str = None,
        name: str = None,
        operate_error_code_list: List[str] = None,
        page_size: str = None,
        parent_event_types: str = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        source_ip: str = None,
        status: str = None,
        target_type: str = None,
        time_end: str = None,
        time_start: str = None,
        unique_info: str = None,
        uuid: str = None,
    ):
        # The collection of asset types.
        self.assets_type_list = assets_type_list
        # The ID of the cluster to query.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The container search field. Valid values:
        # 
        # - **instanceId**: instance ID
        # - **appName**: application name
        # - **clusterId**: cluster ID
        # - **regionId**: region
        # - **nodeName**: node name
        # - **namespace**: namespace
        # - **clusterName**: cluster name
        # - **image**: image name
        # - **imageRepoName**: image repository name
        # - **imageRepoNamespace**: image repository namespace
        # - **imageRepoTag**: image tag
        # - **imageDigest**: image digest
        self.container_field_name = container_field_name
        # The value of the container search field.
        self.container_field_value = container_field_value
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # Specifies whether the alert event is handled. Valid values:
        # - **N**: Unhandled.
        # - **Y**: Handled.
        self.dealed = dealed
        # The data source identifier of the anomaly event. Set the value to sas.
        self.from_ = from_
        # The ID of the asset group.
        self.group_id = group_id
        # The unique ID of the alert event record.
        self.id = id
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The severity levels of the alert events to query. Separate multiple severity levels with commas (,). The severity levels are listed in descending order. Valid values:
        # - **serious**: Urgent.
        # - **suspicious**: Suspicious.
        # - **remind**: Reminder.
        self.levels = levels
        # The full name of the anomaly event.
        self.name = name
        # The collection of alert event handling result codes.
        self.operate_error_code_list = operate_error_code_list
        # The maximum number of entries per page in a paged query. Default value: **20**.
        self.page_size = page_size
        # The Alarm Metric of the alerting events to query. Valid values:
        # 
        # - **Abnormal process behavior**
        # - **Web shell**
        # - **Unusual logon**
        # - **Anomaly event**
        # - **Sensitive file tampering**
        # - **Malicious process (cloud scan)**
        # - **Suspicious network connection**
        # - **Abnormal account**
        # - **Application intrusion event**
        # - **Cloud service threat detection**
        # - **Precise defense**
        # - **Application whitelist**
        # - **Persistent backdoor**
        # - **Web application threat detection**
        # - **Malicious script**
        # - **Threat intelligence**
        # - **Malicious network connectivity behavior**
        # - **Container cluster exception**
        # - **Web shell (local scan)**
        # - **Vulnerability exploits**
        # - **Malicious process (local scan)**
        # - **Trusted exception**
        # - **Other**
        self.parent_event_types = parent_event_types
        # The remarks.
        self.remark = remark
        # The ID of the Alibaba Cloud account of the member accounts in the resource directory.
        # > You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address of the request. You do not need to specify this parameter. The system automatically obtains this value.
        self.source_ip = source_ip
        # The handling status of the anomaly event. Valid values:
        # - **0**: All.
        # - **1**: Unhandled.
        # - **2**: Ignored.
        # - **4**: Confirmed.
        # - **8**: Marked as false positive.
        # - **16**: Handling.
        # - **32**: Handled.
        # - **64**: Expired.
        # - **128**: Deleted.
        self.status = status
        # The dimension of the target switch configuration. Valid values:
        # 
        # - **uuid**: asset UUID
        # - **image_repo**: image repository ID
        # - **Cluster**: cluster ID
        self.target_type = target_type
        # The end time of the anomaly event. Format: YYYY-MM-DD HH:mm:ss.
        self.time_end = time_end
        # The start time of the anomaly event occurrence. Format: YYYY-MM-DD HH:mm:ss.
        self.time_start = time_start
        # The unique key of the security alert.
        self.unique_info = unique_info
        # The unique identifier of the associated instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_type_list is not None:
            result['AssetsTypeList'] = self.assets_type_list

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.from_ is not None:
            result['From'] = self.from_

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.levels is not None:
            result['Levels'] = self.levels

        if self.name is not None:
            result['Name'] = self.name

        if self.operate_error_code_list is not None:
            result['OperateErrorCodeList'] = self.operate_error_code_list

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_event_types is not None:
            result['ParentEventTypes'] = self.parent_event_types

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.time_end is not None:
            result['TimeEnd'] = self.time_end

        if self.time_start is not None:
            result['TimeStart'] = self.time_start

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsTypeList') is not None:
            self.assets_type_list = m.get('AssetsTypeList')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperateErrorCodeList') is not None:
            self.operate_error_code_list = m.get('OperateErrorCodeList')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentEventTypes') is not None:
            self.parent_event_types = m.get('ParentEventTypes')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')

        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

