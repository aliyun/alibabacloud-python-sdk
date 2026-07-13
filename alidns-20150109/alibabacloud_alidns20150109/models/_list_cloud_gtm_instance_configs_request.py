# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudGtmInstanceConfigsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        enable_status: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        schedule_domain_name: str = None,
        schedule_zone_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request. Generate a unique token for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The status of the domain name instance:
        # 
        # - enable: The GTM instance uses intelligent scheduling policies.
        # 
        # - disable: The intelligent scheduling policies of the GTM instance are unavailable.
        self.enable_status = enable_status
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id
        # The page number. The value starts from **1**. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. Maximum value: **100**. Default value: **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The remarks.
        self.remark = remark
        # The GTM access domain name. The domain name is a combination of the host record (ScheduleHostname) and the root or subdomain (ScheduleZoneName).
        self.schedule_domain_name = schedule_domain_name
        # The root domain, such as example.com, or subdomain, such as a.example.com, of the GTM access domain name. This is typically a domain name that is hosted in an authoritative zone in the Alibaba Cloud DNS console and belongs to the same account as the GTM instance.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

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

