# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCdnDeliverTaskRequest(DaraModel):
    def __init__(
        self,
        deliver: str = None,
        domain_name: str = None,
        name: str = None,
        reports: str = None,
        schedule: str = None,
    ):
        # The method that is used to send operations reports. Operations reports are sent to you only by email. The settings must be escaped in JSON.
        # 
        # This parameter is required.
        self.deliver = deliver
        # The domain names to be tracked. Separate multiple domain names with commas (,). You can specify up to 500 domain names. If you want to specify more than 500 domain names, [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=5176.2020520001.aliyun_topbar.18.dbd44bd3e4f845#/ticket/createIndex).
        # 
        # > If you do not specify a domain name, the tracking task is created for all domain names that belong to your Alibaba Cloud account.
        self.domain_name = domain_name
        # The name of the tracking task.
        # 
        # This parameter is required.
        self.name = name
        # The operations reports that are tracked by the task. The data must be escaped in JSON.
        # 
        # This parameter is required.
        self.reports = reports
        # The parameters that specify the time interval at which the tracking task sends operations reports. The settings must be escaped in JSON.
        # 
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deliver is not None:
            result['Deliver'] = self.deliver

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.name is not None:
            result['Name'] = self.name

        if self.reports is not None:
            result['Reports'] = self.reports

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deliver') is not None:
            self.deliver = m.get('Deliver')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reports') is not None:
            self.reports = m.get('Reports')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        return self

