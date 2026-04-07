# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetRemindResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRemindResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the custom alert rule.
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
            temp_model = main_models.GetRemindResponseBodyData()
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

class GetRemindResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_interval: int = None,
        alert_methods: List[str] = None,
        alert_targets: List[str] = None,
        alert_unit: str = None,
        allow_nodes: List[int] = None,
        baselines: List[main_models.GetRemindResponseBodyDataBaselines] = None,
        biz_processes: List[main_models.GetRemindResponseBodyDataBizProcesses] = None,
        detail: str = None,
        dnd_end: str = None,
        dnd_start: str = None,
        founder: str = None,
        max_alert_times: int = None,
        nodes: List[main_models.GetRemindResponseBodyDataNodes] = None,
        projects: List[main_models.GetRemindResponseBodyDataProjects] = None,
        receivers: List[main_models.GetRemindResponseBodyDataReceivers] = None,
        remind_id: int = None,
        remind_name: str = None,
        remind_type: str = None,
        remind_unit: str = None,
        robots: List[main_models.GetRemindResponseBodyDataRobots] = None,
        useflag: bool = None,
        webhooks: List[str] = None,
    ):
        # The minimum interval at which alerts are reported. Unit: seconds.
        self.alert_interval = alert_interval
        # The notification method.
        self.alert_methods = alert_methods
        # The description of the alert recipient. For more information about alert recipients, see the Receivers parameter.
        self.alert_targets = alert_targets
        # The type of the alert recipient. For more information about alert recipient types, see the Receivers parameter. Valid values:
        # 
        # *   OWNER: the task owner
        # *   OTHER: specified personnel
        # *   SHIFT_SCHEDULE: personnel in a shift schedule
        self.alert_unit = alert_unit
        # The IDs of the nodes that are added to a whitelist.
        self.allow_nodes = allow_nodes
        # The baselines to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is BASELINE.
        self.baselines = baselines
        # The workflows to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is BIZPROCESS.
        self.biz_processes = biz_processes
        # *   If the value of the RemindType parameter is FINISHED, this parameter is left empty.
        # *   If the value of the RemindType parameter is UNFINISHED, the trigger conditions are returned as key-value pairs. Example: {"hour":23,"minu":59}. Valid values of hour: [0,47]. Valid values of minu: [0,59].
        # *   If the value of the RemindType parameter is ERROR, this parameter is left empty.
        # *   If the value of the RemindType parameter is CYCLE_UNFINISHED, the trigger conditions are returned as key-value pairs. Example: {"1":"05:50","2":"06:50","3":"07:50","4":"08:50","5":"09:50","6":"10:50","7":"11:50","8":"12:50","9":"13:50","10":"14:50","11":"15:50","12":"16:50","13":"17:50","14":"18:50","15":"19:50","16":"20:50","17":"21:50","18":"22:50","19":"23:50","20":"24:50","21":"25:50"}. The key indicates the ID of the cycle. Valid values: [1,288]. The value indicates the timeout period of the node that is running in the cycle. Specify the value in the hh:mm format. Valid values of hh: [0,47]. Valid values of mm: [0,59].
        # *   If the value of the RemindType parameter is TIMEOUT, the timeout period is returned. Unit: seconds. Example: 1800. This value indicates that an alert is reported if the node has run for more than 30 minutes.
        self.detail = detail
        # The end time of the quiet hours. The value is in the hh:mm format. Valid values of hh: [0,23]. Valid values of mm: [0,59].
        self.dnd_end = dnd_end
        # The start time of the quiet hours. The value is in the hh:mm format. Valid values of hh: [0,23]. Valid values of mm: [0,59].
        self.dnd_start = dnd_start
        # The ID of the Alibaba Cloud account used by the creator of the custom alert rule.
        self.founder = founder
        # The maximum number of alerts.
        self.max_alert_times = max_alert_times
        # The nodes to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is NODE.
        self.nodes = nodes
        # The workspaces to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is PROJECT.
        self.projects = projects
        # The information about the alert recipients.
        self.receivers = receivers
        # The custom alert rule ID.
        self.remind_id = remind_id
        # The name of the rule.
        self.remind_name = remind_name
        # The conditions that trigger an alert. Valid values: FINISHED, UNFINISHED, ERROR, CYCLE_UNFINISHED, and TIMEOUT.
        self.remind_type = remind_type
        # The type of the object to which the custom alert rule is applied. Valid values: NODE, BASELINE, PROJECT, and BIZPROCESS. The value NODE indicates a node. The value BASELINE indicates a baseline. The value PROJECT indicates a workspace. The value BIZPROCESS indicates a workflow.
        self.remind_unit = remind_unit
        # The webhook URLs of the DingTalk chatbots.
        self.robots = robots
        # Indicates whether the custom alert rule is enabled. Valid values: true and false.
        self.useflag = useflag
        # WebHook URL
        self.webhooks = webhooks

    def validate(self):
        if self.baselines:
            for v1 in self.baselines:
                 if v1:
                    v1.validate()
        if self.biz_processes:
            for v1 in self.biz_processes:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()
        if self.receivers:
            for v1 in self.receivers:
                 if v1:
                    v1.validate()
        if self.robots:
            for v1 in self.robots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_interval is not None:
            result['AlertInterval'] = self.alert_interval

        if self.alert_methods is not None:
            result['AlertMethods'] = self.alert_methods

        if self.alert_targets is not None:
            result['AlertTargets'] = self.alert_targets

        if self.alert_unit is not None:
            result['AlertUnit'] = self.alert_unit

        if self.allow_nodes is not None:
            result['AllowNodes'] = self.allow_nodes

        result['Baselines'] = []
        if self.baselines is not None:
            for k1 in self.baselines:
                result['Baselines'].append(k1.to_map() if k1 else None)

        result['BizProcesses'] = []
        if self.biz_processes is not None:
            for k1 in self.biz_processes:
                result['BizProcesses'].append(k1.to_map() if k1 else None)

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.dnd_end is not None:
            result['DndEnd'] = self.dnd_end

        if self.dnd_start is not None:
            result['DndStart'] = self.dnd_start

        if self.founder is not None:
            result['Founder'] = self.founder

        if self.max_alert_times is not None:
            result['MaxAlertTimes'] = self.max_alert_times

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        result['Receivers'] = []
        if self.receivers is not None:
            for k1 in self.receivers:
                result['Receivers'].append(k1.to_map() if k1 else None)

        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        if self.remind_name is not None:
            result['RemindName'] = self.remind_name

        if self.remind_type is not None:
            result['RemindType'] = self.remind_type

        if self.remind_unit is not None:
            result['RemindUnit'] = self.remind_unit

        result['Robots'] = []
        if self.robots is not None:
            for k1 in self.robots:
                result['Robots'].append(k1.to_map() if k1 else None)

        if self.useflag is not None:
            result['Useflag'] = self.useflag

        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertInterval') is not None:
            self.alert_interval = m.get('AlertInterval')

        if m.get('AlertMethods') is not None:
            self.alert_methods = m.get('AlertMethods')

        if m.get('AlertTargets') is not None:
            self.alert_targets = m.get('AlertTargets')

        if m.get('AlertUnit') is not None:
            self.alert_unit = m.get('AlertUnit')

        if m.get('AllowNodes') is not None:
            self.allow_nodes = m.get('AllowNodes')

        self.baselines = []
        if m.get('Baselines') is not None:
            for k1 in m.get('Baselines'):
                temp_model = main_models.GetRemindResponseBodyDataBaselines()
                self.baselines.append(temp_model.from_map(k1))

        self.biz_processes = []
        if m.get('BizProcesses') is not None:
            for k1 in m.get('BizProcesses'):
                temp_model = main_models.GetRemindResponseBodyDataBizProcesses()
                self.biz_processes.append(temp_model.from_map(k1))

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('DndEnd') is not None:
            self.dnd_end = m.get('DndEnd')

        if m.get('DndStart') is not None:
            self.dnd_start = m.get('DndStart')

        if m.get('Founder') is not None:
            self.founder = m.get('Founder')

        if m.get('MaxAlertTimes') is not None:
            self.max_alert_times = m.get('MaxAlertTimes')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetRemindResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.GetRemindResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k1))

        self.receivers = []
        if m.get('Receivers') is not None:
            for k1 in m.get('Receivers'):
                temp_model = main_models.GetRemindResponseBodyDataReceivers()
                self.receivers.append(temp_model.from_map(k1))

        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        if m.get('RemindName') is not None:
            self.remind_name = m.get('RemindName')

        if m.get('RemindType') is not None:
            self.remind_type = m.get('RemindType')

        if m.get('RemindUnit') is not None:
            self.remind_unit = m.get('RemindUnit')

        self.robots = []
        if m.get('Robots') is not None:
            for k1 in m.get('Robots'):
                temp_model = main_models.GetRemindResponseBodyDataRobots()
                self.robots.append(temp_model.from_map(k1))

        if m.get('Useflag') is not None:
            self.useflag = m.get('Useflag')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

