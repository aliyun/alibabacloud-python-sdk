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
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The availability state of the access domain name. Valid values:
        # 
        # *   available: If the access domain name is **enabled** and the health state is **normal**, the access domain name is deemed **available**.
        # *   unavailable: If the access domain name is **disabled** or the health state is **abnormal**, the access domain name is deemed **unavailable**.
        self.available_status = available_status
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The enabling state of the access domain name. Valid values:
        # 
        # *   enable: The access domain name is enabled and the intelligent scheduling policy of the corresponding GTM instance takes effect.
        # *   disable: The access domain name is disabled and the intelligent scheduling policy of the corresponding GTM instance does not take effect.
        self.enable_status = enable_status
        # The health state of the access domain name. Valid values:
        # 
        # *   ok: The health state of the access domain name is normal and all address pools that are referenced by the access domain name are available.
        # *   ok_alert: The health state of the access domain name is warning and some of the address pools that are referenced by the access domain name are unavailable. In this case, only the available address pools are returned for Domain Name System (DNS) requests.
        # *   exceptional: The health state of the access domain name is abnormal and all address pools that are referenced by the access domain name are unavailable. In this case, addresses in the non-empty address pool with the smallest sequence number are preferentially used for fallback resolution. This returns DNS results for clients as much as possible.
        self.health_status = health_status
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id
        # Current page number, starting from 1, default is 1.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of **100**, and a default of **20**.
        self.page_size = page_size
        # Remarks for the domain instance.
        self.remark = remark
        # The access domain name. The value of this parameter is composed of the value of ScheduleHostname and the value of ScheduleZoneName.
        self.schedule_domain_name = schedule_domain_name
        # The zone such as example.com or subzone such as a.example.com of the access domain name. In most cases, the zone or subzone is hosted by the Public Authoritative DNS module of Alibaba Cloud DNS. This zone belongs to the account to which the GTM instance belongs.
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

