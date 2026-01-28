# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceDashboardReport(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        grafana_workspace_id: str = None,
        id: int = None,
        last_send_time: int = None,
        msg: str = None,
        name: str = None,
        report_channel_target: str = None,
        report_channel_type: str = None,
        report_style: str = None,
        report_type: str = None,
        status: str = None,
        trigger_day: str = None,
        trigger_time: str = None,
        trigger_type: str = None,
        url: str = None,
        user_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.grafana_workspace_id = grafana_workspace_id
        self.id = id
        self.last_send_time = last_send_time
        self.msg = msg
        self.name = name
        self.report_channel_target = report_channel_target
        self.report_channel_type = report_channel_type
        self.report_style = report_style
        self.report_type = report_type
        self.status = status
        self.trigger_day = trigger_day
        self.trigger_time = trigger_time
        self.trigger_type = trigger_type
        self.url = url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.grafana_workspace_id is not None:
            result['grafanaWorkspaceId'] = self.grafana_workspace_id

        if self.id is not None:
            result['id'] = self.id

        if self.last_send_time is not None:
            result['lastSendTime'] = self.last_send_time

        if self.msg is not None:
            result['msg'] = self.msg

        if self.name is not None:
            result['name'] = self.name

        if self.report_channel_target is not None:
            result['reportChannelTarget'] = self.report_channel_target

        if self.report_channel_type is not None:
            result['reportChannelType'] = self.report_channel_type

        if self.report_style is not None:
            result['reportStyle'] = self.report_style

        if self.report_type is not None:
            result['reportType'] = self.report_type

        if self.status is not None:
            result['status'] = self.status

        if self.trigger_day is not None:
            result['triggerDay'] = self.trigger_day

        if self.trigger_time is not None:
            result['triggerTime'] = self.trigger_time

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        if self.url is not None:
            result['url'] = self.url

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('grafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('grafanaWorkspaceId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastSendTime') is not None:
            self.last_send_time = m.get('lastSendTime')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('reportChannelTarget') is not None:
            self.report_channel_target = m.get('reportChannelTarget')

        if m.get('reportChannelType') is not None:
            self.report_channel_type = m.get('reportChannelType')

        if m.get('reportStyle') is not None:
            self.report_style = m.get('reportStyle')

        if m.get('reportType') is not None:
            self.report_type = m.get('reportType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('triggerDay') is not None:
            self.trigger_day = m.get('triggerDay')

        if m.get('triggerTime') is not None:
            self.trigger_time = m.get('triggerTime')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

