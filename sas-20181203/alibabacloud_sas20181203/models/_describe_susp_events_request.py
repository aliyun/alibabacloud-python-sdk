# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSuspEventsRequest(DaraModel):
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
        source_ali_uids: List[int] = None,
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
        # The unique ID of the alert event.
        # 
        # > To query the exception information of a single alert event, provide the unique ID of the alert event. You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to obtain the ID.
        self.alarm_unique_info = alarm_unique_info
        # The collection of asset types.
        self.assets_type_list = assets_type_list
        # The ID of the cluster for which you want to query alert events.
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
        # The page number of the results to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether the alert events to query have been handled. Valid values:
        self.dealed = dealed
        # The discovery source. This parameter is invalid.
        self.detect_source = detect_source
        # The subtypes of the alert events. Separate multiple subtypes with commas (,).
        self.event_names = event_names
        # The data source identifier of the alert event. The value is fixed as sas.
        self.from_ = from_
        # The group ID of the asset affected by the alert event.
        self.group_id = group_id
        # The unique ID that identifies the alert event record.
        self.id = id
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The severity levels of the security alerts that you want to query. Separate multiple severity levels with commas (,). The severity levels are listed in descending order. Valid values:
        # 
        # - **serious**: Critical.
        # - **suspicious**: Suspicious.
        # - **remind**: Informational.
        self.levels = levels
        # The multi-account query type. Default value: **0**. Valid values:
        # - **0**: Queries data of the current account.
        # - **1**: Queries data of all accounts.
        self.multi_account_action_type = multi_account_action_type
        # The name of the asset affected by the alert event.
        self.name = name
        # The collection of alert event handling result codes.
        self.operate_error_code_list = operate_error_code_list
        # The end timestamp of the handling time.
        self.operate_time_end = operate_time_end
        # The start timestamp of the handling time.
        self.operate_time_start = operate_time_start
        # The number of alert events to display on each page in a paged query. Default value: **20**. Maximum value: 100.
        self.page_size = page_size
        # The Alarm Metric of the alerting events to query. Valid values:
        self.parent_event_types = parent_event_types
        # The alert name or asset information to query.
        self.remark = remark
        # The China site (Chinese mainland) account ID of the member account in the resource directory.
        # >Call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The custom sort field. Default value: **operateTime**. Valid values:
        # 
        # - **lastTime**: the most recent occurrence time.
        # - **operateTime**: the processing time.
        # 
        # > This field takes effect only when **Dealed** is set to Y.
        self.sort_column = sort_column
        # The custom sort type. Default value: **desc**. Valid values:
        # 
        # - **asc**: ascending order.
        # - **desc**: descending order.
        # 
        # > This parameter takes effect only when **Dealed** is set to Y.
        self.sort_type = sort_type
        # The alert source.
        self.source = source
        # The list of Alibaba Cloud account IDs that generated the alerts.
        self.source_ali_uids = source_ali_uids
        # The IP address of the access source.
        self.source_ip = source_ip
        # The status of the alert events to query. Valid values:
        self.status = status
        # Specifies whether the alert is identified in strict mode.
        self.strict_mode = strict_mode
        # The list of operation types supported by the alert.
        self.support_operate_code_list = support_operate_code_list
        # The tactic ID in ATT&CK.
        self.tactic_id = tactic_id
        # The type of the container search target. Valid values:
        # 
        # - **containerId**: container ID.
        # - **uuid**: server UUID.
        # - **imageUuid**: image UUID.
        self.target_type = target_type
        # The end time of the latest occurrence time range.
        self.time_end = time_end
        # The start time of the latest occurrence time range.
        self.time_start = time_start
        # The unique key of the security alert.
        self.unique_info = unique_info
        # The UUIDs of the servers for which you want to query alerts. Separate multiple UUIDs with commas (,).
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

        if self.source_ali_uids is not None:
            result['SourceAliUids'] = self.source_ali_uids

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
            self.source_ali_uids = m.get('SourceAliUids')

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

