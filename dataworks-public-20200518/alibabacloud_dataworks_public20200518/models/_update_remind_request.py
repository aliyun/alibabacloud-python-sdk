# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRemindRequest(DaraModel):
    def __init__(
        self,
        alert_interval: int = None,
        alert_methods: str = None,
        alert_targets: str = None,
        alert_unit: str = None,
        baseline_ids: str = None,
        biz_process_ids: str = None,
        detail: str = None,
        dnd_end: str = None,
        max_alert_times: int = None,
        node_ids: str = None,
        project_id: int = None,
        remind_id: int = None,
        remind_name: str = None,
        remind_type: str = None,
        remind_unit: str = None,
        robot_urls: str = None,
        use_flag: bool = None,
        webhooks: str = None,
    ):
        # The alert interval, in seconds. Minimum value: 1200. Default value: 1800.
        self.alert_interval = alert_interval
        # The alert notification method. Valid values:
        # - MAIL
        # - SMS
        # - PHONE. Only DataWorks Professional Edition and higher support phone alerts.
        # - DINGROBOTS (DingTalk chatbot). This method takes effect only after the RobotUrls parameter is configured.
        # - Webhooks (WeCom or Lark chatbot). This method takes effect only after the Webhooks parameter is configured.
        # 
        # Separate multiple alert methods with commas (,).
        self.alert_methods = alert_methods
        # The configuration details for different alert recipients:
        # - When AlertUnit is set to OWNER (node owner), the configuration is left empty.
        # - When AlertUnit is set to OTHER (specified user), set this parameter to the Alibaba Cloud UIDs of the specified users. Separate multiple UIDs with commas (,). You can specify up to 10 users to receive alerts.
        self.alert_targets = alert_targets
        # The recipient of the alert. Valid values:
        # - OWNER: the node owner.
        # - OTHER: a specified user.
        self.alert_unit = alert_unit
        # The baseline IDs when the monitored object is a baseline. A rule can monitor up to 5 baselines. Separate multiple baseline IDs with commas (,).
        # This parameter takes effect only when RemindUnit is set to BASELINE.
        self.baseline_ids = baseline_ids
        # The business process IDs when the monitored object is a business process. A rule can monitor up to 5 business processes. Separate multiple business process IDs with commas (,).
        # This parameter takes effect only when RemindUnit is set to BIZPROCESS.
        self.biz_process_ids = biz_process_ids
        # The configuration details for different trigger conditions:
        # - When RemindType (trigger condition) is set to FINISHED, the configuration is left empty.
        # - When RemindType (trigger condition) is set to UNFINISHED, the configuration format is {"hour":23,"minu":59}. Valid values of hour: [0,47\\]. Valid values of minu: [0,59\\].
        # - When RemindType (trigger condition) is set to ERROR, the configuration is left empty.
        # - When RemindType (trigger condition) is set to CYCLE_UNFINISHED (cycle unfinished), the configuration format is {"1":"05:50","2":"06:50","3":"07:50","4":"08:50","5":"09:50","6":"10:50","7":"11:50","8":"12:50","9":"13:50","10":"14:50","11":"15:50","12":"16:50","13":"17:50","14":"18:50","15":"19:50","16":"20:50","17":"21:50","18":"22:50","19":"23:50","20":"24:50","21":"25:50"}.
        # The key in the JSON string is the cycle number. Valid values: [1,288\\]. The value is the unfinished time for the corresponding cycle in the format hh:mm. Valid values of hh: [0,47\\]. Valid values of mm: [0,59\\].
        # - When RemindType (trigger condition) is set to TIMEOUT, the configuration format is 1800, in seconds. This means an alert is triggered if the instance has been running for more than 30 minutes.
        self.detail = detail
        # The end time of the do-not-disturb period. Alerts are not sent before this time. Format: hh:mm. Valid values of hh: [0,23\\]. Valid values of mm: [0,59\\].
        self.dnd_end = dnd_end
        # The maximum number of alerts. Valid values: [1,10\\]. Default value: 3.
        self.max_alert_times = max_alert_times
        # The node IDs when the monitored object is a node. A rule can monitor up to 50 nodes. Separate multiple node IDs with commas (,).
        # This parameter takes effect only when RemindUnit is set to NODE.
        self.node_ids = node_ids
        # The workspace ID when the monitored object is a workspace. A rule can monitor only one workspace.
        # This parameter takes effect only when RemindUnit is set to PROJECT.
        self.project_id = project_id
        # The ID of the custom rule.
        # 
        # This parameter is required.
        self.remind_id = remind_id
        # The name of the custom rule. The name cannot exceed 128 characters in length.
        self.remind_name = remind_name
        # The condition that triggers the alert rule. Valid values:
        # - FINISHED: The system monitors the instance from the start time and sends an alert when the node runs successfully.
        # - UNFINISHED: The system monitors the instance from the start time and sends an alert if the node has not finished running by the specified target time.
        # - ERROR: The system monitors the instance from the start time and sends an alert when the node encounters an error.
        # - CYCLE_UNFINISHED: The system sends an alert if the instance has not finished running within the specified cycle. This is typically used to monitor instances that run on an hourly cycle.
        # - TIMEOUT: The system monitors the instance from the start time and sends an alert if the node has not finished running after the specified duration. This is typically used to monitor the running duration of instances.
        # 
        # For more information about alert trigger conditions, see [Custom rules](https://help.aliyun.com/document_detail/138172.html).
        self.remind_type = remind_type
        # The type of the monitored object. Valid values:
        # - NODE
        # - BASELINE
        # - PROJECT (workspace)
        # - BIZPROCESS (business process)
        self.remind_unit = remind_unit
        # The webhook URLs of DingTalk group chatbots. Separate multiple webhook URLs with commas (,).
        # When the parameter settings are set to undefined, the system clears the DingTalk chatbot webhook URLs.
        self.robot_urls = robot_urls
        # Specifies whether to enable the alert rule. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.use_flag = use_flag
        # The webhook URLs of WeCom or Lark chatbots. Separate multiple webhook URLs with commas (,). The alertMethods parameter must include the WEBHOOKS alerting method. When the parameter is set to undefined, the system clears the webhook URLs.
        # 
        # Only DataWorks Enterprise Edition is supported.
        # Active regions: China (Shanghai), China (Chengdu), China (Zhangjiakou), China (Beijing), China (Hangzhou), China (Shenzhen), Hong Kong (China), Germany (Frankfurt), Asia-Pacific Southeast 1 (Singapore).
        self.webhooks = webhooks

    def validate(self):
        pass

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

        if self.baseline_ids is not None:
            result['BaselineIds'] = self.baseline_ids

        if self.biz_process_ids is not None:
            result['BizProcessIds'] = self.biz_process_ids

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.dnd_end is not None:
            result['DndEnd'] = self.dnd_end

        if self.max_alert_times is not None:
            result['MaxAlertTimes'] = self.max_alert_times

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        if self.remind_name is not None:
            result['RemindName'] = self.remind_name

        if self.remind_type is not None:
            result['RemindType'] = self.remind_type

        if self.remind_unit is not None:
            result['RemindUnit'] = self.remind_unit

        if self.robot_urls is not None:
            result['RobotUrls'] = self.robot_urls

        if self.use_flag is not None:
            result['UseFlag'] = self.use_flag

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

        if m.get('BaselineIds') is not None:
            self.baseline_ids = m.get('BaselineIds')

        if m.get('BizProcessIds') is not None:
            self.biz_process_ids = m.get('BizProcessIds')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('DndEnd') is not None:
            self.dnd_end = m.get('DndEnd')

        if m.get('MaxAlertTimes') is not None:
            self.max_alert_times = m.get('MaxAlertTimes')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        if m.get('RemindName') is not None:
            self.remind_name = m.get('RemindName')

        if m.get('RemindType') is not None:
            self.remind_type = m.get('RemindType')

        if m.get('RemindUnit') is not None:
            self.remind_unit = m.get('RemindUnit')

        if m.get('RobotUrls') is not None:
            self.robot_urls = m.get('RobotUrls')

        if m.get('UseFlag') is not None:
            self.use_flag = m.get('UseFlag')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

