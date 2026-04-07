# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRemindRequest(DaraModel):
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
        remind_name: str = None,
        remind_type: str = None,
        remind_unit: str = None,
        robot_urls: str = None,
        webhooks: str = None,
    ):
        # The minimum interval at which alerts are reported. Unit: seconds. Minimum value: 1200. Default value: 1800.
        self.alert_interval = alert_interval
        # The notification method. Valid values:
        # 
        # *   MAIL: Alert notifications are sent by email.
        # *   SMS: Alert notifications are sent by text message. Alert notifications can be sent by text message only in the Singapore, Malaysia (Kuala Lumpur), and Germany (Frankfurt) regions.
        # *   WEBHOOKS (WeCom or Lark chatbot): Alert notifications are sent by WeCom or Lark message. If you want to use this notification method, you must configure the Webhooks parameter.
        # *   DINGROBOTS: Alert notifications are sent by DingTalk chatbot.
        # 
        # You can specify multiple notification methods. Separate them with commas (,).
        # 
        # This parameter is required.
        self.alert_methods = alert_methods
        # *   If the AlertUnit parameter is set to OWNER, leave this parameter empty.
        # *   If the AlertUnit parameter is set to OTHER, set this parameter to the ID of the Alibaba Cloud account used by the specified user. You can specify multiple IDs. Separate multiple IDs with commas (,). You can specify a maximum of 10 IDs.
        self.alert_targets = alert_targets
        # The recipient of the alert. Valid values: OWNER and OTHER. The value OWNER indicates the node owner. The value OTHER indicates a specified user.
        # 
        # This parameter is required.
        self.alert_unit = alert_unit
        # The ID of the baseline to which the custom alert rule is applied. This parameter takes effect when the RemindUnit parameter is set to BASELINE. You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of five baselines can be specified for a custom alert rule.
        self.baseline_ids = baseline_ids
        # The ID of the workflow to which the custom alert rule is applied. This parameter takes effect when the RemindUnit parameter is set to BIZPROCESS. You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of five workflows can be specified for a custom alert rule.
        self.biz_process_ids = biz_process_ids
        # The details of the conditions that trigger an alert.
        # 
        # *   If the RemindType parameter is set to FINISHED, leave this parameter empty.
        # *   If the RemindType parameter is set to UNFINISHED, configure this parameter as key-value pairs. Example: {"hour":23,"minu":59}. Valid values of hour: [0,47]. Valid values of minu: [0,59].
        # *   If the RemindType parameter is set to ERROR, leave this parameter empty.
        # *   If the RemindType parameter is set to CYCLE_UNFINISHED, configure this parameter as key-value pairs. Example: {"1":"05:50","2":"06:50","3":"07:50","4":"08:50","5":"09:50","6":"10:50","7":"11:50","8":"12:50","9":"13:50","10":"14:50","11":"15:50","12":"16:50","13":"17:50","14":"18:50","15":"19:50","16":"20:50","17":"21:50","18":"22:50","19":"23:50","20":"24:50","21":"25:50"}. The key indicates the ID of the cycle. Valid values: [1,288]. The value indicates the timeout period of the node that is running in the cycle. Specify the value in the hh:mm format. Valid values of hh: [0,47]. Valid values of mm: [0,59].
        # *   If the RemindType parameter is set to TIMEOUT, set this parameter to the timeout period. Unit: seconds. Example: 1800. This value indicates that an alert is reported if the node has run for more than 30 minutes.
        self.detail = detail
        # The end time of the quiet hours. Specify the time in the hh:mm format. Valid values of hh: [0,23]. Valid values of mm: [0,59].
        self.dnd_end = dnd_end
        # The maximum number of alerts. Valid values: 1 to 10. Default value: 3.
        self.max_alert_times = max_alert_times
        # The ID of the node to which the custom alert rule is applied. This parameter takes effect when the RemindUnit parameter is set to NODE. You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of 50 nodes can be specified for a custom alert rule.
        self.node_ids = node_ids
        # The ID of the workspace to which the custom alert rule is applied. This parameter takes effect when the RemindUnit parameter is set to PROJECT. You can specify only one workspace for a custom alert rule.
        self.project_id = project_id
        # The name of the custom alert rule. The name cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.remind_name = remind_name
        # The conditions that trigger an alert. Valid values: FINISHED, UNFINISHED, ERROR, CYCLE_UNFINISHED, and TIMEOUT.
        # 
        # This parameter is required.
        self.remind_type = remind_type
        # The type of the object to which the custom alert rule is applied. Valid values: NODE, BASELINE, PROJECT, and BIZPROCESS. The value NODE indicates a node. The value BASELINE indicates a baseline. The value PROJECT indicates a workspace. The value BIZPROCESS indicates a workflow.
        # 
        # This parameter is required.
        self.remind_unit = remind_unit
        # The webhook URL of the DingTalk chatbot. You can specify multiple webhook URLs. Separate multiple webhook URLs with commas (,).
        self.robot_urls = robot_urls
        # The webhook URL of the WeCom or Lark chatbot. You can specify multiple webhook URLs. Separate multiple webhook URLs with commas (,). You must specify WEBHOOKS for AlertMethods.
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

        if self.remind_name is not None:
            result['RemindName'] = self.remind_name

        if self.remind_type is not None:
            result['RemindType'] = self.remind_type

        if self.remind_unit is not None:
            result['RemindUnit'] = self.remind_unit

        if self.robot_urls is not None:
            result['RobotUrls'] = self.robot_urls

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

        if m.get('RemindName') is not None:
            self.remind_name = m.get('RemindName')

        if m.get('RemindType') is not None:
            self.remind_type = m.get('RemindType')

        if m.get('RemindUnit') is not None:
            self.remind_unit = m.get('RemindUnit')

        if m.get('RobotUrls') is not None:
            self.robot_urls = m.get('RobotUrls')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

