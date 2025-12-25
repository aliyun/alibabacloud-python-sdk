# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetSiteDeliveryTaskResponseBody(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_list: str = None,
        filter_rules: str = None,
        filter_ver: str = None,
        raw_rule: str = None,
        request_id: str = None,
        sink_config: Any = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
        task_name: str = None,
    ):
        # The log category. Valid values:
        # 
        # *   dcdn_log_access_l1 (default): access logs.
        # *   dcdn_log_er: Edge Routine logs.
        # *   dcdn_log_waf: firewall logs.
        # *   dcdn_log_ipa: TCP/UDP proxy logs.
        self.business_type = business_type
        # The data center. Valid values:
        # 
        # 1.  cn: the Chinese mainland.
        # 2.  sg: outside the Chinese mainland.
        self.data_center = data_center
        # The destination of the delivery. Valid values:
        # 
        # 1.  sls: Alibaba Cloud Simple Log Service (SLS).
        # 2.  http: HTTP server.
        # 3.  aws3: Amazon Simple Storage Service (S3).
        # 4.  oss: Alibaba Cloud Object Storage Service (OSS).
        # 5.  kafka: Kafka.
        # 6.  aws3cmpt: S3-compatible storage service.
        self.delivery_type = delivery_type
        # The discard rate.
        self.discard_rate = discard_rate
        # The log fields.
        self.field_list = field_list
        # The filtering rules.
        self.filter_rules = filter_rules
        self.filter_ver = filter_ver
        self.raw_rule = raw_rule
        # The request ID.
        self.request_id = request_id
        # The delivery configuration.
        self.sink_config = sink_config
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The status of the delivery task.
        # 
        # *   **online**
        # *   **offline**
        self.status = status
        # The name of the delivery task.
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

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate

        if self.field_list is not None:
            result['FieldList'] = self.field_list

        if self.filter_rules is not None:
            result['FilterRules'] = self.filter_rules

        if self.filter_ver is not None:
            result['FilterVer'] = self.filter_ver

        if self.raw_rule is not None:
            result['RawRule'] = self.raw_rule

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sink_config is not None:
            result['SinkConfig'] = self.sink_config

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')

        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')

        if m.get('FilterRules') is not None:
            self.filter_rules = m.get('FilterRules')

        if m.get('FilterVer') is not None:
            self.filter_ver = m.get('FilterVer')

        if m.get('RawRule') is not None:
            self.raw_rule = m.get('RawRule')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SinkConfig') is not None:
            self.sink_config = m.get('SinkConfig')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

