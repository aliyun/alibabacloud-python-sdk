# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDcdnDeliverTaskRequest(DaraModel):
    def __init__(
        self,
        deliver: str = None,
        deliver_id: int = None,
        domain_name: str = None,
        name: str = None,
        reports: str = None,
        schedule: str = None,
    ):
        # The method that is used to send operations reports. Operations reports are sent to you only by email. The settings need to be escaped in JSON.
        self.deliver = deliver
        # The ID of the tracking task that you want to update.
        # 
        # This parameter is required.
        self.deliver_id = deliver_id
        # The domain names from which the tracking task collects data. Separate domain names with commas (,). If you do not specify a domain name, the task collects data from all domain names that belong to your Alibaba Cloud account.
        self.domain_name = domain_name
        # The name of the tracking task.
        self.name = name
        # The operations reports that are tracked by the task. The data needs to be escaped in JSON.
        self.reports = reports
        # The parameters that specify the time interval at which the tracking task sends operations reports. The settings need to be escaped in JSON.
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

        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id

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

        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reports') is not None:
            self.reports = m.get('Reports')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        return self

