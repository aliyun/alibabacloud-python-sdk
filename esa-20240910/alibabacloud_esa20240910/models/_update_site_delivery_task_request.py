# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteDeliveryTaskRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        filter_ver: str = None,
        site_id: int = None,
        task_name: str = None,
    ):
        # The log category. Valid values:
        # 
        # *   dcdn_log_access_l1 (default): access logs.
        # *   dcdn_log_er: Edge Routine logs.
        # *   dcdn_log_waf: firewall logs.
        # *   dcdn_log_ipa: TCP/UDP proxy logs.
        self.business_type = business_type
        # The discard rate.
        self.discard_rate = discard_rate
        # The log fields that you want to include in real-time logs to be delivered. Separate the log fields with commas (,).
        # 
        # This parameter is required.
        self.field_name = field_name
        self.filter_ver = filter_ver
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.site_id = site_id
        # The name of the delivery task.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.filter_ver is not None:
            result['FilterVer'] = self.filter_ver

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FilterVer') is not None:
            self.filter_ver = m.get('FilterVer')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

