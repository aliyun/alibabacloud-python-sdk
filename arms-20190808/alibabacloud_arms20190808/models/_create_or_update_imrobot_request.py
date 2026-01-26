# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateIMRobotRequest(DaraModel):
    def __init__(
        self,
        card_template: str = None,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        ding_sign_key: str = None,
        enable_outgoing: bool = None,
        robot_address: str = None,
        robot_id: int = None,
        robot_name: str = None,
        token: str = None,
        type: str = None,
    ):
        # The configurations of the alert card template. For more information about the parameters in the template, see the following section.
        self.card_template = card_template
        # Specifies whether to send daily statistics. Valid values:
        # 
        # *   `false` (default): Daily statistics are not sent.
        # *   `true`: Daily statistics are sent. If you set the value to `true`, the **DailyNocTime** parameter is required.
        self.daily_noc = daily_noc
        # The points in time at which the daily statistics are sent. Separate multiple points in time with commas (,). The points in time are in the HH:SS format. The information that ARMS sends at the specified points in time includes the total number of alerts generated on the current day, the number of cleared alerts, and the number of alerts to be cleared.
        self.daily_noc_time = daily_noc_time
        # The signature key of DingTalk. If you specify a signature key, DingTalk authentication is performed by using the signature key. If you do not specify a signature key, a whitelist is used for authentication by default. The keyword of the whitelist is **Alert**.
        self.ding_sign_key = ding_sign_key
        # Specifies whether to enable the Outgoing feature.
        self.enable_outgoing = enable_outgoing
        # The webhook URL of the IM chatbot.
        # 
        # This parameter is required.
        self.robot_address = robot_address
        # The ID of the IM chatbot.
        # > If you do not specify the parameter, a new IM chatbot is created.
        self.robot_id = robot_id
        # The name of the IM chatbot.
        # 
        # This parameter is required.
        self.robot_name = robot_name
        # The token required to enable the Outgoing feature.
        self.token = token
        # The type of the IM chatbot. Valid values:
        # 
        # *   `dingding`: DingTalk chatbot
        # *   `wechat`: WeCom chatbot
        # *   `feishu`: Lark chatbot
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_template is not None:
            result['CardTemplate'] = self.card_template

        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc

        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time

        if self.ding_sign_key is not None:
            result['DingSignKey'] = self.ding_sign_key

        if self.enable_outgoing is not None:
            result['EnableOutgoing'] = self.enable_outgoing

        if self.robot_address is not None:
            result['RobotAddress'] = self.robot_address

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.token is not None:
            result['Token'] = self.token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardTemplate') is not None:
            self.card_template = m.get('CardTemplate')

        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')

        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')

        if m.get('DingSignKey') is not None:
            self.ding_sign_key = m.get('DingSignKey')

        if m.get('EnableOutgoing') is not None:
            self.enable_outgoing = m.get('EnableOutgoing')

        if m.get('RobotAddress') is not None:
            self.robot_address = m.get('RobotAddress')

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

