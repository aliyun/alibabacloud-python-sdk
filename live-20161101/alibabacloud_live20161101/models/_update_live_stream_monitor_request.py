# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveStreamMonitorRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        callback_url: str = None,
        ding_talk_web_hook_url: str = None,
        domain: str = None,
        input_list: str = None,
        monitor_config: str = None,
        monitor_id: str = None,
        monitor_name: str = None,
        output_template: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream: str = None,
    ):
        # The name of the application to which the output stream of the monitoring session belongs. You can specify a name. If you do not specify a name, the system uses **monitor** as the name of the application.
        self.app = app
        # The callback URL. Supported formats include HTTP and HTTPS.
        self.callback_url = callback_url
        # The URL of the DingTalk chatbot. Specify a DingTalk chatbot that you have configured, and you can receive live monitoring alerts from the chatbot. For more information, see [Configure a custom chatbot](https://open.dingtalk.com/document/robots/custom-robot-access).
        # 
        # >  Specify "Alert" as the custom keyword of the DingTalk chatbot. Otherwise, you cannot receive messages.
        self.ding_talk_web_hook_url = ding_talk_web_hook_url
        # The domain name.
        self.domain = domain
        # The list of input streams to monitor. For more information, see the following **InputConfig** table.
        # 
        # This parameter is required.
        self.input_list = input_list
        # The monitoring alert thresholds. The value is a JSON string. For more information, see the following MonitorConfig table.
        self.monitor_config = monitor_config
        # The ID of the monitoring session.
        # 
        # >  You can obtain the monitoring session ID from the response of the [CreateLiveStreamMonitor](https://help.aliyun.com/document_detail/2848129.html) operation.
        # 
        # This parameter is required.
        self.monitor_id = monitor_id
        # The name of the monitoring session.
        self.monitor_name = monitor_name
        # The output template of the monitoring session. Valid values:
        # 
        # *   **lp_ld**: low definition
        # *   **lp_sd**: standard definition
        # *   **lp_hd**: high definition
        # *   **lp_ud**: ultra-high definition
        self.output_template = output_template
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the output stream of the monitoring session.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.ding_talk_web_hook_url is not None:
            result['DingTalkWebHookUrl'] = self.ding_talk_web_hook_url

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.input_list is not None:
            result['InputList'] = self.input_list

        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config

        if self.monitor_id is not None:
            result['MonitorId'] = self.monitor_id

        if self.monitor_name is not None:
            result['MonitorName'] = self.monitor_name

        if self.output_template is not None:
            result['OutputTemplate'] = self.output_template

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('DingTalkWebHookUrl') is not None:
            self.ding_talk_web_hook_url = m.get('DingTalkWebHookUrl')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InputList') is not None:
            self.input_list = m.get('InputList')

        if m.get('MonitorConfig') is not None:
            self.monitor_config = m.get('MonitorConfig')

        if m.get('MonitorId') is not None:
            self.monitor_id = m.get('MonitorId')

        if m.get('MonitorName') is not None:
            self.monitor_name = m.get('MonitorName')

        if m.get('OutputTemplate') is not None:
            self.output_template = m.get('OutputTemplate')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

