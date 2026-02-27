# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
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
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The information about the alert events.
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
        contain_hw_mode: bool = None,
        container_id: str = None,
        container_image_id: str = None,
        container_image_name: str = None,
        data_source: str = None,
        desc: str = None,
        details: List[main_models.DescribeSuspEventsResponseBodySuspEventsDetails] = None,
        detect_source: str = None,
        display_sandbox_result: bool = None,
        event_notes: List[main_models.DescribeSuspEventsResponseBodySuspEventsEventNotes] = None,
        event_status: int = None,
        event_sub_type: str = None,
        has_trace_info: bool = None,
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
        source_ali_uid: int = None,
        stages: str = None,
        support_operate_code: str = None,
        tactic_items: List[main_models.DescribeSuspEventsResponseBodySuspEventsTacticItems] = None,
        unique_info: str = None,
        uuid: str = None,
        cluster_id: str = None,
    ):
        # Indicates whether the alert event was analyzed offline.
        self.advanced = advanced
        # The name of the alert event.
        self.alarm_event_name = alarm_event_name
        # The name of the alert.
        self.alarm_event_name_display = alarm_event_name_display
        # The type of the alert event.
        self.alarm_event_type = alarm_event_type
        # The display name of the type of the alert event.
        self.alarm_event_type_display = alarm_event_type_display
        # The unique ID of the alert event.
        self.alarm_unique_info = alarm_unique_info
        # The name of the application to which the alert event belongs.
        self.app_name = app_name
        # Indicates whether automatic defense is enabled.
        self.auto_breaking = auto_breaking
        # Indicates whether you can handle the alert event online, such as quarantining the source file of the malicious process. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_be_deal_on_line = can_be_deal_on_line
        # Indicates whether you can cancel marking the alert event as a false positive. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_cancel_fault = can_cancel_fault
        # Indicates whether the safeguard mode for major activities is enabled for the server. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.contain_hw_mode = contain_hw_mode
        # The ID of the container.
        self.container_id = container_id
        # The ID of the container image.
        self.container_image_id = container_image_id
        # The name of the container image.
        self.container_image_name = container_image_name
        # The source of data. This parameter can be ignored.
        self.data_source = data_source
        # The impact of the alert event.
        self.desc = desc
        # The details of the alert event.
        self.details = details
        self.detect_source = detect_source
        # Indicates whether the alert event can be detected by cloud sandbox. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.display_sandbox_result = display_sandbox_result
        # The note information about the alert event.
        self.event_notes = event_notes
        # The status of the alert event. Valid values:
        # 
        # *   **1**: pending handling
        # *   **2**: ignored
        # *   **4**: confirmed
        # *   **8**: marked as a false positive
        # *   **16**: handling
        # *   **32**: handled
        # *   **64**: expired
        # *   **604**: marked as a false positive by the system
        self.event_status = event_status
        # The subtype of the alert event.
        self.event_sub_type = event_sub_type
        # Indicates whether the alert event has tracing information. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.has_trace_info = has_trace_info
        # The unique ID of the alert event.
        self.id = id
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The instance ID of the affected asset.
        self.instance_id = instance_id
        # The name of the associated instance.
        self.instance_name = instance_name
        # The public IP address of the associated instance.
        self.internet_ip = internet_ip
        # The private IP address of the associated instance.
        self.intranet_ip = intranet_ip
        # The ID of the Kubernetes cluster.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The name of the Kubernetes cluster.
        self.k_8s_cluster_name = k_8s_cluster_name
        # The namespace of the Kubernetes cluster.
        self.k_8s_namespace = k_8s_namespace
        # The ID of the Kubernetes node.
        self.k_8s_node_id = k_8s_node_id
        # The name of the Kubernetes node.
        self.k_8s_node_name = k_8s_node_name
        # The name of the Kubernetes pod.
        self.k_8s_pod_name = k_8s_pod_name
        # Indicates whether the large model analysis tag is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.large_model = large_model
        # The time when the alert event was last detected.
        self.last_time = last_time
        # The timestamp when the alert event was last detected. Unit: milliseconds.
        self.last_time_stamp = last_time_stamp
        # The severity of the alert event. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level
        # The status of the malicious behavior defense rule. Valid values:
        # 
        # *   **open**
        # *   **close**
        self.malicious_rule_status = malicious_rule_status
        # The tags of the alert events.
        self.mark_list = mark_list
        # The advanced whitelist rule.
        self.mark_mis_rules = mark_mis_rules
        # The complete name of the alert event.
        self.name = name
        # The time when the alert event was first detected.
        self.occurrence_time = occurrence_time
        # The timestamp when the alert event was first detected. Unit: milliseconds.
        self.occurrence_time_stamp = occurrence_time_stamp
        # The handling result code of the alert event.
        self.operate_error_code = operate_error_code
        # The handing result message of the alert event.
        self.operate_msg = operate_msg
        # The handling timestamp of the alert event. Unit: milliseconds.
        self.operate_time = operate_time
        # The edition of Security Center in which the alert event can be detected. Valid values:
        # 
        # *   **0**: Basic edition
        # *   **1**: Enterprise edition
        self.sale_version = sale_version
        # The ID of the associated alert event.
        self.security_event_ids = security_event_ids
        # The ID of the Alibaba Cloud account within which an alert is generated.
        self.source_ali_uid = source_ali_uid
        # The stage at which the attack is detected.
        self.stages = stages
        # Supported alarm operation types: 
        # - **AI.false_positive**: Suspected false positive 
        # - **AI.real_attack**: Real attack 
        # - **AI.Insufficient_information_to_evaluate**: Insufficient information to evaluate
        self.support_operate_code = support_operate_code
        # The display name of the attack stage.
        self.tactic_items = tactic_items
        # The unique key of the alert.
        self.unique_info = unique_info
        # The unique ID of the associated instance.
        self.uuid = uuid
        # The ID of the cluster.
        self.cluster_id = cluster_id

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

        if self.desc is not None:
            result['Desc'] = self.desc

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.detect_source is not None:
            result['DetectSource'] = self.detect_source

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

        if self.source_ali_uid is not None:
            result['SourceAliUid'] = self.source_ali_uid

        if self.stages is not None:
            result['Stages'] = self.stages

        if self.support_operate_code is not None:
            result['SupportOperateCode'] = self.support_operate_code

        result['TacticItems'] = []
        if self.tactic_items is not None:
            for k1 in self.tactic_items:
                result['TacticItems'].append(k1.to_map() if k1 else None)

        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

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

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeSuspEventsResponseBodySuspEventsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('DetectSource') is not None:
            self.detect_source = m.get('DetectSource')

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

        if m.get('SourceAliUid') is not None:
            self.source_ali_uid = m.get('SourceAliUid')

        if m.get('Stages') is not None:
            self.stages = m.get('Stages')

        if m.get('SupportOperateCode') is not None:
            self.support_operate_code = m.get('SupportOperateCode')

        self.tactic_items = []
        if m.get('TacticItems') is not None:
            for k1 in m.get('TacticItems'):
                temp_model = main_models.DescribeSuspEventsResponseBodySuspEventsTacticItems()
                self.tactic_items.append(temp_model.from_map(k1))

        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        return self

class DescribeSuspEventsResponseBodySuspEventsTacticItems(DaraModel):
    def __init__(
        self,
        tactic_display_name: str = None,
        tactic_id: str = None,
    ):
        # The tactic name of ATT\\&CK.
        self.tactic_display_name = tactic_display_name
        # The stage information about ATT\\&CK.
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
        # The note.
        self.note = note
        # The ID of the note.
        self.note_id = note_id
        # The time when the note was created.
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
        # The display name of the alert event.
        self.name_display = name_display
        # The type of the alert event.
        self.type = type
        # The path of the alert event.
        self.value = value
        # The display name of the path of the alert event.
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

