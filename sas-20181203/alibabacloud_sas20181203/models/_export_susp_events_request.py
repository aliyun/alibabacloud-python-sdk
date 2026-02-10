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
        source_ip: str = None,
        status: str = None,
        target_type: str = None,
        time_end: str = None,
        time_start: str = None,
        unique_info: str = None,
        uuid: str = None,
    ):
        # The types of assets.
        self.assets_type_list = assets_type_list
        # The ID of the cluster that you want to query.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The key of the condition that is used to query alert events on containers. Valid values:
        # 
        # *   **instanceId**: the ID of the asset
        # *   **appName**: the name of the application
        # *   **clusterId**: the ID of the cluster
        # *   **regionId**: the ID of the region
        # *   **nodeName**: the name of the node
        # *   **namespace**: the namespace
        # *   **clusterName**: the name of the cluster
        # *   **image**: the name of the image
        # *   **imageRepoName**: the name of the image repository
        # *   **imageRepoNamespace**: the namespace to which the image repository belongs
        # *   **imageRepoTag**: the tag that is added to the image
        # *   **imageDigest**: the digest of the image
        self.container_field_name = container_field_name
        # The value of the condition that is used to query alert events on containers.
        self.container_field_value = container_field_value
        # The number of the page to return.
        self.current_page = current_page
        # The status of the alert event. Valid values:
        # 
        # *   **N**: unhandled
        # *   **Y**: handled
        self.dealed = dealed
        # The data source of the exception. Set the value to sas.
        self.from_ = from_
        # The ID of the asset group.
        self.group_id = group_id
        # The unique ID of the alert event.
        self.id = id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The severity of the alert event. Separate multiple severities with commas (,). Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.levels = levels
        # The complete name of the exception.
        self.name = name
        # The status codes of alert events.
        self.operate_error_code_list = operate_error_code_list
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The alert type of the alert event. Valid values:
        # 
        # *   **Suspicious process**
        # *   **Webshell**
        # *   **Unusual logon**
        # *   **Exception**
        # *   **Sensitive file tampering**
        # *   **Malicious process (cloud threat detection)**
        # *   **Suspicious network connection**
        # *   **Suspicious account**
        # *   **Application intrusion event**
        # *   **Cloud threat detection**
        # *   **Precise defense**
        # *   **Application whitelist**
        # *   **Persistent webshell**
        # *   **Web application threat detection**
        # *   **Malicious script**
        # *   **Threat intelligence**
        # *   **Malicious network activity**
        # *   **Cluster exception**
        # *   **Webshell (on-premises threat detection)**
        # *   **Vulnerability exploitation**
        # *   **Malicious process (on-premises threat detection)**
        # *   **Trusted exception**
        # *   **Others**
        self.parent_event_types = parent_event_types
        # The remarks.
        self.remark = remark
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip
        # The handling status of the exception. Valid values:
        # 
        # *   **0**: all status
        # *   **1**: pending handling
        # *   **2**: ignored
        # *   **4**: confirmed
        # *   **8**: marked as false positive
        # *   **16**: handling
        # *   **32**: handled
        # *   **64**: expired
        # *   **128**: deleted
        self.status = status
        # The dimension from which you want to configure the feature. Valid values:
        # 
        # *   **uuid**: the UUID of the asset
        # *   **image_repo**: the ID of the image repository
        # *   **Cluster**: the ID of the cluster
        self.target_type = target_type
        # The end of the time range during which the exception is detected.
        self.time_end = time_end
        # The beginning of the time range during which the exception is detected.
        self.time_start = time_start
        # The unique key of the alert event.
        self.unique_info = unique_info
        # The unique ID of the associated instance.
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

