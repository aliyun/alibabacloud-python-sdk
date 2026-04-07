# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListAlertMessagesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListAlertMessagesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about returned alerts.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListAlertMessagesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAlertMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_messages: List[main_models.ListAlertMessagesResponseBodyDataAlertMessages] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The alerts.
        self.alert_messages = alert_messages
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of alerts returned.
        self.total_count = total_count

    def validate(self):
        if self.alert_messages:
            for v1 in self.alert_messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertMessages'] = []
        if self.alert_messages is not None:
            for k1 in self.alert_messages:
                result['AlertMessages'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_messages = []
        if m.get('AlertMessages') is not None:
            for k1 in m.get('AlertMessages'):
                temp_model = main_models.ListAlertMessagesResponseBodyDataAlertMessages()
                self.alert_messages.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlertMessagesResponseBodyDataAlertMessages(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_message_status: str = None,
        alert_method: str = None,
        alert_time: int = None,
        alert_user: str = None,
        content: str = None,
        instances: List[main_models.ListAlertMessagesResponseBodyDataAlertMessagesInstances] = None,
        nodes: List[main_models.ListAlertMessagesResponseBodyDataAlertMessagesNodes] = None,
        remind_id: int = None,
        remind_name: str = None,
        sla_alert: main_models.ListAlertMessagesResponseBodyDataAlertMessagesSlaAlert = None,
        source: str = None,
        topics: List[main_models.ListAlertMessagesResponseBodyDataAlertMessagesTopics] = None,
    ):
        # The alert ID.
        self.alert_id = alert_id
        # The sending status of the notification. Valid values: READY_TO_SEND, SEND_FAIL, SEND_SUCCESS, and SEND_OVERLIMIT. The value READY_TO_SEND indicates that the notification is waiting to be sent. The value SEND_FAIL indicates that the notification fails to be sent. The value SEND_SUCCESS indicates that the notification is sent. The value SEND_OVERLIMIT indicates that the number of notifications that are sent exceeds the upper limit.
        self.alert_message_status = alert_message_status
        # The notification method. Valid values: MAIL, SMS, and PHONE. Only DataWorks Professional Edition and more advanced editions support the PHONE notification method.
        self.alert_method = alert_method
        # The timestamp when the alert was reported.
        self.alert_time = alert_time
        # The ID of the Alibaba Cloud used by the alert recipient.
        self.alert_user = alert_user
        # The content of the alert.
        self.content = content
        # The instances that triggered the custom alert rule. This parameter is returned if the value of the Source parameter is REMIND_ALERT. This parameter is left empty if the value of the Source parameter is not REMIND_ALERT.
        self.instances = instances
        # The nodes returned for different alert sources.
        # 
        # *   The nodes that form a loop are returned if the value of the Source parameter is NODE_CYCLE_ALERT.
        # *   The nodes that are isolated are returned if the value of the Source parameter is NODE_LONELY_ALERT.
        self.nodes = nodes
        # The ID of the custom alert rule that was triggered. This parameter is returned if the value of the Source parameter is REMIND_ALERT.
        self.remind_id = remind_id
        # The name of the custom alert rule that was triggered. This parameter is returned if the value of the Source parameter is REMIND_ALERT.
        self.remind_name = remind_name
        # The basic information about the baseline instance that triggered an alert. This parameter is returned if the value of the Source parameter is SLA_ALERT. This parameter is left empty if the value of the Source parameter is not SLA_ALERT.
        self.sla_alert = sla_alert
        # The type of the alert. Valid values: REMIND_ALERT, TOPIC_ALERT, SLA_ALERT, NODE_CYCLE_ALERT, and NODE_LONELY_ALERT. The value REMIND_ALERT indicates that the alert is a custom alert. The value TOPIC_ALERT indicates that the alert is an event alert. The value SLA_ALERT indicates that the alert is a baseline alert. The value NODE_CYCLE_ALERT indicates that the alert is reported for a node dependency loop. The value NODE_LONELY_ALERT indicates that the alert is reported for isolated nodes.
        self.source = source
        # The events that triggered alerts. This parameter is returned if the value of the Source parameter is TOPIC_ALERT. This parameter is left empty if the value of the Source parameter is not TOPIC_ALERT.
        self.topics = topics

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.sla_alert:
            self.sla_alert.validate()
        if self.topics:
            for v1 in self.topics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_message_status is not None:
            result['AlertMessageStatus'] = self.alert_message_status

        if self.alert_method is not None:
            result['AlertMethod'] = self.alert_method

        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.alert_user is not None:
            result['AlertUser'] = self.alert_user

        if self.content is not None:
            result['Content'] = self.content

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        if self.remind_name is not None:
            result['RemindName'] = self.remind_name

        if self.sla_alert is not None:
            result['SlaAlert'] = self.sla_alert.to_map()

        if self.source is not None:
            result['Source'] = self.source

        result['Topics'] = []
        if self.topics is not None:
            for k1 in self.topics:
                result['Topics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertMessageStatus') is not None:
            self.alert_message_status = m.get('AlertMessageStatus')

        if m.get('AlertMethod') is not None:
            self.alert_method = m.get('AlertMethod')

        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('AlertUser') is not None:
            self.alert_user = m.get('AlertUser')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListAlertMessagesResponseBodyDataAlertMessagesInstances()
                self.instances.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListAlertMessagesResponseBodyDataAlertMessagesNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        if m.get('RemindName') is not None:
            self.remind_name = m.get('RemindName')

        if m.get('SlaAlert') is not None:
            temp_model = main_models.ListAlertMessagesResponseBodyDataAlertMessagesSlaAlert()
            self.sla_alert = temp_model.from_map(m.get('SlaAlert'))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        self.topics = []
        if m.get('Topics') is not None:
            for k1 in m.get('Topics'):
                temp_model = main_models.ListAlertMessagesResponseBodyDataAlertMessagesTopics()
                self.topics.append(temp_model.from_map(k1))

        return self

class ListAlertMessagesResponseBodyDataAlertMessagesTopics(DaraModel):
    def __init__(
        self,
        instance_id: int = None,
        node_id: int = None,
        topic_id: int = None,
        topic_name: str = None,
        topic_owner: str = None,
        topic_status: str = None,
    ):
        # The ID of the instance that triggered the event.
        self.instance_id = instance_id
        # The ID of the node that triggered the event.
        self.node_id = node_id
        # The event ID.
        self.topic_id = topic_id
        # The name of the event.
        self.topic_name = topic_name
        # The ID of the Alibaba Cloud account used by the event owner.
        self.topic_owner = topic_owner
        # The status of the event. Valid values: IGNORE, NEW, FIXING, and RECOVER. The value IGNORE indicates that the event is ignored. The value NEW indicates that the event is a new event. The value FIXING indicates that the event is being handled. The value RECOVER indicates that the event is handled.
        self.topic_status = topic_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner

        if self.topic_status is not None:
            result['TopicStatus'] = self.topic_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')

        if m.get('TopicStatus') is not None:
            self.topic_status = m.get('TopicStatus')

        return self

class ListAlertMessagesResponseBodyDataAlertMessagesSlaAlert(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_owner: str = None,
        bizdate: int = None,
        in_group_id: int = None,
        project_id: int = None,
        status: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The ID of the Alibaba Cloud account used by the baseline owner. Multiple IDs are separated by commas (,).
        self.baseline_owner = baseline_owner
        # The data timestamp of the baseline instance.
        self.bizdate = bizdate
        # The ID of the cycle of the baseline instance. Valid values of the ID of an hour-level cycle: [1,24]. The ID of a day-level cycle is 1.
        self.in_group_id = in_group_id
        # The ID of the workspace to which the baseline belongs.
        self.project_id = project_id
        # The status of the baseline. Valid values: ERROR, SAFE, DANGEROUS, and OVER. The value ERROR indicates that no nodes are associated with the baseline, or all nodes associated with the baseline are suspended. The value SAFE indicates that nodes are run before the alert duration begins. The value DANGEROUS indicates that nodes are still running after the alert duration ends but the committed completion time does not arrive. The value OVER indicates that nodes are still running after the committed completion time.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_owner is not None:
            result['BaselineOwner'] = self.baseline_owner

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.in_group_id is not None:
            result['InGroupId'] = self.in_group_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineOwner') is not None:
            self.baseline_owner = m.get('BaselineOwner')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('InGroupId') is not None:
            self.in_group_id = m.get('InGroupId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListAlertMessagesResponseBodyDataAlertMessagesNodes(DaraModel):
    def __init__(
        self,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        project_id: int = None,
    ):
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account used by the node owner.
        self.owner = owner
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ListAlertMessagesResponseBodyDataAlertMessagesInstances(DaraModel):
    def __init__(
        self,
        instance_id: int = None,
        node_id: int = None,
        node_name: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The status of the instance. Valid values: NOT_RUN, WAIT_TIME, WAIT_RESOURCE, RUNNING, CHECKING, CHECKING_CONDITION, FAILURE, and SUCCESS. The value NOT_RUN indicates that the instance is not run. The value WAIT_TIME indicates that the instance is waiting to be run. The value WAIT_RESOURCE indicates that the instance is waiting for resources. The value RUNNING indicates that the instance is running. The value CHECKING indicates that data quality is being checked for the node for which the instance is generated. The value CHECKING_CONDITION indicates that branch conditions are being checked for the node for which the instance is generated. The value FAILURE indicates that the instance fails to run. The value SUCCESS indicates that the instance is successfully run.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

