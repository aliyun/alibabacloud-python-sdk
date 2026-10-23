# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csasedr20241122 import models as main_models
from darabonba.model import DaraModel

class DescribeSuspEventsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        susp_events: List[main_models.DescribeSuspEventsResponseBodySuspEvents] = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page in a paging query.
        self.count = count
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # The maximum number of entries that can be displayed on each page in a paging query.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The list of endpoint security alert events returned on the current page.
        self.susp_events = susp_events
        # The total number of alert events.
        self.total_count = total_count

    def validate(self):
        if self.susp_events:
            for v1 in self.susp_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k1 in self.susp_events:
                result['SuspEvents'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k1 in m.get('SuspEvents'):
                temp_model = main_models.DescribeSuspEventsResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSuspEventsResponseBodySuspEvents(DaraModel):
    def __init__(
        self,
        advanced: bool = None,
        alarm_event_name: str = None,
        alarm_event_name_display: str = None,
        alarm_event_type: str = None,
        alarm_event_type_display: str = None,
        alarm_unique_info: str = None,
        app_name: str = None,
        auto_breaking: bool = None,
        can_be_deal_on_line: bool = None,
        can_cancel_fault: bool = None,
        cluster_id: str = None,
        contain_hw_mode: bool = None,
        container_id: str = None,
        container_image_id: str = None,
        container_image_name: str = None,
        data_source: str = None,
        department: str = None,
        desc: str = None,
        details: List[main_models.DescribeSuspEventsResponseBodySuspEventsDetails] = None,
        dev_tag: str = None,
        dev_type: str = None,
        display_sandbox_result: bool = None,
        event_notes: List[main_models.DescribeSuspEventsResponseBodySuspEventsEventNotes] = None,
        event_status: int = None,
        event_sub_type: str = None,
        has_trace_info: bool = None,
        host_name: str = None,
        id: int = None,
        image_uuid: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        k_8s_cluster_id: str = None,
        k_8s_cluster_name: str = None,
        k_8s_namespace: str = None,
        k_8s_node_id: str = None,
        k_8s_node_name: str = None,
        k_8s_pod_name: str = None,
        large_model: bool = None,
        last_time: str = None,
        last_time_stamp: int = None,
        level: str = None,
        mac: str = None,
        malicious_rule_status: str = None,
        mark_list: List[str] = None,
        mark_mis_rules: str = None,
        name: str = None,
        occurrence_time: str = None,
        occurrence_time_stamp: int = None,
        operate_error_code: str = None,
        operate_msg: str = None,
        operate_time: int = None,
        sale_version: str = None,
        security_event_ids: str = None,
        src_ip: str = None,
        stages: str = None,
        tactic_items: List[main_models.DescribeSuspEventsResponseBodySuspEventsTacticItems] = None,
        unique_info: str = None,
        user_name: str = None,
        uuid: str = None,
    ):
        # Indicates whether the alert is generated by offline analysis.
        self.advanced = advanced
        # The internal name or rule name of the alert event. For the user-facing alert name, see AlarmEventNameDisplay.
        self.alarm_event_name = alarm_event_name
        # The user-facing name of the alert event.
        self.alarm_event_name_display = alarm_event_name_display
        # The type of the alert event.
        self.alarm_event_type = alarm_event_type
        # The user-facing name of the alert type.
        self.alarm_event_type_display = alarm_event_type_display
        # The unique ID of the alert event.
        self.alarm_unique_info = alarm_unique_info
        # The name of the application to which the alert event belongs.
        self.app_name = app_name
        # The completion status of automatic blocking. Returns true when the alert status is AUTO_DEALING_DONE (513), and returns false for other statuses. This field cannot be used to determine whether automatic defense has occurred. Even if OperateErrorCode is auto_defense.Success, this field may return false.
        self.auto_breaking = auto_breaking
        # Indicates whether the legacy online scan and kill capability is supported. This operation returns false. This field is not a list of executable operations for the alert. A value of false does not mean that the alert cannot be ignored, added to the whitelist, or marked as manually handled. To query executable operations, call DescribeSecurityEventOperations.
        self.can_be_deal_on_line = can_be_deal_on_line
        # Indicates whether the alert is in a state where the false positive mark can be canceled. Returns true when the alert status is FAULT (8), and returns false for other statuses. This status indicator does not replace full capability checks such as feature switches and operation configurations. To query the actual executable operations for canceling the whitelist, call DescribeSecurityEventOperations.
        self.can_cancel_fault = can_cancel_fault
        # The ID of the container cluster. Not supported by SASE-EDR.
        self.cluster_id = cluster_id
        # Indicates whether the enhanced protection mode is enabled for the server. Not supported by SASE-EDR.
        self.contain_hw_mode = contain_hw_mode
        # The ID of the container. Not supported by SASE-EDR.
        self.container_id = container_id
        # The ID of the container image. Not supported by SASE-EDR.
        self.container_image_id = container_image_id
        # The name of the container image. Not supported by SASE-EDR.
        self.container_image_name = container_image_name
        # The identifier of the alert data source. The return example for endpoint alerts is `aegis_suspicious_event_pc`.
        self.data_source = data_source
        # The name of the department.
        self.department = department
        # The summary of the alert event, which describes the detected or blocked behavior.
        self.desc = desc
        # The list of alert detail items, which may include prompts, attack phases, malicious behaviors, process paths, command lines, handling suggestions, and parent process relationships. The detail items and their quantities may vary for different alerts.
        self.details = details
        # **[Deprecated]** This field is deprecated.
        self.dev_tag = dev_tag
        # **[Deprecated]** This field is deprecated.
        self.dev_type = dev_type
        # Indicates whether cloud sandbox detection is supported. Not supported by SASE-EDR.
        self.display_sandbox_result = display_sandbox_result
        # The list of notes for the alert event. An empty array `[]` is returned if there are no notes.
        self.event_notes = event_notes
        # The handling status of the endpoint alert. Valid values:
        # 
        # - `1`: Pending.
        # - `2`: Ignored.
        # - `4`: Manually handled.
        # - `8`: Whitelisted (marked as a false positive).
        # - `32`: Handled, such as successful blocking by automatic defense.
        # - `64`: Expired.
        # 
        # The system may change the status of an unhandled alert to Expired if more than 31 days have passed since its last occurrence.
        # 
        # The actual statuses that appear depend on the alert template and the actual handling results.
        self.event_status = event_status
        # The subtype identifier of the alert event. The value of this field may be the same as AlarmEventName.
        self.event_sub_type = event_sub_type
        # Indicates whether the alert event has tracing information. Not supported by SASE-EDR.
        self.has_trace_info = has_trace_info
        # The name of the device.
        self.host_name = host_name
        # The numeric ID of the alert event.
        self.id = id
        # The UUID of the image. Not supported by SASE-EDR.
        self.image_uuid = image_uuid
        # The instance identifier of the endpoint or asset affected by the alert event.
        self.instance_id = instance_id
        # The instance name of the endpoint or asset affected by the alert event.
        self.instance_name = instance_name
        # The public IP address of the associated instance.
        self.internet_ip = internet_ip
        # The private IP address of the endpoint or asset affected by the alert event.
        self.intranet_ip = intranet_ip
        # The ID of the K8s cluster. Not supported by SASE-EDR.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The name of the K8s cluster. Not supported by SASE-EDR.
        self.k_8s_cluster_name = k_8s_cluster_name
        # The K8s namespace. Not supported by SASE-EDR.
        self.k_8s_namespace = k_8s_namespace
        # The ID of the K8s node. Not supported by SASE-EDR.
        self.k_8s_node_id = k_8s_node_id
        # The name of the K8s node. Not supported by SASE-EDR.
        self.k_8s_node_name = k_8s_node_name
        # The name of the K8s pod. Not supported by SASE-EDR.
        self.k_8s_pod_name = k_8s_pod_name
        # Indicates whether large model analysis tags are supported. Valid values:
        # 
        # - **true**: Supported.
        # - **false**: Not supported.
        self.large_model = large_model
        # The last time the alert event occurred. The format is YYYY-MM-DD HH:mm:ss.
        self.last_time = last_time
        # The timestamp of the last occurrence, in milliseconds.
        self.last_time_stamp = last_time_stamp
        # The risk level of the alert event. Valid values:
        # - **serious**: Urgent.
        # - **suspicious**: Suspicious.
        # - **remind**: Reminder.
        self.level = level
        # **[Deprecated]** This field is deprecated.
        self.mac = mac
        # The status of the malicious behavior defense rule. Valid values:
        # - **open**: Enabled.
        # - **close**: Disabled.
        self.malicious_rule_status = malicious_rule_status
        # The collection of tags for the alert event.
        self.mark_list = mark_list
        # The advanced whitelist rules.
        self.mark_mis_rules = mark_mis_rules
        # The full name of the alert event, such as Precise defense - untrusted process startup.
        self.name = name
        # The time when the alert event first occurred. The format is YYYY-MM-DD HH:mm:ss.
        self.occurrence_time = occurrence_time
        # The timestamp of the first occurrence, in milliseconds.
        self.occurrence_time_stamp = occurrence_time_stamp
        # The result code of the alert handling operation, in the format of Operation type.Result code. For example, `auto_defense.Success` indicates that automatic defense is successful. This field also returns success results and does not only indicate errors.
        self.operate_error_code = operate_error_code
        # The note for the alert event operation.
        self.operate_msg = operate_msg
        # The timestamp of the alert event operation, in milliseconds.
        self.operate_time = operate_time
        # The product edition supported for alert event detection. SASE-EDR is not supported.
        self.sale_version = sale_version
        # The IDs of the associated alert events, returned as strings.
        self.security_event_ids = security_event_ids
        # The source IP address.
        self.src_ip = src_ip
        # The list of ATT&CK attack stage names, returned as a serialized JSON array string. For example, if the field value is `["Execution"]`, parsing it yields a string array.
        self.stages = stages
        # The list of ATT&CK attack stage details. Each item contains the stage ID and display name.
        self.tactic_items = tactic_items
        # The unique key of the security alert.
        self.unique_info = unique_info
        # The username of the endpoint.
        self.user_name = user_name
        # The unique identifier of the endpoint or asset affected by the alert event. For endpoint alerts, the identifier may start with `inet-pc-`.
        self.uuid = uuid

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()
        if self.event_notes:
            for v1 in self.event_notes:
                 if v1:
                    v1.validate()
        if self.tactic_items:
            for v1 in self.tactic_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced is not None:
            result['Advanced'] = self.advanced

        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name

        if self.alarm_event_name_display is not None:
            result['AlarmEventNameDisplay'] = self.alarm_event_name_display

        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type

        if self.alarm_event_type_display is not None:
            result['AlarmEventTypeDisplay'] = self.alarm_event_type_display

        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auto_breaking is not None:
            result['AutoBreaking'] = self.auto_breaking

        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line

        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_image_id is not None:
            result['ContainerImageId'] = self.container_image_id

        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.department is not None:
            result['Department'] = self.department

        if self.desc is not None:
            result['Desc'] = self.desc

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.display_sandbox_result is not None:
            result['DisplaySandboxResult'] = self.display_sandbox_result

        result['EventNotes'] = []
        if self.event_notes is not None:
            for k1 in self.event_notes:
                result['EventNotes'].append(k1.to_map() if k1 else None)

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_sub_type is not None:
            result['EventSubType'] = self.event_sub_type

        if self.has_trace_info is not None:
            result['HasTraceInfo'] = self.has_trace_info

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.id is not None:
            result['Id'] = self.id

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id

        if self.k_8s_cluster_name is not None:
            result['K8sClusterName'] = self.k_8s_cluster_name

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.k_8s_node_id is not None:
            result['K8sNodeId'] = self.k_8s_node_id

        if self.k_8s_node_name is not None:
            result['K8sNodeName'] = self.k_8s_node_name

        if self.k_8s_pod_name is not None:
            result['K8sPodName'] = self.k_8s_pod_name

        if self.large_model is not None:
            result['LargeModel'] = self.large_model

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp

        if self.level is not None:
            result['Level'] = self.level

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.malicious_rule_status is not None:
            result['MaliciousRuleStatus'] = self.malicious_rule_status

        if self.mark_list is not None:
            result['MarkList'] = self.mark_list

        if self.mark_mis_rules is not None:
            result['MarkMisRules'] = self.mark_mis_rules

        if self.name is not None:
            result['Name'] = self.name

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.occurrence_time_stamp is not None:
            result['OccurrenceTimeStamp'] = self.occurrence_time_stamp

        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code

        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.sale_version is not None:
            result['SaleVersion'] = self.sale_version

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.stages is not None:
            result['Stages'] = self.stages

        result['TacticItems'] = []
        if self.tactic_items is not None:
            for k1 in self.tactic_items:
                result['TacticItems'].append(k1.to_map() if k1 else None)

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advanced') is not None:
            self.advanced = m.get('Advanced')

        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')

        if m.get('AlarmEventNameDisplay') is not None:
            self.alarm_event_name_display = m.get('AlarmEventNameDisplay')

        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')

        if m.get('AlarmEventTypeDisplay') is not None:
            self.alarm_event_type_display = m.get('AlarmEventTypeDisplay')

        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AutoBreaking') is not None:
            self.auto_breaking = m.get('AutoBreaking')

        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')

        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerImageId') is not None:
            self.container_image_id = m.get('ContainerImageId')

        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeSuspEventsResponseBodySuspEventsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('DisplaySandboxResult') is not None:
            self.display_sandbox_result = m.get('DisplaySandboxResult')

        self.event_notes = []
        if m.get('EventNotes') is not None:
            for k1 in m.get('EventNotes'):
                temp_model = main_models.DescribeSuspEventsResponseBodySuspEventsEventNotes()
                self.event_notes.append(temp_model.from_map(k1))

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventSubType') is not None:
            self.event_sub_type = m.get('EventSubType')

        if m.get('HasTraceInfo') is not None:
            self.has_trace_info = m.get('HasTraceInfo')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')

        if m.get('K8sClusterName') is not None:
            self.k_8s_cluster_name = m.get('K8sClusterName')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('K8sNodeId') is not None:
            self.k_8s_node_id = m.get('K8sNodeId')

        if m.get('K8sNodeName') is not None:
            self.k_8s_node_name = m.get('K8sNodeName')

        if m.get('K8sPodName') is not None:
            self.k_8s_pod_name = m.get('K8sPodName')

        if m.get('LargeModel') is not None:
            self.large_model = m.get('LargeModel')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('MaliciousRuleStatus') is not None:
            self.malicious_rule_status = m.get('MaliciousRuleStatus')

        if m.get('MarkList') is not None:
            self.mark_list = m.get('MarkList')

        if m.get('MarkMisRules') is not None:
            self.mark_mis_rules = m.get('MarkMisRules')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('OccurrenceTimeStamp') is not None:
            self.occurrence_time_stamp = m.get('OccurrenceTimeStamp')

        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')

        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('SaleVersion') is not None:
            self.sale_version = m.get('SaleVersion')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('Stages') is not None:
            self.stages = m.get('Stages')

        self.tactic_items = []
        if m.get('TacticItems') is not None:
            for k1 in m.get('TacticItems'):
                temp_model = main_models.DescribeSuspEventsResponseBodySuspEventsTacticItems()
                self.tactic_items.append(temp_model.from_map(k1))

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeSuspEventsResponseBodySuspEventsTacticItems(DaraModel):
    def __init__(
        self,
        tactic_display_name: str = None,
        tactic_id: str = None,
    ):
        # The display name of the ATT&CK tactic (attack stage).
        self.tactic_display_name = tactic_display_name
        # The ID of the ATT&CK tactic (attack stage). For example, `TA0002` corresponds to Execution.
        self.tactic_id = tactic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tactic_display_name is not None:
            result['TacticDisplayName'] = self.tactic_display_name

        if self.tactic_id is not None:
            result['TacticId'] = self.tactic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TacticDisplayName') is not None:
            self.tactic_display_name = m.get('TacticDisplayName')

        if m.get('TacticId') is not None:
            self.tactic_id = m.get('TacticId')

        return self

class DescribeSuspEventsResponseBodySuspEventsEventNotes(DaraModel):
    def __init__(
        self,
        note: str = None,
        note_id: int = None,
        note_time: str = None,
    ):
        # The note content.
        self.note = note
        # The ID of the event record.
        self.note_id = note_id
        # The time when the event was recorded. The format is YYYY-MM-DD HH:mm:ss.
        self.note_time = note_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.note is not None:
            result['Note'] = self.note

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.note_time is not None:
            result['NoteTime'] = self.note_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('NoteTime') is not None:
            self.note_time = m.get('NoteTime')

        return self

class DescribeSuspEventsResponseBodySuspEventsDetails(DaraModel):
    def __init__(
        self,
        name_display: str = None,
        type: str = None,
        value: str = None,
        value_display: str = None,
    ):
        # The display text of the detail item name, such as ATT&CK attack phase, Process path, or Handling suggestion.
        self.name_display = name_display
        # The data display type of the detail item. Valid values:
        # 
        # - `text`: Text.
        # - `processChain`: Process chain (parent process relationship).
        self.type = type
        # The raw value of the detail item. The meaning is determined by Name and Type. For example, the value is the phase name for an attack phase item, and the path for a process path item. When Type is `processChain`, the value is a process chain data string.
        self.value = value
        # The display value of the detail item, which may be the same as Value. The specific meaning depends on the detail item and is not strictly fixed as a file path.
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')

        return self

