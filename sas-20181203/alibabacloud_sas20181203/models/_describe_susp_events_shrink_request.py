# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSuspEventsShrinkRequest(DaraModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        assets_type_list: List[str] = None,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: str = None,
        dealed: str = None,
        detect_source: str = None,
        event_names: str = None,
        from_: str = None,
        group_id: int = None,
        id: int = None,
        lang: str = None,
        levels: str = None,
        multi_account_action_type: int = None,
        name: str = None,
        operate_error_code_list: List[str] = None,
        operate_time_end: str = None,
        operate_time_start: str = None,
        page_size: str = None,
        parent_event_types: str = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        sort_column: str = None,
        sort_type: str = None,
        source: str = None,
        source_ali_uids_shrink: str = None,
        source_ip: str = None,
        status: str = None,
        strict_mode: str = None,
        support_operate_code_list: List[str] = None,
        tactic_id: str = None,
        target_type: str = None,
        time_end: str = None,
        time_start: str = None,
        unique_info: str = None,
        uuids: str = None,
    ):
        # The ID of the alert event.
        # 
        # > To query the details of an alert event, you must specify the ID of the alert event. You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to query the IDs of alert events.
        self.alarm_unique_info = alarm_unique_info
        # The types of the assets.
        self.assets_type_list = assets_type_list
        # The ID of the cluster of whose alert events you want to query.
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
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether the alert event is handled. Valid values:
        # 
        # *   **N**: unhandled
        # *   **Y**: handled
        self.dealed = dealed
        self.detect_source = detect_source
        # The subtype of the alert event. Separate multiple subtypes with commas (,).
        self.event_names = event_names
        # The data source of the alert event. Set the value to sas.
        self.from_ = from_
        # The ID of the asset group to which the affected asset belongs.
        self.group_id = group_id
        # The ID of the alert event.
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
        # The type of the accounts that you want to query. Default value: **0**. Valid values:
        # 
        # *   **0**: the current account.
        # *   **1**: all accounts.
        self.multi_account_action_type = multi_account_action_type
        # The name of the asset that is affected by the alert event.
        self.name = name
        # An array that consists of the handling result codes of alert events.
        self.operate_error_code_list = operate_error_code_list
        # The timestamp when the handling operation ends.
        self.operate_time_end = operate_time_end
        # The timestamp when the handling operation starts.
        self.operate_time_start = operate_time_start
        # The number of entries per page. Default value: **20**. Maximum value: 100.
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
        # The name of the alert or the information about the asset.
        # 
        # >  Fuzzy search is supported. The asset information includes the name, public IP address, and private IP address of an asset.
        self.remark = remark
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to query the ID.
        self.resource_directory_account_id = resource_directory_account_id
        # The custom sorting field. Default value: **operateTime**. Valid values:
        # 
        # *   **lastTime**: the latest occurrence time.
        # *   **operateTime**: the handling time.
        # 
        # >  This parameter takes effect if you set the **Dealed** parameter to Y.
        self.sort_column = sort_column
        # The custom sorting order. Default value: **desc**. Valid values:
        # 
        # *   **asc**: the ascending order
        # *   **desc**: the descending order
        # 
        # >  This parameter takes effect if you set the **Dealed** parameter to Y.
        self.sort_type = sort_type
        # The source of the alert.
        self.source = source
        # The IDs of the Alibaba Cloud accounts within which alerts are generated.
        self.source_ali_uids_shrink = source_ali_uids_shrink
        # The source IP address of the request.
        self.source_ip = source_ip
        # The status of the alert event. Valid values:
        # 
        # *   **0**: all
        # *   **1**: pending handling
        # *   **2**: ignored
        # *   **4**: confirmed
        # *   **8**: marked as a false positive
        # *   **16**: handling
        # *   **32**: handled
        # *   **64**: expired
        # *   **128**: deleted
        # *   **512**: automatically blocking
        # *   **513**: automatically blocked
        self.status = status
        # Specifies whether to enable the strict alerting mode.
        # 
        # *   N: no
        # *   Y: Yes
        self.strict_mode = strict_mode
        # 告警支持的操作类型列表。
        self.support_operate_code_list = support_operate_code_list
        # The tactic ID of ATT\\&CK.
        self.tactic_id = tactic_id
        # The item that is used to search for the container. Valid values:
        # 
        # *   **containerId**: the ID of the container
        # *   **uuid**: the UUID of the server
        # *   **imageUuid**: the UUID of the image
        self.target_type = target_type
        # The end time when the alert event was last detected.
        self.time_end = time_end
        # The start time when the alert event was last detected.
        self.time_start = time_start
        # The unique key of the alert.
        self.unique_info = unique_info
        # The UUID of the server on which the alert is detected. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

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

        if self.detect_source is not None:
            result['DetectSource'] = self.detect_source

        if self.event_names is not None:
            result['EventNames'] = self.event_names

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

        if self.multi_account_action_type is not None:
            result['MultiAccountActionType'] = self.multi_account_action_type

        if self.name is not None:
            result['Name'] = self.name

        if self.operate_error_code_list is not None:
            result['OperateErrorCodeList'] = self.operate_error_code_list

        if self.operate_time_end is not None:
            result['OperateTimeEnd'] = self.operate_time_end

        if self.operate_time_start is not None:
            result['OperateTimeStart'] = self.operate_time_start

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_event_types is not None:
            result['ParentEventTypes'] = self.parent_event_types

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ali_uids_shrink is not None:
            result['SourceAliUids'] = self.source_ali_uids_shrink

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        if self.support_operate_code_list is not None:
            result['SupportOperateCodeList'] = self.support_operate_code_list

        if self.tactic_id is not None:
            result['TacticId'] = self.tactic_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.time_end is not None:
            result['TimeEnd'] = self.time_end

        if self.time_start is not None:
            result['TimeStart'] = self.time_start

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

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

        if m.get('DetectSource') is not None:
            self.detect_source = m.get('DetectSource')

        if m.get('EventNames') is not None:
            self.event_names = m.get('EventNames')

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

        if m.get('MultiAccountActionType') is not None:
            self.multi_account_action_type = m.get('MultiAccountActionType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperateErrorCodeList') is not None:
            self.operate_error_code_list = m.get('OperateErrorCodeList')

        if m.get('OperateTimeEnd') is not None:
            self.operate_time_end = m.get('OperateTimeEnd')

        if m.get('OperateTimeStart') is not None:
            self.operate_time_start = m.get('OperateTimeStart')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentEventTypes') is not None:
            self.parent_event_types = m.get('ParentEventTypes')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceAliUids') is not None:
            self.source_ali_uids_shrink = m.get('SourceAliUids')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        if m.get('SupportOperateCodeList') is not None:
            self.support_operate_code_list = m.get('SupportOperateCodeList')

        if m.get('TacticId') is not None:
            self.tactic_id = m.get('TacticId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')

        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

