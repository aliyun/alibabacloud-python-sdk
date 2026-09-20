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
        # The minimum alert interval, in seconds. Minimum value: 1200. Default value: 1800.
        self.alert_interval = alert_interval
        # The alert method. Valid values:
        # - MAIL: email.
        # - SMS: text message.
        # <props="intl">The regions that support SMS alerts are Singapore, Malaysia (Kuala Lumpur), and Germany (Frankfurt).
        # <props="china">- PHONE: phone call. Only DataWorks Professional Edition and higher editions are supported.
        # - Webhooks (WeCom or Lark chatbot). This alert method takes effect only after the Webhooks parameter is configured.
        # - DINGROBOTS: DingTalk chatbot.
        # 
        # Separate multiple alert methods with commas (,).
        # 
        # This parameter is required.
        self.alert_methods = alert_methods
        # - When AlertUnit (alert recipient) is set to OWNER (node owner), pass an empty value.
        # 
        # - When AlertUnit (alert recipient) is set to OTHER (specified user), pass the Alibaba Cloud UIDs of the specified users. Separate multiple Alibaba Cloud UIDs with commas (,). A maximum of 10 UIDs are supported.
        self.alert_targets = alert_targets
        # The granularity of the alert recipient. Valid values: OWNER (node owner) and OTHER (specified user).
        # 
        # This parameter is required.
        self.alert_unit = alert_unit
        # The IDs of the baselines to monitor when RemindUnit (object type) is set to BASELINE (baseline). Separate multiple IDs with commas (,). A maximum of 5 baselines can be monitored by a single rule.
        self.baseline_ids = baseline_ids
        # The IDs of the business processes to monitor when RemindUnit (object type) is set to BIZPROCESS (business process). Separate multiple business process IDs with commas (,). A maximum of 5 business processes can be monitored by a single rule.
        self.biz_process_ids = biz_process_ids
        # The descriptions for different trigger conditions are as follows:
        # 
        # - When RemindType (trigger condition) is set to FINISHED (completed), pass an empty value.
        # 
        # - When RemindType (trigger condition) is set to UNFINISHED (not completed), pass parameter in the format of {"hour":23,"minu":59}. Valid values of hour: [0,47\\]. Valid values of minu: [0,59\\].
        # 
        # - When RemindType (trigger condition) is set to ERROR (error), pass an empty value.
        # 
        # - When RemindType (trigger condition) is set to CYCLE_UNFINISHED (cycle not completed), pass parameter in the format of {"1":"05:50","2":"06:50","3":"07:50","4":"08:50","5":"09:50","6":"10:50","7":"11:50","8":"12:50","9":"13:50","10":"14:50","11":"15:50","12":"16:50","13":"17:50","14":"18:50","15":"19:50","16":"20:50","17":"21:50","18":"22:50","19":"23:50","20":"24:50","21":"25:50"}. The key in the JSON character string is the cycle number. Valid values: [1,288\\]. The value is the not-completed time for the corresponding cycle, in the hh:mm format. Valid values of hh: [0,47\\]. Valid values of mm: [0,59\\].
        # 
        # - When RemindType (trigger condition) is set to TIMEOUT (running timeout), pass parameter as a value such as 1800, in seconds. This means that an alert is triggered if the running time exceeds 30 minutes from the start of execution.
        self.detail = detail
        # The end time of the do-not-disturb period, in the hh:mm format. Valid values of hh: [0,23\\]. Valid values of mm: [0,59\\].
        self.dnd_end = dnd_end
        # The maximum number of alerts. Minimum value: 1. Maximum value: 10. Default value: 3.
        self.max_alert_times = max_alert_times
        # The IDs of the nodes to monitor when RemindUnit (object type) is set to NODE (node). Separate multiple IDs with commas (,). A maximum of 50 nodes can be monitored by a single rule.
        self.node_ids = node_ids
        # The ID of the workspace to monitor when RemindUnit (object type) is set to PROJECT (workspace). A single rule can monitor only one workspace.
        self.project_id = project_id
        # The name of the custom rule. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.remind_name = remind_name
        # The trigger condition. Valid values: FINISHED (completed), UNFINISHED (not completed), ERROR (error), CYCLE_UNFINISHED (cycle not completed), and TIMEOUT (running timeout).
        # 
        # This parameter is required.
        self.remind_type = remind_type
        # The type of the object. Valid values: NODE (node), BASELINE (baseline), PROJECT (workspace), and BIZPROCESS (business process).
        # 
        # This parameter is required.
        self.remind_unit = remind_unit
        # The webhook URLs of DingTalk chatbots. Separate multiple webhook URLs with commas (,).
        self.robot_urls = robot_urls
        # The webhook URLs of WeCom or Lark chatbots. Separate multiple webhook URLs with commas (,). The alertMethods parameter must include the WEBHOOKS alert method.
        # 
        # Only DataWorks Enterprise Edition is supported.
        # Available regions: China (Shanghai), China (Chengdu), China (Zhangjiakou), China (Beijing), China (Hangzhou), China (Shenzhen), Hong Kong (China), Germany (Frankfurt), and Singapore.
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

