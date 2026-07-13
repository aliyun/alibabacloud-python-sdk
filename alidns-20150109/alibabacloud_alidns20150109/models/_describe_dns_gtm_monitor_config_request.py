# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsGtmMonitorConfigRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
    ):
        # The language of the response. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The ID of the health check configuration.<props="china"> For more information, see [DescribeDnsGtmInstanceAddressPool](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describednsgtminstanceaddresspool?spm=a2c4g.11186623.help-menu-29697.d_0_5_1_3_9_6.7db77000nMCPI1).<props="intl"> For more information, see [DescribeDnsGtmInstanceAddressPool](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describednsgtminstanceaddresspool?spm=a2c63.p38356.help-menu-search-29697.d_0).
        # 
        # This parameter is required.
        self.monitor_config_id = monitor_config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')

        return self

