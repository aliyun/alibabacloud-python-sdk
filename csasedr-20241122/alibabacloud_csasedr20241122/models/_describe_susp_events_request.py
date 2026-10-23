# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSuspEventsRequest(DaraModel):
    def __init__(
        self,
        alarm_event_name: str = None,
        alarm_unique_info: str = None,
        assets_type_list: List[str] = None,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: int = None,
        dealed: str = None,
        department: str = None,
        event_names: str = None,
        group_id: int = None,
        host_name: str = None,
        id: int = None,
        inner_ip: str = None,
        lang: str = None,
        levels: str = None,
        name: str = None,
        operate_error_code_list: List[str] = None,
        operate_time_end: str = None,
        operate_time_start: str = None,
        page_size: int = None,
        parent_event_types: str = None,
        remark: str = None,
        sort_column: str = None,
        sort_type: str = None,
        source: str = None,
        source_ip: str = None,
        src_ip: str = None,
        status: str = None,
        strict_mode: str = None,
        tactic_id: str = None,
        target_type: str = None,
        time_end: str = None,
        time_start: str = None,
        unique_info: str = None,
        user_name: str = None,
        uuids: str = None,
    ):
        # The name of the alert event.
        self.alarm_event_name = alarm_event_name
        # The unique ID of the alert event.
        # 
        # To query the exception event information of a single alert event, you must provide the unique ID of the alert event. You can call the DescribeSuspEvents operation to obtain the ID.
        self.alarm_unique_info = alarm_unique_info
        # The collection of asset types. Not supported by SASE-EDR.
        self.assets_type_list = assets_type_list
        # The ID of the cluster for which you want to query alert events.
        self.cluster_id = cluster_id
        # The container search field. Not supported by SASE-EDR.
        self.container_field_name = container_field_name
        # The value of the container search field. Not supported by SASE-EDR.
        self.container_field_value = container_field_value
        # The page number of the returned page. Default value: 1.
        self.current_page = current_page
        # Filters alerts by processing group. Valid values:
        # 
        # - `N`: Pending.
        # - `Y`: Processed.
        # - `A`: All.
        # 
        # If this parameter is not specified, all groups are queried. The Status parameter further filters alerts within the selected group. If the specified status does not match the group, an empty result is returned.
        self.dealed = dealed
        # The department to which the user belongs.
        self.department = department
        # The internal subtype identifiers of the alerts. Separate multiple subtypes with commas (,). This parameter is used to match event names. The valid values must belong to the alert configurations visible to the current account and are not the alert names displayed to users.
        self.event_names = event_names
        # The ID of the group to which the asset affected by the alert event belongs.
        self.group_id = group_id
        # The name of the endpoint device.
        self.host_name = host_name
        # The unique ID of the recorded alert event.
        self.id = id
        # The private IP address of the endpoint device.
        self.inner_ip = inner_ip
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The urgency levels of the alert events to query. Separate multiple urgency levels with commas (,). The urgency levels are listed in descending order. Valid values:
        # - **serious**: Urgent.
        # - **suspicious**: Suspicious.
        # - **remind**: Reminder.
        self.levels = levels
        # The name of the asset affected by the alert event.
        self.name = name
        # The collection of alert event processing result codes.
        self.operate_error_code_list = operate_error_code_list
        # The end time of the alert processing time. Specify a datetime string in the YYYY-MM-DD HH:mm:ss format.
        self.operate_time_end = operate_time_end
        # The start time of the alert processing time. Specify a datetime string in the YYYY-MM-DD HH:mm:ss format.
        self.operate_time_start = operate_time_start
        # The number of alert events to return on each page in a paging query. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The internal type identifiers of the alerts. Separate multiple types with commas (,). The valid values are derived from the current alert configurations. You can call the DescribeNsasSuspEventType operation to query the Type field in EventTypes. The Name field is the display name and is not used as a fixed enumeration list.
        self.parent_event_types = parent_event_types
        # The alert name or asset information to query.
        # 
        # Note: Fuzzy match is supported. Asset information includes the asset name, public IP address, and private IP address.
        self.remark = remark
        # The custom sort field. Default value: **operateTime**. Valid values:
        # 
        # - **lastTime**: Latest occurrence time.
        # - **operateTime**: Processing time.
        # 
        # > This field takes effect only when Dealed is set to Y.
        self.sort_column = sort_column
        # The custom sort order. Default value: **desc**. Valid values:
        # 
        # - **asc**: Ascending order.
        # - **desc**: Descending order.
        # 
        # > This field takes effect only when Dealed is set to Y.
        self.sort_type = sort_type
        # The compatibility source classification parameter. This parameter is not used to specify the alert data source. You do not need to specify this parameter for common alert list queries.
        self.source = source
        # The IP address of the access source.
        self.source_ip = source_ip
        # The IP address of the endpoint.
        self.src_ip = src_ip
        # Further filters alerts by individual alert status within the processing group specified by the Dealed parameter. Status descriptions:
        # 
        # - `0`: No further status restriction. The alerts are still subject to the Dealed group.
        # - `1`: Pending.
        # - `2`: Ignored.
        # - `4`: Manually processed.
        # - `8`: Whitelisted (marked as false positive).
        # - `32`: Processed. For example, automatic defense interception succeeded.
        # - `64`: Expired.
        # 
        # Unprocessed alerts are automatically marked as expired if more than 31 days have passed since the last occurrence.
        # 
        # Deleted alerts cannot be queried. If the specified status does not belong to the group specified by Dealed, an empty result is returned.
        self.status = status
        # Specifies whether the alert is in strict mode. Not supported by SASE-EDR.
        self.strict_mode = strict_mode
        # The ATT&CK tactic ID.
        self.tactic_id = tactic_id
        # The container search target type. Not supported by SASE-EDR.
        self.target_type = target_type
        # The end time of the latest occurrence. Specify a datetime string in the YYYY-MM-DD HH:mm:ss format.
        self.time_end = time_end
        # The start time of the latest occurrence. Specify a datetime string in the YYYY-MM-DD HH:mm:ss format.
        self.time_start = time_start
        # The unique key of the security alert.
        self.unique_info = unique_info
        # The username of the endpoint.
        self.user_name = user_name
        # The UUIDs of the servers for which you want to query alerts. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name

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

        if self.department is not None:
            result['Department'] = self.department

        if self.event_names is not None:
            result['EventNames'] = self.event_names

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.id is not None:
            result['Id'] = self.id

        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.levels is not None:
            result['Levels'] = self.levels

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

        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

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

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')

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

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('EventNames') is not None:
            self.event_names = m.get('EventNames')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

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

        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

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

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

