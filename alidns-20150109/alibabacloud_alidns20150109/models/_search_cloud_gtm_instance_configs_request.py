# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchCloudGtmInstanceConfigsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        available_status: str = None,
        client_token: str = None,
        enable_status: str = None,
        health_status: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        schedule_domain_name: str = None,
        schedule_zone_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - `zh-CN`: Chinese
        # 
        # - `en-US` (default): English
        self.accept_language = accept_language
        # The service availability status of the instance configuration. Valid values:
        # 
        # - `available`: The service for the GTM access domain is available when the instance configuration is **enabled** and its health status is **Normal** or Alert.
        # 
        # - `unavailable`: The service for the GTM access domain is unavailable when the instance configuration is **disabled** or its health status is **Exceptional**.
        self.available_status = available_status
        # A client-generated token to ensure the idempotence of the request. The token must be unique across requests and can contain up to 64 ASCII characters.
        self.client_token = client_token
        # The status of the instance configuration. Valid values:
        # 
        # - `enable`: Enabled. The intelligent scheduling policy of the GTM instance is in effect.
        # 
        # - `disable`: Disabled. The intelligent scheduling policy of the GTM instance is unavailable.
        self.enable_status = enable_status
        # The health status of the instance configuration. Valid values:
        # 
        # - `ok`: Normal. All address pools referenced by the GTM access domain are available.
        # 
        # - `ok_alert`: Alert. Some address pools referenced by the GTM access domain are unavailable. In this state, DNS resolution continues for available address pools but stops for unavailable ones.
        # 
        # - `exceptional`: Exceptional. All address pools referenced by the GTM access domain are unavailable. In this case, failover resolution uses the addresses from the non-empty address pool with the smallest sequence number to ensure clients receive a resolution result.
        self.health_status = health_status
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id
        # The page number. Pages start from 1. The default value is 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page for a paged query. The maximum value is **100** and the default value is **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # A note for the instance configuration.
        self.remark = remark
        # The GTM access domain. It is formed by combining the host record (`ScheduleHostname`) with the primary or subdomain name (`ScheduleZoneName`).
        self.schedule_domain_name = schedule_domain_name
        # The primary domain name (for example, `example.com`) or subdomain name (for example, `a.example.com`) of the GTM access domain. This is typically a domain name managed by Alibaba Cloud DNS under the same account that owns the GTM instance.
        self.schedule_zone_name = schedule_zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.available_status is not None:
            result['AvailableStatus'] = self.available_status

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.schedule_domain_name is not None:
            result['ScheduleDomainName'] = self.schedule_domain_name

        if self.schedule_zone_name is not None:
            result['ScheduleZoneName'] = self.schedule_zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AvailableStatus') is not None:
            self.available_status = m.get('AvailableStatus')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ScheduleDomainName') is not None:
            self.schedule_domain_name = m.get('ScheduleDomainName')

        if m.get('ScheduleZoneName') is not None:
            self.schedule_zone_name = m.get('ScheduleZoneName')

        return self

