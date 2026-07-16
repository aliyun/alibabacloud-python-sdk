# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchCloudGtmAddressesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        address_id: str = None,
        available_status: str = None,
        enable_status: str = None,
        health_status: str = None,
        monitor_template_name: str = None,
        name_search_condition: str = None,
        names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        remark_search_condition: str = None,
        remarks: List[str] = None,
        type: str = None,
    ):
        # The language of the return value. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English. This is the default value.
        self.accept_language = accept_language
        # Performs an exact search by endpoint. IP addresses and domain names are supported.
        self.address = address
        # The ID of the address. The address ID is a unique identifier.
        self.address_id = address_id
        # Performs an exact search by the availability status of the address.
        # 
        # - available: The address is available.
        # 
        # - unavailable: The address is unavailable.
        self.available_status = available_status
        # Performs an exact search by the status of the address.
        # 
        # - enable: The address is enabled.
        # 
        # - disable: The address is disabled.
        self.enable_status = enable_status
        # Performs an exact search by the health status of the address.
        # 
        # - ok: All health check tasks for the referenced health check template are normal.
        # 
        # - ok_alert: Some health check tasks for the referenced health check template are abnormal, but the address is still considered normal.
        # 
        # - ok_no_monitor: The address does not reference any health check templates.
        # 
        # - exceptional: Some or all health check tasks for the referenced health check template are abnormal, and the address is considered abnormal.
        self.health_status = health_status
        # The name of the health check template.
        self.monitor_template_name = monitor_template_name
        # The search logic for querying by address name. This parameter is required when you query by address name.
        # 
        # - and: The query returns results that match all the specified keywords.
        # 
        # - or: The query returns results that match some or all of the specified keywords.
        self.name_search_condition = name_search_condition
        # The name of the address. This name is used for easy identification.
        self.names = names
        # The current page number. The value starts from 1. The default value is 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. The maximum value is 100. The default value is 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The search logic for querying by address remarks. This parameter is required when you query by address remarks.
        # 
        # and: The query returns results that match all the specified keywords.
        # 
        # or: The query returns results that match some or all of the specified keywords.
        self.remark_search_condition = remark_search_condition
        # The remarks for the address.
        self.remarks = remarks
        # Performs an exact search by the address type.
        # 
        # - IPv4
        # 
        # - IPv6
        # 
        # - domain
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address is not None:
            result['Address'] = self.address

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.available_status is not None:
            result['AvailableStatus'] = self.available_status

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.monitor_template_name is not None:
            result['MonitorTemplateName'] = self.monitor_template_name

        if self.name_search_condition is not None:
            result['NameSearchCondition'] = self.name_search_condition

        if self.names is not None:
            result['Names'] = self.names

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark_search_condition is not None:
            result['RemarkSearchCondition'] = self.remark_search_condition

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('AvailableStatus') is not None:
            self.available_status = m.get('AvailableStatus')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('MonitorTemplateName') is not None:
            self.monitor_template_name = m.get('MonitorTemplateName')

        if m.get('NameSearchCondition') is not None:
            self.name_search_condition = m.get('NameSearchCondition')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RemarkSearchCondition') is not None:
            self.remark_search_condition = m.get('RemarkSearchCondition')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