class GetRemindResponseBodyDataRobots(DaraModel):
    def __init__(
        self,
        at_all: bool = None,
        web_url: str = None,
    ):
        # Indicates whether all group members are notified when the alert notification is sent to a DingTalk group. Valid values: true and false.
        self.at_all = at_all
        # The webhook URL of the DingTalk chatbot.
        self.web_url = web_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at_all is not None:
            result['AtAll'] = self.at_all

        if self.web_url is not None:
            result['WebUrl'] = self.web_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtAll') is not None:
            self.at_all = m.get('AtAll')

        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')

        return self

class GetRemindResponseBodyDataReceivers(DaraModel):
    def __init__(
        self,
        alert_targets: List[str] = None,
        alert_unit: str = None,
    ):
        # The alert recipient.
        self.alert_targets = alert_targets
        # The type of the alert recipient. For more information about alert recipients, see the Receivers parameter. Valid values:
        # 
        # *   OWNER: indicate the task owner.
        # *   OTHER: indicates specified personnel.
        # *   SHIFT_SCHEDULE: indicates personnel in a shift schedule.
        self.alert_unit = alert_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_targets is not None:
            result['AlertTargets'] = self.alert_targets

        if self.alert_unit is not None:
            result['AlertUnit'] = self.alert_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTargets') is not None:
            self.alert_targets = m.get('AlertTargets')

        if m.get('AlertUnit') is not None:
            self.alert_unit = m.get('AlertUnit')

        return self

class GetRemindResponseBodyDataProjects(DaraModel):
    def __init__(
        self,
        project_id: int = None,
    ):
        # The workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class GetRemindResponseBodyDataNodes(DaraModel):
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

class GetRemindResponseBodyDataBizProcesses(DaraModel):
    def __init__(
        self,
        biz_id: int = None,
        biz_process_name: str = None,
    ):
        # The ID of the workflow.
        self.biz_id = biz_id
        # The name of the workflow.
        self.biz_process_name = biz_process_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_process_name is not None:
            result['BizProcessName'] = self.biz_process_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizProcessName') is not None:
            self.biz_process_name = m.get('BizProcessName')

        return self

class GetRemindResponseBodyDataBaselines(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        baseline_name: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        return self

