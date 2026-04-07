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
        # The intervals at which alert notifications are sent. Unit: seconds. Minimum value: 1200. Default value: 1800.
        self.alert_interval = alert_interval
        # The notification method. Valid values:
        # 
        # *   MAIL: Alert notifications are sent by email.
        # *   SMS: Alert notifications are sent by text message.
        # *   PHONE: Alert notifications are sent by phone call. You can use this notification method only in DataWorks Professional Edition or more advanced editions.
        # *   DINGROBOTS: Alert notifications are sent by DingTalk message. You can use this notification method only if the RobotUrls parameter is configured.
        # *   WEBHOOKS (WeCom or Lark chatbot): Alert notifications are sent by WeCom or Lark message. You can use this notification method only if the Webhooks parameter is configured.
        # 
        # Multiple notification methods are separated by commas (,).
        self.alert_methods = alert_methods
        # The value format required by this parameter varies based on the value that you specify for the AlertUnit parameter. Take note of the following items:
        # 
        # *   If the AlertUnit parameter is set to OWNER, leave this parameter empty.
        # *   If the AlertUnit parameter is set to OTHER, set this parameter to the unique ID (UID) of the specified user. You can specify multiple UIDs. Separate them with commas (,). A maximum of 10 UIDs can be specified for receiving alert notifications.
        self.alert_targets = alert_targets
        # The recipient to whom alert notifications are sent. Valid values: OWNER and OTHER. The value OWNER indicates that alert notifications are sent to the object owner. The value OTHER indicates that alert notifications are sent to a specified user.
        self.alert_unit = alert_unit
        # The ID of the baseline to which the custom alert rule is applied. A maximum of 5 baselines can be specified for a custom alert rule. You can specify multiple IDs. Separate multiple IDs with commas (,). This parameter takes effect when you set the RemindUnit parameter to BASELINE.
        self.baseline_ids = baseline_ids
        # The ID of the workflow to which the custom alert rule is applied. A maximum of 5 workflows can be specified for a custom alert rule. You can specify multiple IDs. Separate multiple IDs with commas (,). This parameter takes effect when you set the RemindUnit parameter to BIZPROCESS.
        self.biz_process_ids = biz_process_ids
        # The details of the conditions that trigger an alert.
        # 
        # *   If the RemindType parameter is set to FINISHED, leave this parameter empty.
        # *   If the RemindType parameter is set to UNFINISHED, set this parameter to key-value pairs. Example: {"hour":23,"minu":59}. Valid values of hour: [0,47]. Valid values of minu: [0,59].
        # *   If the RemindType parameter is set to ERROR, leave this parameter empty.
        # *   If the RemindType parameter is set to CYCLE_UNFINISHED, set this parameter to key-value pairs in the JSON format. Example: {"1":"05:50","2":"06:50","3":"07:50","4":"08:50","5":"09:50","6":"10:50","7":"11:50","8":"12:50","9":"13:50","10":"14:50","11":"15:50","12":"16:50","13":"17:50","14":"18:50","15":"19:50","16":"20:50","17":"21:50","18":"22:50","19":"23:50","20":"24:50","21":"25:50"}. A key in the JSON string indicates the sequence number of a cycle. Valid values of keys: 1 to 288. A value in the JSON string indicates the time in point when a monitored instance times out in the relevant cycle. Values must be in the format of hh:mm. Valid values of hh: [0,47]. Valid values of mm: [0,59].
        # *   If the RemindType parameter is set to TIMEOUT, set this parameter to the timeout period. Unit: seconds. Example: 1800. This indicates that an alert notification is sent if the running duration of a monitored instance exceeds 30 minutes.
        self.detail = detail
        # The end of the period during which no alert notifications are sent. Specify the time in the hh:mm format. Valid values of hh: [0,23]. Valid values of mm: [0,59].
        self.dnd_end = dnd_end
        # The maximum number of alerts. Valid values: 1 to 10. Default value: 3.
        self.max_alert_times = max_alert_times
        # The ID of the node to which the custom alert rule is applied. A maximum of 50 nodes can be specified for a custom alert rule. You can specify multiple IDs. Separate multiple IDs with commas (,). This parameter takes effect when you set the RemindUnit parameter to NODE.
        self.node_ids = node_ids
        # The ID of the workspace to which the custom alert rule is applied. You can specify only one workspace for a custom alert rule. This parameter takes effect when you set the RemindUnit parameter to PROJECT.
        self.project_id = project_id
        # The custom alert rule ID.
        # 
        # This parameter is required.
        self.remind_id = remind_id
        # The name of the custom alert rule. The name cannot exceed 128 characters in length.
        self.remind_name = remind_name
        # The condition that triggers the alert rule. Valid values:
        # 
        # *   FINISHED: The system monitors an instance when it starts to run and sends an alert notification after the running of the instance is complete.
        # *   UNFINISHED: The system monitors an instance when it starts to run and sends an alert notification if the instance is still running at the specified point in time.
        # *   ERROR: The system monitors an instance when it starts to run and sends an alert notification if an error occurs.
        # *   CYCLE_UNFINISHED: The system sends an alert notification if a monitored instance is still running at the end of the specified cycle. In most cases, you can configure this trigger condition for node instances that are scheduled to run by hour.
        # *   TIMEOUT: The system monitors an instance when it starts to run and sends an alert notification if the instance is still running after the specified period ends. In most cases, you can configure this trigger condition to monitor the running duration of node instances.
        # 
        # For more information, see [Manage custom alert rules](https://help.aliyun.com/document_detail/138172.html).
        self.remind_type = remind_type
        # The type of the object to which the custom alert rule is applied. Valid values:
        # 
        # *   NODE
        # *   BASELINE
        # *   PROJECT
        # *   BIZPROCESS
        self.remind_unit = remind_unit
        # The webhook URL of the DingTalk chatbot. You can specify multiple webhook URLs. Separate multiple webhook URLs with commas (,). If this parameter is set to undefined, the specified webhook URLs are cleared.
        self.robot_urls = robot_urls
        # Specifies whether to enable the alert rule. Valid values:
        # 
        # *   true
        # *   false
        self.use_flag = use_flag
        # The webhook URL of the WeCom or Lark chatbot. You can specify multiple webhook URLs. Separate multiple webhook URLs with commas (,). The value of AlertMethods must include WEBHOOKS. If this parameter is set to undefined, the specified webhook URLs are cleared.
        # 
        # Only DataWorks Enterprise Edition supports this parameter. The webhook URL-based alerting feature is supported in the following regions: China (Shanghai), China (Chengdu), China (Zhangjiakou), China (Beijing), China (Hangzhou), China (Shenzhen), China (Hong Kong), Germany (Frankfurt), and Singapore.
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

